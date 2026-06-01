# REFRIGER CHARGING MACHINE — Function Spec: refinj.csv

> **Module**: `refinj.csv`  
> **Execution**: Step 진입 시 (M15/M16/M19/M1A=L0, M25/M26/M29/M2A=L1)  
> **PLC**: Mitsubishi Q03UDV  
> **Role**: **가장 복잡한 Function** — Type 분기, Oil+Refrig 순차 제어, 고속→저속 전환

---

## 1. Purpose

냉매(Refrigerant) 및 오일(Oil) 주입 공정 전체를 제어.

- **Gun Type (0=1-Sol Base / 1=H+L Fast+Normal)** 에 따라 솔레노이드 구동 방식 분기
- **Oil Mode (D276=0 REF Only / D276=1 REF+OIL)** 에 따라 Oil 선주입 후 Refrig 주입
- HSC(고속카운터) 펄스 적산 → 주입량 계산
- 목표량 ± 공차(Tolerance) 도달 확인 → Done/NG 판정
- 주입 완료 후 Gas Exhaust → Complete

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| M15 (L0) / M25 (L1) | Step: REFRIG FAST INJ |
| M16 (L0) / M26 (L1) | Step: REFRIG NORMAL INJ |
| M19 (L0) / M29 (L1) | Step: OIL FAST INJ |
| M1A (L0) / M2A (L1) | Step: OIL NORMAL INJ |
| M17 (L0) / M27 (L1) | Step: EXHAUST |
| D62/D76/D90/D104 | Gun Type (0=Base, 1=H+L) — Active Gun 기준 |
| D64~D65 | Refrig Injection Volume (32-bit, g) — Active Gun |
| D72~D73 | Oil Injection Volume (32-bit, g) — Active Gun |
| D10 / D40 | Refrig High-Speed Inj Stop (g) |
| D12 / D42 | Oil High-Speed Inj Stop (g) |
| D26 / D54 | Refrig Injection Tolerance (±g) |
| D28 / D56 | Oil Injection Tolerance (±g) |
| D8 / D38 | Gas Exhaust Time (0.1 sec) |
| D276 | Oil Mode (0=REF Only, 1=REF+OIL) |
| HSC | Flow Meter Pulse (고속카운터, 별도 채널) |
| M304~M305 | Gun Coupler Sensors L0 |
| M314~M315 | Gun Coupler Sensors L1 |
| M60~M63 | Injection Active Flags (1 per Gun) |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| M34 | REFRIG BASE/FAST SOL L0 G0 → Y13 |
| M35 | REFRIG NORMAL SOL L0 G0 → Y14 |
| M36 | OIL BASE/FAST SOL L0 G0 → Y15 |
| M37 | OIL NORMAL SOL L0 G0 → Y16 |
| M38~M3B | L0 G1 Equivalent (Y17~Y1A) |
| M44~M4B | L1 G0/G1 Equivalent (Y23~Y2A) |
| M60~M63 | Injection Active Flag (각 Gun) |
| T3 | Exhaust Timer |
| T4 | Refrig Fast Injection Timer |
| T5 | Refrig Normal Injection Timer |
| T6 | Oil Injection Timer |
| L16 (L0) / L26 (L1) | Injection Done |
| L17 (L0) / L27 (L1) | Injection NG |
| L45 | Injection Timeout Alarm |
| L46 | Injection Over Alarm |
| L47 | Injection Under Alarm |
| D124 | Charging Pulse (HMI Display) |
| D128 | Injection Setting Amount (Refrig, g) |
| D130 | Actual Injection Volume (Refrig, g) |
| D132 | Oil Injection Setting Amount (g) |
| D134 | Actual Oil Injection Volume (g) |
| D126 | Injection Time (0.1 sec) |

---

## 4. Injection Sequences

### 4-1. Type 0 (1-Sol Base) + D276=0 (REF Only)

```
VacCheck Done
    │
    ▼
[REFRIG FAST INJ]  ← M15 진입 (Type 0은 Base만)
    ├── SET M34 (REFRIG BASE SOL ON)
    ├── SET M60 (Injection Active)
    ├── T4 Start
    ├── HSC Pulse 적산 시작
    │
    ├── 적산량 ≥ D64 (Target Volume)?
    │   → RST M34 (SOL OFF)
    │   → SET L16 (Injection Done 준비)
    │
    ├── 적산량 ≥ D64 + D26 (Over Tolerance)?
    │   → SET L17 (Injection NG), SET L46 (Over Alarm)
    │
    └── T4 ≥ Timeout?
        → SET L17, SET L45 (Timeout Alarm)
    │
    ▼
[EXHAUST]  ← M17 진입
    ├── SET M33 (EXHAUST SOL ON)
    ├── T3 Start
    │
    ├── T3 ≥ D8?
    │   → RST M33 (SOL OFF)
    │   → SET L16 (Injection Done)
    │
    └── T3 ≥ D8+5s (Timeout)?
        → SET L17, SET L45
    │
    ▼
[COMPLETE] ← M18 진입 (gmes)
    ├── D280+ (Total Usage), D282+ (Count)
    ├── RST M60 (Injection Active)
    ├── RST M15~M17
    └── SET M10 (IDLE)
```

### 4-2. Type 0 (1-Sol Base) + D276=1 (REF+OIL)

```
VacCheck Done
    │
    ▼
[OIL FAST INJ]  ← M19 진입
    ├── SET M36 (OIL BASE SOL ON)
    ├── T6 Start
    ├── Oil Volume 적산
    │
    ├── 적산량 ≥ D72 (Oil Target)?
    │   → RST M36 (Oil SOL OFF)
    │   → SET M15 (REFRIG FAST INJ 진입)
    │
    └── T6 ≥ Timeout → NG
    │
    ▼
[REFRIG FAST INJ]  ← M15 진입
    ├── SET M34 (REFRIG BASE SOL ON)
    ├── T4 Start
    ├── Refrig Volume 적산
    │
    ├── 적산량 ≥ D64 (Refrig Target)?
    │   → RST M34
    │   → EXHAUST → COMPLETE
    │
    └── Error → NG
```

### 4-3. Type 1 (H+L Fast+Normal) + D276=0 (REF Only)

```
VacCheck Done
    │
    ▼
[REFRIG FAST INJ]  ← M15 진입
    ├── SET M34 (REFRIG FAST SOL ON)  ← Type1: Fast 역할
    ├── SET M35 (REFRIG NORMAL SOL ON) ← 같이 ON
    ├── 고속 적산 (Fast + Normal 동시)
    │
    ├── 적산량 ≥ D10 (Fast Stop Setting)?
    │   → RST M34 (Fast SOL OFF), Normal만 유지
    │   → SET M16 (REFRIG NORMAL INJ)
    │
    └── Error → NG
    │
    ▼
[REFRIG NORMAL INJ]  ← M16 진입
    ├── M35 ON 유지 (Normal SOL)
    ├── 저속 적산
    │
    ├── 적산량 ≥ D64 (Target Volume)?
    │   → RST M35 (Normal SOL OFF)
    │   → Tolerance Check
    │       ├── |Actual - Target| ≤ D26 → OK → EXHAUST
    │       ├── Actual > Target + D26 → L46 (Over)
    │       └── Actual < Target - D26 → L47 (Under)
    │
    └── Error → NG
    │
    ▼
[EXHAUST → COMPLETE] (동일)
```

### 4-4. Type 1 (H+L) + D276=1 (REF+OIL)

```
VacCheck Done
    │
    ▼
[OIL FAST INJ]  ← M19 진입
    ├── SET M36 (OIL FAST SOL ON)
    ├── SET M37 (OIL NORMAL SOL ON)
    ├── Oil 고속 적산
    │
    ├── 적산 ≥ D12 (Oil Fast Stop)?
    │   → RST M36 (Oil Fast OFF)
    │   → SET M1A (OIL NORMAL INJ)
    │
    └── Error → NG
    │
    ▼
[OIL NORMAL INJ]  ← M1A 진입
    ├── M37 ON 유지 (Oil Normal)
    ├── 적산 ≥ D72 (Oil Target)?
    │   → RST M37
    │   → SET M15 (REFRIG FAST INJ 진입)
    │
    └── Error → NG
    │
    ▼
[REFRIG FAST INJ]  ← M15 진입
    ├── SET M34 (REFRIG FAST)
    ├── SET M35 (REFRIG NORMAL)
    ├── Refrig 고속 적산
    │
    ├── 적산 ≥ D10 (RF Fast Stop)?
    │   → RST M34 (Fast OFF)
    │   → SET M16 (REFRIG NORMAL INJ)
    │
    └── Error → NG
    │
    ▼
[REFRIG NORMAL INJ]  ← M16 진입
    ├── M35 ON 유지 (Normal)
    ├── 적산 ≥ D64 (RF Target)?
    │   → RST M35
    │   → Tolerance Check
    │   → EXHAUST
    │
    └── Error → NG
    │
    ▼
[EXHAUST → COMPLETE]
```

---

## 5. CJ (Conditional Jump) — Type 분기

```
// Active Gun의 Type 읽기
// D62(G0)/D76(G1)/D90(G2)/D104(G3) 중 Active Gun 선택

LD= D62 K0    // Type 0?
CJ TYPE0_SEQ

LD= D62 K1    // Type 1?
CJ TYPE1_SEQ

TYPE0_SEQ:
// 1-Sol Base Sequence
...

TYPE1_SEQ:
// H+L Fast+Normal Sequence
...
```

---

## 6. Volume Calculation

```
Pulse_Count = HSC (Flow Meter)
Volume = Pulse_Count × Scale_Factor

// Scale Factor는 교정값(D66/D80/D94/D108)과 HMI Cal(D68/D82/D96/D110) 적용
// 사용자 보정: Volume = Pulse × (1 + Corr/1000) + HMI_Cal

Actual_Volume = Pulse_Count × (1000 + Correction) / 1000 + HMI_Cal
```

---

## 7. Tolerance Check

```
Difference = |Actual_Volume - Target_Volume|

|Difference| ≤ D26(D54) → Injection OK → Done
Difference > 0 AND > D26 → Injection Over → NG + L46
Difference < 0 AND |Difference| > D26 → Injection Under → NG + L47
```

---

## 8. Gas Exhaust

주입 완료 후 또는 오류 정지 시 항상 Gas Exhaust 실행:

```
M17/M27 진입 조건:
    1. Injection Done (정상 완료)
    2. Injection NG (오류 정지)
    3. STOP 감지 (사용자 정지)
    4. EMG (비상 정지)

실행:
    SET M33/M43 (EXHAUST SOL ON)
    T3 Start
    T3 ≥ D8/D38 → RST M33/M43
    → COMPLETE (M18/M28)
```

---

## 9. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| Injection Timeout | 적산 변화 없음 × 시간 초과 | SET L45, All SOL OFF → Exhaust |
| Injection Over | Actual > Target + Tolerance | SET L46, NG |
| Injection Under | Actual < Target - Tolerance | SET L47, NG (±공차) |
| Gun Coupler OFF | 센서 OFF during injection | 즉시 All SOL OFF, Alarm |
| High-Speed NG | Fast Stop 미도달 (Type 1) | Normal만으로 계속 |

---

## 10. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Step / Sensor read |
| `AND` | Safety + 조건 체크 |
| `D+` | 적산 (Volume Accumulate) |
| `D-` | 차분 계산 (Volume Difference) |
| `D*` | Scale Factor 곱셈 |
| `D/` | Pulse → Volume 변환 |
| `LDD=` | 적산량 = 목표량? (Done 조건) |
| `LDD<=` | 적산량 ≤ 목표량 (진행 중) |
| `LDD>=` | 적산량 ≥ 목표량 (Over 체크) |
| `MOV` | 16-bit 데이터 전송 |
| `DMOV` | 32-bit Volume 전송 |
| `SET` | SOL ON / Step SET / Done |
| `RST` | SOL OFF / Step RST |
| `TMR` | Timer Start |
| `CJ` | Type 분기 (Gun Type 0 / 1) |
| `PLS` | Rising Edge 검출 |
