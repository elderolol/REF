# REFRIGER CHARGING MACHINE — Function Spec: 485.csv

> **Module**: `485.csv`  
> **Execution**: Always ON  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

RS-485 통신 프로토콜을 사용하는 필드 센서들의 데이터를 수신하여 D 레지스터에 저장.
RS-485 방식의 진공 센서, 압력 센서, 온도 센서 등이 대상.

> **아날로그 센서** (0~10V, 4~20mA)는 `ad.csv` 에서 처리.  
> **Barcode/PC 데이터**는 Ethernet (PC → PLC 직접 D 영역 Write)으로 처리.

---

## 2. 대상 센서

| 센서 | 통신 방식 | 비고 |
|------|:---------:|------|
| 진공 센서 (Vacuum) | RS-485 | 실시간 진공도 (Torr) |
| 압력 센서 (Pressure) | RS-485 | 냉매 압력 (고압/저압) |
| 온도 센서 (Temperature) | RS-485 | 냉매 온도 |
| 기타 RS-485 센서 | RS-485 | 필요 시 추가 |

---

## 3. Inputs

| Device | Description |
|:------:|-------------|
| RS-485 Buffer | RS-485 통신 수신 버퍼 |
| D150~D179 | Analog Raw Data (ad.csv와 데이터 공유 가능) |

---

## 4. Outputs

| Device | Description |
|:------:|-------------|
| D160~D161 | L0 Vacuum EU (32-bit Torr) — RS-485 센서값 |
| D172~D173 | L1 Vacuum EU (32-bit Torr) |
| D152 | L0 Pressure EU — RS-485 센서값 |
| D164 | L1 Pressure EU |
| D156 | L0 Temperature EU — RS-485 센서값 |
| D168 | L1 Temperature EU |
| D138~D148 | Operation Display Mirror (HMI 표시용) |

---

## 5. Data Flow

```
RS-485 Network
    │
    ├── [Vacuum Sensor L0]  ←→ 485 통신 Polling
    │   └── 응답 파싱 → D160~D161 (32-bit Torr)
    │
    ├── [Pressure Sensor L0] ←→ 485 통신 Polling
    │   └── 응답 파싱 → D152 (kgf/㎠)
    │
    ├── [Temperature Sensor L0] ←→ 485 통신
    │   └── 응답 파싱 → D156 (0.1℃)
    │
    ├── [Line 1 Sensors] (D270≥2)
    │   └── D172~D173, D164, D168
    │
    └── Display Mirror
        D138~D148 갱신
```

---

## 6. Communication Protocol

> 센서별 프로토콜은 제조사 사양에 따름 (Modbus RTU 등 RS-485 기반).

| 단계 | 처리 |
|:----:|------|
| ① | Polling 명령 전송 (센서 주소, 기능 코드) |
| ② | 응답 수신 대기 |
| ③ | CRC 검증 |
| ④ | 데이터 파싱 → EU 변환 |
| ⑤ | D 레지스터 저장 |
| ⑥ | Timeout → Comm Error |

---

## 7. 센서 Type 선택 아키텍처 (미래 확장)

> **485.csv와 ad.csv는 동일한 출력 영역(D152/D156/D160/D164/D168/D172)을 공유.**
> 센서 HW Type에 따라 실제 값을 기록하는 모듈이 결정됨.

```
[Sensor Hardware]
    ├── RS-485 → 485.csv가 D152/D156/D160... 에 기록
    └── Analog → ad.csv가 D152/D156/D160... 에 기록

[Dxxx Sensor Type Select]
    ├── = 0 → ad.csv 출력 사용
    └── = 1 → 485.csv 출력 사용
```

---

## 8. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| Sensor Comm NG | 응답 없음 / Timeout | Alarm, 해당 센서값 Invalid |
| CRC Error | Checksum 불일치 | 재전송 요청, N회 실패 시 Alarm |

---

## 8. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Buffer read / 통신 상태 |
| `MOV` | 16-bit data transfer |
| `DMOV` | 32-bit data transfer (Vacuum) |
| `AND=` | Data validation |
| `SET` | Data valid flag |
| `RST` | Comm error flag |
