# Device Map — REFRIGER CHARGING MACHINE Standard Program

> **Target PLC**: Mitsubishi QCPU (Q mode) Q03UDV  
> **Refactoring Note (2024.06)**: All L devices migrated to M800-M916 (self-holding refactoring).  
> L device retention is unnecessary — M devices reset on power cycle, simplifying debugging.  
> **Device 할당 원칙**:
> - **M device (M0-M916)**: 모든 Bit (Step, 결과래치, 알람, 토글, 인터록)
> - **D device**: 짝수 주소 할당, 16-bit도 Dn+1 예약 (32-bit 확장 대비)
> - **X/Y device**: `input.csv` / `output.csv` 로 매핑. 프로그램 내 직접 참조 없음.

---

## 1. M8xx Device — Former L Device (Migrated, Volatile)

> **2024.06 Refactoring**: L device 전량 M8xx로 마이그레이션.  
> 정전 유지 불필요 (M device, 전원 ON 시 OFF). 디버깅 편의성 향상.  
> 매핑 규칙: `M8xx = Lxx` (예: L64 → M864)

| M Addr | Former L | 용도 | 상세 |
|:------:|:--------:|------|------|
| **M800** | L0 | System | 초기화 완료 (InitDone, idata INIT SET) |
| **M801** | L1 | System | Auto Mode (HMI PLS toggle) |
| **M802** | L2 | System | Manual Mode |
| **M803** | L3 | System | Barcode Use Flag |
| **M804~M815** | L4~L15 | — | 예비 |
| | | | |
| **Line 0 — Done/NG** | | | |
| **M816** | L16 | Done/NG L0 | GunVac Done (OUT, gunvac) |
| **M817** | L17 | Done/NG L0 | GunVac NG (SET, gunvac) |
| **M818** | L18 | Done/NG L0 | UnitVac Done (OUT, unitvac) |
| **M819** | L19 | Done/NG L0 | UnitVac NG (SET, unitvac) |
| **M820** | L20 | Done/NG L0 | VacCheck OK (OUT, vacchec) |
| **M821** | L21 | Done/NG L0 | VacCheck NG (OUT, vacchec) |
| **M822** | L22 | Done/NG L0 | Injection Done (SET, refinj) |
| **M823** | L23 | Done/NG L0 | Injection NG (alarm trigger) |
| **M824** | L24 | Done/NG L0 | Cycle Complete L0 (SET, refinj) |
| | | | |
| **Line 1 — Done/NG** | | | |
| **M832** | L32 | Done/NG L1 | GunVac Done (OUT, gunvac) |
| **M833** | L33 | Done/NG L1 | GunVac NG (SET, gunvac) |
| **M834** | L34 | Done/NG L1 | UnitVac Done (OUT, unitvac) |
| **M835** | L35 | Done/NG L1 | UnitVac NG (SET, unitvac) |
| **M836** | L36 | Done/NG L1 | VacCheck OK (OUT, vacchec) |
| **M837** | L37 | Done/NG L1 | VacCheck NG (OUT, vacchec) |
| **M838** | L38 | Done/NG L1 | Injection Done (SET, refinj) |
| **M839** | L39 | Done/NG L1 | Injection NG (alarm trigger) |
| **M840** | L40 | Done/NG L1 | Cycle Complete L1 (SET, refinj) |
| | | | |
| **Alarm Latch (self-holding OUT)** | | | |
| **M864** | L64 | Alarm | Emergency Stop (self-holding, alarm.csv) |
| **M865** | L65 | Alarm | Door Open (self-holding) |
| **M866** | L66 | Alarm | Gun Vacuum Timeout (self-holding) |
| **M867** | L67 | Alarm | Unit Vacuum Timeout (self-holding) |
| **M868** | L68 | Alarm | Vacuum Leak (self-holding) |
| **M869** | L69 | Alarm | Injection Timeout (self-holding) |
| **M870** | L70 | Alarm | Injection Over (self-holding) |
| **M871** | L71 | Alarm | Injection Under (self-holding) |
| **M872** | L72 | Alarm | Pressure High (self-holding) |
| **M873** | L73 | Alarm | Pressure Low (self-holding) |
| **M874** | L74 | Alarm | Temperature Abnormal (self-holding) |
| **M875** | L75 | Alarm | Refriger Bombe Low (SET, spc) |
| **M876** | L76 | Alarm | Model Not Selected (SET, indexs) |
| **M877** | L77 | Alarm | Inj Amount Zero (SET, indexs) |
| **M878** | L78 | Alarm | Door Open (self-holding) |
| **M879** | L79 | Alarm | SPARE (self-holding) |
| | | | |
| **Line 0 — Interlock** | | | |
| **M880** | L80 | Interlock L0 | Interlock Active (전체 조건 AND) |
| **M881** | L81 | Interlock L0 | Safety OK |
| **M882** | L82 | Interlock L0 | Vacuum Pump FB |
| **M883** | L83 | Interlock L0 | Pressure Normal |
| **M884** | L84 | Interlock L0 | Gun Connected |
| **M885** | L85 | Interlock L0 | Refriger Supply OK |
| **M886~M895** | L86~L95 | — | 예비 |
| | | | |
| **Line 1 — Interlock** | | | |
| **M896** | L96 | Interlock L1 | Interlock Active |
| **M897** | L97 | Interlock L1 | Safety OK |
| **M898** | L98 | Interlock L1 | Vacuum Pump FB |
| **M899** | L99 | Interlock L1 | Pressure Normal |
| **M900** | L100 | Interlock L1 | Gun Connected |
| **M901** | L101 | Interlock L1 | Refriger Supply OK |
| **M902~M911** | L102~L111 | — | 예비 |
| | | | |
| **Line Select / 상태** | | | |
| **M912** | L112 | HMI | Active Line = 0 (self-holding toggle) |
| **M913** | L113 | HMI | Active Line = 1 (self-holding toggle) |
| **M914** | L114 | HMI | Active Gun A (self-holding toggle) |
| **M915** | L115 | HMI | Active Gun B (self-holding toggle) |
| **M916** | L116 | HMI | Interlock Use Flag (self-holding toggle) |
| **M917~M999** | — | — | 예비 |

---

## 2. M Device — Internal Relay (Volatile)

> 정전 유지 불필요. 전원 ON 시 항상 OFF에서 시작.

### 2-1. System Flags (M0~M9)

| Addr | 용도 | 상세 |
|:----:|------|------|
| **M0** | System | AlwaysON (SM400 mirror) |
| **M1** | System | AlwaysOFF (SM401 mirror) |
| **M2** | System | Initial Pulse (SM402 mirror, 1 scan only) |
| **M3** | System | 1 Second Clock (SM412 mirror) |
| **M4~M9** | System | 예비 |

### 2-2. Step State — Line 0 (M10~M19)

| Addr | Step | 상세 |
|:----:|:----:|------|
| **M10** | IDLE | 대기 상태 |
| **M11** | PRECHECK | 사전 체크 |
| **M12** | GUN VAC | 건 진공 |
| **M13** | UNIT VAC | 유닛 진공 |
| **M14** | VAC CHECK | 진공 체크 |
| **M15** | REFRIG FAST INJ | 고속 주입 |
| **M16** | REFRIG NORMAL INJ | 저속 주입 |
| **M17** | EXHAUST | 가스 배기 |
| **M18** | COMPLETE | 완료 |
| **M19** | 예비 | |

### 2-2b. WARMUP Flags (M520~M521)
### 2-2b. WARMUP Flags (M520~M521)

> Auto mode START 시 0.5s warm-up 상태. MAIN.csv가 관리.

| Addr | 용도 | SET | RST |
|:----:|------|:---:|:---:|
| **M520** | WARMUP L0 | M413+Auto+Validation OK | T10 done or STOP/EMG/NG |
| **M521** | WARMUP L1 | M415+Auto+Validation OK | T10 done or STOP/EMG/NG |
### 2-3. Step State — Line 1 (M20~M29)

| Addr | Step | 상세 |
|:----:|:----:|------|
| **M20** | IDLE | 대기 상태 |
| **M21** | PRECHECK | 사전 체크 |
| **M22** | GUN VAC | 건 진공 |
| **M23** | UNIT VAC | 유닛 진공 |
| **M24** | VAC CHECK | 진공 체크 |
| **M25** | REFRIG FAST INJ | 고속 주입 |
| **M26** | REFRIG NORMAL INJ | 저속 주입 |
| **M27** | EXHAUST | 가스 배기 |
| **M28** | COMPLETE | 완료 |
| **M29** | 예비 | |

### 2-4. Solenoid Coil Images (M30~M6F)

> 출력 Solenoid의 논리적 ON/OFF 상태. `output.csv` 에서 M→Y 매핑.

#### Line 0 — 진공 (M30~M33)

| Addr | Signal | 매핑 Y |
|:----:|--------|:------:|
| **M30** | VAC_PUMP_RUN_L0 | Y10 |
| **M31** | LINE_VAC_SOL_L0 | Y11 |
| **M32** | LINE_STEM_SOL_L0 | Y12 |
| **M33** | EXHAUST_SOL_L0 | Y1B |

#### Line 0 — Gun 0 Injection (M34~M37)

| Addr | Signal | 매핑 Y | Note |
|:----:|--------|:------:|------|
| **M34** | REFRIG_BASE_SOL_L0_G0 | Y13 | Type0: Base, Type1: Fast |
| **M35** | REFRIG_NORMAL_SOL_L0_G0 | Y14 | Type1만 |
| **M36** | OIL_BASE_SOL_L0_G0 | Y15 | D234=1 전용 |
| **M37** | OIL_NORMAL_SOL_L0_G0 | Y16 | D234=1 + Type1만 |

#### Line 0 — Gun 1 Injection (M38~M3B)

| Addr | Signal | 매핑 Y |
|:----:|--------|:------:|
| **M38** | REFRIG_BASE_SOL_L0_G1 | Y17 |
| **M39** | REFRIG_NORMAL_SOL_L0_G1 | Y18 |
| **M3A** | OIL_BASE_SOL_L0_G1 | Y19 |
| **M3B** | OIL_NORMAL_SOL_L0_G1 | Y1A |

#### Line 1 — 진공 (M40~M43)

| Addr | Signal | 매핑 Y |
|:----:|--------|:------:|
| **M40** | VAC_PUMP_RUN_L1 | Y20 |
| **M41** | LINE_VAC_SOL_L1 | Y21 |
| **M42** | LINE_STEM_SOL_L1 | Y22 |
| **M43** | EXHAUST_SOL_L1 | Y2B |

#### Line 1 — Gun 0 Injection (M44~M47)

| Addr | Signal | 매핑 Y | Note |
|:----:|--------|:------:|------|
| **M44** | REFRIG_BASE_SOL_L1_G0 | Y23 | Type0: Base, Type1: Fast |
| **M45** | REFRIG_NORMAL_SOL_L1_G0 | Y24 | Type1만 |
| **M46** | OIL_BASE_SOL_L1_G0 | Y25 | D234=1 전용 |
| **M47** | OIL_NORMAL_SOL_L1_G0 | Y26 | D234=1 + Type1만 |

#### Line 1 — Gun 1 Injection (M48~M4B)

| Addr | Signal | 매핑 Y |
|:----:|--------|:------:|
| **M48** | REFRIG_BASE_SOL_L1_G1 | Y27 |
| **M49** | REFRIG_NORMAL_SOL_L1_G1 | Y28 |
| **M4A** | OIL_BASE_SOL_L1_G1 | Y29 |
| **M4B** | OIL_NORMAL_SOL_L1_G1 | Y2A |

#### Global Outputs (M4C~M4F)

| Addr | Signal | 매핑 Y |
|:----:|--------|:------:|
| **M4C** | BUZZER | Y30 |
| **M4D** | LAMP_GREEN | Y31 |
| **M4E** | LAMP_RED | Y32 |
| **M4F** | LAMP_YELLOW | Y33 |

#### Safety / Spare (M50~M5F)

| Addr | Signal | 매핑 Y | Note |
|:----:|--------|:------:|------|
| **M50** | SAFETY_RESET_ACK | Y1C | Safety Reset Ack |
| **M51~M5F** | SPARE_DO | — | 예비 |

#### Injection Active Flags (M60~M6F)

| Addr | Signal | Note |
|:----:|--------|------|
| **M60** | INJ_ACTIVE_L0_G0 | Line 0 Gun A Injection 진행 중 |
| **M61** | INJ_ACTIVE_L0_G1 | Line 0 Gun B Injection 진행 중 |
| **M62** | INJ_ACTIVE_L1_G0 | Line 1 Gun A Injection 진행 중 |
| **M63** | INJ_ACTIVE_L1_G1 | Line 1 Gun B Injection 진행 중 |
| **M64~M6F** | 예비 | |

### 2-5. Physical Input Mirrors (M300~M31F)

> `input.csv` 에서 X → M 매핑. 프로그램은 이 M만 참조.

| Addr | 신호 | Source X |
|:----:|------|:--------:|
| **M300** | START_PB_L0 | X00 |
| **M301** | STOP_PB_L0 | X01 |
| **M302** | SAFETY_RESET | X02 |
| **M303** | EMG_STOP | X03 |
| **M304** | GUN_COUPLER_L0_G0 | X04 |
| **M305** | GUN_COUPLER_L0_G1 | X05 |
| **M306** | VAC_PUMP_FB_L0 | X06 |
| **M307** | DOOR_SENSOR_L0 | X07 |
| **M308** | PRESSURE_SW_H_L0 | X08 |
| **M309** | PRESSURE_SW_L_L0 | X09 |
| **M30A** | REFRIG_SUPPLY_OK_L0 | X0A |
| **M30B** | SAFETY_PLC_HEALTHY | X0B |
| **M30C~M30F** | SPARE_DI_L0 | X0C~X0F |

| **M310** | START_PB_L1 | X10 |
| **M311** | STOP_PB_L1 | X11 |
| **M312** | SPARE_L1 | X12 |
| **M313** | EMG_STOP_L1 | X13 |
| **M314** | GUN_COUPLER_L1_G0 | X14 |
| **M315** | GUN_COUPLER_L1_G1 | X15 |
| **M316** | VAC_PUMP_FB_L1 | X16 |
| **M317** | DOOR_SENSOR_L1 | X17 |
| **M318** | PRESSURE_SW_H_L1 | X18 |
| **M319** | PRESSURE_SW_L_L1 | X19 |
| **M31A** | REFRIG_SUPPLY_OK_L1 | X1A |
| **M31B~M31F** | SPARE_DI_L1 | X1B~X1F |

### 2-6. HMI Button Buffer (M1024~M1046)

> HMI momentary 입력. 상태 기억/토글은 PLC self-holding OUT으로 처리.

| Addr | HMI Button | Action | Note |
|:----:|------------|:------:|------|
| **M1024** | LINE 0 SELECT | Momentary | → PLC Self-Hold (M912) |
| **M1025** | LINE 1 SELECT | Momentary | → PLC Self-Hold (M913) |
| **M1026** | INTERLOCK USE/NOT USE | Momentary | → PLC Toggle (M916, PLS 필요) |
| **M1027** | ALARM RESET | Momentary | → 직접 alarm latch self-holding 해제 (ANI M1027) |
| **M1028** | BUZZER STOP | Momentary | → SET M500 (buzzer mute) |
| | ... | | |
| **M1038** | MANUAL/AUTO | Momentary | → PLC Toggle (M801/M802, PLS 필요) |
| **M1039~M1042** | MANUAL STEP | Momentary | → SET ready flag |
| **M1043** | START (Line 0) | Momentary | → SET step bit + RST ready |
| **M1044** | STOP (Line 0) | Momentary | → Bulk RST steps |
| **M1045** | START (Line 1) | Momentary | → SET step bit + RST ready |
| **M1046** | STOP (Line 1) | Momentary | → Bulk RST steps |
| | | | |

### 2-6b. HMI Lamp Bits (M530~M541)

> HMI GOT가 읽어서 버튼 백라이트에 반영. MAIN.csv가 갱신.

| Addr | Lamp | 점등 조건 |
|:----:|------|----------|
| **M530** | GUN VAC Lamp L0 | M502(READY) OR M18(GUN VAC) |
| **M531** | UNIT VAC Lamp L0 | M503(READY) OR M19(UNIT VAC) |
| **M532** | VAC CHECK Lamp L0 | M504(READY) OR M20(VAC CHECK) |
| **M533** | INJECTION Lamp L0 | M505(READY) OR M21/M22(INJ) |
| **M534** | GUN VAC Lamp L1 | M506(READY) OR M34 |
| **M535** | UNIT VAC Lamp L1 | M507(READY) OR M35 |
| **M536** | VAC CHECK Lamp L1 | M508(READY) OR M36 |
| **M537** | INJECTION Lamp L1 | M509(READY) OR M37/M38 |
| **M540** | START Lamp L0 | M18~M24 (any L0 step) |
| **M541** | START Lamp L1 | M34~M40 (any L1 step) |

### 2-7. Communication Flags (M500~M50F) + Function Flags (M502~M509)

| Addr | Signal | Note |
|:----:|--------|------|
| **M500** | Buzzer mute flag | SET by M1028 BUZZER STOP |
| **M502~M505** | Manual step ready L0 | SET by HMI, RST by START EXEC |
| **M506~M509** | Manual step ready L1 | SET by HMI, RST by START EXEC |
### 2-6b. HMI Lamp Bits (M530~M541)

> HMI GOT가 읽어서 버튼 백라이트에 반영. MAIN.csv가 갱신.

| Addr | Lamp | 점등 조건 |
|:----:|------|----------|
| **M530** | GUN VAC Lamp L0 | M502(READY) OR M18(GUN VAC) |
| **M531** | UNIT VAC Lamp L0 | M503(READY) OR M19(UNIT VAC) |
| **M532** | VAC CHECK Lamp L0 | M504(READY) OR M20(VAC CHECK) |
| **M533** | INJECTION Lamp L0 | M505(READY) OR M21/M22(INJ) |
| **M534** | GUN VAC Lamp L1 | M506(READY) OR M34 |
| **M535** | UNIT VAC Lamp L1 | M507(READY) OR M35 |
| **M536** | VAC CHECK Lamp L1 | M508(READY) OR M36 |
| **M537** | INJECTION Lamp L1 | M509(READY) OR M37/M38 |
| **M540** | START Lamp L0 | M18~M24 (any L0 step) |
| **M541** | START Lamp L1 | M34~M40 (any L1 step) |

### 2-7. Communication Flags (M500~M50F) + Function Flags (M502~M509)

| Addr | Signal | Note |
|:----:|--------|------|
| **M500** | SPARE | (RS-485 바코드 — 미사용) |
| **M501** | SPARE | (RS-485 바코드 — 미사용) |
| **M502** | SPARE | (RS-485 SCAN — 미사용) |
| **M503** | WORK_AREA_VALID_L0 | Line 0 Barcode Working Area 유효 |
| **M504** | WORK_AREA_VALID_L1 | Line 1 Barcode Working Area 유효 |
| **M505~M50F** | 예비 | |

---

## 3. D Device — Data Register

### 3-1. Latch 설정 영역

> **PLC 파라미터 래치 설정**:  
> **D0~D299** — 전 범위 Battery Backup (래치)  
> 전원 OFF 후에도 유지되어야 하는 파라미터, 설정값, 누계는 D 영역에 할당.

| Range | 용도 | Retentive |
|:-----:|------|:---------:|
| D0~D29 | Parameter Settings — Line 0 | Y (래치) |
| D30~D59 | Parameter Settings — Line 1 | Y (래치) |
| D60~D115 | User Settings — Gun별 (4 Gun × 14 words) | Y (래치) |
| D116~D149 | Operation Display (HMI Read) | Y (래치) |
| D150~D189 | 예비 Parameter | Y (래치) |
| D190~D209 | Barcode Write Area (PC Ethernet → PLC) | Y (래치) |
| D210~D229 | Barcode Working Area (PLC 내부) | Y (래치) |
| D230~D249 | Barcode Write Area — Line 1 | Y (래치) |
| D250~D269 | Barcode Working Area — Line 1 | Y (래치) |
| D270~D279 | 예비 | Y (래치) |
| D280~D299 | SPC 누계 데이터 (L0/L1 분리) | Y (래치) |
| D300~ | 비래치 영역 (임시/스크래치) | N |

### 3-2. Parameter Settings — Line 0 (D0~D29)

| Addr | Width | 항목 | Unit | Note |
|:----:|:-----:|------|:----:|------|
| **D0** | 16 | L0 Model Number | — | Line 0 현재 작업 모델# |
| **D2** | **32** | Gun Vacuum Time | 0.1 sec | |
| **D4** | **32** | Unit Vacuum Time | 0.1 sec | |
| **D6** | **32** | Vacuum Check Time | 0.1 sec | |
| **D8** | 16 | Gas Exhaust Time | 0.1 sec | |
| **D10** | 16 | Refrig High-Speed Inj Stop | g | |
| **D12** | 16 | Oil High-Speed Inj Stop | g | D234=1 + Type 1 |
| **D14** | **32** | Refriger Bombe Alarm Setting | Kg | Global |
| **D16** | **32** | Refriger Gas Used Amount | Kg | Global |
| **D18** | 16 | Pressure High Limit | kgf/㎠ | |
| **D20** | 16 | Pressure Low Limit | kgf/㎠ | |
| **D22** | **32** | Unit Vacuum Setting Value | Torr | |
| **D24** | **32** | Vacuum Check Setting Value | Torr | |
| **D26** | 16 | Refrig Injection Tolerance | ±g | |
| **D28** | 16 | Oil Injection Tolerance | ±g | D234=1 |

### 3-3. Parameter Settings — Line 1 (D30~D59)

| Addr | Width | 항목 | Addr | Width | 항목 |
|:----:|:-----:|------|:----:|:-----:|------|
| **D30** | 16 | L1 Model Number | **D46** | 16 | Pressure High Limit |
| **D32** | **32** | Gun Vacuum Time | **D48** | 16 | Pressure Low Limit |
| **D34** | **32** | Unit Vacuum Time | **D50** | **32** | Unit Vacuum Setting |
| **D36** | **32** | Vacuum Check Time | **D52** | **32** | Vacuum Check Setting |
| **D38** | 16 | Gas Exhaust Time | **D54** | 16 | Refrig Injection Tolerance |
| **D40** | 16 | Refrig H-Speed Stop | **D56** | 16 | Oil Injection Tolerance |
| **D42** | 16 | Oil H-Speed Stop | **D58~D59** | — | 예비 |
| **D44~D45** | — | (Bombe/Usage: Global) | | | |

### 3-4. User Settings — Gun당 14 words (D60~D115)

> Gun Global Index 공식: `GlobalIndex = Line × D230 + GunLocal`

| Global Gun | Line | Gun | Base | Model# | Type | Refrig Vol(32) | Corr | HMI Cal | Batch | Oil Vol(32) |
|:----------:|:----:|:---:|:----:|:------:|:----:|:--------------:|:----:|:-------:|:-----:|:-----------:|
| **0** | 0 | 0 | D60 | — | D62 | D64~D65 | D66 | D68 | D70 | D72~D73 |
| **1** | 0 | 1 | D74 | — | D76 | D78~D79 | D80 | D82 | D84 | D86~D87 |
| **2** | 1 | 0 | D88 | — | D90 | D92~D93 | D94 | D96 | D98 | D100~D101 |
| **3** | 1 | 1 | D102 | — | D104 | D106~D107 | D108 | D110 | D112 | D114~D115 |

> **Gun Type**: `D62/D76/D90/D104` — 0=1-Sol(Base), 1=H+L(Fast+Normal)

### 3-5. Operation Display (HMI Read) — D116~D149

| Addr | Width | 항목 | Unit | Note |
|:----:|:-----:|------|:----:|------|
| **D116** | **32** | Refrigerant Usage | Kg | 전체 누계 |
| **D118** | 16 | Number of Injections | — | 현재 Gun 기준 |
| **D120** | 16 | Injection Model | — | 현재 Gun 모델# |
| **D122** | 16 | Current Gun Type | — | 0=1-Sol(Base), 1=H+L |
| **D124** | **32** | Charging Pulse | — | 현재 Line Flow Meter |
| **D126** | 16 | Injection Time | 0.1 sec | 현재 주입 경과 |
| **D128** | **32** | Injection Setting Amount (Refrig) | g | 현재 Gun 냉매 목표 |
| **D130** | **32** | Actual Injection Volume (Refrig) | g | 현재 Gun 냉매 실주입 |
| **D132** | **32** | Oil Injection Setting Amount | g | D234=1 시 오일 목표 |
| **D134** | **32** | Actual Oil Injection Volume | g | D234=1 시 오일 실주입 |
| **D136** | 16 | SCAN Injection Volume | g | |
| **D138** | **32** | Current Vacuum Level (Line 0) | Torr | |
| **D140** | 16 | Temperature (Line 0) | 0.1℃ | |
| **D142** | 16 | Pressure (Line 0) | 0.1 kgf/㎠ | |
| **D144** | **32** | Current Vacuum Level (Line 1) | Torr | D228≥2 |
| **D146** | 16 | Temperature (Line 1) | 0.1℃ | D228≥2 |
| **D148** | 16 | Pressure (Line 1) | 0.1 kgf/㎠ | D228≥2 |

### 3-6. Analog Raw → EU (D150~D179)

| Addr | Width | 항목 | Source | Note |
|:----:|:-----:|------|:------:|------|
| D150 | 16 | L0 CH0 AD Raw | ad.csv | 0~4000 |
| D152 | 16 | L0 CH0 EU | ad.csv or 485.csv | 변환값 (공통 출력) |
| D154 | 16 | L0 CH1 AD Raw | ad.csv | 0~4000 |
| D156 | 16 | L0 CH1 EU | ad.csv or 485.csv | 변환값 (공통 출력) |
| D158 | **32** | L0 CH2 AD Raw | ad.csv | 0~4000 |
| D160 | **32** | L0 CH2 EU | ad.csv or 485.csv | 변환값 (공통 출력) |
| D162 | 16 | L1 CH0 AD Raw | ad.csv | 0~4000 (D270≥2) |
| D164 | 16 | L1 CH0 EU | ad.csv or 485.csv | |
| D166 | 16 | L1 CH1 AD Raw | ad.csv | |
| D168 | 16 | L1 CH1 EU | ad.csv or 485.csv | |
| D170 | **32** | L1 CH2 AD Raw | ad.csv | |
| D172 | **32** | L1 CH2 EU | ad.csv or 485.csv | |
| D174~D179 | — | 예비 | — | |

### 센서 Type 선택 아키텍처

```
[Sensor Hardware]
    ├── RS-485 type → 485.csv (RS-485 통신 parsing)
    └── Analog 4~20mA → ad.csv (Analog Scaling)
              │
              │ D152/D156/D160/D164/D168/D172 (공통 출력 Interface)
              ▼
        gmes / vacchec / alarm (공통 소비)
```

> **D150~D179는 공통 출력 영역.** ad.csv와 485.csv 중 실제 센서 Type에 따라 하나만 이 영역에 값을 기록.
> **미래 확장**: 동일한 종류의 센서(예: Vacuum)가 RS-485 Type과 Analog Type으로 각각 존재할 경우,
> `485.csv`와 `ad.csv` 모두 구현하고 `setting.csv`의 설정값(Dxxx Sensor Type Select)으로
> 어느 모듈의 출력을 사용할지 선택. → "플러그인" 방식의 센서 인터페이스.

### 3-7. Barcode Data (D180~D269)

| Offset | L0 Write | L0 Work | L1 Write | L1 Work | 내용 |
|:------:|:--------:|:-------:|:--------:|:-------:|------|
| +0 | D180 | D200 | D230 | D250 | Model Number (16-bit) |
| +1 | D181 | D201 | D231 | D251 | Line / Gun Select (16-bit) |
| +2~+3 | D182~D183 | D202~D203 | D232~D233 | D252~D253 | Serial No Low (32-bit) |
| +4~+5 | D184~D185 | D204~D205 | D234~D235 | D254~D255 | Serial No High (32-bit) |
| +6 | D186 | D206 | D236 | D256 | Refriger Type (16-bit) |
| +7 | D187 | D207 | D237 | D257 | Injection Amount (16-bit) |
| +8~+19 | D188~D189 | D208~D219 | D238~D249 | D258~D269 | Reserve |

### 3-8. Configuration (D270~D279)

| Addr | 항목 | Range | 설명 |
|:----:|------|:-----:|------|
| **D270** | Line Count | 1~2 | 운전 라인 수 (setting.csv) |
| **D272** | Gun Per Line | 1~2 | 라인당 건 수 (setting.csv) |
| **D274** | Total Gun (= D270 × D272) | 1~4 | PLC 연산, Read-Only |
| **D276** | Oil Mode | 0~1 | 0=REF Only, 1=REF+OIL |

> **D270/D272 변경 시 PLC STOP 후 다운로드 필요.**  
> **D276는 운전 중 변경 가능 (모드 전환).**

### 3-9. SPC 누계 — Line 0 (D280~D289)

| Addr | Width | 항목 | Update Trigger |
|:----:|:-----:|------|:-------------:|
| D280~D281 | 32 | L0 냉매 총 사용량 (Kg) | L0 Cycle Complete |
| D282~D283 | 32 | L0 총 주입 횟수 | L0 Cycle Complete |
| D284~D285 | 32 | L0 총 펄스 카운트 | L0 매 주입 시 적산 |
| D286~D287 | 32 | L0 최근 실주입량 (g) | L0 마지막 Cycle Complete |
| D288~D289 | 32 | L0 최근 설정 주입량 (g) | L0 마지막 Cycle Complete |

### 3-10. SPC 누계 — Line 1 (D290~D299)

| Addr | Width | 항목 | Update Trigger |
|:----:|:-----:|------|:-------------:|
| D290~D291 | 32 | L1 냉매 총 사용량 (Kg) | L1 Cycle Complete |
| D292~D293 | 32 | L1 총 주입 횟수 | L1 Cycle Complete |
| D294~D295 | 32 | L1 총 펄스 카운트 | L1 매 주입 시 적산 |
| D296~D297 | 32 | L1 최근 실주입량 (g) | L1 마지막 Cycle Complete |
| D298~D299 | 32 | L1 최근 설정 주입량 (g) | L1 마지막 Cycle Complete |

### 3-11. HSC Parameters (D310~D31F)

> Flow Meter 펄스 카운팅용 HSC(고속카운터) 파라미터.  
> Non-retentive (전원 ON 시 0 초기화).

| Addr | Width | 항목 | Note |
|:----:|:-----:|------|------|
| **D310** | 16 | HSC Channel | HSC 채널 어드레스 (QCPU 설정에 따름) |
| **D312** | **32** | L0 Flow Scale Factor | 펄스→부피 변환 계수 (g/pulse) |
| **D314** | **32** | L0 Current HSC Pulse | 현재 펄스 카운트 (실시간) |
| **D316** | **32** | L0 Accumulated Pulse | 적산 펄스 (주입량 계산용) |
| **D318** | 16 | HSC Channel L1 | D270≥2 시 사용 |
| **D31A** | **32** | L1 Flow Scale Factor | |
| **D31C** | **32** | L1 Current HSC Pulse | |
| **D31E** | **32** | L1 Accumulated Pulse | |

### 3-12. HMI Display / Scratch (D400~D499)

> Line 1 전용 동시 실행 데이터. L0는 D124~D134 사용, L1은 D400~D410 사용.

| Addr | Width | 항목 | Line | Note |
|:----:|:-----:|------|:----:|------|
| **D400** | **32** | L1 Charging Pulse | L1 | Flow Meter 펄스 (L0=D124) |
| **D402** | 16 | L1 Injection Time | L1 | 0.1sec (L0=D126) |
| **D404** | **32** | L1 Inj Setting Amount (Refrig) | L1 | g (L0=D128) |
| **D406** | **32** | L1 Actual Inj Volume (Refrig) | L1 | g (L0=D130) |
| **D408** | **32** | L1 Oil Inj Setting Amount | L1 | g (L0=D132) |
| **D410** | **32** | L1 Actual Oil Inj Volume | L1 | g (L0=D134) |
| **D412~D499** | — | 예비 | — | |

### 3-13. PC Communication Area

### 3-12. SPC Data Logging

> 별도의 로깅 D 레지스터 없음. **D7020~D7219** (L1) 및 **D8020~D8219** (L2) PC 통신 영역에 직접 기록.  
> Gun Vac / Unit Vac / Vac Check 동작 중 자동 모드에서 **0.08초마다** 2 words 씩 쉬프트하며 기록.  
> 4초 = 50 data points → 50 entries × 32-bit = 100 words (기존 200 words 영역 내 충분).

### 3-13. PC Communication Area — Line 1 (D6980~D7239)

> **PC ↔ PLC 데이터 교환 영역.** 이 영역은 기존 설비와의 호환성을 위해 유지.
> PC가 Ethernet으로 직접 Read/Write 하는 주소.

| Addr | Width | Direction | 항목 |
|:----:|:-----:|:---------:|------|
| D6860~D6869 | 10 words | PC → PLC | Model Number (10자) |
| D6870~D6879 | 10 words | PC → PLC | Suffix |
| D6980~D6999 | 20 words | PC → PLC | Barcode (40 Text) |
| D7000 | 16 | PC → PLC | Gas Type (0001=Refrig1, 0002=Refrig2, 0003=No Info) |
| D7001 | 16 | PC → PLC | Target Amount (g) |
| D7002 | 16 | PLC → PC | Gas Type (Echo) |
| D7003 | 16 | PLC → PC | Target Amount (Echo) |
| D7004 | 16 | PLC → PC | Real Amount (g/10) |
| D7005 | 16 | PLC → PC | Refrig Pressure Low (bar/10) |
| D7006 | 16 | PLC → PC | Refrig Pressure High (bar/10) |
| D7007 | 16 | PLC → PC | Target Pulse |
| D7008 | 16 | PLC → PC | Refrig Temperature (℃/10) |
| D7009 | 16 | PLC → PC | Barcode Use Flag (1=Use, 2=Not Use) |
| D7010~D7011 | **32** | PLC → PC | Vacuum Check Value (Torr/10000) |
| D7012 | 16 | PLC → PC | **Result Code** (1=OK, 2~11=Error) |
| D7013~D7014 | **32** | PLC → PC | Vacuum Check Setting (Torr/10000) |
| D7015 | 16 | PLC → PC | **Process Code** (0=None, 1=GunEx, 2=UnitEx, 3=VacChk, 4=Charging) |
| D7016 | 16 | PLC → PC | Information Call (1=START) |
| D7017 | 16 | PLC → PC | Line Code (1=Line#1, 2=Line#2) |
| D7018 | 16 | PLC → PC | Not Charge Unit (0=Default, 1=Pass 1sec) |
| D7020~D7219 | 200 words | PLC → PC | Vacuum SPC Data (100개 × 32-bit, Torr/10000) |
| D7220~D7239 | 20 words | PLC → PC | Barcode (40 Text) |

### 3-14. PC Communication Area — Line 2 (D7860~D8239)

| Addr | Width | Direction | 항목 |
|:----:|:-----:|:---------:|------|
| D7860~D7869 | 10 words | PC → PLC | Model Number (10자) |
| D7870~D7879 | 10 words | PC → PLC | Suffix |
| D7980~D7999 | 20 words | PC → PLC | Barcode (40 Text) |
| D8000 | 16 | PC → PLC | Gas Type |
| D8001 | 16 | PC → PLC | Target Amount |
| D8002 | 16 | PLC → PC | Gas Type (Echo) |
| D8003 | 16 | PLC → PC | Target Amount (Echo) |
| D8004 | 16 | PLC → PC | Real Amount (g/10) |
| D8005 | 16 | PLC → PC | Refrig Pressure Low (bar/10) |
| D8006 | 16 | PLC → PC | Refrig Pressure High (bar/10) |
| D8007 | 16 | PLC → PC | Target Pulse |
| D8008 | 16 | PLC → PC | Refrig Temperature (℃/10) |
| D8009 | 16 | PLC → PC | Barcode Use Flag |
| D8010~D8011 | **32** | PLC → PC | Vacuum Check Value (Torr/10000) |
| D8012 | 16 | PLC → PC | Result Code |
| D8013~D8014 | **32** | PLC → PC | Vacuum Check Setting |
| D8015 | 16 | PLC → PC | Process Code |
| D8016 | 16 | PLC → PC | Information Call |
| D8017 | 16 | PLC → PC | Line Code |
| D8018 | 16 | PLC → PC | Not Charge Unit |
| D8020~D8219 | 200 words | PLC → PC | Vacuum SPC Data (100개 × 32-bit) |
| D8220~D8239 | 20 words | PLC → PC | Barcode (40 Text) |

### 3-15. Device Range 요약

| Device | Range | 용도 | Retentive |
|:------:|:-----:|------|:---------:|
| **M** | M0~M9 | System Flags | N |
| **M** | M10~M42 | Step State (Line 0/1) | N |
| **M** | M48~M80 | Solenoid Coil Images + Safety | N |
| **M** | M96~M99 | Injection Active Flags | N |
| **M** | M100~M103 | Scratch (temp flags) | N |
| **M** | M500 | Buzzer mute | N |
| **M** | M502~M509 | Manual step ready | N |
| **M** | M530~M541 | HMI Lamp bits | N |
| **M** | M600~M601 | PLS toggle intermediate | N |
| **M** | M768~M799 | Physical Input Mirrors | N |
| **M** | M800~M916 | Former L devices (Done/NG/알람/토글/인터록) | N |
| **M** | M1024~M1046 | HMI Button Buffer | N |
| **D** | D0~D299 | 파라미터 / 설정 / 누계 / 통신 | Y (전체 래치) |
| **D** | D300~D32F | HSC Parameters (D310~D31F) | N |
| **D** | D330~D6979 | Scratch / Temp / 예비 | N |
| **D** | D6980~D7239 | PC Communication Area — Line 1 | N |
| **D** | D7860~D8239 | PC Communication Area — Line 2 | N |
| **T** | T0~T31 | Timer (100ms base) | — |
| **X** | X00~X1F | Physical Input (input.csv mapping) | — |
| **Y** | Y10~Y3F | Physical Output (output.csv mapping) | — |

---

## 3. Timer 할당 (T)

| Addr | 용도 | Time Base | 소속 |
|:----:|------|:---------:|:----:|
| **T0** | Gun Vacuum Timer L0 | 100ms | gunvac |
| **T1** | Unit Vacuum Timer L0 | 100ms | unitvac |
| **T2** | Vacuum Check Timer L0 | 100ms | vacchec |
| **T3** | Exhaust Timer L0 | 100ms | refinj |
| **T4** | Refrig Fast Timer L0 | 100ms | refinj |
| **T5** | Refrig Normal Timer L0 | 100ms | refinj |
| **T6** | Oil Inj Timer L0 | 100ms | refinj |
| **T7** | Grace Timer L0 | 100ms | gunvac/unitvac |
| **T8** | Gun Vacuum Timer L1 | 100ms | gunvac |
| **T9** | Unit Vacuum Timer L1 | 100ms | unitvac |
| **T10** | Inj Warmup Timer L0 | 100ms | MAIN |
| **T11** | Vacuum Check Timer L1 | 100ms | vacchec |
| **T12** | Exhaust Timer L1 | 100ms | refinj |
| **T13** | Refrig Fast Timer L1 | 100ms | refinj |
| **T14** | Refrig Normal Timer L1 | 100ms | refinj |
| **T15** | Oil Inj Timer L1 | 100ms | refinj |
| **T16** | Inj Warmup Timer L1 | 100ms | MAIN |
| **T17** | Grace Timer L1 | 100ms | gunvac/unitvac |
| **T18** | VAC SPC Logging Interval L0 | **10ms(K8=80ms)** | gmes(OUTH) |
| **T19** | VAC SPC Logging Interval L1 | **10ms(K8=80ms)** | gmes(OUTH) |
| **T19~T31** | 확장 예비 | 100ms | |

---

## 5. Device Range 요약

| Device | Range | 용도 | Retentive |
|:------:|:-----:|------|:---------:|
| **L** | L0~L999 | 정전유지 Bit (Done/NG/알람/상태) | Y (전체 래치) |
| **M** | M0~M9 | System Flags | N |
| **M** | M10~M29 | Step State (Line 0/1) | N |
| **M** | M30~M6F | Solenoid Coil Images + Injection Active | N |
| **M** | M300~M31F | Physical Input Mirrors (input.csv) | N |
| **M** | M400~M41F | HMI Button Buffer | N |
| **M** | M500~M50F | Communication Flags | N |
| **M** | M600~ | 예비 | N |
| **D** | D0~D299 | 파라미터 / 설정 / 누계 / 통신 | Y (전체 래치) |
| **D** | D300~ | Scratch / Temp | N |
| **T** | T0~T31 | Timer (100ms base) | — |
| **X** | X00~X1F | Physical Input (input.csv mapping) | — |
| **Y** | Y10~Y3F | Physical Output (output.csv mapping) | — |



