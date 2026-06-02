> **NOTE (2026-06)**: 시퀀스/모드/스텝 제어 기능은 MAIN.csv로 이관되었습니다.
> gmes.csv는 PC 통신 영역 매핑(D7000~D7239, D8000~D8239), Barcode Model Lookup, VAC SPC Logging만 담당합니다.

# REFRIGER CHARGING MACHINE — Function Spec: gmes.csv

> **Module**: `gmes.csv`  
> **Execution**: Always ON  
> **PLC**: Mitsubishi Q03UDV  
> **Role**: **메인 시퀀스 컨트롤러** — 전체 장비의 동작 모드, 스텝 제어, 사이클 관리 담당

---

## 1. Purpose

- Manual / Auto 모드 전환 및 관리
- Line / Gun 선택 및 Active Line 관리
- 전체 공정 Step State Machine 제어 (Line 0 / Line 1 독립)
- Type 분기 (CJ: D270=1→L1 Skip, D272=1→Gun B Skip, D276=0→Oil Skip)
- Done/NG 수신 → 다음 Step 전이
- Barcode Data 유효성 검증 및 Model# 매핑
- Lamp 상태 출력 (Green=Running, Red=Alarm, Yellow=Interlock)

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| M400 (HMI) | LINE 0 SELECT (Momentary → Self-Hold) |
| M401 (HMI) | LINE 1 SELECT |
| M408 (HMI) | GUN SELECT A |
| M409 (HMI) | GUN SELECT B |
| M40D (HMI) | BARCODE USE/NOT USE Toggle |
| M40E (HMI) | MANUAL/AUTO Toggle |
| M40F~M412 (HMI) | Manual Function Buttons (GunVac, UnitVac, VacCheck, Injection) |
| M413 (HMI) | START (Line 0) |
| M414 (HMI) | STOP (Line 0) |
| M415 (HMI) | START (Line 1) |
| M416 (HMI) | STOP (Line 1) |
| M300 (input.csv) | START_PB_L0 (Hardware) |
| M301 (input.csv) | STOP_PB_L0 (Hardware) |
| M303 (input.csv) | EMG_STOP |
| M30B (input.csv) | SAFETY_PLC_HEALTHY |
| L10~L19 | Line 0 Done/NG (각 서브 Function에서 SET) |
| L20~L29 | Line 1 Done/NG |
| L40~L4F | Alarm Latches |
| L50~L55 | Line 0 Interlock Status |
| L60~L65 | Line 1 Interlock Status |
| D270 | Line Count (Config) |
| D272 | Gun Per Line (Config) |
| D276 | Oil Mode (Config) |
| D7000 | Gas Type (PC Ethernet Write) — Line 1 |
| D8000 | Gas Type (PC Ethernet Write) — Line 2 |
| D7001 | Target Amount (PC Ethernet Write) — Line 1 |
| D8001 | Target Amount (PC Ethernet Write) — Line 2 |
| D7012 | Result Code (PLC → PC, Line 1) |
| D8012 | Result Code (PLC → PC, Line 2) |
| D7015 | Process Code (PLC → PC, Line 1) |
| D8015 | Process Code (PLC → PC, Line 2) |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| L70 | HMI Active Line = 0 (Self-Hold) |
| L71 | HMI Active Line = 1 (Self-Hold) |
| L72 | HMI Active Gun A (Self-Hold) |
| L73 | HMI Active Gun B (Self-Hold) |
| L1 | Auto Mode Flag |
| L2 | Manual Mode Flag |
| L74 | Interlock Use Flag |
| M10~M18 | Line 0 Step State (IDLE~COMPLETE) |
| M20~M28 | Line 1 Step State (IDLE~COMPLETE) |
| M4D | LAMP_GREEN (Running) → output.csv → Y31 |
| M4E | LAMP_RED (Alarm) → output.csv → Y32 |
| M4F | LAMP_YELLOW (Interlock) → output.csv → Y33 |
| D0 | L0 Model Number (매핑 결과) |
| D30 | L1 Model Number |
| D128 | Injection Setting Amount (Refrig) |
| D132 | Oil Injection Setting Amount |

---

## 4. Mode Management

### 4-1. Manual / Auto Toggle (M40E)

```
M40E (HMI Momentary) → PLC Rising Edge 검출
    └── L1 (Auto) 와 L2 (Manual) Toggle
        ├── L1=1, L2=0 → Auto Mode (START → Full Sequence)
        └── L1=0, L2=1 → Manual Mode (Button → Individual Function)
```

### 4-2. Line Select (M400 / M401)

```
M400 (LINE 0 SELECT Momentary) → Self-Hold → L70=1, L71=0
M401 (LINE 1 SELECT Momentary) → Self-Hold → L71=1, L70=0

(CJ: D270=1 → M401 입력 무시, L70 고정)
```

### 4-3. Gun Select (M408 / M409)

```
M408 (GUN A Momentary) → Self-Hold → L72=1, L73=0
M409 (GUN B Momentary) → Self-Hold → L73=1, L72=0

(CJ: D272=1 → M409 입력 무시, L72 고정)
```

### 4-4. PC Barcode Data 수신

> **Barcode는 PLC에서 처리하지 않음.**  
> PC가 Ethernet으로 D6980~D6999(D7980~D7999)에 Barcode Text를 Write.  
> PC가 Barcode를 파싱하여 Gas Type(D7000/D8000)과 Target Amount(D7001/D8001)를 별도 Write.  
> PLC는 D7000/D7001(D8000/D8001)의 값만 읽어서 사용.  
> PC는 D7220~/D8220~ 영역을 Read하여 현재 공정 진행중인 제품의 Barcode 확인.

#### AUTO START 시 Barcode Working Area 갱신

AUTO CHARGER START 시, PC가 Target Amount를 설정했으면 (D7001 > 0) PC가 보낸 Suffix 데이터를 Barcode 표시 영역으로 복사:

```
AUTO START (M413/M415) ─── Rising Edge
    │
    ├── [Line 1] LDD> D7001 K0  (Target Amount > 0?)
    │   ├── YES → BMOV D6870~D6879  D7220~D7239  K10
    │   │         (Suffix → Barcode Display Area)
    │   └── THEN → FMOV K0  D6870  K10
    │               (Source Clear — consume 방지)
    │
    └── [Line 2] LDD> D8001 K0  (D270≥2)
        ├── YES → BMOV D7870~D7879  D8220~D8239  K10
        └── THEN → FMOV K0  D7870  K10
```

> **조건**: D7001/D8001 > 0 → PC가 유효한 Injection Amount를 보냄 (데이터 갱신 완료).  
> **복사**: D6870~D6879 (Suffix 10 words) → D7220~D7239 (Barcode 20 words 중 앞 10 words).  
> **용도**: PC가 D7220~/D8220~를 Read하여 현재 진행중인 제품의 Barcode 확인.

---

## 5. Step State Machine

### 5-1. Auto Mode Sequence

```
START (M413/M415)
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│ IDLE (M10/M20)                                           │
│   → L0 (InitDone) AND Interlock OK(L50/L60)              │
│   → SET M11/M21 (PRECHECK)                               │
├──────────────────────────────────────────────────────────┤
│ PRECHECK (M11/M21)                                       │
│   → Interlock, Safety, Pressure, Coupler OK              │
│   → SET M12/M22 (GUN VAC)                               │
├──────────────────────────────────────────────────────────┤
│ GUN VAC (M12/M22)                                        │
│   → gunvac.csv 실행                                       │
│   → L10/L20(Done) → SET M13/M23 (UNIT VAC)              │
│   → L11/L21(NG) → Alarm Latch, SET M10/M20 (IDLE)     │
├──────────────────────────────────────────────────────────┤
│ UNIT VAC (M13/M23)                                       │
│   → unitvac.csv 실행                                      │
│   → L12/L22(Done) → SET M14/M24 (VAC CHECK)             │
│   → L13/L23(NG) → Alarm                               │
├──────────────────────────────────────────────────────────┤
│ VAC CHECK (M14/M24)                                      │
│   → vacchec.csv 실행                                      │
│   → L14/L24(Done) → [D276=1 → OIL] / [D276=0 → REFRIG] │
│   → L15/L25(NG) → Alarm                               │
├──────────────────────────────────────────────────────────┤
│ ┌─ [D276=1] OIL FAST INJ (M19/M29)                      │
│ │    → D62/76/90/104 Type 분기 (CJ)                       │
│ │    → refinj.csv (Oil Sequence)                          │
│ │    → L16/L26(Done) → REFRIG INJ                        │
│ └────────────────────────────────────────────────────────┤
│ REFRIG INJ (M15/M16, M25/M26)                            │
│   → refinj.csv (Refrig Sequence)                          │
│   → L16/L26(Done) → SET M17/M27 (EXHAUST)               │
│   → L17/L27(NG) → Alarm                               │
├──────────────────────────────────────────────────────────┤
│ EXHAUST (M17/M27)                                        │
│   → EXHAUST SOL ON (M33/M43)                             │
│   → T3 ≥ D8 → SET M18/M28 (COMPLETE)                    │
├──────────────────────────────────────────────────────────┤
│ COMPLETE (M18/M28)                                       │
│   → Injection Count+1                                    │
│   → Usage Accumulate (→ spc.csv)                          │
│   → CycleDone SET (L18/L28)                              │
│   → Auto → SET M10/M20 (IDLE)                            │
└──────────────────────────────────────────────────────────┘
```

### 5-2. Manual Mode

```
Manual Function Button (M40F~M412) → Momentary
    └── PLC Rising Edge 검출

M40F (GUN VAC)  → SET M12 (GUN VAC) → gunvac 실행 → Done/NG → IDLE
M410 (UNIT VAC) → SET M13 (UNIT VAC) → unitvac 실행 → Done/NG → IDLE
M411 (VAC CHECK)→ SET M14 (VAC CHECK) → vacchec 실행 → Done/NG → IDLE
M412 (INJECTION)→ SET M15 (INJECTION) → refinj 실행 → Done/NG → IDLE

(각 Function은 단독 실행 후 완료 시 자동 IDLE 복귀)
```

### 5-3. PC Process Code Update (D7015 / D8015)

매 Step 전이 시 PC 통신 영역의 Process Code를 갱신하여 PC가 현재 공정 상태를 알 수 있음.

| Step | D7015 (L1) / D8015 (L2) | Code |
|:----:|:------------------------:|:----:|
| IDLE | None Action | 0 |
| PRECHECK | — | 0 |
| GUN VAC | Gun EXHAUST | 1 |
| UNIT VAC | Unit EXHAUST | 2 |
| VAC CHECK | Vacuum check | 3 |
| REFRIG INJ | Charging | 4 |
| EXHAUST | — | 0 |
| COMPLETE | — | 0 |

```
LD  M12 (GUN VAC Step)
MOV K1  D7015    // Process Code = 1 (Gun EXHAUST)

LD  M13 (UNIT VAC Step)
MOV K2  D7015    // Process Code = 2 (Unit EXHAUST)

LD  M14 (VAC CHECK Step)
MOV K3  D7015    // Process Code = 3 (Vacuum check)

LD  M15 OR M16 (Injection Step)
MOV K4  D7015    // Process Code = 4 (Charging)

LD  M10 (IDLE)
MOV K0  D7015    // Process Code = 0 (None)
```

### 5-4. PC Result Code (D7012 / D8012)

Cycle 완료 시 Result Code 기록:

| Code | Meaning |
|:----:|---------|
| 1 | OK (정상 완료) |
| 2 | Vacuum NG |
| 3 | Gun exhaust NG |
| 4 | Unit exhaust NG |
| 5 | Vacuum check NG |
| 6 | Operator stop |
| 7 | Refrig none flow NG |
| 8 | Charging time over |
| 9 | Refrig back flow |
| 10 | GMES data not match model |
| 11 | GMES data receive time over |

```
// Cycle Complete → OK
LD  M18 (COMPLETE)
MOV K1  D7012    // Result Code = 1 (OK)

// 사용자 STOP
LD  M414 (STOP)
MOV K6  D7012    // Result Code = 6 (Operator stop)

// 알람 발생 시 해당 코드 매핑
```

### 5-5. STOP 처리

```
STOP (M414/M416 or M301/M311)
    │
    ├── RST 모든 Step Bit (M10~M28)
    ├── RST 모든 Solenoid Coil (M30~M4F)
    ├── RST 모든 Done/NG (L10~L29)
    ├── MOV K6 → D7012 (Result=Operator Stop)
    ├── EXHAUST SOL ON (M33/M43) → T3 타이머
    └── SET IDLE (M10/M20)
```

### 5-6. Emergency Stop

```
M303 (EMG_STOP = NC OPEN) → Immediate
    ├── SET L40 (EMG Alarm Latch)
    ├── RST ALL Step (M10~M28)
    ├── RST ALL Solenoid Coil (M30~M4F)
    └── 모든 동작 정지 (안전상태)
```

---

## 6. Interlock 체크

### 6-1. L0 Interlock (L50~L55)

```
L50 → L51(L0 Safety OK) AND L52(L0 Vacuum FB) AND
       L53(L0 Pressure Normal) AND L54(L0 Gun Connected) AND
       L55(L0 Refrig Supply OK) AND [방폭: M307=CLOSE]

L50=1 → Interlock OK → START 허용
L50=0 → START 불가, M4F(Yellow Lamp) ON
```

### 6-2. L1 Interlock (L60~L65)

```
L60 → L61(L1 Safety OK) AND L62(L1 Vacuum FB) AND
       L63(L1 Pressure Normal) AND L64(L1 Gun Connected) AND
       L65(L1 Refrig Supply OK) AND [방폭: M317=CLOSE]
```

---

## 7. CJ (Conditional Jump) 분기

| Condition | Jump Target | Description |
|:---------:|:-----------:|-------------|
| **D270=1** | Line 1 로직 전체 Skip | 1 Line 모드 → Line 1 Step/Interlock/Output 미사용 |
| **D272=1** | Gun B 로직 Skip | 1 Gun/Line 모드 → Gun B Step/Output 미사용 |
| **D276=0** | Oil Injection Skip | REF Only → OIL Step 건너뛰고 직접 REFRIG INJ |
| **D276=1** | Oil Injection 실행 | REF+OIL → Oil → Refrig 순차 |

```
// L1 Skip 예시
LD= D270 K1    // 1 Line 모드
CJ L1_SKIP     // Line 1 관련 로직 모두 Jump

L1_SKIP:
// Line 0 로직만 계속
```

---

## 8. Lamp Control

| Lamp | M | Y | Condition |
|:----:|::|::|-----------|
| GREEN | M4D | Y31 | Running (M10~M18 any ON) AND No Alarm |
| RED | M4E | Y32 | Any L40~L4F ON |
| YELLOW | M4F | Y33 | Interlock Not OK (L50/L60=0) AND Running |

---

## 9. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD=` | Configuration 값 비교 (D270, D272, D276) |
| `AND=` | Interlock 조건 다중 AND |
| `OR=` | OR 조건 |
| `SET` | Step/Mode Flag 설정 |
| `RST` | Step/Mode Flag 해제 |
| `OUT` | Lamp 출력 |
| `MOV` | Model# 데이터 전송 |
| `CJ` | 조건부 점프 (Type 분기, Line/Gun Skip) |
| `BMOV` | Barcode Data Block 복사 |
| `FMOV` | Barcode Working Area Clear |
| `PLS` | Rising Edge 검출 (HMI Button) |
