# LLM Wiki 문서 템플릿

이 파일은 템플릿이며 위키 문서가 아니다. 색인·적재 대상은 `wiki/{entities,sources,concepts}/*.md`뿐이고, `wiki/TEMPLATE.md`는 제외한다.

## 1. 파일 경로

`wiki/{종류}/{doc_id}.md`

| 종류(폴더) | `doc_type` | 내용 |
|---|---|---|
| `entities` | `entity` | 회사, 사람, 부품, 제품 |
| `sources` | `source` | 원문 요약 |
| `concepts` | `concept` | 정책, 개념 |

`doc_id` 규칙
- 영문 소문자, 숫자, 하이픈(kebab-case)만 쓴다. 예: `robosweep-s1`, `nb-200`, `hanbit-energy`
- 파일명(확장자 제외)과 frontmatter의 `id`가 같아야 한다.
- 링크 `[[id]]`에는 폴더가 없으므로, `doc_id`는 세 폴더 전체에서 유일해야 한다.
- `sources` 문서는 원문 파일명(확장자 제외)을 그대로 쓴다. 예: `corpus/raw/product-robosweep-s1.txt` → `product-robosweep-s1`

## 2. Frontmatter (필수 필드 8개, 모두 채운다)

| 필드 | 형식 | 설명 |
|---|---|---|
| `id` | 문자열 | `doc_id`와 동일 |
| `title` | 문자열 | 문서 제목 (한글 가능) |
| `doc_type` | `entity` \| `source` \| `concept` | 폴더와 일치해야 한다 |
| `source_file` | 경로 문자열 | 원문 경로. 프로젝트 루트 기준 상대 경로, `/` 구분. 예: `corpus/raw/product-robosweep-s1.txt`. `entities`·`concepts` 문서는 가장 핵심이 되는 원문 1개를 적고, 나머지 근거는 `관련 문서`에 `[[sources 문서 id]]`로 건다 |
| `created` | `YYYY-MM-DD` | 최초 작성일 |
| `updated` | `YYYY-MM-DD` | 마지막 수정일. 내용을 고칠 때마다 갱신 |
| `tags` | YAML 리스트 | 예: `[제품, 로봇청소기]` |
| `status` | `draft` \| `reviewed` | 사람이 검토하면 `reviewed` |

## 3. 본문 구조

`##` 제목 3개를 이 순서와 이름 그대로 쓴다.

1. `## 요약`: 2~3문장
2. `## 핵심 사실`: 불릿 목록
3. `## 관련 문서`: `[[WikiLink]]` 불릿 목록

## 4. 링크 규칙

- 다른 문서로 존재하는 제품명, 회사명, 사람 이름이 나오면 `[[id]]` 형태로 링크한다. `요약`과 `핵심 사실` 본문에서도 마찬가지다.
- 본문에 링크한 문서는 모두 `관련 문서`에도 나열한다.
- 링크 대상 `id`는 위키에 실제로 있는 문서여야 한다. 없으면 먼저 `status: draft`로 만든다.

## 5. 복사용 템플릿

```markdown
---
id: {doc_id}
title: {문서 제목}
doc_type: {entity | source | concept}
source_file: corpus/raw/{원문 파일명}
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [태그1, 태그2]
status: draft
---

## 요약

{2~3문장. 이 문서가 무엇인지와 가장 중요한 내용을 쓴다.}

## 핵심 사실

- {사실 1}
- {사실 2}
- {사실 3}

## 관련 문서

- [[{다른 문서 id}]]
```

## 6. 작성 예시

`wiki/entities/robosweep-s1.md` (`corpus/raw/product-robosweep-s1.txt` 기반)

```markdown
---
id: robosweep-s1
title: 로보스윕 S1
doc_type: entity
source_file: corpus/raw/product-robosweep-s1.txt
created: 2026-10-11
updated: 2026-10-11
tags: [제품, 로봇청소기]
status: draft
---

## 요약

로보스윕 S1(모델명 RS-S1)은 [[nuritech]] 로보틱스사업부의 첫 프리미엄 로봇청소기로, 2024년 9월에 출시되었다. 배터리는 [[nb-200]]을 쓴다.

## 핵심 사실

- 흡입력은 5,500Pa이다.
- 배터리는 [[nb-200]](공급사 [[hanbit-energy]]), 주행 모터는 DM-40 기어드 모터(공급사 [[daesung-precision]])를 쓴다.
- 펌웨어 2.3부터 배터리 온도 모니터링 주기가 30초에서 5초로 단축되었다.

## 관련 문서

- [[nuritech]]
- [[nb-200]]
- [[hanbit-energy]]
- [[daesung-precision]]
- [[product-robosweep-s1]]
```
