# Wiki 로그

## [2026-10-11] create | 초기 위키 생성

- 입력: `corpus/raw/` 원문 58개 (`.txt`)
- 규칙: `wiki/TEMPLATE.md` (frontmatter 8개 필드, 본문 `요약`·`핵심 사실`·`관련 문서`, `[[id]]` 링크)
- 생성 문서 77개와 색인 `index.md`, 이 로그 `log.md`. 문서는 모두 `status: draft`, `created`·`updated`는 2026-10-11이다.
- 요약과 핵심 사실의 모든 문장 끝에 근거 원문 파일명을 괄호로 표기했다.

### 생성한 문서

- entities 17개
  - 제품: `robosweep-s1`, `robosweep-s2`, `airwell-a1`
  - 공급사: `hanbit-energy`, `daesung-precision`, `clearoptics`
  - 부품: `nb-200`, `nb-300`, `lds-3`, `dm-40`, `dm-45`, `hf-13`
  - 인물: `kim-seojun`, `park-jiwon`, `lee-haneul`, `jeong-minjae`, `han-soyoung`
- concepts 2개: `dual-sourcing`(이중 소싱 정책 PP-07), `document-access-levels`(문서 접근 등급 SEC-03)
- sources 58개: 원문 파일명(확장자 제외)을 `id`로 쓰고 `source_file`에 `corpus/raw/<원문 파일명>`을 기록했다. 목록은 [index.md](index.md)에 있다.

### 작성 시 판단과 주의 사항

- 링크 대상은 위 entities·concepts 19개로 한정했다. 원문에 나오는 세진셀, 신성모터스, 퓨어필터텍, 코스모센서, 대한디스플레이, 강태민, 오세린, 백도현, 조현우 등은 문서를 만들지 않아 링크 없이 평문으로 적었다.
- entities·concepts의 `source_file`은 가장 핵심이 되는 원문 1개이고, 나머지 근거는 `관련 문서`에 sources 링크로 걸었다.
- 원문끼리 수치가 달라 한쪽으로 고치지 않고 두 수치를 출처와 함께 적었다.
  - 에어웰 A1 필터 조기 막힘 6월 CS 건수: 76건(`incident-2026-06-filter.txt`)과 30여 건(`quarterly-report-2026q3.txt`)
  - 로보스윕 S1 리콜 교체 현황: 6월 말 약 74%(`quarterly-report-2026q2.txt`)와 전량 완료(`esg-report-summary-2025.txt`)
- 원문 4개는 문서 날짜가 이 로그의 날짜(2026-10-11)보다 뒤다. 원문 날짜를 그대로 기록했다.
  - `quarterly-report-2026q3.txt`(2026-10-12), `meeting-2026-10-dual-sourcing-review.txt`(2026-10-14), `contract-hanbit-energy-renewal.txt`(2026-10-22), `quarterly-report-2026q4.txt`(2027-01-20)
- `contract-hanbit-energy-renewal.txt`는 원문에 열람 제한, 구매팀 외 공유 금지로 적혀 있다. 등급(CONFIDENTIAL 등) 표기는 원문에 없어 추정하지 않았다. 이 메모의 내용은 `sources/contract-hanbit-energy-renewal.md`에만 상세히 적었다. 다른 문서에는 관련 문서 링크로 걸었고, `concepts/document-access-levels.md`에만 열람 제한 문서라는 사실을 한 줄 적었다.
- `corpus/raw_pdf/nb200_spec.pdf`는 이번 입력(`corpus/raw/`)이 아니어서 반영하지 않았다.

## [2026-10-20] create | concepts/parser-routing 추가

- 입력: `data/lab03_report.md` (실습 03 pypdf vs docling 비교 결과), MinerU·RAG-Anything·LightRAG 저장소 README와 `pyproject.toml` (2026-10-20 확인)
- 생성: `concepts/parser-routing.md` (`status: draft`). 문서 유형별 1차 파서와 대안, GPU 없는 노트북 제약, MinerU·RAG-Anything 도입 조건을 정리했다.
- 수정: `index.md`(문서 수 78개, concepts 3개, 항목 추가), `entities/nb-200.md`(관련 문서에 `[[parser-routing]]` 추가, `updated` 2026-10-20). 고아 문서 린트를 통과시키려고 링크를 추가했다.
- 주의: 실측은 스펙시트 PDF 1건뿐이다. 깨끗한 텍스트·수식 논문 행은 미검증이고, 스캔본은 현재 OCR 엔진이 없어 처리 불가임을 확인했다.
