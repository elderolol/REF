# REFRIGER CHARGING MACHINE — Operation Scenario

> 작성일: 2026-05-31  
> 기준 문서: `PLC_PROGRAM_STRUCTURE.md`, `REFRIGER_CHARGING_MACHINE.md`

---

## 1. 장비 Type 일람

### 1-1. Gun Type (솔레노이드 구조)

| Code | 명칭 | Refrig Sol 구조 | Sol Count (REF Only) | Sol Count (REF+OIL) |
|:----:|------|:---------------:|:--------------------:|:-------------------:|
| **0** | 1-Sol (Base) | Base 1개 | 1 Sol | 2 Sol |
| **1** | H+L (Fast+Normal) | Fast 1 + Normal 1 | 2 Sol | 4 Sol |

> Gun별 설정: `D32/D46/D60/D74` (0 또는 1)  
> Oil Mode 시 Oil은 Gun Type과 동일한 Solenoid 구조 (미러링)

---

### 1-2. Oil Mode (주입 모드)

| D234 | Mode | 주입 순서 |
|:----:|------|----------|
| **0** | **REF Only** | `VacCheck → Refrig 주입 → Exhaust → Complete` |
| **1** | **REF+OIL** | `VacCheck → Oil 주입 완료 → Refrig 주입 → Exhaust → Complete` |

---

### 1-3. 방폭 Type (Enclosure)

| Type | Enclosure | Door Limit Sensor |
|------|-----------|:-----------------:|
| **방폭** (Explosion-Proof) | Pressurized / flameproof | Left + Right (OPEN → Alarm) |
| **비방폭** (Non-Explosion-Proof) | Standard industrial | 미장착 |

---

### 1-4. 냉매 Type

| 저장위치 | 설명 |
|:--------:|------|
| `D196/D216/D236/D256` | Barcode Data로 입력되는 Refrigerant 종류 (예: R134a, R290) |

---

### 1-5. HMI Screen Type

| Screen | 용도 |
|--------|------|
| **OPERATION SCREEN** | 메인 운전 화면 — 실시간 감시/조작 |
| **USER SETTING SCREEN** | Gun별 설정 — Model#, 주입량 보정 |
| **PARAMETER SETTING SCREEN** | 시스템 파라미터 — 진공시간, 압력한계, 허용오차 |
| **ALARM SCREEN** | 알람 표시 및 리셋 |

---

### 1-6. Reset Type

| Type | 방법 |
|:----:|------|
| **Hard Reset** | 물리적 RESET push button |
| **Soft Reset** | HMI 화면 RESET button |

---

### 1-7. 공정 Step Type (시퀀스)

| Step | 명칭 | 동작 |
|:----:|------|------|
| `IDLE` | 대기 | 초기화, PC Write 대기, Coupler 체크 |
| `PRECHECK` | 사전 체크 | Interlock, Safety, Pressure, Gun Coupler |
| `GUN VAC` | 건 진공 | LINE VAC SOL ON |
| `UNIT VAC` | 유닛 진공 | LINE VAC + STEM SOL ON |
| `VAC CHECK` | 진공 체크 | Vac SOL OFF, 진공도 확인 |
| `OIL FAST INJ` | 오일 고속 | D234=1 시에만 (Gun Type에 따라 H+L 또는 Base) |
| `OIL NORMAL INJ` | 오일 저속 | D234=1 + Gun Type 1 시에만 |
| `REFRIG FAST INJ` | 냉매 고속 | Gun Type 1: H+L 동시 / Gun Type 0: Base |
| `REFRIG NORMAL INJ` | 냉매 저속 | Gun Type 1: Normal만 |
| `EXHAUST` | 가스 배기 | EXHAUST SOL ON |
| `COMPLETE` | 완료 | 횟수/사용량 누적, Cycle Done |

---

## 2. Manual / Auto 동작 시나리오

### 2-1. Manual 모드

```
① MANUAL/AUTO 버튼 → MANUAL 상태
② 개별 Function 버튼 선택 (GUN VAC / UNIT VAC / VAC CHECK / REFRIG INJECTION)
③ START 누르면 → 선택한 기능만 단독 동작
④ STOP 누르면 → 완료 여부 관계없이 즉시 정지
```

### 2-2. Auto 모드

```
① MANUAL/AUTO 버튼 → AUTO 상태
② START 누르면 → 전체 시퀀스 자동 진행:

    GUN VAC
       ↓
    UNIT VAC
       ↓
    VAC CHECK
       ↓
    [Oil Type(D234=1)일 경우 OIL INJECTION]
       ↓
    REFRIG INJECTION
       ↓
    Operation Complete (자동 종료)

③ STOP 누르면 → 시퀀스 중간이라도 즉시 정지
```

---

## 3. Injection Model 동작 방식

### 3-1. 저장된 Preset Data 구조

| Index | Injection Amount |
|:-----:|:----------------:|
| 1 | 1000g |
| 2 | 1500g |
| 3 | 2000g |
| ... | ... |

> Index = Model# 역할. 사용자가 미리 저장해둔 주입량 Data Table.

### 3-2. Barcode = Not Used (수동 모드)

```
① 화면 MODEL 버튼 선택 → 숫자 입력창 표시
② 사용자가 Model# (Index) 입력
③ 해당 Index에 해당하는 저장된 Injection Amount를 lookup하여 불러옴
④ Injection Setting Amount에 로드
⑤ MODEL button에 입력한 Model# 표시
```

### 3-3. Barcode = Used (PC 연동 모드)

```
① PC가 GMES의 Injection Amount Address에 주입량 값을 기록
② 시스템이 수신한 Injection Amount와 저장된 Preset Data Table을 비교
③ 일치하는 Data를 찾으면 → 그 값을 Injection Setting Amount에 설정
④ 일치한 Data의 Index(번째)를 카운트하여 → 그 값을 Model# 으로 할당
⑤ MODEL button에 해당 Model# 표시
```

### 3-4. 비교 요약

| 구분 | Model# 입력 방식 | Injection Amount 설정 방식 |
|:----:|:----------------:|:--------------------------:|
| **Barcode Not Used** | 사용자가 숫자 입력 | 입력한 Model# → lookup → Amount |
| **Barcode Used** | PC Data → Amount match → Index 산출 | PC가 기록한 Amount를 그대로 사용 |

---

## 4. Manual Mode 상세 — READY-START 2단계

### 4-1. Function 버튼 동작

`
① MANUAL MODE 진입 (L2=ON)
② Function 버튼 누름 (M40F/M410/M411/M412)
     ├── READY 상태가 아니면 → READY SET (M502~M505)
     │      → Function Lamp ON (M530~M533)
     └── READY 상태이면 → READY RST (취소)
            → Function Lamp OFF
③ START 버튼 누름 (M413/M415) + READY 상태
     ├── 해당 Function Step 실행 (ex: GUN VAC = M18)
     ├── READY RST
     ├── Function Lamp 유지 (step active 상태)
     └── START Lamp ON (M540/M541)
④ Function 완료 or STOP
     ├── Function Lamp OFF
     └── START Lamp OFF
`

### 4-2. HMI Lamp 매핑

| HMI Lamp | PLC M | 점등 조건 |
|----------|:-----:|-----------|
| GUN VAC Lamp L0 | M530 | M502(READY) OR M18(GUN VAC step) |
| UNIT VAC Lamp L0 | M531 | M503(READY) OR M19(UNIT VAC step) |
| VAC CHECK Lamp L0 | M532 | M504(READY) OR M20(VAC CHECK step) |
| INJECTION Lamp L0 | M533 | M505(READY) OR M21/M22(INJ step) |
| GUN VAC Lamp L1 | M534 | M506(READY) OR M34 |
| UNIT VAC Lamp L1 | M535 | M507(READY) OR M35 |
| VAC CHECK Lamp L1 | M536 | M508(READY) OR M36 |
| INJECTION Lamp L1 | M537 | M509(READY) OR M37/M38 |
| START Lamp L0 | M540 | M18~M24 (any L0 step active) |
| START Lamp L1 | M541 | M34~M40 (any L1 step active) |

### 4-3. READY 플래그 (M502~M509)

| M | 용도 | SET 조건 | RST 조건 |
|:-:|------|---------|---------|
| M502 | GUN VAC READY L0 | M40F + L2 + NOT RUNNING | M40F again(토글) or M413+START or STOP/EMG/NG |
| M503 | UNIT VAC READY L0 | M410 + L2 | M410 again or M413+START or STOP/EMG/NG |
| M504 | VAC CHECK READY L0 | M411 + L2 | M411 again or M413+START or STOP/EMG/NG |
| M505 | INJ READY L0 | M412 + L2 | M412 again or M413+START or STOP/EMG/NG |
| M506~M509 | L1 동일 | (L1 버튼 + L2) | 동일 조건 (STOP/START L1=M415) |