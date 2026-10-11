# CLAUDE.md

이 프로젝트는 지식그래프 기반 Agentic RAG 실습(graph-rag)이다.

## 산출물 규칙
- 실습 번호(NN, 2자리) 기준으로 이름을 붙인다.
  - 스크립트: `src/labNN_이름.py`
  - 데이터: `data/labNN_*.jsonl` (여러 실습이 공유하는 데이터는 `data/공용이름.jsonl`, 예: `chunks.jsonl`)
- 모든 스크립트는 파일 상단에 실행 예시 주석을 넣는다. (예: `uv run python src/lab01_check_env.py`)

## 개발 환경
- Python은 uv 가상환경(`.venv`)을 사용한다. 실행은 `uv run python ...`.
- 패키지를 추가할 때는 `uv add`로 하고, 반드시 버전을 고정한다 (`pkg==x.y.z`).

## 코드 규칙
- LLM과 임베딩 호출 코드는 모델명을 상수로 분리한다.
  기본값은 로컬 Ollama(LLM `qwen3.5:9b`, 임베딩 `bge-m3`)이다. 유료 API는 기본값으로 쓰지 않는다.
  구현 패턴은 `src/lab01_check_env.py`를 따른다 (`.env`의 `LLM_BINDING`, `OLLAMA_MODEL`, `EMBEDDING_MODEL`, `LLM_BINDING_HOST`).
- 파일을 열 때는 예외 없이 인코딩을 명시한다: `open(path, encoding="utf-8")`.
  `Path.read_text()`, `Path.write_text()`도 `encoding="utf-8"`을 준다.
- `json.dump`와 `json.dumps`에는 `ensure_ascii=False`를 준다.
- 경로는 문자열 결합 대신 `pathlib.Path`를 쓴다.

## 안전 규칙
- Neo4j에 쓰기 작업을 하기 전에는 반드시 실행할 쿼리를 먼저 보여주고 확인을 받는다.
  쓰기 작업은 CREATE, MERGE, SET, DELETE, REMOVE, DROP, 인덱스·제약 생성, LOAD CSV, 데이터를 변경하는 APOC·GDS 프로시저를 모두 포함한다.
- 데이터 파일을 덮어쓰기 전에 백업 사본을 남긴다.
- `.env`와 API key는 어떤 파일에도 복사하지 않고, 출력에도 드러내지 않는다.

## 실행 환경
- Neo4j: `docker compose up -d` (이미지 `neo4j:5.26-community`, 브라우저 7474, bolt 7687, APOC·GDS 플러그인). 접속 정보는 `.env`의 `NEO4J_*`.
- Ollama: `ollama serve`로 서버를 띄워야 한다 (기본 `http://localhost:11434`). `bge-m3` 임베딩 차원은 1024이므로 Neo4j 벡터 인덱스도 1024로 만든다.
- 환경 점검: `uv run python src/lab01_check_env.py` (LLM, 임베딩, Neo4j 세 가지를 OK/FAIL로 표시).
