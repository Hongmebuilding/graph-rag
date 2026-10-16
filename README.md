# graph-rag (수강생 배포용 스타터)

## 포함물
- corpus/raw/          누리테크 사내 문서 58개 (코퍼스 A, 파이프라인 실습 공용. 2026-07-27 확장 정본, GQ 17문항 기준)
- corpusB/             코퍼스 B (실습 06/21/22 B 트랙): raw/ 문서 271개, gt/ 정답 그래프, eval/ 질문 42문항
- ontology/            실습 26용 위반 주입 그래프(corpusB_violated/)와 채점 정답지(answers/)
- corpus/raw_pdf/      실습 03용 스펙시트 PDF
- eval/golden_questions.json  평가 질문 17문항 (GQ-01~17)
- docker-compose.yml   Neo4j 5.26 + APOC + GDS
- .env.example         환경변수 템플릿

## 시작하기 (환경은 챕터별 단계 설치입니다)
1. uv venv --python 3.11 && source .venv/bin/activate
2. uv sync                       # core만 설치 (전 과정 공통)
3. cp .env.example .env          # OPENAI_API_KEY 채우기
4. docker compose up -d          # Neo4j 5.26 + APOC + GDS
5. 이후는 실습 01 Notion 페이지의 안내를 따르세요.

챕터별 도구는 해당 실습 페이지 안내에 따라 추가합니다.
- 실습 03: uv sync --group parsing     (docling)
- 실습 22: uv sync --group graphrag    (lightrag-hku[api]==1.5.4, WebUI 포함)
- 실습 24: uv sync --group ontology    (rdflib 7.6.0) + ontology/ 폴더 자료 사용
- 실습 28: uv sync --group agent       (langgraph 1.2.9, langfuse 4.14.1)
- 실습 35: uv sync --group eval        (deepeval 4.1.3, openevals 0.2.0)
- 3차수 캡스톤: capstone-* / ops 그룹 (환경 세팅 로드맵 참조)

코퍼스 B는 그래프 우위 조건(사실 1개 = 문서 1개, 다리 엔티티 질문 미등장)을
설계 단계에서 보장한 합성 벤치마크로, 사전 생성된 데이터가 그대로 들어 있습니다.
corpusB/VALIDATION.json이 무결성 검증(위반 0건) 기록입니다. 실습 06의 4-5에서 처음 사용합니다.

주의: 누리테크, 가온모빌리티 등 두 코퍼스의 회사와 인물, 제품은 모두 교육용 가상 설정입니다.
