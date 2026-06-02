# REFRIGER CHARGING MACHINE — PLC Program Structure Design

> **Target PLC**: Mitsubishi QCPU (Q mode) Q03UDV  
> **HMI Spec**: REFRIGER_CHARGING_MACHINE.md  
> **IL CSV Format**: GX_WORKS2_IL_Spec.md  
> **Goal**: 1 Line/1 Gun, 1 Line/2 Gun, 2 Line/2 Gun, 2 Line/4 Gun 모든 구성에서 동작하는 단일 표준 프로그램

---

## 0. 시스템 구성 (System Configuration)

### 0-1. 지원 구성 (Variations)

| Variation | Line | Gun/Line | Total Gun |
|-----------|:----:|:--------:|:---------:|
| **1L1G** | 1 | 1 | 1 |
| **1L2G** | 1 | 2 | 2 |
| **2L2G** | 2 | 1 | 2 |
| **2L4G** | 2 | 2 | 4 |

> **모든 Variation 단일 표준 프로그램으로 동작. D228, D230 파라미터로 구성 결정.**
> **REF/REF+OIL 모드는 D234 파라미터로 전환. D234=0 → Refrigerant Only, D234=1 → Refrigerant + Oil.**
> **REF+OIL 시 오일은 Gun Type과 동일한 Solenoid 구조를 가짐 (미러링). 오일 → 냉매 순차 주입.**

### 0-2. 구성 파라미터 (PLC D-Register)

| Addr | 항목 | Range | 설명 |
|---|---|---|---|
| **D228** | Line Count | 1~2 | 운전 라인 수. 1이면 Line 1 미사용 |
| **D230** | Gun Per Line | 1~2 | 라인당 건 수 |
| **D232** | Total Gun (= D228 × D230) | 1~4 | PLC 연산, Read-Only |
| **D234** | Oil Mode | 0~1 | **0=REF Only, 1=REF+OIL** (오일은 Gun Type과 동일 Sol 구조) |

> 구성(D228/D230) 변경 시 PLC STOP 후 다운로드. D234는 운전 중 변경 가능 (모드 전환).

### 0-3. Line / Gun 개념

```
Line 1 ──┬── Gun A ──┐
         │           ├── 진공계통(공유), 한 번에 1 Gun만 사용
         └── Gun B ──┘

Line 2 ──┬── Gun A ──┐
         │           ├── 진공계통(공유), 한 번에 1 Gun만 사용
         └── Gun B ──┘
```

- **Line**: 독립된 진공 펌프 + 진공 배관 + 유닛. Line 간 완전 독립 운전.
- **Gun**: 동일 Line 내 진공계 공유, **동시 사용 불가**. HMI로 작업 건 선택.
- **2 Gun/Line**: 동일 Line에 Gun A, Gun B 장착 (서로 다른 Type 가능). 작업 시 1개 선택.

### 0-4. Gun Type

> **Gun Type은 Refrigerant의 Solenoid 구조만 정의. Oil Mode(D234=1) 시 동일한 구조가 Oil에도 적용됨 (미러링).**

| Type | 명칭 | Refrig Sol 구조 | Sol Count (D234=0) | Sol Count (D234=1) |
|:----:|------|:---------------:|:------------------:|:------------------:|
| **0** | 1-Sol (Base) | Base 1개 | Refrig 1개 = **1 Sol** | Oil 1 + Refrig 1 = **2 Sol** |
| **1** | H+L (Fast+Normal) | Fast 1 + Normal 1 | Refrig H+L = **2 Sol** | Oil H+L + Refrig H+L = **4 Sol** |

| Type | 주입 시퀀스 (REF Only) | 주입 시퀀스 (REF+OIL) |
|:----:|----------------------|----------------------|
| **0** | `Base_Sol ON → 목표량 → OFF` | `Oil_Sol ON → Oil목표 → OFF → Refrig_Sol ON → 목표 → OFF` |
| **1** | `H+L 동시 ON → 고속중단 → H OFF, L로 목표` | `Oil_H+L ON → Oil고속중단 → Oil H OFF, Oil L로 완료 → Refrig_H+L ON → Refrig고속중단 → H OFF, L로 목표` |

> **고속+저속 동시 Open**: 고속·저속 솔레노이드가 함께 열리고, 고속 중단 설정량 도달 시 고속만 닫히며 저속으로 최종 목표량까지 주입.
> **오일→냉매 순차**: 오일 주입이 먼저 완료된 후 냉매 주입 시작. 각 주입은 독립적인 목표량을 가짐.
> **Gun Type은 Gun별 설정 (D32/D46/D60/D74). 동일 Line 내 Gun A/B가 서로 다른 Type 가능.**

### 0-5. Gun Index 공식

```
Gun Global Index = Line × GunPerLine(D230) + GunLocal
  - Line ∈ {0, 1}     (Line 1 → 0, Line 2 → 1)
  - GunLocal ∈ {0, 1} (Gun A → 0, Gun B → 1)
  - 예: Line 2 Gun B → 1×2+1 = 3 (Global Gun 3)
```

> 2 Gun/Line 구성에서도 **동일 Line내 1개 Gun만 활성**. HMI Gun Select로 작업 건 결정.

---

## 1. I/O 요구사항 분석 (HMI → PLC 신호 매핑)

### 1-1. HMI Button → PLC 내부 릴레이 (M, Momentary)

> **HMI 버튼은 전부 Momentary (누를 때만 ON, 떼면 OFF).**  
> 상태 기억이 필요한 버튼은 PLC에서 Self-Hold / Toggle / Oneshot 처리.  
> 정전 유지가 필요한 상태는 **L device** 사용 (→ `DEVICE_MAP.md` §1 L Device 참조).

| HMI Button | M_Addr | PLC 처리 | 상태 저장 |
|------------|:------:|:--------:|:---------:|
| **LINE 0 SELECT** | `M400` | Self-Hold | `L70` |
| **LINE 1 SELECT** | `M401` | Self-Hold | `L71` |
| INTERLOCK USE/NOT USE | `M402` | Toggle | `L74` |
| ALARM RESET | `M403` | Oneshot | — |
| BUZZER STOP | `M404` | Oneshot | — |
| USER SETTING SCREEN | `M405` | Oneshot | — |
| PARAMETER SETTING SCREEN | `M406` | Oneshot | — |
| ALARM SCREEN | `M407` | Oneshot | — |
| **GUN SELECT A** (현재 Line내) | `M408` | Self-Hold | `L72` |
| **GUN SELECT B** (현재 Line내) | `M409` | Self-Hold | `L73` |
| NUMBER OF INJECTIONS RESET | `M40A` | Oneshot | — |
| MODEL SELECT | `M40B` | Oneshot | — |
| VACUUM PUMP ON/OFF | `M40C` | Toggle | L bit |
| BARCODE USE/NOT USE | `M40D` | Toggle | `L3` |
| MANUAL/AUTO | `M40E` | Toggle | `L1/L2` |
| GUN VACUUM (Manual) | `M40F` | Oneshot | — |
| UNIT VACUUM (Manual) | `M410` | Oneshot | — |
| VACUUM CHECK (Manual) | `M411` | Oneshot | — |
| REFRIGER INJECTION (Manual) | `M412` | Oneshot | — |
| **START (Line 0)** | `M413` | Rising Edge | — |
| **STOP (Line 0)** | `M414` | Rising Edge | — |
| **START (Line 1)** | `M415` | Rising Edge | — |
| **STOP (Line 1)** | `M416` | Rising Edge | — |

> **Line Select**: `M400/M401` 로 활성 Line을 선택 (PLC Self-Hold → L70/L71). D228 값에 따라 1 Line 구성 시 Line 1 버튼 비활성.  
> **Gun Select**: `M408/M409` 로 현재 선택된 Line 내에서 Gun 선택 (PLC Self-Hold → L72/L73). D230 값에 따라 1 Gun/Line 구성 시 Gun B 버튼 비활성.  
> **Line Current**: PLC 내부에서 현재 HMI 제어 대상 Line을 L bit로 유지 (L70=Line0 Active, L71=Line1 Active).

### 1-2. 물리적 I/O 추정 (2 Line 기준, 참고용)

> **실제 I/O 할당은 `input.csv` / `output.csv` 에서 정의.**  
> 프로그램 본체는 X/Y를 직접 참조하지 않고 M만 사용.  
> X/Y 주소 변경 시 `input.csv` / `output.csv` 만 수정하면 됨.

| Signal Class | Count | Device Range | Mapping File |
|---|---|---|---|
| **DI L0** | 16점 | X00~X0F | `input.csv` (→ M300~M30F) |
| **DI L1** | 16점 | X10~X1F | `input.csv` (→ M310~M31F) |
| **DO L0** | 16점 | Y10~Y1F | `output.csv` (M30~M3F → Y) |
| **DO L1** | 16점 | Y20~Y2F | `output.csv` (M40~M4F → Y) |
| **DO Global** | 6점 | Y30~Y3F | `output.csv` (M4C~M4F → Y) |
| **AI L0** | 3ch | — | `ad.csv` (D150~D161) |
| **AI L1** | 3ch | — | `ad.csv` (D162~D173) |
| **HSC** | 2ch | — | Flow Meter Pulse × 2 Line |
| **RS-485** | 1ch | — | Vacuum / Pressure / Temp Sensors |

> 상세 매핑 테이블: `INPUT_OUTPUT_MAP.md` 참조

### 1-3. Safety PLC 인터페이스

| Signal | Device | Direction |
|---|---|---|
| Safety PLC Healthy | `M30B` (← X0B) | Safety → Main |
| Safety Reset Request (Hard) | `M302` (← X02) | Push Button → Main |
| Main → Safety Reset Ack | `M50` → Y1C | Main → Safety |
| Emergency Stop Active | `L40` | Internal latch |

---

## 2. POU (Program Organization Unit) 모듈 구조

```
REF/
├── idata.csv     # 입력 매핑 / 초기화 / 상시 실행
├── gmes.csv      # 메인 시퀀스 제어 / 모드 전환 / 사이클 관리
├── setting.csv   # 파라미터 설정 / 사용자 설정 (PLC ↔ HMI)
├── gunvac.csv    # 건 진공 시퀀스
├── unitvac.csv   # 유닛 진공 시퀀스
├── vacchec.csv   # 진공 체크 (리크 테스트) 시퀀스
├── refinj.csv    # 냉매 주입 시퀀스 (고속→저속→정지)
├── alarm.csv     # 알람 검출 / 알람 리셋 / 부저 제어
├── ad.csv        # 아날로그 입력 처리 (진공도, 온도, 압력)
├── 485.csv       # RS-485 통신 (진공/압력/온도 센서 데이터 수신)
└── spc.csv       # 통계 데이터 (사용량 누계, 주입 횟수, 펄스 누계)
```

### 2-1. 모듈별 책임

| POU | 책임 | 실행 조건 |
|---|---|---|
| **idata.csv** | X→M 매핑, 초기 기동 시 D/T 초기화, 상시 ON 처리 | Always ON |
| **gmes.csv** | PC 통신 영역 갱신 (D7000~D7239 L1, D8000~D8239 L2) — Gas Type/Result/Process Code/SPC Data | Always ON |
| **MAIN.csv** | Auto/Manual 모드 전환, Line/Gun 선택, Step State Machine, Interlock, READY/START, STOP/EMG, Lamp 제어 | Always ON |
| **setting.csv** | Config(D270/D272) → D274 계산, Line별 Preset Injection Table(D60~D84 L0, D88~D112 L1) 관리 | Always ON |
| **gunvac.csv** | 건 진공용 솔레노이드 ON, 진공 시간 T카운트, 진공도 도달 체크, 타임아웃 알람 | 진공 스텝 진입 시 |
| **unitvac.csv** | 유닛 진공용 솔레노이드 ON, 진공 시간 T카운트, 진공도 도달 체크, 타임아웃 알람 | 진공 스텝 진입 시 |
| **vacchec.csv** | 진공 밸브 CLOSE 후 ΔP 감시, 리크 판정 (ΔP > 허용치 → 알람) | 진공 체크 스텝 진입 시 |
| **refinj.csv** | 고속 주입 밸브 ON → 설정량 도달 → 저속 주입 → 목표량 ±공차 도달 → OFF, 펄스 카운트 적산, 주입량 계산 | 주입 스텝 진입 시 |
| **alarm.csv** | 알람 조건 OR 수집, 알람 래치, 부저 출력, 알람 리셋 처리, 인터락 신호 출력 | Always ON |
| **ad.csv** | AI Raw → Engineering Unit 변환 (Scaling), 진공도/온도/압력 현재값 D레지스터 갱신 | Always ON |
| **485.csv** | RS-485 수신 버퍼 → D레지스터 파싱 (진공/압력/온도 센서) | Always ON |
| **spc.csv** | 냉매 총 사용량 적산 (32-bit), 주입 횟수 카운트 (16-bit), 펄스 누계 (32-bit), 실주입량/설정량 기록 | 사이클 완료 시 |

---

## 3. 디바이스 맵 (Device Map)

> **상세 Device Map**: `DEVICE_MAP.md` — 모든 L/M/D/X/Y/T 할당 및 래치 설정 정의  
> **I/O Mapping**: `INPUT_OUTPUT_MAP.md` — X→M (input.csv) / M→Y (output.csv) / HMI 버튼 매핑

### 3-1. 핵심 할당 원칙

| Device | 용도 | Retentive |
|:------:|------|:---------:|
| **L** | 정전유지 Bit (Done/NG, 알람 Latch, 운전모드, Line/Gun 선택) | Y (전체 래치) |
| **M** | Volatile Bit (Step 상태, Solenoid Coil Image, HMI 버퍼, DI Mirror) | N |
| **D** | 파라미터 / 설정 / 누계 / 통신 (D0~D299) | Y (전체 래치) |
| **D** | Scratch / Temp (D300~) | N |
| **X** | 물리적 입력 — `input.csv` 통해 M Mirror | — |
| **Y** | 물리적 출력 — `output.csv` 통해 M Coil Image 매핑 | — |

### 3-2. L Device 요약 (정전유지 Bit)

| Range | 용도 |
|:-----:|------|
| L0~L9 | System (InitDone, Auto/Manual Mode, Barcode Flag) |
| L10~L19 | Line 0 Done/NG (GunVac, UnitVac, VacCheck, Inj, Cycle) |
| L20~L29 | Line 1 Done/NG |
| L30~L3F | 예비 |
| L40~L4F | Alarm Latch (EMG, Safety, Timeout, Leak, Pressure, Temp...) |
| L50~L5F | Line 0 Interlock Status |
| L60~L6F | Line 1 Interlock Status |
| L70~L7F | HMI Select (Line, Gun, Interlock Flag) |
| L80~L8F | SPC 누계 플래그 |
| L90~L999 | 예비 |

### 3-3. M Device 요약 (Volatile Bit)

| Range | 용도 |
|:-----:|------|
| M0~M9 | System (AlwaysON, Clock, Initial Pulse) |
| M10~M19 | Line 0 Step State |
| M20~M29 | Line 1 Step State |
| M30~M6F | Solenoid Coil Image + Injection Active (→ output.csv) |
| M70~M2FF | 예비 |
| M300~M31F | Physical Input Mirror (← input.csv) |
| M320~M3FF | 예비 |
| M400~M41F | HMI Button Buffer |
| M420~M4FF | 예비 |
| M500~M50F | Communication Flags |

### 3-4. D Device 요약 (Data Register)

> **모든 D 레지스터는 짝수 주소 할당 (32-bit 확장 대비 Dn+1 예약).**  
> **D0~D299는 전 범위 Battery Backup (래치).**

#### Parameter — Line 0 (D0~D29)

| Addr | Width | 항목 | Unit | Note |
|:----:|:-----:|------|:----:|------|
| D0 | 16 | L0 Model Number | — | |
| D2 | 16 | Gun Vacuum Time | 0.1 sec | |
| D4 | 16 | Unit Vacuum Time | 0.1 sec | |
| D6 | 16 | Vacuum Check Time | 0.1 sec | |
| D8 | 16 | Gas Exhaust Time | 0.1 sec | |
| D10 | 16 | Refrig High-Speed Inj Stop | g | |
| D12 | 16 | Oil High-Speed Inj Stop | g | D234=1 |
| D14 | **32** | Refriger Bombe Alarm Setting | Kg | Global |
| D16 | **32** | Refriger Gas Used Amount | Kg | Global |
| D18 | 16 | Pressure High Limit | kgf/㎠ | |
| D20 | 16 | Pressure Low Limit | kgf/㎠ | |
| D22 | **32** | Unit Vacuum Setting Value | Torr | |
| D24 | **32** | Vacuum Check Setting Value | Torr | |
| D26 | 16 | Refrig Injection Tolerance | ±g | |
| D28 | 16 | Oil Injection Tolerance | ±g | |

#### Parameter — Line 1 (D30~D59)

| Addr | Width | 항목 | Addr | Width | 항목 |
|:----:|:-----:|------|:----:|:-----:|------|
| D30 | 16 | L1 Model Number | D46 | 16 | Pressure High Limit |
| D32 | 16 | Gun Vacuum Time | D48 | 16 | Pressure Low Limit |
| D34 | 16 | Unit Vacuum Time | D50 | **32** | Unit Vacuum Setting |
| D36 | 16 | Vacuum Check Time | D52 | **32** | Vacuum Check Setting |
| D38 | 16 | Gas Exhaust Time | D54 | 16 | Refrig Tolerance |
| D40 | 16 | Refrig H-Speed Stop | D56 | 16 | Oil Tolerance |
| D42 | 16 | Oil H-Speed Stop | D58~D59 | — | 예비 |

#### User Settings — Gun당 14 words (D60~D115)

| Global Gun | Line | Gun | Base | Type | Refrig Vol(32) | Corr | HMI Cal | Batch | Oil Vol(32) |
|:----------:|:----:|:---:|:----:|:----:|:--------------:|:----:|:-------:|:-----:|:-----------:|
| 0 (G0) | 0 | 0 | D60 | D62 | D64~D65 | D66 | D68 | D70 | D72~D73 |
| 1 (G1) | 0 | 1 | D74 | D76 | D78~D79 | D80 | D82 | D84 | D86~D87 |
| 2 (G2) | 1 | 0 | D88 | D90 | D92~D93 | D94 | D96 | D98 | D100~D101 |
| 3 (G3) | 1 | 1 | D102 | D104 | D106~D107 | D108 | D110 | D112 | D114~D115 |

> Gun Type: `D62/D76/D90/D104` — 0=1-Sol(Base), 1=H+L(Fast+Normal)

#### Configuration (D270~D278)

| Addr | 항목 | Range | 설명 |
|:----:|------|:-----:|------|
| **D270** | Line Count | 1~2 | 운전 라인 수 (setting.csv) |
| **D272** | Gun Per Line | 1~2 | 라인당 건 수 (setting.csv) |
| **D274** | Total Gun | 1~4 | PLC 연산, Read-Only |
| **D276** | Oil Mode | 0~1 | 0=REF Only, 1=REF+OIL |

> 나머지 D 영역 (Operation Display, Analog, Barcode, SPC): `DEVICE_MAP.md` §3 상세 참조.

### 10-2. 봄베 알람

```
D10~D11 = 봄베 알람 설정값 (Kg)
D12~D13 = 냉매 사용량 누계 (HMI 표시용) → D280~D281 참조
D12~D13 ≥ D10~D11 → M101 Alarm (Refriger Bombe Low)
```

---

## 11. 아날로그 처리 (ad.csv)

### 11-1. 스케일링 (Line별)

| Channel | Line | Raw Addr | EU Addr | Range |
|---|---|---|---|---|
| Pressure | L0 | D120 | D122 | D14~D16 (kgf/㎠) |
| Pressure | L1 | D132 | D134 | (D228≥2) |
| Temperature | L0 | D124 | D126 | -20.0~80.0 (0.1℃) |
| Temperature | L1 | D136 | D138 | (D228≥2) |
| Vacuum | L0 | D128 | D130~D131 | 0~760 (Torr) |
| Vacuum | L1 | D140 | D142~D143 | (D228≥2) |

### 11-2. 샘플링

```
매 스캔 AD 변환값을 Raw 영역에 저장
이동평균 or 1차 지연 필터 적용 후 EU 갱신
Operation Display(D96~D107)에 EU 값 복사 (미러링)
```

---

## 12. 데이터 플로우 요약

```
┌──────────┐     ┌──────────┐     ┌───────────┐
│  HMI     │     │   PLC    │     │  FIELD    │
│ (GOT)    │     │ (Q03UDV) │     │  I/O      │
└─────┬────┘     └────┬─────┘     └─────┬─────┘
      │               │                │
      │ M50~M72 ─────▶│                │  Buttons (Write)
      │◀──── D0~D107  │                │  Display (Read)
      │               │                │
      │               │◀─── X00~X1F ───│  DI × 2 Line
      │               │──── Y10~Y2F ───▶│  DO × 2 Line
      │               │                │
      │               │◀─── AI Ch ─────│  P/T/V × 2 Line
      │               │◀── HSC ×2 ─────│  Flow Meter × 2 Line


┌──────────┐     ┌──────────┐
│   PC     │     │   PLC    │
│ (Host)   │     │ (Q03UDV) │
└─────┬────┘     └────┬─────┘
      │               │
      │──▶ D190~D209  │  PC Write Area (Line 0)
      │──▶ D230~D249  │  PC Write Area (Line 1)
      │◀── D190=0     │  L0 Complete → Clear
      │◀── D230=0     │  L1 Complete → Clear
```

```
HMI Write → M400~M416 (Momentary) → PLC Self-Hold/Toggle → L70~L73(Line/Gun Sel)
Line 0: M10~M18 Step → L50~L55 Interlock(L bit) → M30~M3F Control → output.csv → Y
Line 1: M20~M28 Step → L60~L65 Interlock(L bit) → M40~M4F Control → output.csv → Y
D270=1 이면 Line 1 로직 Skip (1 Line 모드)
D272=1 이면 Gun B 로직 Skip (1 Gun/Line 모드)
PC Write → D180~D189(L0) / D230~D249(L1) → START → Working Area → Cycle 사용
Cycle Complete → Write Area 0 Clear → PC 확인 후 다음 Write
AI Raw → ad.csv → Line별 EU → vacchec / alarm / gmes
Pulse Counter → refinj.csv → Charging Pulse, Actual Volume
refinj.csv → spc.csv → Cumulative Usage (Global 합산)
```

---

## 13. Safety PLC 연동

```
[Main PLC]                          [Safety PLC]
    │                                    │
│◀─────── SafetyOK (M30B ← X0B) ────│ (Healthy Signal → L51/L61)
│─────── M50 → Y1C Reset Ack ──────▶│
│  EMG Stop (M303 ← X03) ───────────│ Emergency Stop Relay
│  Safety Reset PB (M302 ← X02) ────▶│ Reset Request

Safety PLC가 독립적으로 Emergency Stop 회로를 감시. Main PLC는 Safety PLC Healthy 신호(M30B)가 ON일 때만 동작. Reset Ack는 M50 → Y1C 사용.
L40(EMG Stop)이 ON이면 전체 정지.

---

## 14. CSV 파일별 주요 디바이스 사용 요약

> **주의**: 아래 주소는 새 Device Map(`DEVICE_MAP.md`) 기준. 기존 코드와 다름.
> **X/Y 직접 참조 금지** — `input.csv` / `output.csv` 통해 M 간접 참조.

| CSV File | 입력 (Read) | 출력 (Write) | 주요 Mnemonic |
|---|---|---|---|
| **idata.csv** | M300~M31F(←input.csv), D270~D276(Config) | M0~M2(System), L0(InitDone), X→M / M→Y 매핑 | LD, OUT, MOV, SET, RST |
| **gmes.csv** | M10~M28(Step), L10~L29(Done/NG), M400~M416(HMI), L50~L65(Interlock) | M4C~M4F(Lamp), M10~M28(Step), L10~L29(Done/NG), L70~L71(Line Sel) | LD=, AND=, OR=, SET, RST, OUT, MOV, CJ, BMOV, FMOV, **CJ**(D270=1→L1 Skip) |
| **setting.csv** | D60~D115(Preset Table) | D274(Total Gun) | MOV, D* |
| **gunvac.csv** | M12/M22(Step), L51/L61(Safety), D2/D32, D22/D50, Vacuum EU(D160/D172) | M31/M41(Vac SOL), T0, L10/L20(Done), L11/L21(NG) | LD, AND, OUT, MOV, DMOV, LDD<=, SET, RST, OUT |
| **unitvac.csv** | M13/M23(Step), L51/L61(Safety), D4/D34, D22/D50, Vacuum EU | M31+M32/M41+M42(Vac+Stem), T1, L12/L22(Done), L13/L23(NG) | LD, AND, OUT, MOV, DMOV, LDD<=, SET, RST, OUT |
| **vacchec.csv** | M14/M24(Step), D6/D36, D24/D52, Vacuum EU | T2, L14/L24(Done), L15/L25(NG), D160/D172(ΔP) | LD, AND, MOV, DMOV, D-, LDD<=, SET, RST, OUT |
| **refinj.csv** | M15~M16/M25~M26(Step), D8~D10/D38~D40, D60~D115(User), Gun Type(D62/D76/D90/D104) | M34~M3B/M44~M4B(Valves), T4/T5/T6, L16/L26(Done), L17/L27(NG), D124(Disp), M60~M63(Active) | LD, AND, D+, D-, D*, D/, LDD=, LDD<=, LDD>=, MOV, DMOV, SET, RST, OUT, **CJ**(Type 분기) |
| **alarm.csv** | L40~L4F(Alarm latch), M403(Reset), M404(Buzzer Stop) | M4C(Buzzer), M4E/M4F(Lamp R/Y), L40~L4F | LD, OR, SET, RST, OUT, OUT |
| **ad.csv** | (User Fill — 현재 END only) | — | — |
| **485.csv** | (User Fill — 현재 END only) | — | — |
| **spc.csv** | L18/L28(CycleDone×2), M60~M63(Inj Active) | D280~D289(SPC), L24/L40(CycleDone) | LD, D+, DMOV, LDD>=, SET |

