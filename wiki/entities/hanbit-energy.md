---
id: hanbit-energy
title: 한빛에너지
doc_type: entity
source_file: corpus/raw/supplier-hanbit-energy.txt
created: 2026-10-11
updated: 2026-10-11
tags: [공급사, 배터리]
status: draft
---

## 요약

한빛에너지는 2018년부터 누리테크에 배터리 팩을 공급해 온 핵심 공급사이며 본사와 1공장은 청주, 2공장은 천안에 있다 (supplier-hanbit-energy.txt). [[nb-200]]([[robosweep-s1]]용)과 [[nb-300]]([[robosweep-s2]]용)을 공급하고, 2026년 3월 [[robosweep-s1]] 배터리 과열 사건의 문제 로트는 2공장에서 생산되었다 (supplier-hanbit-energy.txt, incident-2026-03-battery.txt). 이중 소싱 정책에 따라 세진셀이 두 번째 배터리 공급사로 승인되면서 단독 공급 구조에서 벗어났다 (audit-sejincell-2026-06-final.txt, quarterly-report-2026q4.txt).

## 핵심 사실

- [[nb-200]]은 1공장과 2공장에서, [[nb-300]]은 1공장 전용 라인에서 생산한다 (supplier-hanbit-energy.txt).
- 계약 기간은 2025년 1월부터 2027년 12월까지 3년이다 (supplier-hanbit-energy.txt).
- 품질 조항으로 로트별 출하 검사 성적서 제출 의무가 있고, 중대 결함이 발생하면 72시간 내 원인을 보고해야 한다 (supplier-hanbit-energy.txt).
- 리콜 원인이 공급사 공정 결함으로 판명되면 회수 비용의 60%를 분담하는 페널티 조항이 있다 (supplier-hanbit-energy.txt).
- 2018년 누리테크와 배터리 공급 계약을 체결하고 공급을 개시했다 (company-history-timeline.txt).
- 문제 로트 HB-2601-B2는 2공장에서 2026년 1월에 생산되었고, 한빛에너지는 3월 26일 1차 원인 보고서를 제출했다 (incident-2026-03-battery.txt).
- 근본 원인은 셀 조립 공정에서 절연 필름이 규격보다 얇게 적용된 것으로 추정된다 (incident-2026-03-battery.txt).
- 사건 이후 2공장 생산분에 대한 추가 전수 검사가 진행 중이다 (supplier-hanbit-energy.txt).
- 리콜 비용 분담은 2분기 기준 60% 비용분담 협상이 진행 중이었고, 협의 결과는 3분기 이사회에 재보고하기로 했다 (quarterly-report-2026q2.txt, meeting-2026-06-board.txt).
- 2026년 1월 기준 배터리 팩([[nb-200]], [[nb-300]])은 한빛에너지 단독 공급 예외 품목이었다 (policy-procurement.txt).
- 세진셀의 [[nb-300]] 공급이 7월 중순 개시된 뒤 4분기까지 이어지며 공급 비중이 점차 확대되고 있다 (quarterly-report-2026q4.txt).
- 세진셀과 한빛에너지 간 물량 배분 비율은 구매팀이 2026년 11월 중 확정해 보고하기로 했다 (meeting-2026-10-dual-sourcing-review.txt).
- 로보스윕 S3용 NB-400은 한빛에너지·세진셀 이중 소싱을 전제로 개발 중이며, 한빛에너지 물량은 청주 1공장 라인에서 우선 검토한다 (product-robosweep-s3.txt).

## 관련 문서

- [[nb-200]]
- [[nb-300]]
- [[robosweep-s1]]
- [[robosweep-s2]]
- [[dual-sourcing]]
- [[supplier-hanbit-energy]]
- [[incident-2026-03-battery]]
- [[meeting-2026-04-recall]]
- [[meeting-2026-06-board]]
- [[meeting-2026-10-dual-sourcing-review]]
- [[audit-sejincell-2026-06-final]]
- [[policy-procurement]]
- [[company-history-timeline]]
- [[quarterly-report-2026q2]]
- [[quarterly-report-2026q4]]
- [[product-robosweep-s3]]
- [[contract-hanbit-energy-renewal]]
