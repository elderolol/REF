# REFRIGER CHARGING MACHINE — PLC Program Structure Design

> **Target PLC**: Mitsubishi QCPU (Q mode) Q03UDV  
> **HMI Spec**: REFRIGER_CHARGING_MACHINE.md  
> **IL CSV Format**: GX_WORKS2_IL_Spec.md  
> **Goal**: 1 Line/1 Gun, 1 Line/2 Gun, 2 Line/2 Gun, 2 Line/4 Gun 모든 구성에서 동작하는 단일 표준 프로그램

---

## 0. 시스템 구성 (System Configuration)

### 0-1. 지원 구성

| 구성 | Line 수 | Gun/Line | Total Gun |
|---|---|---|---|
| 1L/1G | 1 | 1 | 1 |
| 1L/2G | 1 | 2 | 2 |
| 2L/2G | 2 | 1 | 2 |
| 2L/4G | 2 | 2 | 4 |

### 0-2. 구성 파라미터 (PLC D-Register)

| Addr | 항목 | Range | 설명 |
|---|---|---|---|
| **D228** | Line Count | 1~2 | 운전 라인 수. 1이면 Line 1 미사용 |
| **D230** | Gun Per Line | 1~2 | 라인당 건 수 |
| **D232** | Total Gun (= D228 × D230) | 1~4 | PLC 연산, Read-Only |

> 구성 변경 시 PLC STOP 후 다운로드. 운전 중 변경 불가.

### 0-3. Line / Gun 개념

```
Line 0 ──┬── Gun 0 (Type A or B) ──┐
         │                          ├── 진공계통(공유), 한 번에 1 Gun만 사용
         └── Gun 1 (Type A or B) ──┘

Line 1 ──┬── Gun 0 (Type A or B) ──┐
         │                          ├── 진공계통(공유), 한 번에 1 Gun만 사용
         └── Gun 1 (Type A or B) ──┘
```

- **Line**: 독립된 진공 펌프 + 진공 배관 + 유닛. Line 간 완전 독립 운전.
- **Gun**: 동일 Line 내 진공계 공유, **동시 사용 불가**. HMI로 작업 건 선택.
- **D230=2**: 동일 Line에 2개의 Gun 장착 (서로 다른 Type 가능). 작업 시 1개 선택.

### 0-4. Gun Type

| Type | 명칭 | 솔레노이드 구성 | 주입 시퀀스 |
|---|---|---|---|
| **0** | 1-Solenoid Refrig | Refrig 기본 1개 = **1 Sol** | Refrig_Sol ON → 목표량 → OFF |
| **1** | Refrig H+L (2-Sol) | Refrig 고속 1개 + Refrig 저속 1개 = **2 Sol** | **RF_H + RF_L 동시 ON** → 고속정지 도달 → RF_H OFF, RF_L로 최종 목표 |
| **2** | Oil 1-Sol + Refrig 1-Sol | Oil 1개 + Refrig 1개 = **2 Sol** | Oil_Sol ON → 목표 → OFF → Refrig_Sol ON → 목표 → OFF |
| **3** | Oil H+L + Refrig H+L | Oil H+L + Refrig H+L = **4 Sol** | **Oil_H+Oil_L 동시 ON** → Oil고속정지 → Oil_H OFF, Oil_L로 완료 → **RF_H+RF_L 동시 ON** → RF고속정지 → RF_H OFF, RF_L로 완료 |

> **고속+저속 동시 Open**: 주입 시작 시 고속·저속 솔레노이드가 함께 열리고, 고속 중단 설정량 도달 시 고속만 닫히며 저속으로 최종 목표량까지 주입. 오일/냉매 동일한 패턴.

### 0-5. Gun Index 공식

### 0-5. Gun Index 공식

```
Gun Global Index = Line × GunPerLine(D230) + GunLocal
  - Line ∈ {0, 1}
  - GunLocal ∈ {0, 1}
  - 예: Line1 Gun0 → 1×2+0 = 2 (Global Gun 2)
```

> D230=2 구성에서도 **동일 Line내 1개 Gun만 활성**. HMI Gun Select로 작업 건 결정.

---

## 1. I/O 요구사항 분석 (HMI → PLC 신호 매핑)

### 1-1. HMI Button → PLC 내부 릴레이 (M, 푸시=ON)

| HMI Button | PLC Device | Type | Description |
|---|---|---|---|
| **LINE 0 SELECT** | M40 | ALT | Line 0 선택 (해당 Line의 Gun Select 활성화) |
| **LINE 1 SELECT** | M41 | ALT | Line 1 선택 |
| INTERLOCK USE/NOT USE | M42 | ALT | 인터락 사용/미사용 토글 |
| ALARM RESET | M43 | PULSE | 알람 리셋 (현재 선택 Line) |
| BUZZER STOP | M44 | PULSE | 부저 정지 |
| USER SETTING SCREEN | M45 | PULSE | 사용자 설정 화면 이동 |
| PARAMETER SETTING SCREEN | M46 | PULSE | 파라미터 설정 화면 이동 |
| ALARM SCREEN | M47 | PULSE | 알람 화면 이동 |
| **GUN SELECT 0** (현재 Line내) | M48 | ALT | 현재 선택 Line의 Gun 0 선택 |
| **GUN SELECT 1** (현재 Line내) | M49 | ALT | 현재 선택 Line의 Gun 1 선택 |
| NUMBER OF INJECTIONS RESET | M50 | PULSE | 현재 선택 Line/Gun 주입 횟수 리셋 |
| MODEL SELECT | M51 | PULSE | 주입 모델 선택 (현재 Gun) |
| VACUUM PUMP ON/OFF | M52 | ALT | 진공 펌프 수동 ON/OFF (현재 Line) |
| BARCODE USE/NOT USE | M53 | ALT | 바코드 사용/미사용 토글 |
| MANUAL/AUTO | M54 | ALT | 수동/자동 모드 전환 |
| GUN VACUUM | M55 | PULSE | 건 진공 시작 (현재 Line/Gun, 수동) |
| UNIT VACUUM | M56 | PULSE | 유닛 진공 시작 (현재 Line, 수동) |
| VACUUM CHECK | M57 | PULSE | 진공 체크 시작 (현재 Line, 수동) |
| REFRIGER INJECTION | M58 | PULSE | 냉매 주입 시작 (현재 Line/Gun, 수동) |
| **START (Line 0)** | M59 | PULSE | Line 0 자동 사이클 시작 |
| **STOP (Line 0)** | M60 | PULSE | Line 0 사이클 정지 |
| **START (Line 1)** | M61 | PULSE | Line 1 자동 사이클 시작 |
| **STOP (Line 1)** | M62 | PULSE | Line 1 사이클 정지 |

> **Line Select**: M40/M41로 활성 Line을 선택. D228 값에 따라 1 Line 구성 시 Line 1 버튼 비활성.  
> **Gun Select**: M48/M49는 현재 선택된 Line 내에서 Gun 선택. D230 값에 따라 1 Gun/Line 구성 시 Gun 1 버튼 비활성.  
> **Line Current**: PLC 내부에서 현재 HMI 제어 대상 Line을 M-register로 유지 (M200=Line0 Active, M201=Line1 Active).

### 1-2. 물리적 I/O 추정 (2 Line 기준)

| Signal Class | Count | Device Range | Description |
|---|---|---|---|
| **DI L0** | 16점 | X00~X0F | Start PB, Stop PB, Safety Reset, EMG, Gun Sensor×2, Vac Pump FB, Door, Pressure SW×2, Supply OK |
| **DI L1** | 16점 | X10~X1F | (D228≥2) Start, Stop, Gun Sensor×2, Vac Pump FB, Door, Pressure SW×2, Supply OK |
| **DO L0** | 16점 | Y10~Y1F | Vac Pump, Gun Vac V, Unit Vac V, High Inj V×2, Low Inj V×2, Gas Exhaust V, Buzzer, Lamp G/R/Y |
| **DO L1** | 16점 | Y20~Y2F | (D228≥2) Vac Pump, Gun Vac V, Unit Vac V, High Inj V×2, Low Inj V×2, Gas Exhaust V |
| **AI L0** | 3ch | D120~D131 | Pressure, Temperature, Vacuum (각 Raw+EU) |
| **AI L1** | 3ch | D132~D143 | (D228≥2) Pressure, Temperature, Vacuum |
| **HSC** | 2ch | — | Flow Meter Pulse × 2 Line |
| **RS-485** | 1ch | — | Barcode / SCAN (시분할 or 채널 분리) |

### 1-3. Safety PLC 인터페이스

| Signal | Device | Direction |
|---|---|---|
| Safety PLC Healthy | X0B → M131/M141 | Safety → Main |
| Safety Reset Request (Hard) | X03 | Push Button → Main |
| Main → Safety Reset Ack | Y1C | Main → Safety |
| Emergency Stop Active | M90 | Internal flag |

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
├── 485.csv       # RS-485 통신 (바코드, SCAN 데이터 수신)
└── spc.csv       # 통계 데이터 (사용량 누계, 주입 횟수, 펄스 누계)
```

### 2-1. 모듈별 책임

| POU | 책임 | 실행 조건 |
|---|---|---|
| **idata.csv** | X→M 매핑, 초기 기동 시 D/T 초기화, 상시 ON 처리 | Always ON |
| **gmes.csv** | 자동/수동 모드, 메인 시퀀스 스텝 제어, 각 서브시퀀스 기동/완료/실패 인터페이스, 사이클 완료 판정 | Always ON |
| **setting.csv** | 파라미터 화면 값 ↔ PLC D레지스터, 사용자 설정(건별) ↔ PLC D레지스터, 설정값 범위 체크 | Always ON |
| **gunvac.csv** | 건 진공용 솔레노이드 ON, 진공 시간 T카운트, 진공도 도달 체크, 타임아웃 알람 | 진공 스텝 진입 시 |
| **unitvac.csv** | 유닛 진공용 솔레노이드 ON, 진공 시간 T카운트, 진공도 도달 체크, 타임아웃 알람 | 진공 스텝 진입 시 |
| **vacchec.csv** | 진공 밸브 CLOSE 후 ΔP 감시, 리크 판정 (ΔP > 허용치 → 알람) | 진공 체크 스텝 진입 시 |
| **refinj.csv** | 고속 주입 밸브 ON → 설정량 도달 → 저속 주입 → 목표량 ±공차 도달 → OFF, 펄스 카운트 적산, 주입량 계산 | 주입 스텝 진입 시 |
| **alarm.csv** | 알람 조건 OR 수집, 알람 래치, 부저 출력, 알람 리셋 처리, 인터락 신호 출력 | Always ON |
| **ad.csv** | AI Raw → Engineering Unit 변환 (Scaling), 진공도/온도/압력 현재값 D레지스터 갱신 | Always ON |
| **485.csv** | RS-485 수신 버퍼 → D레지스터 파싱, 바코드 데이터 검증, SCAN 주입량 수신 | Always ON |
| **spc.csv** | 냉매 총 사용량 적산 (32-bit), 주입 횟수 카운트 (16-bit), 펄스 누계 (32-bit), 실주입량/설정량 기록 | 사이클 완료 시 |

---

## 3. 디바이스 맵 (Device Map)

> **규칙**  
> - Bit device (M, L, X, Y): 0번부터 연속 할당, 그룹 간 빈 공간 없음  
> - Word device (D): 모든 항목 짝수 주소(D0, D2, D4, D6…)에 할당. 16-bit 항목도 Dn+1을 예약하여 향후 32-bit 확장 대비  
> - Timer (T): 0번부터 연속 할당

### 3-1. M (Internal Relay) — Bit Device (0~)

| Addr | 용도 | 상세 |
|---|---|---|
| **M0** | System | AlwaysON (SM400 mirror) |
| **M1** | System | AlwaysOFF (SM401 mirror) |
| **M2** | System | 초기화 완료 (InitDone) |
| **M3** | System | Auto Mode (M54 mirror) |
| **M4** | System | Manual Mode |
| **M5~M9** | System | 예비 |
| | | |
| **Line 0 — Step** | | |
| **M10** | Step L0 | IDLE |
| **M11** | Step L0 | PRECHECK |
| **M12** | Step L0 | GUN VAC |
| **M13** | Step L0 | UNIT VAC |
| **M14** | Step L0 | VAC CHECK |
| **M15** | Step L0 | HIGH SPEED INJECTION |
| **M16** | Step L0 | LOW SPEED INJECTION |
| **M17** | Step L0 | GAS EXHAUST |
| **M18** | Step L0 | COMPLETE |
| **M19** | Step L0 | 예비 |
| | | |
| **Line 1 — Step** | | |
| **M20** | Step L1 | IDLE |
| **M21** | Step L1 | PRECHECK |
| **M22** | Step L1 | GUN VAC |
| **M23** | Step L1 | UNIT VAC |
| **M24** | Step L1 | VAC CHECK |
| **M25** | Step L1 | HIGH SPEED INJECTION |
| **M26** | Step L1 | LOW SPEED INJECTION |
| **M27** | Step L1 | GAS EXHAUST |
| **M28** | Step L1 | COMPLETE |
| **M29** | Step L1 | 예비 |
| | | |
| **Line 0 — Done/Fail** | | |
| **M30** | Done/Fail L0 | GunVac Done |
| **M31** | Done/Fail L0 | GunVac Fail |
| **M32** | Done/Fail L0 | UnitVac Done |
| **M33** | Done/Fail L0 | UnitVac Fail |
| **M34** | Done/Fail L0 | VacCheck Done |
| **M35** | Done/Fail L0 | VacCheck Fail |
| **M36** | Done/Fail L0 | Injection Done |
| **M37** | Done/Fail L0 | Injection Fail |
| **M38** | Done/Fail L0 | Cycle Done |
| **M39** | Done/Fail L0 | Cycle Fail |
| | | |
| **Line 1 — Done/Fail** | | |
| **M40** | Done/Fail L1 | GunVac Done |
| **M41** | Done/Fail L1 | GunVac Fail |
| **M42** | Done/Fail L1 | UnitVac Done |
| **M43** | Done/Fail L1 | UnitVac Fail |
| **M44** | Done/Fail L1 | VacCheck Done |
| **M45** | Done/Fail L1 | VacCheck Fail |
| **M46** | Done/Fail L1 | Injection Done |
| **M47** | Done/Fail L1 | Injection Fail |
| **M48** | Done/Fail L1 | Cycle Done |
| **M49** | Done/Fail L1 | Cycle Fail |
| | | |
| **HMI / Line Select** | | |
| **M50~M72** | HMI Button | 상기 1-1 참조 (23버튼: M50=LINE0 SEL, M51=LINE1 SEL ... M72=STOP L1) |
| **M73~M79** | HMI Button | 예비 |
| | | |
| **Line 상태 추적** | | |
| **M80** | Line Track | HMI 활성 Line = 0 |
| **M81** | Line Track | HMI 활성 Line = 1 |
| **M82~M84** | Line Track | 예비 |
| | | |
| **Alarm (Global)** | | |
| **M90** | Alarm | Emergency Stop (전체 정지) |
| **M91** | Alarm | Safety PLC Fault (전체 정지) |
| **M92** | Alarm | Gun Vacuum Timeout (Line별 발생) |
| **M93** | Alarm | Unit Vacuum Timeout |
| **M94** | Alarm | Vacuum Leak (ΔP 초과) |
| **M95** | Alarm | Injection Timeout |
| **M96** | Alarm | Injection Over (±공차 초과) |
| **M97** | Alarm | Injection Under (±공차 미달) |
| **M98** | Alarm | Pressure High |
| **M99** | Alarm | Pressure Low |
| **M100** | Alarm | Temperature Abnormal |
| **M101** | Alarm | Refriger Bombe Low |
| **M102** | Alarm | Barcode Read Fail |
| **M103** | Alarm | SCAN Comm Fail |
| **M104~M109** | Alarm | 예비 |
| | | |
| **Line 0 — Alarm Instance** | | |
| **M110~M119** | Alarm L0 | Line 0 전용 알람 인스턴스 (M110=L0 GunVac Timeout, ...) |
| | | |
| **Line 1 — Alarm Instance** | | |
| **M120~M129** | Alarm L1 | Line 1 전용 알람 인스턴스 (D228≥2일 때만 사용) |
| | | |
| **Interlock (Line별)** | | |
| **M130** | Interlock L0 | Interlock Active |
| **M131** | Interlock L0 | Safety OK |
| **M132** | Interlock L0 | Vacuum Pump Run FB |
| **M133** | Interlock L0 | Pressure Normal |
| **M134** | Interlock L0 | Gun Connected |
| **M135** | Interlock L0 | Refriger Supply OK |
| **M136~M139** | Interlock L0 | 예비 |
| | | |
| **M140** | Interlock L1 | Interlock Active |
| **M141** | Interlock L1 | Safety OK |
| **M142** | Interlock L1 | Vacuum Pump Run FB |
| **M143** | Interlock L1 | Pressure Normal |
| **M144** | Interlock L1 | Gun Connected |
| **M145** | Interlock L1 | Refriger Supply OK |
| **M146~M149** | Interlock L1 | 예비 |
| | | |
| **Line 0 — 진공/주입 제어** | | |
| **M150** | Vac L0 | **LINE VACUUM SOL** |
| **M151** | Vac L0 | **LINE STEM SOL** (Unit Vac 시 추가 ON) |
| **M152** | Vac L0 | **EXHAUST SOL** (Gas Exhaust / Dead Zone) |
| **M153** | Vac L0 | Vacuum Pump Run |
| | | |
| **M154** | Inj L0 G0 | **REFRIG FAST SOL** (Type0: 단일솔) |
| **M155** | Inj L0 G0 | **REFRIG NORMAL SOL** (Type1/3) |
| **M156** | Inj L0 G0 | **OIL FAST SOL** (Type3) / Oil Sol (Type2) |
| **M157** | Inj L0 G0 | **OIL NORMAL SOL** (Type3) |
| **M158** | Inj L0 G0 | Injection Active |
| | | |
| **M159** | Inj L0 G1 | REFRIG FAST SOL |
| **M160** | Inj L0 G1 | REFRIG NORMAL SOL |
| **M161** | Inj L0 G1 | OIL FAST SOL |
| **M162** | Inj L0 G1 | OIL NORMAL SOL |
| **M163** | Inj L0 G1 | Injection Active |
| **M164~M169** | — | 예비 |
| | | |
| **Line 1 — 진공/주입 제어** | | |
| **M170** | Vac L1 | **LINE VACUUM SOL** |
| **M171** | Vac L1 | **LINE STEM SOL** |
| **M172** | Vac L1 | **EXHAUST SOL** |
| **M173** | Vac L1 | Vacuum Pump Run |
| | | |
| **M174** | Inj L1 G0 | REFRIG FAST SOL |
| **M175** | Inj L1 G0 | REFRIG NORMAL SOL |
| **M176** | Inj L1 G0 | OIL FAST SOL |
| **M177** | Inj L1 G0 | OIL NORMAL SOL |
| **M178** | Inj L1 G0 | Injection Active |
| | | |
| **M179** | Inj L1 G1 | REFRIG FAST SOL |
| **M180** | Inj L1 G1 | REFRIG NORMAL SOL |
| **M181** | Inj L1 G1 | OIL FAST SOL |
| **M182** | Inj L1 G1 | OIL NORMAL SOL |
| **M183** | Inj L1 G1 | Injection Active |
| **M184~M189** | — | 예비 |
| | | |
| **통신 (Global)** | | |
| **M190** | 통신 | Barcode Read OK |
| **M191** | 통신 | Barcode Read Fail |
| **M192** | 통신 | SCAN Data Valid |
| **M193** | 통신 | Working Area Valid (Line 0) |
| **M194** | 통신 | Working Area Valid (Line 1) |
| **M195~M199** | 통신 | 예비 |
| **M200~** | Spare | 예비 |

### 3-2. D (Data Register) — Word Device (짝수 주소)

> **16-bit** 항목: Dn 사용, Dn+1 예약. **32-bit** 항목: Dn+Dn+1 사용.  
> **Parameter는 Line별 분리**: L0=D0~D29, L1=D30~D59 (D228≥2)

#### Parameter Settings — Line 0 (D0~D29)

| Addr | Width | 항목 | Unit | Note |
|---|---|---|---|---|
| **D0** | 16 | **L0 Model Number** | — | Line 0 현재 작업 모델# |
| **D2** | 16 | Gun Vacuum Time | 0.1 sec | |
| **D4** | 16 | Unit Vacuum Time | 0.1 sec | |
| **D6** | 16 | Vacuum Check Time | 0.1 sec | |
| **D8** | 16 | Gas Exhaust Time | 0.1 sec | |
| **D10** | 16 | Refrig High-Speed Inj Stop | g | |
| **D12** | 16 | **Oil High-Speed Inj Stop** | g | Type 2,3 |
| **D14** | **32** | Refriger Bombe Alarm Setting | Kg | Global |
| **D16** | **32** | Refriger Gas Used Amount | Kg | Global |
| **D18** | 16 | Pressure High Limit | kgf/㎠ | |
| **D20** | 16 | Pressure Low Limit | kgf/㎠ | |
| **D22** | **32** | Unit Vacuum Setting Value | Torr | |
| **D24** | **32** | Vacuum Check Setting Value | Torr | |
| **D26** | 16 | **Refrig Injection Tolerance** | ±g | |
| **D28** | 16 | **Oil Injection Tolerance** | ±g | Type 2,3 |

#### Parameter Settings — Line 1 (D30~D59, D228≥2)

| Addr | Width | 항목 | Addr | Width | 항목 |
|---|---|---|---|---|---|
| **D30** | 16 | **L1 Model Number** | **D46** | 16 | Pressure High Limit |
| **D32** | 16 | Gun Vacuum Time | **D48** | 16 | Pressure Low Limit |
| **D34** | 16 | Unit Vacuum Time | **D50** | **32** | Unit Vacuum Setting |
| **D36** | 16 | Vacuum Check Time | **D52** | **32** | Vacuum Check Setting |
| **D38** | 16 | Gas Exhaust Time | **D54** | 16 | Refrig Injection Tolerance |
| **D40** | 16 | Refrig H-Speed Stop | **D56** | 16 | Oil Injection Tolerance |
| **D42** | 16 | Oil H-Speed Stop | **D58~D59** | — | 예비 |
| **D44~D45** | — | (Bombe/Usage: Global) | | | |

> **Bombe Alarm / Used Amount**: D14~D17은 Global (양 Line 공통 봄베). Model Number는 Line별 독립.

#### User Settings (Gun당 14 words, 최대 4 Gun = 56 words)

> Gun Global Index = Line × D230 + GunLocal  
> Base Addr = **D60 + (GlobalIndex × 14)**

| Global Gun | Line | Gun | Base | Model# | Type | Refrig Vol(32) | Corr | HMI Cal | Batch | Oil Vol(32) |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | D60 | — | D62 | D64~D65 | D66 | D68 | D70 | D72~D73 |
| **1** | 0 | 1 | D74 | — | D76 | D78~D79 | D80 | D82 | D84 | D86~D87 |
| **2** | 1 | 0 | D88 | — | D90 | D92~D93 | D94 | D96 | D98 | D100~D101 |
| **3** | 1 | 1 | D102 | — | D104 | D106~D107 | D108 | D110 | D112 | D114~D115 |

> **Model#는 Line Parameter(D0/D30)에서 관리. User Setting의 Model#는 Gun별 Preset 매핑용.**

> **Gun Type (D32, D46, D60, D74)**: 0=1-Sol, 1=Refrig H+L(2Sol), 2=Oil+Refrig 1Sol(2Sol), 3=Oil+Refrig H+L(4Sol)  
> **Oil Volume**: Type≠2 이면 0 (무시). Type=2 이면 유효.  
> D228=1 일 때 Gun 2,3 미사용. D230=1 일 때 Gun 1,3 미사용.

#### Operation Display (HMI Read) — 현재 선택 Line/Gun 기준

| Addr | Width | 항목 | Unit | Note |
|---|---|---|---|---|
| **D86** | **32** | Refrigerant Usage | Kg | 전체 누계 |
| **D88** | 16 | Number of Injections | — | 현재 Gun 기준 |
| **D90** | 16 | Injection Model | — | 현재 Gun 모델# |
| **D92** | 16 | **Current Gun Type** | — | 0=Refrig, 1=Oil+Refrig |
| **D94** | **32** | Charging Pulse | — | 현재 Line Flow Meter |
| **D96** | 16 | Injection Time | 0.1 sec | 현재 주입 경과 |
| **D98** | **32** | Injection Setting Amount (Refrig) | g | 현재 Gun 냉매 목표 |
| **D100** | **32** | Actual Injection Volume (Refrig) | g | 현재 Gun 냉매 실주입 |
| **D102** | **32** | Oil Injection Setting Amount | g | Type B 시 오일 목표 |
| **D104** | **32** | Actual Oil Injection Volume | g | Type B 시 오일 실주입 |
| **D106** | 16 | SCAN Injection Volume | g | |
| **D108** | **32** | Current Vacuum Level (Line 0) | Torr | |
| **D110** | 16 | Temperature (Line 0) | 0.1 ℃ | |
| **D112** | 16 | Pressure (Line 0) | 0.1 kgf/㎠ | |
| **D114** | **32** | Current Vacuum Level (Line 1) | Torr | D228≥2 |
| **D116** | 16 | Temperature (Line 1) | 0.1 ℃ | D228≥2 |
| **D118** | 16 | Pressure (Line 1) | 0.1 kgf/㎠ | D228≥2 |

#### Analog (Line 0 / Line 1)

| Addr | Width | 항목 | Note |
|---|---|---|---|
| **D120** | 16 | L0 Pressure AD Raw | 0~4000 |
| **D122** | 16 | L0 Pressure EU | kgf/㎠ |
| **D124** | 16 | L0 Temperature AD Raw | 0~4000 |
| **D126** | 16 | L0 Temperature EU | 0.1 ℃ |
| **D128** | 16 | L0 Vacuum AD Raw | 0~4000 |
| **D130** | **32** | L0 Vacuum EU | Torr |
| **D132** | 16 | L1 Pressure AD Raw | D228≥2 사용 |
| **D134** | 16 | L1 Pressure EU | |
| **D136** | 16 | L1 Temperature AD Raw | |
| **D138** | 16 | L1 Temperature EU | |
| **D140** | 16 | L1 Vacuum AD Raw | |
| **D142** | **32** | L1 Vacuum EU | Torr |
| **D144~D149** | — | 예비 (6 words) | |

#### Calculation Work (Line 0 / Line 1)

| Addr (L0) | Addr (L1) | Width | 항목 |
|---|---|---|---|
| **D150** | **D170** | **32** | Injection Accumulated Amount (현재 Gun) |
| **D152** | **D172** | **32** | P_start (Vac Check 시작 시 진공도) |
| **D154** | **D174** | **32** | ΔP (리크 판정용) |
| **D156** | **D176** | 16 | Timer Elapsed (EU) |
| **D158~D169** | **D178~D189** | — | 예비 (12 words per Line) |

#### Communication

| Addr | Width | 항목 | Note |
|---|---|---|---|
| **D190~D209** | 16×20 | **PC Write Area** (Line 0) | PC→PLC, L0 Cycle 완료 시 0 Clear |
| **D210~D229** | 16×20 | **Working Area** (Line 0) | L0 START 시 PC Write→복사 |
| **D230~D249** | 16×20 | **PC Write Area** (Line 1) | D228≥2일 때 사용 |
| **D250~D269** | 16×20 | **Working Area** (Line 1) | D228≥2일 때 사용 |
| **D270~D279** | — | 예비 (10 words) | RS-485 Raw Buffer |

#### SPC (Statistics) — 전 Line 합산

| Addr | Width | 항목 |
|---|---|---|
| **D280** | **32** | Refriger Total Usage (Kg) |
| **D282** | **32** | Total Injection Count (전체) |
| **D284** | **32** | Total Charging Pulse |
| **D286** | **32** | Last Actual Injection Volume |
| **D288** | **32** | Last Injection Setting Amount |
| **D290~D299** | — | 예비 (10 words) |

#### System Configuration

| Addr | Width | 항목 | Default |
|---|---|---|---|
| **D228** | 16 | Line Count (1 or 2) | 1 |
| **D230** | 16 | Gun Per Line (1 or 2) | 1 |
| **D232** | 16 | Total Gun (= D228 × D230, Read-Only) | 1 |
| **D234~D239** | — | 예비 | |

> **D Map 총괄**: D0~D299 사용 (짝수 주소 기준). 향후 확장은 D300부터.

### 3-3. T (Timer) — 100ms 설정

| Addr | Group | 용도 |
|---|---|---|
| **T0** | 진공 | Gun Vac Timer |
| **T1** | 진공 | Unit Vac Timer |
| **T2** | 진공 | Vac Check Timer |
| **T3** | 진공 | Gas Exhaust Timer |
| **T4** | 주입 | Refrig High-Speed Injection Timer |
| **T5** | 주입 | **Oil High-Speed Injection Timer** (Type 2) |
| **T6** | 주입 | Injection Timeout (Refrig) |
| **T7** | 주입 | Injection Timeout (Oil) |
| **T8** | 알람 | Pressure Alarm Delay |
| **T9** | 알람 | Vacuum Fail Delay |
| **T10** | 알람 | Injection Timeout Delay |
| **T11** | 알람 | Barcode Timeout |
| **T12** | 범용 | Buzzer ON Time |
| **T13** | 범용 | Start Pulse Width |
| **T14** | 범용 | Valve Delay |
| **T15** | 범용 | Alarm Auto-Off Delay |
| **T16~T19** | — | 예비 |

### 3-4. X (Digital Input) — Hex Address

| Addr | Line | Signal | Description |
|---|---|---|---|
| **X00** | L0 | START_PB L0 | Line 0 시작 푸시버튼 |
| **X01** | L0 | STOP_PB L0 | Line 0 정지 푸시버튼 (NC) |
| **X02** | Global | EMG_STOP | 비상정지 (NC) |
| **X03** | Global | SAFETY_RESET_PB | 안전 리셋 |
| **X04** | L0 | GUN0_SENSOR L0 | Line 0 Gun 0 장착 |
| **X05** | L0 | VAC_PUMP_FB L0 | Line 0 진공 펌프 FB |
| **X06** | L0 | PRESSURE_HIGH L0 | Line 0 압력 상한 |
| **X07** | L0 | PRESSURE_LOW L0 | Line 0 압력 하한 |
| **X08** | L0 | DOOR_GUARD L0 | Line 0 도어 인터락 |
| **X09** | L0 | REFRIG_SUPPLY L0 | Line 0 냉매 공급 |
| **X0A** | L0 | GUN1_SENSOR L0 | Line 0 Gun 1 장착 (D230≥2) |
| **X0B~X0F** | L0 | SPARE | 예비 |
| | | | |
| **X10** | L1 | START_PB L1 | Line 1 시작 (D228≥2) |
| **X11** | L1 | STOP_PB L1 | Line 1 정지 |
| **X14** | L1 | GUN0_SENSOR L1 | Line 1 Gun 0 장착 |
| **X15** | L1 | VAC_PUMP_FB L1 | Line 1 진공 펌프 FB |
| **X16** | L1 | PRESSURE_HIGH L1 | Line 1 압력 상한 |
| **X17** | L1 | PRESSURE_LOW L1 | Line 1 압력 하한 |
| **X18** | L1 | DOOR_GUARD L1 | Line 1 도어 인터락 |
| **X19** | L1 | REFRIG_SUPPLY L1 | Line 1 냉매 공급 |
| **X1A** | L1 | GUN1_SENSOR L1 | Line 1 Gun 1 장착 (D230≥2) |
| **X1B~X1F** | L1 | SPARE | 예비 |

### 3-5. Y (Digital Output) — Hex Address

> Gun Type별 사용 솔레노이드: Type0=기본1개, Type1=기본+저속2개, Type2=오일(H+L)+냉매(H+L)=4개

| Addr | Line | Gun | Signal | Used by Type |
|---|---|---|---|---|
| **Y10** | L0 | 공용 | VAC_PUMP_RUN | All |
| **Y11** | L0 | 공용 | **LINE VACUUM SOL** | All |
| **Y12** | L0 | 공용 | **LINE STEM SOL** | All (Unit Vac 시 ON) |
| **Y13** | L0 | G0 | REFRIG FAST SOL (or SINGLE) | Type0→단일, Type1/3→FAST |
| **Y14** | L0 | G0 | REFRIG NORMAL SOL | Type1/3 |
| **Y15** | L0 | G0 | OIL FAST SOL | Type3 / Type2 Oil Sol |
| **Y16** | L0 | G0 | OIL NORMAL SOL | Type3 |
| **Y17** | L0 | G1 | REFRIG FAST SOL (or SINGLE) | |
| **Y18** | L0 | G1 | REFRIG NORMAL SOL | |
| **Y19** | L0 | G1 | OIL FAST SOL | |
| **Y1A** | L0 | G1 | OIL NORMAL SOL | |
| **Y1B** | L0 | 공용 | **EXHAUST SOL** | All |
| **Y1C~Y1F** | — | — | SPARE | |
| | | | | |
| **Y20** | L1 | 공용 | VAC_PUMP_RUN | D228≥2 |
| **Y21** | L1 | 공용 | **LINE VACUUM SOL** | |
| **Y22** | L1 | 공용 | **LINE STEM SOL** | |
| **Y23** | L1 | G0 | REFRIG FAST SOL | |
| **Y24** | L1 | G0 | REFRIG NORMAL SOL | |
| **Y25** | L1 | G0 | OIL FAST SOL | |
| **Y26** | L1 | G0 | OIL NORMAL SOL | |
| **Y27** | L1 | G1 | REFRIG FAST SOL | |
| **Y28** | L1 | G1 | REFRIG NORMAL SOL | |
| **Y29** | L1 | G1 | OIL FAST SOL | |
| **Y2A** | L1 | G1 | OIL NORMAL SOL | |
| **Y2B** | L1 | 공용 | **EXHAUST SOL** | |
| **Y2C~Y2F** | — | — | SPARE | |
| | | | | |
| **Y30** | Global | BUZZER | | |
| **Y31** | Global | LAMP_GREEN | | |
| **Y32** | Global | LAMP_RED | | |
| **Y33** | Global | LAMP_YELLOW | | |
| **Y34** | Global | SAFETY_RESET_ACK | | |
| **Y35~Y3F** | — | SPARE | | |

---

## 4. 메인 시퀀스 설계 (Step Control)

> **핵심 원칙**: Line 0, Line 1은 **완전히 독립적인** 시퀀스를 가진다. 각 Line은 자체 Step M-Relay로 제어되며, 상대 Line 상태에 영향받지 않는다. 단, EMG Stop / Safety Fault는 전체 정지.

### 4-1. 시퀀스 상태 천이도 (Line 0 기준, Line 1은 M-relay +10 offset)

```
                         ┌──────────────────────────────────────────┐
                         │              ANY STEP                    │
                         │         EMG Stop / Safety Fault          │
                         └─────────────────┬────────────────────────┘
                                           ▼
                                      ┌─────────┐
                                      │  ALARM  │ (M90/M91 ON → 전체정지)
                                      └────┬────┘
                                           │ ALARM RESET + 조건 정상
                                           ▼
    ┌──────┐   START    ┌───────────┐   OK   ┌──────────┐   Done   ┌───────────┐
    │ IDLE │───────────▶│ PRECHECK  │───────▶│ GUN VAC  │─────────▶│ UNIT VAC  │
    │ M10  │   (M59)    │ M11       │        │ M12      │          │ M13       │
    └──────┘            └───────────┘        └──────────┘          └─────┬─────┘
         ▲                                                               │ Done
         │                    ┌──────────┐    ┌───────────┐    ┌─────────▼────┐
         │◀── CycleDone───────│ COMPLETE │◀───│GAS EXHAUST│◀───│  VAC CHECK   │
         │   M38 ON          │ M18      │    │ M17       │    │  M14          │
         │                    └──────────┘    └─────┬─────┘    └───────┬───────┘
         │                                          │Done              │Done
         │                                   ┌──────▼──────┐          │
         │                                   │ LOW SPEED   │◀─────────┘
         │                                   │ INJECTION   │
         │                                   │ M16         │    (현재 Gun 기준)
         │                                   └──────┬──────┘
         │                                          │Done (목표량 도달)
         │                                   ┌──────▼──────┐
         └───────────────────────────────────│ HIGH SPEED  │
            (Stop M60 누르면 Idle로 복귀)     │ INJECTION   │
                                             │ M15         │
                                             └─────────────┘
```

> Line 1: M20~M28 (Step), M40~M48 (Done/Fail), START=M61, STOP=M62. 동일한 천이 구조.

### 4-2. Gun 선택과 시퀀스 연동

```
[Line 내 Gun 선택] (D230≥2 구성에서 HMI Gun Select로 활성 Gun 결정)
    선택된 Gun의 Type(D32, D46, D60, D74)에 따라 주입 시퀀스 분기:

    Type 0 (1-Sol):
        VAC CHECK OK → INJECTION (단일솔 ON→목표량→OFF) → GAS EXHAUST → COMPLETE

    Type 1 (Refrig H+L, 2-Sol):
        VAC CHECK OK → RF_H + RF_L 동시 ON → RF고속정지(D8) 도달 → RF_H OFF, RF_L로 최종목표 → GAS EXHAUST → COMPLETE

    Type 2 (Oil 1+Refrig 1, 2-Sol):
        VAC CHECK OK → Oil_Sol ON → Oil목표 도달 → Oil_Sol OFF → Refrig_Sol ON → Refrig목표 도달 → Refrig_Sol OFF → GAS EXHAUST → COMPLETE

    Type 3 (Oil+Refrig H+L, 4-Sol):
        VAC CHECK OK → Oil_H+Oil_L 동시 ON → Oil고속정지(D10) → Oil_H OFF, Oil_L로 Oil완료 →
        RF_H+RF_L 동시 ON → RF고속정지(D8) → RF_H OFF, RF_L로 RF완료 → GAS EXHAUST → COMPLETE
```

### 4-3. 스텝 상세 정의 (Line 0 / Line 1 공통)

| Step | L0-M | L1-M | Entry | Action | Exit | Timeout |
|---|---|---|---|---|---|---|
| **IDLE** | M10 | M20 | Power ON / CycleDone / Stop | 초기화, PC Write 대기, **Gun Coupler 체크** | START + 조건 충족 → 진입 | — |
| **PRECHECK** | M11 | M21 | IDLE→START | 인터락 체크, Safety, Pressure, 진공 펌프 기동, **Gun Coupler ON 확인** | 모든 조건 OK → Next | 5s |
| **GUN VAC** | M12 | M22 | PRECHECK OK | **LINE VAC SOL** ON, T0, **Gun Coupler 감시** | T0 ≥ D2 → Done (NO ALARM) | D2+10s |
| **UNIT VAC** | M13 | M23 | GUN VAC Done | **LINE VAC SOL + LINE STEM SOL** ON, T1, Vacuum EU 감시 | T1 ≥ D4 AND Vac ≤ D22 → Done | D4+10s |
| **VAC CHECK** | M14 | M24 | UNIT VAC Done | **모든 Vac SOL OFF**, T2, P_start | T2 ≥ D6 AND Vac ≤ D24 → Done | D6+5s |
| **OIL FAST INJ** | M19 | M29 | VAC CHECK OK AND Type=3 | **OIL FAST+NORMAL 동시 ON**, T5 | 적산 ≥ OilVol−D12 → FAST OFF | |
| **OIL NORMAL INJ** | M1A | M2A | OIL FAST Done | OIL NORMAL ON | 적산 ≥ OilVol−D28 → |실주입−목표| ≤ D28 확인 | |
| **REFRIG FAST INJ** | M15 | M25 | VAC CHECK OK or OIL 완료 | Type1/3: **REFRIG FAST+NORMAL 동시 ON** | 적산 ≥ 목표−D10 → FAST OFF | D10/유량+10s |
| **REFRIG NORMAL INJ** | M16 | M26 | FAST → D10 도달 | REFRIG NORMAL ON | 적산 ≥ 목표−D26 → |실주입−목표| ≤ D26 확인 | |
| **EXHAUST** | M17 | M27 | INJ Done | **EXHAUST SOL** ON, T3 | T3 ≥ D8 → FINISH (NO ALARM) | D8+5s |
| **COMPLETE** | M18 | M28 | EXHAUST Done | 주입횟수+1, 사용량 적산, CycleDone SET, PC Write 0 Clear | Auto→IDLE | — |

> **Gun Coupler Sensor**: 전 공정에서 OFF 감지 시 **즉시 Alarm + OPERATION STOP**. ALL Solenoid OFF, IDLE 복귀.  
> **±Tolerance**: 실주입량과 목표량 차이가 D26(Refrig) / D28(Oil) 초과 시 NG ALARM / STOP.

### 4-4. 시퀀스 실패 처리

| 실패 조건 | 감지 시점 | L0 Flag | L1 Flag | 액션 |
|---|---|---|---|---|
| 진공 타임아웃 | GUN/UNIT VAC | M30/M32 Fail | M40/M42 Fail | Alarm SET, IDLE 복귀 |
| 진공 리크 | VAC CHECK | M34 Fail | M44 Fail | Alarm SET, IDLE 복귀 |
| 주입 타임아웃 | HIGH/LOW INJ | M36 Fail | M46 Fail | Alarm SET, 가스 배기 후 IDLE |
| 압력 이상 | PRECHECK/상시 | M98~M99 Alarm | M120~M129 | 주입 중 정지 |
| Emergency Stop | ANY | **전체 정지** | M90 Latch | 전 출력 OFF |
| Safety PLC Fault | ANY | **전체 정지** | M91 Latch | 전 출력 OFF |
| Gun 미장착 | PRECHECK | M134=M144 | — | 진행 불가 |
| Barcode Fail | PRECHECK | M171 | M171 | Alarm |

---

## 5. 진공 시퀀스 상세 (gunvac.csv / unitvac.csv)

> 각 Line 독립 실행. Line 0은 M150~M153 사용, Line 1은 M170~M173 사용.  
> **솔레노이드 구성**: LINE VACUUM SOL (공통) + LINE STEM SOL (Unit Vac 시 추가)

### 5-1. Solenoid 동작 요약

| 공정 | LINE VACUUM SOL | LINE STEM SOL | Timer | 종료 조건 | Alarm |
|---|---|---|---|---|---|
| **GUN VACUUM** | ON | OFF | T0 ≥ D2 | Time Over → FINISH | **NO ALARM** |
| **UNIT VACUUM** | ON | ON | T1 ≥ D4 | Time Over → FINISH | Vacuum > D22 → **NG ALARM / STOP** |
| **VACUUM CHECK** | OFF | OFF | T2 ≥ D6 | Time Over → FINISH | Vacuum > D24 → **NG ALARM / STOP** |

### 5-2. GUN VACUUM

```
[진입] M12/M22 ON
    ├── LINE VACUUM SOL(L0: M150, L1: M170) ON
    ├── LINE STEM SOL(L0: M151, L1: M171) OFF
    ├── Vacuum Pump Run(L0: M153, L1: M173) ON
    ├── Timer T0 START (L0: D2, L1: D32)
    │
    ├── [T0 Done] → Gun Vac Done (L0: M30, L1: M40) ON
    │   └── NO ALARM (단순 Time 기준, 진공도 체크 없음)
    │
    └── 진공 펌프 FB 확인 (L0: X05→M132, L1: X15→M142)
```

### 5-3. UNIT VACUUM

```
[진입] M13/M23 ON
    ├── LINE VACUUM SOL(L0: M150, L1: M170) ON
    ├── LINE STEM SOL(L0: M151, L1: M171) ON  ← 추가 솔레노이드
    ├── Vacuum Pump Run(L0: M153, L1: M173) ON
    ├── Timer T1 START (L0: D4, L1: D34)
    ├── Vacuum EU(L0: D160~D161, L1: D172~D173) 감시
    │
    ├── [T1 Done]
    │   ├── Vacuum EU ≤ Setting(L0: D22~D23, L1: D50~D51)
    │   │   └── Unit Vac Done (L0: M32, L1: M42) ON → Next
    │   │
    │   └── Vacuum EU > Setting → **NG ALARM**
    │       └── L0: M33 ON, Alarm M111  /  L1: M43 ON, Alarm M121
    │       └── OPERATION STOP → IDLE 복귀
```

### 5-4. VACUUM CHECK

```
[진입] M14/M24 ON
    ├── LINE VACUUM SOL(L0: M150, L1: M170) OFF
    ├── LINE STEM SOL(L0: M151, L1: M171) OFF
    ├── Vacuum Pump Run OFF
    ├── P_start = Current Vacuum → L0: D182~D183, L1: D202~D203
    ├── Timer T2 START (L0: D6, L1: D36)
    │
    ├── [T2 Done]
    │   ├── ΔP = P_end − P_start 계산
    │   ├── Vacuum EU ≤ Setting(L0: D24~D25, L1: D52~D53)
    │   │   └── Vac Check Done (L0: M34, L1: M44) ON → Next
    │   │
    │   └── Vacuum EU > Setting → **NG ALARM**
    │       └── L0: M35 ON, Alarm M112  /  L1: M45 ON, Alarm M122
    │       └── OPERATION STOP → IDLE 복귀
```
[진입] Step Signal ON (L=0: M12, L=1: M22)
    ├── VacuumPumpRun(L=0: M153, L=1: M173) ON (피드백 확인)
    ├── 해당 Vac Valve ON
    │     Gun Vac:  L=0: M150, L=1: M170
    │     Unit Vac: L=0: M151, L=1: M171
    ├── Timer(T0 or T1) START (L0: D2 or D4, L1: D32 or D34)
    ├── Vacuum EU(L=0: D160~D161, L=1: D172~D173) ≤ 설정값(L0: D22~D23, L1: D50~D51) 체크
    │
    ├── [OK]  Timer Done AND Vacuum ≤ Setting
    │       L0: M30/M32 ON,  L1: M40/M42 ON → Step Next
    │
    └── [Fail] Timer Done AND Vacuum > Setting
            L0: M31/M33 ON, Alarm M110  /  L1: M41/M43 ON, Alarm M120
```

### 5-2. Vacuum Check 상세 (vacchec.csv)

```
[진입] L0: M14 ON / L1: M24 ON
    ├── 모든 Vac Valve OFF
    ├── VacuumPumpRun OFF
    ├── P_start = Current Vacuum → L0: D182~D183, L1: D202~D203
    ├── Timer T2 START (L0: D6, L1: D36)
    │
    ├── [T2 Done] P_end = Current Vacuum
    │   ├── ΔP = P_end - P_start → L0: D184~D185, L1: D204~D205
    │   │
    │   ├── [OK]  ΔP ≤ 허용치 (L0: D24~D25, L1: D52~D53)
    │   │       L0: M34 ON  /  L1: M44 ON
    │   │
    │   └── [Fail] ΔP > 허용치 → LEAK
    │           L0: M35 ON, Alarm M110  /  L1: M45 ON, Alarm M120
```

---

## 6. 주입 시퀀스 상세 (refinj.csv)

> **공통**: FAST SOL + NORMAL SOL **동시 ON**. FAST 중단량 도달 → FAST OFF, NORMAL로 최종 목표까지. 실주입량 ±Tolerance 초과 → NG ALARM / STOP.

### 6-1. Type 0 — 1-Sol Refrig

```
[진입] M15/M25 ON
    ├── REFRIG SOL(L0: M154, L1: M174) ON  // FAST SOL 단독 사용
    ├── InjectionActive(L0: M158, L1: M178) ON, T4 START
    ├── 적산(L0: D180~D181, L1: D200~D201)
    │
    ├── [완료] 적산 ≥ (RefrigVol + 보정 − D26)
    │   ├── REFRIG SOL OFF, InjDone(L0: M36, L1: M46) ON
    │   │
    │   └── [실주입량 ±Tolerance Check] |실주입량 − 목표| > D26 → **NG ALARM**
    │       └── L0: M37 ON, Alarm M115  /  L1: M47 ON, Alarm M125
    │       └── OPERATION STOP → GAS EXHAUST 후 IDLE
    │
    └── [FAIL] T4 타임아웃 → InjFail, Alarm M113/M123
```

### 6-2. Type 1 — Refrig FAST + NORMAL (2-Sol)

```
[진입] M15/M25 ON
    ├── REFRIG FAST SOL(L0: M154, L1: M174) ON AND REFRIG NORMAL SOL(L0: M155, L1: M175) ON  ← 동시 ON
    ├── InjectionActive(L0: M158, L1: M178) ON, T4 START
    ├── 적산(L0: D180~D181, L1: D200~D201)
    │
    ├── [FAST STOP] 적산 ≥ (목표 − D10)
    │   ├── REFRIG FAST SOL OFF  ← FAST만 OFF
    │   ├── REFRIG NORMAL SOL ON 유지
    │   └── M16/M26 ON (NORMAL SPEED)
    │
    ├── [완료] 적산 ≥ (목표 − D26)
    │   ├── REFRIG NORMAL SOL OFF, InjDone(L0: M36, L1: M46) ON
    │   │
    │   └── [±Tolerance Check] |실주입량 − 목표| > D26 → **NG ALARM / STOP**
    │
    └── [FAIL] T4 타임아웃 → InjFail
```

### 6-3. Type 2 — Oil 1-Sol + Refrig 1-Sol

```
[Phase 1 — OIL] M19/M29 ON
    └── (Type 0과 동일 패턴, Oil Sol로 오일 주입 후 D28 Tolerance 체크)

[Phase 2 — REFRIG] M15/M25 ON
    └── (Type 0과 동일 패턴)
```

### 6-4. Type 3 — Oil FAST+NORMAL + Refrig FAST+NORMAL

```
[Phase 1 — OIL] M19/M29 ON
    ├── OIL FAST SOL(L0: M156, L1: M176) ON AND OIL NORMAL SOL(L0: M157, L1: M177) ON
    ├── T5 START, 적산
    ├── 적산 ≥ (OilVol − D12) → OIL FAST OFF, NORMAL 유지
    ├── 적산 ≥ (OilVol − D28) → OIL NORMAL OFF, |실주입−목표| > D28 → NG ALARM
    │
[Phase 2 — REFRIG] M15/M25 ON
    └── (Type 1과 동일 패턴)
```

### 6-5. 보정 로직 (Active Gun G, Base=D60+G×14)

```
실제 목표(Refrig) = RefrigVol(D64+G×14) + Corr(D66+G×14) + HMI_Cal(D68+G×14) + Batch(D70+G×14)
실제 목표(Oil)    = OilVol(D72+G×14)                                          // Type 2,3
```

---

## 6B. EXHAUST 시퀀스 (DEAD ZONE)

```
[진입] M17/M27 ON
    ├── EXHAUST SOL(L0: M152, L1: M172) ON
    ├── Timer T3 START (L0: D8, L1: D38)
    │
    ├── [T3 Done] → EXHAUST FINISH
    │   └── NO ALARM (단순 Time 기준)
    │
    └── → COMPLETE (M18/M28)
```

---

## 6C. GUN COUPLER SENSOR INTERLOCK (전 공정)

```
[감시] 전 공정에서 GUN COUPLER SENSOR(X04/X0A, X14/X1A) 상태 감시
    Gun Coupler Sensor OFF 감지 시 → **IMMEDIATE ALARM / OPERATION STOP**
    ├── L0: M134 OFF → Alarm (Gun Not Connected)
    ├── L1: M144 OFF → Alarm
    └── All Solenoid OFF, IDLE 복귀
```

---

## 7. 알람 설계 (alarm.csv)

### 7-1. 알람 구조

```
[Global Alarm]  M90~M103  ← Line 상관없이 전체 영향 (EMG, Safety 등)
[Line 0 Alarm]  M110~M119 ← Line 0 전용 인스턴스
[Line 1 Alarm]  M120~M129 ← Line 1 전용 인스턴스 (D228≥2)
```

> Global Alarm 발생 시 → Global Action (전 출력 OFF). Line Alarm 발생 시 → 해당 Line만 정지.

### 7-2. 알람 목록

| # | Alarm | Global Dev | L0 Inst | L1 Inst | Level | Action |
|---|---|---|---|---|---|---|
| 1 | Emergency Stop | M90 | — | — | **Critical** | 전 출력 OFF, Latch |
| 2 | Safety PLC Fault | M91 | — | — | **Critical** | 전 출력 OFF, Latch |
| 3 | Gun Vacuum Timeout | — | M110 | M120 | Major | 해당 Line 정지 |
| 4 | Unit Vacuum Timeout | — | M111 | M121 | Major | 해당 Line 정지 |
| 5 | Vacuum Leak | — | M112 | M122 | Major | 해당 Line 정지 |
| 6 | Injection Timeout | — | M113 | M123 | Major | 해당 Line 정지 |
| 7 | Injection Over | — | M114 | M124 | Minor | 경고 |
| 8 | Injection Under | — | M115 | M125 | Major | 해당 Line 정지 |
| 9 | Pressure High | — | M116 | M126 | Major | 해당 Line 정지 |
| 10 | Pressure Low | — | M117 | M127 | Major | 해당 Line 정지 |
| 11 | Temperature Abnormal | — | M118 | M128 | Minor | 경고만 |
| 12 | Refriger Bombe Low | M101 | — | — | Minor | Global 경고 |
| 13 | Barcode Read Fail | M102 | — | — | Minor | 해당 Line 시작 불가 |
| 14 | SCAN Comm Fail | M103 | — | — | Minor | 경고 |
| 15 | Gun Not Connected | — | L0:M134, L1:M144 | — | Minor | 해당 Line 시작 불가 |

### 7-3. 알람 처리 로직

```
[알람 검출 — Global]
    M90 = X02 (EMG Stop, NC→OFF 시 SET)
    M91 = !X10 (Safety PLC Healthy OFF 시 SET)
    M101 = D12~D13 ≥ D10~D11 (봄베 부족)
    M102 = Barcode Read Fail
    M103 = SCAN Comm Timeout

[알람 검출 — Line Instance]
    Line 0 Alarm = L0 조건 OR → M110~M118 SET
    Line 1 Alarm = L1 조건 OR → M120~M128 SET (D228≥2일 때만)

[알람 출력]
    Global OR L0 Alarm OR L1 Alarm → LAMP_RED(Y18) ON
    Line Alarm AND M42(INTERLOCK USE) → 해당 Line Interlock Active(M130/M140)

[부저]
    알람 발생 Edge → BUZZER(Y16) ON
    BUZZER STOP(M44) PULSE → BUZZER OFF
    T12 (Buzzer Auto-Off Timer) → BUZZER OFF

[알람 리셋]
    ALARM RESET(M43) PULSE AND (알람 조건 모두 해제)
    → Global(M90~M103) RST + 해당 Line Instance RST
    → LAMP_RED OFF
```

---

## 8. 인터락 설계 (gmes.csv 내)

### 8-1. 인터락 조건 (Line L 기준)

| Condition | L0 Device | L1 Device | Logic |
|---|---|---|---|
| Emergency Stop NOT Active | M90 (NC) | 동일 | Global |
| Safety PLC Healthy | M131 (X0B) | M141 | Global |
| **Gun Coupler Sensor** | M134 (X04/X0A) | M144 (X14/X1A) | **전 공정 감시. OFF→즉시 STOP** |
| Door/Guard Closed | X08 | X18 | Line별 |
| Pressure Normal Range | M133 | M143 | L0: D18≤P≤D20, L1: D46≤P≤D48 |
| Refriger Supply OK | M135 | M145 | X09(L0) / X19(L1) |
| Vacuum Pump Run FB OK | M132 | M142 | X05(L0) / X15(L1) |

### 8-2. Start 조건 + Barcode 처리 (Line L 기준)

```
[START 버튼 Rising Edge — L0: M59, L1: M61]
    1. 인터락 체크 (Line L)
       START 가능 = IDLE 상태(L0:M10, L1:M20)
                 AND NOT Emergency Stop(M90)
                 AND NOT 해당 Line Alarm Latch
                 AND Gun Connected(L0:M134, L1:M144)
                 AND Pressure Normal(L0:M133, L1:M143)
                 AND Refriger Supply OK(L0:M135, L1:M145)
                 AND (INTERLOCK NOT USE → M42 OFF) OR (ALL 인터락 OK)

    2. Barcode 데이터 복사 (Line L PC Write Area → Working Area)
       L0: BMOV D190 D210 K20
       L1: BMOV D230 D250 K20  (D228≥2)
       → Model#(L0:D210, L1:D250) → D84 (현재 선택 Line 표시)
       → Working Area Valid(L0:M193, L1:M194) SET

    3. 시퀀스 진입 → PRECHECK (L0:M11, L1:M21)
```

---

## 9. 통신 설계 (485.csv)

### 9-1. Barcode 데이터 흐름 (PC ↔ PLC) — Line별 독립 영역

| Line | PC Write Area | Working Area | START | Cycle Done | Valid Flag |
|---|---|---|---|---|---|
| **Line 0** | D190~D209 | D210~D229 | M59 | M38 | M193 |
| **Line 1** | D230~D249 | D250~D269 | M61 | M48 | M194 |

```
[IDLE 대기 중 — Line L]
    PC Write Area(L0:D190~D209, L1:D230~D249) ← PC에서 바코드 Write
    Working Area = 0

[START (Line L) Rising Edge]
    L0: BMOV D190 D210 K20
    L1: BMOV D230 D250 K20
    Working Area로 Model, Line, Gun, Serial 설정

[Cycle 동작 중]
    Working Area Read-Only (변경 불가)

[Cycle Complete (Line L Done or Fail)]
    L0: FMOV K0 D190 K20
    L1: FMOV K0 D230 K20
    → PC는 해당 Line Write Area=0 확인 후 다음 바코드 Write
```

### 9-2. Barcode 데이터 구조

| Offset | L0 Write | L0 Work | L1 Write | L1 Work | 내용 |
|---|---|---|---|---|---|
| +0 | D190 | D210 | D230 | D250 | Model Number (16-bit) |
| +1 | D191 | D211 | D231 | D251 | Line / Gun Select (16-bit) |
| +2~+3 | D192~D193 | D212~D213 | D232~D233 | D252~D253 | Serial No Low (32-bit) |
| +4~+5 | D194~D195 | D214~D215 | D234~D235 | D254~D255 | Serial No High (32-bit) |
| +6 | D196 | D216 | D236 | D256 | Refriger Type (16-bit) |
| +7 | D197 | D217 | D237 | D257 | Injection Amount (16-bit) |
| +8~+19 | D198~D209 | D218~D229 | D238~D249 | D258~D269 | Reserve |

### 9-6. SCAN 데이터

```
SCAN → PLC: 현재 SCAN 주입량 (16-bit, gram)
PLC → D94 저장
Barcode와 SCAN 주입량 크로스체크 (Option)
```

---

## 10. SPC/통계 (spc.csv)

### 10-1. 누계 데이터 (Global 합산)

| Data | Device | Update Trigger |
|---|---|---|
| 냉매 총 사용량 (Kg) | D280~D281 | 모든 Line Cycle Complete 시 실주입량 합산 |
| 총 주입 횟수 | D282~D283 | 모든 Line Cycle Complete 시 +1 |
| 총 펄스 카운트 | D284~D285 | 매 주입 시 펄스 누계 합산 |
| 최근 실주입량 | D286~D287 | 마지막 Cycle Complete 시 기록 |
| 최근 설정 주입량 | D288~D289 | 마지막 Cycle Complete 시 기록 |

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
HMI Write → M50~M72 → PLC → Line Select(M80/M81) → Active Line 결정
Line 0: M10~M18 Step → M130~M135 Interlock → M150~M156 Control → Y10~Y1A Actuator
Line 1: M20~M28 Step → M140~M145 Interlock → M160~M166 Control → Y1B~Y2x Actuator
D228=1 이면 Line 1 로직 Skip (M800 조건 분기)
D230=1 이면 Gun 1 로직 Skip (1 Gun/Line 모드)
PC Write → D190~D209(L0) / D230~D249(L1) → START → Working Area → Cycle 사용
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
    │◀─────── SafetyOK (X0B) ───────────│ (Healthy Signal → M131/M141)
    │                                    │
    │─────── Y1C Reset Ack ─────────────▶│
    │                                    │
    │  EMG Stop (X02) ← hardwired ──────│ Emergency Stop Relay
    │                                    │
    │  Safety Reset PB (X03) ───────────▶│ Reset Request
```

Safety PLC가 독립적으로 Emergency Stop 회로를 감시. Main PLC는 Safety PLC Healthy 신호(X0B→M131/M141)가 ON일 때만 동작. Reset Ack는 Y1C 사용.

---

## 14. CSV 파일별 주요 디바이스 사용 요약

| CSV File | 입력 (Read) | 출력 (Write) | 주요 Mnemonic |
|---|---|---|---|
| **idata.csv** | X00~X2F (2 Line), D228~D230(Config) | M0~M2, Line Step 초기화 | LD, MOV, SET, RST |
| **gmes.csv** | M10~M49(Step/Done), M50~M72(HMI), M130~M145(Interlock×2), D228~D230 | Y31~Y33(Lamp), M10~M29(Step), M30~M49(Done), M80~M81(Line Sel), BMOV, FMOV | LD=, AND=, OR=, SET, RST, OUT, MOV, CJ, BMOV, FMOV, **CJ**(D228=1→L1 Skip) |
| **setting.csv** | D0~D28(Param), D30~D85(User×4×14word) | D0~D28, D30~D85 | DMOV, MOV, LD= |
| **gunvac.csv** | M12/M22, M132/M142, D0, D20~D21, Line Vacuum EU | M150/M170, T0, M30/M40, M31/M41, Line Alarm | LD, AND, OUT, MOV, DMOV, LDD<=, SET, RST, TMR |
| **unitvac.csv** | M13/M23, D2, D20~D21, Line Vacuum EU | M151/M171, T1, M32/M42, M33/M43, Line Alarm | LD, AND, OUT, MOV, DMOV, LDD<=, SET, RST, TMR |
| **vacchec.csv** | M14/M24, D4, D22~D23, Line Vacuum EU | T2, M34/M44, M35/M45, D152/D172, D154/D174, Line Alarm | LD, AND, MOV, DMOV, D-, LDD<=, SET, RST, TMR |
| **refinj.csv** | M15~M16/M25~M26, M19~M1A/M29~M2A, D8/D10/D24/D26, D30~D85(User), Active Gun Type | M154~M163/M174~M183(Valves), T4/T5, M36~M37/M46~M47, D98~D105(Display) | LD, AND, D+, D-, D*, D/, LDD=, LDD<=, LDD>=, MOV, DMOV, SET, RST, TMR, **CJ**(Type 분기) |
| **alarm.csv** | M90~M109(Global), M110~M129(Line), M42~M44 | Y30, Y32~Y33, M90~M129 | LD, OR, SET, RST, OUT, TMR |
| **ad.csv** | D120~D143(2 Line Raw) | D122~D143(EU), D108~D119(Display) | LD, MOV, DMOV, D*, D/, D+, D- |
| **485.csv** | RS-485 Buffer | D190~D269(2 Line PC/Work), M190~M194 | LD, MOV, AND=, SET, RST |
| **spc.csv** | M38/M48(CycleDone×2), D100~D105 | D280~D289(SPC Global), D88, M101 | LD, D+, DMOV, LDD>=, SET |

