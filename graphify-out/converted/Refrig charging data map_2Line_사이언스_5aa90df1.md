<!-- converted from Refrig charging data map_2Line_사이언스.xlsx -->

## Sheet: Sheet1
|  |  | 기본 통신 셋업 |  |  |  | PLC DATA 번지 (WORD) | PLC DATA 번지 (WORD) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 통신 방식 | Ethernet |  |  |  | Line #1 | Line #2 |
|  | IP | 192.168.20.69 |  |  |  |  |  |
|  | SUB NET | 255.255.255.0 |  |  |  |  |  |
|  | GATE WAY | 192.168.20.1 |  |  |  |  |  |
|  | DNS | 168.126.63.1 |  |  |  |  |  |
|  |  | PC to Charging_MC(PLC) |  |  | model | D6860~D6869 | D7860~D7869 |
|  | 항목 | 항목 | 길이 | Description | sufix | D6870~D6879 | D7870~D7879 |
|  | 바코드 | Barcode | 40 | 40 Text |  | D6980~D6999 | D7980~D7999 |
|  | 가스 종류 | Gas type | 2 | 0001 : Refrig type1
0002 : Reffrig type 2
0003 : 주입정보 없음 |  | D7000 | D8000 |
|  | 주입 설정량 | Target amount | 2 | oooo g |  | D7001 | D8001 |
|  |  | Charging_MC(PLC) to PC <Charging data> |  |  |  |  |  |
|  | 항목 | 항목 | 길이 | Description |  |  |  |
|  | 가스 종류 | Gas type | 2 | 0001 : Refrig type1(R600a)
0002 : Reffrig type 2(R134a) |  | D7002 | D8002 |
|  | 주입 설정량 | Target amount | 2 | oooo g |  | D7003 | D8003 |
|  | 실 주입량 | Real amount | 2 | Data/10 (000.0 g) |  | D7004 | D8004 |
|  | 주입중 냉매 저압 | Refrig pressure low | 2 | Data/10 (000.0 bar) |  | D7005 | D8005 |
|  | 주입중 냉매 고압 | Refrig pressure high | 2 | Data/10 (000.0 bar) |  | D7006 | D8006 |
|  | 주입 목표 펄스 | Target puls | 2 | pls |  | D7007 | D8007 |
|  | 냉매 온도 | refrig temperture | 2 | Data/10 (000.0 ℃) |  | D7008 | D8008 |
|  | 바코드 사용 설정 | Bacocd use/not use | 2 | 0001 : Barcode use
0002 : Barcode not use |  | D7009 | D8009 |
|  | 진공체크 진공도 | Vacuum check value | 4 | Data/10000 (000.0000 torr) |  | D7010~D7011 | D8010~D8011 |
|  | 주입 결과 상태 | Result code | 2 | 1 : OK
2 : Vacuum NG
3 : Gun exhaust NG
4 : Unit exhaust NG
5 : Vacuum check NG
6: Operrator stop
7 : Refrig none flow NG
8 : Charging time over
9 : Refrig back flow
10 : GMES data not match model in M/C
11 : GMES data receive time over |  | D7012 | D8012 |
|  | 진공체크 설정 값 | Vacuum check setting value | 4 | Data/10000 (000.0000 torr) |  | D7013~D7014 | D8013~D8014 |
|  | 공정 코드 | Process code | 2 | 0 : None action
1 : Gun EXHAUST
2 : Unit EXHAUST
3 : Vacuum check
4 : Charging |  | D7015 | D8015 |
|  | 주입 시작 신호 | Information call | 2 | 0 : None action
1 : START |  | D7016 | D8016 |
|  | 라인 넘버 | Line code | 2 | 1 : LINE #1
2 : LINE #2 |  | D7017 | D8017 |
|  | 제품 패스 | Not charge unit | 2 | 0 : Default
1 : Pass (1 sec) |  | D7018 | D8018 |
|  | 진공 SPC 데이터 | 0.08sec save vacuum value 1 | 4 | Data/10000 (000.0000 torr) |  | D7020~D7021 | D8020~D8021 |
|  | 진공 SPC 데이터 | 0.08sec save vacuum value 2 | 4 | Data/10000 (000.0000 torr) |  | D7022~D7023 | D8022~D8023 |
|  | 진공 SPC 데이터 | 0.08sec save vacuum value… | 4 | Data/10000 (000.0000 torr) |  | D7024~D7217 | D8024~D8217 |
|  | 진공 SPC 데이터 | 0.08sec save vacuum value 100 | 4 | Data/10000 (000.0000 torr) |  | D7218~D7219 | D8218~D8219 |
|  | 바코드 | Barcode | 40 | 40 Text |  | D7220~D7239 | D8220~D8239 |