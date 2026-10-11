---
id: robosweep-s2
title: 로보스윕 S2
doc_type: entity
source_file: corpus/raw/product-robosweep-s2.txt
created: 2026-10-11
updated: 2026-10-11
tags: [제품, 로봇청소기]
status: draft
---

## 요약

로보스윕 S2(모델명 RS-S2)는 [[robosweep-s1]]의 후속 모델로 물걸레 스테이션을 통합한 올인원 로봇청소기이며 2026년 5월에 출시되었다 (product-robosweep-s2.txt). 배터리는 셀 단위 온도 센서를 갖춘 [[nb-300]]인데, 당초 [[nb-200]] 공용화 계획이 2026년 4월 리콜 대응 회의에서 바뀌면서 출시가 약 3주 지연되었다 (product-robosweep-s2.txt, meeting-2026-04-recall.txt). 2026년 7월에는 배터리 온도 모니터링을 강화한 펌웨어 1.3이 배포되었다 (product-robosweep-s2-refresh.txt).

## 핵심 사실

- 흡입력은 7,000Pa이다 (product-robosweep-s2.txt).
- 배터리는 [[nb-300]] 리튬이온 배터리 팩(6,000mAh, 공급사 [[hanbit-energy]])이다 (product-robosweep-s2.txt).
- 내비게이션은 [[lds-3]] 라이다 센서와 전방 ToF 카메라이고, 주행 모터는 [[dm-45]] 기어드 모터, 브러시는 듀얼 러버 브러시 V2이며, 모터와 브러시 공급사는 [[daesung-precision]]이다 (product-robosweep-s2.txt).
- 스테이션은 자동 세척과 온풍 건조를 지원한다 (product-robosweep-s2.txt).
- KC 인증을 완료했고 국제 안전 규격 IEC 62133에 적합하다 (product-robosweep-s2.txt).
- 2026년 4월 2일 회의에서 [[park-jiwon]]이 [[nb-300]] 조기 전환을 제안했고 [[lee-haneul]]이 약 3주 출시 지연은 수용 가능하다고 답해, 로보스윕 S2는 [[nb-300]]으로 출시하기로 결정되었다 (meeting-2026-04-recall.txt).
- [[nb-300]]은 [[hanbit-energy]] 1공장 전용 라인에서만 생산하기로 결정되었다 (meeting-2026-04-recall.txt).
- 2026년 5월 20일 정식 출시되었고 초기 판매 호조가 로보틱스 매출 비중 확대에 기여했다 (quarterly-report-2026q2.txt).
- 세진셀이 [[nb-300]] 물량 일부를 [[hanbit-energy]] 생산분과 병행해 공급하며, 첫 출하는 7월 중순부터 시작되었다 (audit-sejincell-2026-06-final.txt, quarterly-report-2026q3.txt).
- 펌웨어 1.3은 셀 단위 온도 센서 값 기반 모니터링 주기를 10초에서 5초로 줄이고, 45도 초과 시 충전을 자동 중단하며, 1분당 8도 이상 급상승하면 누리홈 앱으로 사전 경고를 보낸다 (product-robosweep-s2-refresh.txt).
- 펌웨어 1.3은 2026년 5월 이후 출고된 전체 RS-S2가 대상이고 7월 22일부터 OTA로 순차 적용되며, 리콜 로트 HB-2601-B2([[nb-200]], [[robosweep-s1]] 전용)와는 무관한 예방적 조치이다 (product-robosweep-s2-refresh.txt).
- 2026년 상반기 고객만족도는 4.5점(5점 만점)이며 흡입력 7,000Pa와 물걸레 스테이션 일체형 구조에 대한 호평이 많았다 (customer-satisfaction-survey-2026.txt).
- 경쟁 구도에서 흡입력 기준 상위권이나 브랜드 인지도는 메가일렉트로닉스 대비 열세로 평가되었다 (competitor-analysis-2026.txt).

## 관련 문서

- [[robosweep-s1]]
- [[nb-300]]
- [[nb-200]]
- [[lds-3]]
- [[dm-45]]
- [[hanbit-energy]]
- [[daesung-precision]]
- [[park-jiwon]]
- [[lee-haneul]]
- [[product-robosweep-s2]]
- [[product-robosweep-s2-refresh]]
- [[meeting-2026-04-recall]]
- [[audit-sejincell-2026-06-final]]
- [[quarterly-report-2026q2]]
- [[quarterly-report-2026q3]]
- [[customer-satisfaction-survey-2026]]
- [[competitor-analysis-2026]]
