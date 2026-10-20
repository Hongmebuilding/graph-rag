---
id: parser-routing
title: 문서 파서 라우팅 기준
doc_type: concept
source_file: data/lab03_report.md
created: 2026-10-20
updated: 2026-10-20
tags: [파싱, 파서, docling, pypdf, MinerU, RAG-Anything]
status: draft
---

## 요약

문서 유형(깨끗한 텍스트, 표 중심 스펙, 스캔본, 수식 많은 논문)별로 어떤 PDF 파서를 먼저 쓰고 무엇을 대안으로 둘지 정한 기준이다. 우리 환경은 GPU 없는 개인 노트북(Mac 또는 Windows)이므로 CPU에서 돌아가는 pypdf와 docling을 1차 선택으로 두고, MinerU와 RAG-Anything은 아래 조건이 충족될 때 도입을 검토한다 (lab03_report.md). 판정 근거는 [[nb-200]] 스펙시트 PDF 1건의 실측이며, 실측하지 못한 유형은 "미검증"으로 표시했다.

## 핵심 사실

### 1. 환경 제약

- 하드웨어는 GPU 없는 개인 노트북(Mac 또는 Windows)이다. 파서는 CPU만으로 동작해야 하고, GPU 전제의 도구는 기본 선택에서 제외한다.
- 기본 LLM과 임베딩은 로컬 Ollama(`qwen3.5:9b`, `bge-m3`)이고 유료 API는 기본값으로 쓰지 않는다 (CLAUDE.md). 이미지를 이해하는 VLM이 필요한 도구는 이 규칙과 충돌할 수 있다.
- 아래 실측은 Linux x86_64 서버(48코어, RAM 125GB, GPU 없음)에서 한 것이다. 소요 시간(docling 1페이지: 첫 실행 약 26초(모델 다운로드 포함), 재실행 약 6초)은 노트북의 속도를 대표하지 않는다. 노트북에서 다시 재야 한다.

### 2. 라우팅 표

| 문서 유형 | 1차 선택 | 대안 | 선택 이유 | 근거 상태 |
|---|---|---|---|---|
| 깨끗한 텍스트 (텍스트 레이어가 있는 본문 위주, 표·수식 거의 없음) | pypdf | docling | 문자열을 원형 그대로 보존하고, 가볍고 모델 다운로드가 필요 없다. 제목 위계가 필요하면(문서 > 섹션 청킹) 대안인 docling으로 바꾼다. pypdf는 제목 표시가 소실되고 문장 중간에서 줄이 끊긴다(`25` / `마이크로미터`). | 부분 검증: 문자열 보존과 줄 끊김은 스펙 PDF에서 확인. 본문 위주 문서 자체는 미검증 |
| 표 중심 스펙 | docling | MinerU `basic` 티어 (조건부, 아래 4절) | 표의 행·열 구조와 머리글·단위의 열 귀속을 보존한다. pypdf는 열 경계가 없어 `16.8 ± 0.05`처럼 값 안에 공백이 있으면 4열을 복원할 수 없다. | 검증됨 (스펙 PDF 실측) |
| 스캔본 (이미지 PDF) | docling + OCR 엔진 설치 (macOS는 `OcrMacOptions`, Windows는 `RapidOcrOptions` 등 docling이 제공하는 옵션 중 선택) | MinerU `basic` 티어 (OCR 포함, ONNX CPU) | 텍스트 레이어가 없어서 OCR이 필수다. **현재 환경은 OCR 엔진이 동작하지 않아서 스캔본을 처리할 수 없다.** | 현재 설정은 실패를 재현함. 설치 후 OCR 품질은 미검증 |
| 수식 많은 논문 | docling (`do_formula_enrichment=True`로 수식 LaTeX 변환) | MinerU (README가 표·수식·복잡한 레이아웃을 주 용도로 명시) | 수식을 일반 텍스트가 아니라 LaTeX로 받을 수 있는지가 관건이다. 이 옵션은 기본값이 False이고 CPU에서는 느릴 수 있다. | 미검증. 스펙 PDF의 수식은 평문이라 근거가 못 된다 |

### 3. 라우팅 규칙과 후처리

- **스캔본 판별:** pypdf로 먼저 글자 수를 센다. 0자이면 스캔본으로 보고 OCR 경로로 보낸다. 이미지 PDF에서 pypdf는 0자였다.
- **빈 결과는 실패로 처리한다:** 이미지 PDF를 docling에 넣으면 OCR 엔진이 없어도 에러 없이 0자를 돌려준다. 출력이 비어 있으면 성공으로 넘기지 말고 실패로 기록한다.
- **docling 후처리 두 가지:** Markdown에서 `\_`를 `_`로 되돌린다(`I\_charge` -> `I_charge`). 문서 제목이 섹션 제목과 같은 `##`로 나오므로 첫 제목을 `#`로 올린다.
- **2단 배치 논문은 읽기 순서를 따로 검증한다.** 스펙 PDF는 단일 단이라 2단 배치의 읽기 순서는 두 파서 모두 판정 불가였다.

### 4. MinerU 도입을 검토할 조건

MinerU는 문서 파서이며 RAG 프레임워크나 벡터 DB가 아니다. README 기준 4.x는 CPU와 Mac에서도 동작하므로 "GPU가 없다"는 이유만으로 배제하지 않는다.

- 하드웨어 요건 (README의 티어 표):

  | 노트북 | 가능한 티어 | 엔진 | 최소 RAM |
  |---|---|---|---|
  | Apple Silicon Mac | `standard` | PyTorch + llama.cpp | 16GB (PyTorch), 8GB (ONNX + llama.cpp) |
  | Intel Mac, 가속기 없는 Windows | `basic` | ONNX (CPU) | 2GB |
  | 내장 GPU가 있는 Windows | `standard` | ONNX + llama.cpp | 8GB |

- 도입을 검토하는 상황 (모두 만족할 때):
  1. docling이 기준 미달이다. 우리 문서 샘플로 읽기 순서(2단 논문), 수식, OCR 품질을 비교했을 때 docling의 결과가 후처리로 못 고칠 만큼 손상된다.
  2. 노트북이 위 표의 RAM 요건을 만족하고, 처리 시간(페이지당)을 노트북에서 재서 허용 범위 안이다.
  3. 라이선스를 검토했다. "MinerU Open Source License"(Apache 2.0 기반, 추가 조건 있음)이므로 사내 사용 범위를 `LICENSE.md`로 확인한다.
  4. 문서를 외부로 보내지 않는다. 기본은 로컬 파싱이며 원격 파싱은 `--remote`를 명시할 때만 동작한다. 이 옵션은 쓰지 않는다.
- `flash` 티어는 가장 빠르지만 품질이 가장 낮아 최종 읽기용으로 쓰지 않는다 (README).
- 프로젝트 의존성과 섞이지 않도록 별도 가상환경에 설치한다 (README는 Python `>=3.10,<3.15`, 별도 venv를 안내한다).

### 5. RAG-Anything 도입을 검토할 조건

RAG-Anything은 파서가 아니라 LightRAG 위에 만든 멀티모달 RAG 프레임워크다. 이미지·표·수식을 VLM 등으로 설명해 지식그래프에 연결한다. 파서는 `mineru`, `docling`, `paddleocr` 중에서 고른다.

- **현재는 도입하지 않는다.** 이유는 두 가지다.
  1. **의존성이 충돌한다.** RAG-Anything `main`의 `pyproject.toml`은 `lightrag-hku<1.5`와 `mineru[core]>=3.4.1`을 요구한다. 우리는 `lightrag-hku[api]==1.5.4`로 고정했다. 선언상 같은 환경에 설치할 수 없다 (실제 설치로 확인하지는 않았다).
  2. **LightRAG 1.5부터 같은 기능이 내장됐다.** LightRAG README는 RAG-Anything을 LightRAG에 합쳤고(2026.05), 문서 파싱 엔진으로 MinerU·Docling·Native를 지원하며, 파서 라우팅을 `LIGHTRAG_PARSER` 설정으로 한다고 적는다. 멀티모달이 필요해지면 별도 설치 전에 이 내장 기능을 먼저 쓴다.
- 멀티모달 기능 자체를 검토할 조건 (모두 만족할 때):
  1. 평가 질문 중 이미지·차트 내용을 알아야 답할 수 있는 질문이 의미 있는 비중으로 있다. 현재 위키 코퍼스는 텍스트 58개(`corpus/raw/*.txt`)이고 PDF는 스펙시트 1개뿐이라 해당하지 않는다.
  2. 이미지를 입력받는 VLM을 쓸 수 있다. LightRAG README는 VLM을 별도 역할로 두고 로컬 예시로 Qwen3.6-35B-A3B를 든다. GPU 없는 노트북에서는 현실적이지 않고, 호스팅 API를 쓰면 "유료 API는 기본값 금지" 규칙에 따라 사전 승인이 필요하다. 현재 기본 LLM `qwen3.5:9b`의 이미지 입력 지원 여부는 확인하지 않았다.
  3. 위 1, 2가 충족되면 LightRAG 1.5.x 내장 멀티모달을 먼저 시도하고, 부족할 때만 RAG-Anything을 별도 환경에서 평가한다.
- RAG-Anything의 라이선스는 MIT다 (`pyproject.toml`).

### 6. 확인한 환경 상태 (2026-10-20)

- docling 2.130.0, pypdf 6.20.0이 설치되어 있다.
- docling이 선택할 OCR 엔진이 없다. `rapidocr`는 설치되어 있지만 `onnxruntime`이 없고, `tesseract`, `easyocr`, `ocrmac`도 없다. 실행하면 `No OCR engine found`를 출력한다.
- `~/.cache/huggingface`가 root 소유라서 `src/lab03_parse_compare.py`는 모델 캐시를 프로젝트의 `.cache/huggingface`에 둔다.
- MinerU와 RAG-Anything 정보는 2026-10-20에 각 저장소의 README와 `pyproject.toml`에서 읽은 것이다. 두 프로젝트는 버전이 빠르게 바뀌므로 도입 시점에 다시 확인한다.

## 관련 문서

- [[nb-200]]
- [[hanbit-energy]]
