"""실습 01: 실습 환경 점검 (LLM / 임베딩 / Neo4j).

실행 예시:
    uv run python src/lab01_check_env.py

LLM_BINDING(.env)에 따라 로컬 Ollama(기본) 또는 OpenAI로 점검한다.
Ollama는 OpenAI 호환 엔드포인트(/v1)로 호출하므로 openai 패키지를 그대로 쓴다.
세 가지 체크 결과를 OK/FAIL로 표시하고, 하나라도 FAIL이면 종료 코드 1로 끝난다.
입력 해시 캐시는 일부러 붙이지 않았다. 캐시가 있으면 실제 연결이 아니라 캐시를 확인하게 된다.
"""

import os
import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase
from openai import APIConnectionError, NotFoundError, OpenAI

DEFAULT_BINDING = "ollama"
DEFAULT_OLLAMA_LLM = "qwen3.5:9b"
DEFAULT_OLLAMA_EMBEDDING = "bge-m3"
DEFAULT_OLLAMA_HOST = "http://localhost:11434"
OPENAI_LLM = "gpt-4o-mini"
OPENAI_EMBEDDING = "text-embedding-3-small"
DEFAULT_NEO4J_URI = "bolt://localhost:7687"
REQUEST_TIMEOUT = 120  # 로컬 모델은 첫 호출 때 메모리에 올리느라 오래 걸릴 수 있다

# 알려진 임베딩 모델의 벡터 차원. 목록에 없는 모델은 차원만 출력하고 검증하지 않는다.
EMBEDDING_DIMS = {"bge-m3": 1024, "text-embedding-3-small": 1536}

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Config:
    binding: str
    llm_model: str
    embedding_model: str
    base_url: str | None  # None이면 OpenAI 기본 주소


def load_config() -> Config:
    binding = os.getenv("LLM_BINDING", DEFAULT_BINDING)
    if binding == "ollama":
        host = os.getenv("LLM_BINDING_HOST", DEFAULT_OLLAMA_HOST).rstrip("/")
        return Config(
            binding,
            os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_LLM),
            os.getenv("EMBEDDING_MODEL", DEFAULT_OLLAMA_EMBEDDING),
            f"{host}/v1",
        )
    if binding == "openai":
        return Config(binding, OPENAI_LLM, OPENAI_EMBEDDING, None)
    raise ValueError(f"지원하지 않는 LLM_BINDING: {binding!r} (ollama | openai)")


def make_client(cfg: Config) -> OpenAI:
    if cfg.binding == "ollama":
        # Ollama는 키를 검사하지 않지만 클라이언트가 값을 요구한다 (비밀 값 아님)
        return OpenAI(base_url=cfg.base_url, api_key="ollama", timeout=REQUEST_TIMEOUT)
    return OpenAI(timeout=REQUEST_TIMEOUT)  # OPENAI_API_KEY 환경변수를 사용한다


def explain(cfg: Config, model: str, e: Exception) -> Exception:
    """Ollama에서 흔한 실패(서버 꺼짐, 모델 미설치)는 해결 방법을 붙여 돌려준다."""
    if cfg.binding != "ollama":
        return e
    if isinstance(e, APIConnectionError):
        return RuntimeError(f"{cfg.base_url} 에 연결할 수 없음 (Ollama 실행 여부 확인)")
    if isinstance(e, NotFoundError):
        return RuntimeError(f"모델 '{model}' 이 설치되어 있지 않음 (ollama pull {model})")
    return e


def check_llm(cfg: Config, client: OpenAI) -> str:
    try:
        resp = client.chat.completions.create(
            model=cfg.llm_model,
            messages=[{"role": "user", "content": "안녕!"}],
            temperature=0,
        )
    except Exception as e:
        raise explain(cfg, cfg.llm_model, e) from e
    return resp.choices[0].message.content.strip()


def check_embedding(cfg: Config, client: OpenAI) -> str:
    try:
        resp = client.embeddings.create(model=cfg.embedding_model, input="지식그래프")
    except Exception as e:
        raise explain(cfg, cfg.embedding_model, e) from e
    dim = len(resp.data[0].embedding)
    expected = EMBEDDING_DIMS.get(cfg.embedding_model)
    if expected is not None and dim != expected:
        raise ValueError(f"벡터 차원 {dim} (기대값 {expected})")
    return f"차원 {dim}"


def check_neo4j() -> str:
    uri = os.getenv("NEO4J_URI", DEFAULT_NEO4J_URI)
    auth = (os.getenv("NEO4J_USERNAME", "neo4j"), os.getenv("NEO4J_PASSWORD", ""))
    with GraphDatabase.driver(uri, auth=auth) as driver:
        records, _, _ = driver.execute_query("RETURN 1 AS ok")
    return f"RETURN 1 -> {records[0]['ok']}"


def run(name: str, fn) -> bool:
    try:
        detail = fn()
    except Exception as e:  # 점검 스크립트이므로 원인 종류와 무관하게 FAIL로 보고한다
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")
        return False
    print(f"[ OK ] {name}: {detail}")
    return True


def main() -> int:
    load_dotenv(PROJECT_ROOT / ".env")

    try:
        cfg = load_config()
        client = make_client(cfg)
    except Exception as e:
        print(f"[FAIL] 설정/클라이언트 생성: {type(e).__name__}: {e}")
        return 1

    print(f"LLM_BINDING={cfg.binding}\n")
    results = [
        run(f"1. LLM ({cfg.llm_model})", lambda: check_llm(cfg, client)),
        run(f"2. 임베딩 ({cfg.embedding_model})", lambda: check_embedding(cfg, client)),
        run("3. Neo4j", check_neo4j),
    ]

    print()
    print("전체 결과:", "ALL OK" if all(results) else "FAIL")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
