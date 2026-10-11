---
id: document-access-levels
title: 문서 접근 등급(SEC-03)
doc_type: concept
source_file: corpus/raw/policy-security.txt
created: 2026-10-11
updated: 2026-10-11
tags: [정책, 정보보안, 접근통제]
status: draft
---

## 요약

SEC-03은 2025년 8월 개정된 정보보안 정책으로, 누리테크의 사내 문서를 PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED 네 등급으로 분류한다 (policy-security.txt). AI 검색 시스템과 챗봇은 사용자 권한 범위 안의 문서만 검색 대상으로 삼아야 하며, 권한 밖 문서는 존재 여부도 노출하지 않는 것이 원칙이다 (policy-security.txt). 공급사 계약 조건(단가, 페널티 조항)은 CONFIDENTIAL이며 구매팀 외 조직에는 요약 정보만 제공한다 (policy-security.txt).

## 핵심 사실

- PUBLIC은 대외 공개 가능 문서로 제품 카탈로그와 공개 FAQ가 해당한다 (policy-security.txt).
- INTERNAL은 임직원 공용 문서로 제품 사양서, 조직도, 일반 정책이 해당한다 (policy-security.txt).
- CONFIDENTIAL은 부서 제한 문서로 공급사 계약 조건, 원가 정보, 감사 보고서가 해당하며 해당 부서와 경영진만 접근한다 (policy-security.txt).
- RESTRICTED는 지정 인원 전용 문서로 인사 평가, 급여, 법무 분쟁 자료가 해당한다 (policy-security.txt).
- 2025년 ESG 보고서는 SEC-03 체계로 공급사 계약조건 등 민감 정보를 등급별로 관리한다고 밝힌다 (esg-report-summary-2025.txt).
- 데이터 프라이버시 정책 DP-01은 누리홈·누리허브 사용자 데이터를 SEC-03 기준 INTERNAL 등급으로 관리하되 원본 로그는 CONFIDENTIAL에 준해 취급하고, 플랫폼사업부와 법무팀만 접근하도록 정한다 (policy-data-privacy.txt).
- 코퍼스에서 고객센터 공개 FAQ 두 건은 PUBLIC으로 표기되어 있다 (faq-cs.txt, faq-cs-v2.txt).
- 고객만족도 조사 요약과 제품 로드맵 메모는 INTERNAL로 표기되어 있다 (customer-satisfaction-survey-2026.txt, roadmap-2026.txt).
- [[hanbit-energy]] 계약 갱신 논의 메모는 등급 표기 없이 열람 제한 문서로 지정되어 있고 구매팀 외 공유가 금지되어 있다 (contract-hanbit-energy-renewal.txt).

## 관련 문서

- [[hanbit-energy]]
- [[policy-security]]
- [[policy-data-privacy]]
- [[esg-report-summary-2025]]
- [[faq-cs]]
- [[faq-cs-v2]]
- [[customer-satisfaction-survey-2026]]
- [[roadmap-2026]]
- [[contract-hanbit-energy-renewal]]
