---
id: product-robosweep-s2-refresh
title: 로보스윕 S2 펌웨어 1.3 릴리즈 노트 (2026-07-20)
doc_type: source
source_file: corpus/raw/product-robosweep-s2-refresh.txt
created: 2026-10-11
updated: 2026-10-11
tags: [원문요약, 릴리즈노트, 펌웨어, 배터리안전]
status: draft
---

## 요약

품질보증팀이 2026년 7월 20일 공지한 [[robosweep-s2]](RS-S2) 펌웨어 1.3 릴리즈 노트로, [[nb-300]] 배터리 팩의 온도 모니터링 로직을 개선한다 (product-robosweep-s2-refresh.txt). [[robosweep-s1]]의 IR-2026-031 대응 과정에서 도입된 펌웨어 2.3 계열의 안전 강화 방향을 셀 단위 온도 센서와 개선된 BMS 보호 회로를 갖춘 [[robosweep-s2]]에도 같은 취지로 반영했다 (product-robosweep-s2-refresh.txt).

## 핵심 사실

- 셀 단위 온도 센서 값을 활용한 모니터링 주기를 10초에서 5초로 단축했다 (product-robosweep-s2-refresh.txt).
- BMS 보호 회로와 연동해 45도 초과 시 충전을 자동 중단하도록 보강했으며 [[robosweep-s1]] 펌웨어 2.3과 동일한 임계값을 적용했다 (product-robosweep-s2-refresh.txt).
- 1분당 8도 이상 급상승하는 온도 패턴을 감지하면 누리홈 앱으로 사전 경고 알림을 전송하는 기능을 신규 추가했다 (product-robosweep-s2-refresh.txt).
- 적용 범위는 2026년 5월 이후 출고된 전체 RS-S2이며 대상 배터리는 [[nb-300]] 단일 사양(6,000mAh, [[hanbit-energy]])이다 (product-robosweep-s2-refresh.txt).
- 리콜 대상 로트 HB-2601-B2([[nb-200]], [[robosweep-s1]] 전용)와는 무관한 예방적 조치이다 (product-robosweep-s2-refresh.txt).
- 누리홈 앱을 통한 OTA 자동 배포로 2026년 7월 22일부터 순차 적용되며 업데이트 중 청소 예약이 자동 일시 중지될 수 있다 (product-robosweep-s2-refresh.txt).
- 증상이 계속되거나 업데이트 오류가 발생하면 CS센터(백도현) 또는 품질보증팀([[jeong-minjae]])으로 문의한다 (product-robosweep-s2-refresh.txt).

## 관련 문서

- [[robosweep-s2]]
- [[robosweep-s1]]
- [[nb-300]]
- [[nb-200]]
- [[hanbit-energy]]
- [[jeong-minjae]]
- [[incident-2026-03-battery]]
- [[product-robosweep-s2]]
