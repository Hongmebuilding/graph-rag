# 누리테크 LLM Wiki 색인

- 생성일: 2026-10-11
- 문서 수: 78개 (entities 17 · concepts 3 · sources 58), 전부 `status: draft`
- 작성 규칙: [TEMPLATE.md](TEMPLATE.md)
- 각 줄 끝의 괄호는 한 줄 설명의 근거 원문 파일명이다. 원문은 `corpus/raw/`에 있다.

## Entities (17)

### 제품

- [[robosweep-s1]] — 로보스윕 S1: 2024년 9월 출시된 첫 프리미엄 로봇청소기로, NB-200 배터리 과열로 2026년 4월 리콜이 결정되었다 (product-robosweep-s1.txt, meeting-2026-04-recall.txt).
- [[robosweep-s2]] — 로보스윕 S2: 물걸레 스테이션 일체형 후속 모델로 2026년 5월 출시되었고, NB-300 조기 전환으로 약 3주 지연되었다 (product-robosweep-s2.txt, meeting-2026-04-recall.txt).
- [[airwell-a1]] — 에어웰 A1: 2025년 3월 출시된 66㎡급 공기청정기로, 2026년 6월 HF-13 필터 조기 막힘 CS가 늘었다 (product-airwell-a1.txt, incident-2026-06-filter.txt).

### 공급사

- [[hanbit-energy]] — 한빛에너지: 2018년부터 배터리 팩을 공급하는 핵심 공급사로, 2공장 생산 로트가 S1 과열 사건의 대상이었다 (supplier-hanbit-energy.txt, incident-2026-03-battery.txt).
- [[daesung-precision]] — 대성정밀: DM-40·DM-45 모터와 듀얼 러버 브러시를 공급하며 모터는 이중 소싱 예외 품목이다 (supplier-daesung-precision.txt).
- [[clearoptics]] — 클리어옵틱스: LDS-3 라이다 렌즈 모듈과 에어웰 A1 PM2.5 센서를 공급하며 라이다 렌즈는 단독 공급이다 (supplier-clearoptics.txt).

### 부품

- [[nb-200]] — NB-200: 로보스윕 S1용 5,200mAh 배터리 팩으로, 로트 HB-2601-B2가 과열 리콜 대상이다 (product-robosweep-s1.txt, incident-2026-03-battery.txt).
- [[nb-300]] — NB-300: 로보스윕 S2용 6,000mAh 배터리 팩으로 셀 단위 온도 센서를 갖추었고, 세진셀이 병행 공급한다 (product-robosweep-s2.txt, audit-sejincell-2026-06-final.txt).
- [[lds-3]] — LDS-3: 로보스윕 S1·S2의 라이다 센서이며 렌즈 모듈은 클리어옵틱스 단독 공급이다 (supplier-clearoptics.txt).
- [[dm-40]] — DM-40: 로보스윕 S1 주행 모터로, 2025년 11월 베어링 소음 개선 후 불량률이 0.8%에서 0.2%로 내려갔다 (supplier-daesung-precision.txt).
- [[dm-45]] — DM-45: 로보스윕 S2 주행 모터로, 신성모터스가 대체 후보 모터를 평가 중이다 (product-robosweep-s2.txt, supplier-sinsung-motors.txt).
- [[hf-13]] — HF-13: 에어웰 A1·A2가 공용하는 H13 등급 헤파필터이며 2026년 6월 조기 막힘 이슈가 있었다 (product-airwell-a1.txt, incident-2026-06-filter.txt).

### 인물

- [[kim-seojun]] — 김서준: 2015년 창업한 대표이사(CEO)로, 2026년 4월 S1 로트 전량 자발적 리콜을 결정했다 (org-people.txt, meeting-2026-04-recall.txt).
- [[park-jiwon]] — 박지원: CTO로 로보스윕 시리즈 아키텍처를 총괄하며 S2의 NB-300 조기 전환을 제안했다 (org-people.txt, meeting-2026-04-recall.txt).
- [[lee-haneul]] — 이하늘: 로보틱스사업부장 상무로 리콜 대응 TF 팀장을 겸임한다 (org-people.txt).
- [[jeong-minjae]] — 정민재: 품질보증팀장으로 IR-2026-031과 IR-2026-058 필드 장애 보고서를 담당한다 (org-people.txt, incident-2026-03-battery.txt, incident-2026-06-filter.txt).
- [[han-soyoung]] — 한소영: 구매팀장으로 공급사 계약과 이중 소싱 정책 운영, 세진셀·신성모터스 평가를 맡는다 (org-people.txt, audit-sejincell-2026-06-final.txt, supplier-sinsung-motors.txt).

## Concepts (3)

- [[parser-routing]] — 문서 파서 라우팅 기준: 문서 유형별 1차 파서와 대안, GPU 없는 노트북 제약, MinerU·RAG-Anything 도입 조건 (data/lab03_report.md).
- [[dual-sourcing]] — 이중 소싱 정책(PP-07): A급 부품은 승인 공급사 둘 이상을 확보해야 하며 2026년 1월 이행률은 60%였다 (policy-procurement.txt, quarterly-report-2026q1.txt).
- [[document-access-levels]] — 문서 접근 등급(SEC-03): PUBLIC·INTERNAL·CONFIDENTIAL·RESTRICTED 4등급이며 AI 검색은 권한 범위 안의 문서만 대상으로 한다 (policy-security.txt).

## Sources (58)

### 회사·조직·전략

- [[company-overview]] — 회사 소개: 2015년 설립, 세 개 사업부, 2025년 매출 4,120억 원 (company-overview.txt).
- [[company-history-timeline]] — 연혁: 2015년 창업부터 2026년 6월 세진셀 승인까지의 이정표 (company-history-timeline.txt).
- [[mid-term-strategy-2027-2029]] — 중기 전략: 2029년 매출 7,500억 원, 해외 비중 30% 목표 (mid-term-strategy-2027-2029.txt).
- [[org-people]] — 2026년 3월 기준 경영진과 주요 팀장 현황 (org-people.txt).
- [[org-people-v2]] — 2026년 7월 기준 신규 담당자 여섯 명 현황 (org-people-v2.txt).
- [[org-chart-update-2026h2]] — 2026년 7월 1일자 환경안전팀·마케팅팀 신설 공지 (org-chart-update-2026h2.txt).
- [[announcement-cfo-appointment]] — 2025년 9월 1일자 강태민 CFO 선임 공지 (announcement-cfo-appointment.txt).
- [[announcement-vietnam-factory-expansion]] — 하이퐁 공장 증설 발표: 투자 약 380억 원, 2026년 완공 목표 (announcement-vietnam-factory-expansion.txt).
- [[esg-report-summary-2025]] — 2025년 ESG 보고서 요약 (esg-report-summary-2025.txt).

### 정책

- [[policy-procurement]] — 구매 정책 PP-07: 핵심 부품 이중 소싱 원칙과 2026년 1월 예외 품목 (policy-procurement.txt).
- [[policy-security]] — 정보보안 정책 SEC-03: 문서 접근 4등급 (policy-security.txt).
- [[policy-data-privacy]] — 데이터 프라이버시 정책 DP-01: 누리홈·누리허브 사용자 데이터 처리 원칙 (policy-data-privacy.txt).
- [[policy-environment-safety]] — 환경안전 정책 EHS-01: 아산·하이퐁 공장 안전 및 환경 규제 준수 원칙 (policy-environment-safety.txt).

### 감사·구매·계약

- [[audit-sejin-2026-05]] — 2026년 5월 20일 세진셀 1차 공장 감사 결과 (audit-sejin-2026-05.txt).
- [[audit-sejincell-2026-06-final]] — 2026년 6월 30일 세진셀 최종 양산 승인 감사 보고서 (audit-sejincell-2026-06-final.txt).
- [[compliance-audit-2026]] — 2026년 7월 20일 PP-07 준수 현황 컴플라이언스 감사 (compliance-audit-2026.txt).
- [[procurement-cost-negotiation-2026]] — 2026년 7월 28일 대성정밀·클리어옵틱스 원가절감 협상 메모 (procurement-cost-negotiation-2026.txt).
- [[contract-hanbit-energy-renewal]] — 한빛에너지 계약 조기 갱신 논의 메모로, 열람 제한 문서이다 (contract-hanbit-energy-renewal.txt).

### 회의록

- [[meeting-2026-04-recall]] — 2026년 4월 2일 S1 배터리 대응 회의: 전량 자발적 리콜과 S2 NB-300 전환 결정 (meeting-2026-04-recall.txt).
- [[meeting-2026-05-recall-followup]] — 2026년 5월 28일 리콜 접수율(약 62%)과 세진셀 1차 감사 보고 (meeting-2026-05-recall-followup.txt).
- [[meeting-2026-06-board]] — 2026년 6월 30일 이사회: 1분기 실적, 리콜 비용, 누리허브 투자 승인 (meeting-2026-06-board.txt).
- [[meeting-2026-07-roadmap-review]] — 2026년 7월 22일 S3·에어웰 A2·누리허브 로드맵 점검 (meeting-2026-07-roadmap-review.txt).
- [[meeting-2026-08-safety-committee]] — 2026년 8월 6일 아산 공장 안전 점검과 배터리 취급 수칙 (meeting-2026-08-safety-committee.txt).
- [[meeting-2026-09-budget-planning]] — 2026년 9월 8일 2027년 예산 방향과 이중 소싱 투자 우선순위 (meeting-2026-09-budget-planning.txt).
- [[meeting-2026-10-dual-sourcing-review]] — 2026년 10월 14일 PP-07 반기 리뷰: 세진셀 물량 배분, 신성모터스, 라이다 렌즈 (meeting-2026-10-dual-sourcing-review.txt).

### 장애·CS

- [[incident-2026-03-battery]] — IR-2026-031: 2026년 3월 S1 배터리 과열 CS 47건과 원인 분석 (incident-2026-03-battery.txt).
- [[incident-2026-06-filter]] — IR-2026-058: 2026년 6월 에어웰 A1 HF-13 필터 조기 막힘 CS 76건 (incident-2026-06-filter.txt).
- [[incident-2026-08-platform-outage]] — 2026년 8월 12일 누리홈 앱 클라우드 연동 서비스 약 2시간 장애 (incident-2026-08-platform-outage.txt).
- [[faq-cs]] — 고객센터 공개 FAQ(2026년 5월, PUBLIC): 리콜 확인, 펌웨어, 필터 교체 주기 (faq-cs.txt).
- [[faq-cs-v2]] — 고객센터 공개 FAQ 추가분(2026년 7월, PUBLIC): 미스트웨이브 H1·누리허브·에어웰 A2 (faq-cs-v2.txt).
- [[customer-satisfaction-survey-2026]] — 2026년 상반기 고객만족도 조사: S2 4.5점, S1 4.0점, A1 3.6점 (customer-satisfaction-survey-2026.txt).

### 제품·로드맵

- [[product-robosweep-s1]] — 로보스윕 S1 제품 사양서 (product-robosweep-s1.txt).
- [[product-robosweep-s2]] — 로보스윕 S2 제품 사양서 (product-robosweep-s2.txt).
- [[product-robosweep-s2-refresh]] — 로보스윕 S2 펌웨어 1.3 릴리즈 노트(2026년 7월 20일) (product-robosweep-s2-refresh.txt).
- [[product-robosweep-s3]] — 로보스윕 S3 개발 진행 보고서(2026년 7월 15일) (product-robosweep-s3.txt).
- [[product-airwell-a1]] — 에어웰 A1 제품 사양서 (product-airwell-a1.txt).
- [[product-airwell-a2]] — 에어웰 A2 제품 사양서(2026년 11월 출시 목표) (product-airwell-a2.txt).
- [[product-mistwave-h1]] — 미스트웨이브 H1 가습기 제품 사양서 (product-mistwave-h1.txt).
- [[product-nurihub]] — 누리허브 제품 사양서(2026년 4분기 출시 목표) (product-nurihub.txt).
- [[roadmap-2026]] — 2026년 하반기~2027년 제품 로드맵 메모(INTERNAL) (roadmap-2026.txt).

### 시장·마케팅

- [[competitor-analysis-2026]] — 2026년 7월 로봇청소기·공기청정기 경쟁 구도 분석 (competitor-analysis-2026.txt).
- [[marketing-campaign-brief-nurihub]] — 2026년 7월 누리허브 출시 마케팅 캠페인 기획안 (marketing-campaign-brief-nurihub.txt).

### 분기 보고

- [[quarterly-report-2025q1]] — 2025년 1분기: 매출 970억 원 (quarterly-report-2025q1.txt).
- [[quarterly-report-2025q2]] — 2025년 2분기: 매출 995억 원 (quarterly-report-2025q2.txt).
- [[quarterly-report-2025q3]] — 2025년 3분기: 매출 1,050억 원 (quarterly-report-2025q3.txt).
- [[quarterly-report-2025q4]] — 2025년 4분기 및 연간: 연결 매출 4,120억 원 (quarterly-report-2025q4.txt).
- [[quarterly-report-2026q1]] — 2026년 1분기: 매출 1,080억 원, 리콜 충당금 42억 원 (quarterly-report-2026q1.txt).
- [[quarterly-report-2026q2]] — 2026년 2분기: 매출 1,150억 원, 상반기 누계 2,230억 원 (quarterly-report-2026q2.txt).
- [[quarterly-report-2026q3]] — 2026년 3분기: 필터 품질 이슈와 세진셀 최종 양산 승인 (quarterly-report-2026q3.txt).
- [[quarterly-report-2026q4]] — 2026년 4분기: 매출 1,220억 원, 에어웰 A2·누리허브 출시 (quarterly-report-2026q4.txt).

### 공급사 프로파일

- [[supplier-hanbit-energy]] — 한빛에너지 프로파일: 배터리 팩 공급, 계약 2025~2027년 (supplier-hanbit-energy.txt).
- [[supplier-sejincell]] — 세진셀 프로파일: 2차 배터리 공급사로 승인 (supplier-sejincell.txt).
- [[supplier-daesung-precision]] — 대성정밀 프로파일: 모터·브러시 공급 (supplier-daesung-precision.txt).
- [[supplier-sinsung-motors]] — 신성모터스 프로파일: 모터 이중 소싱 후보로 서류 심사 착수 (supplier-sinsung-motors.txt).
- [[supplier-clearoptics]] — 클리어옵틱스 프로파일: 라이다 렌즈·PM2.5 센서 공급 (supplier-clearoptics.txt).
- [[supplier-purefiltertech]] — 퓨어필터텍 프로파일: HF-13 헤파필터 단독 공급 (supplier-purefiltertech.txt).
- [[supplier-cosmo-sensor]] — 코스모센서 프로파일: 미스트웨이브 H1 온습도 센서 신규 공급 (supplier-cosmo-sensor.txt).
- [[supplier-daehan-display]] — 대한디스플레이 프로파일: 누리허브 7인치 터치 패널 신규 공급 (supplier-daehan-display.txt).
