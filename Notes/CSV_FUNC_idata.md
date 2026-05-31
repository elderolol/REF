# REFRIGER CHARGING MACHINE — Function Spec: idata.csv

> **Module**: `idata.csv`  
> **Execution**: Always ON, **first POU** in scan order  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

- 물리적 입력(X)을 내부 M 레지스터로 매핑 (input.csv 기반)
- 내부 솔레노이드 코일 이미지(M)를 물리적 출력(Y)으로 매핑 (output.csv 기반)
- 시스템 초기화 (First Scan)
- Configuration 유효성 검증

**핵심 원칙**: 프로그램 본체는 절대 X/Y를 직접 참조하지 않음.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| X00~X0F | Line 0 Physical Input (from input.csv) |
| X10~X1F | Line 1 Physical Input (from input.csv) |
| SM400 | Always ON (System Monitor) |
| SM402 | Initial Pulse (1 scan only at PLC start) |
| D270 | Line Count (Config) |
| D272 | Gun Per Line (Config) |
| D274 | Total Gun (연산값) |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| M300~M30F | Line 0 Input Mirrors (X00~X0F image) |
| M310~M31F | Line 1 Input Mirrors (X10~X1F image) |
| M30~M33 | L0 Vacuum Control Coil Images (→ output.csv → Y10~Y1B) |
| M34~M3B | L0 Injection Solenoid Coil Images (→ output.csv → Y13~Y1A) |
| M40~M43 | L1 Vacuum Control Coil Images (→ output.csv → Y20~Y2B) |
| M44~M4B | L1 Injection Solenoid Coil Images (→ output.csv → Y23~Y2A) |
| M4C~M4F | Global Output Coil Images (→ output.csv → Y30~Y33) |
| M0 | AlwaysON (SM400 mirror) |
| M1 | AlwaysOFF (SM401 mirror) |
| M2 | Initial Pulse (SM402 mirror) |
| L0 | InitDone Flag |

---

## 4. Initialization Logic (First Scan Only)

```
SM402 (Initial Pulse)
    │
    ├── SET L0 (InitDone) ────────── 정전복구 후 최초 1회만 실행
    ├── RST M10~M28 ──────────────── 모든 Step Bit 초기화 (안전상태)
    ├── RST M30~M4F ──────────────── 모든 Solenoid Coil OFF
    ├── RST L10~L29 ──────────────── 모든 Done/Fail 초기화
    ├── RST L40~L4F ──────────────── 모든 Alarm Latch 초기화
    ├── MOV D270 → D274 계산 ─────── Total Gun = D270 × D272
    └── D270/D272 Validation ─────── 범위 체크 → 이상 시 Alarm
```

---

## 5. Main Scan Logic (Always ON, SM400)

### 5-1. X → M Mapping (Input Scan)

매 스캔마다 물리적 입력 상태를 내부 M 레지스터에 복사.

```
LD  X00  →  OUT M300    // START_PB_L0
LD  X01  →  OUT M301    // STOP_PB_L0
LD  X02  →  OUT M302    // SAFETY_RESET
LD  X03  →  OUT M303    // EMG_STOP
LD  X04  →  OUT M304    // GUN_COUPLER_L0_G0
LD  X05  →  OUT M305    // GUN_COUPLER_L0_G1
LD  X06  →  OUT M306    // VAC_PUMP_FB_L0
LD  X07  →  OUT M307    // DOOR_SENSOR_L0 (방폭)
LD  X08  →  OUT M308    // PRESSURE_SW_H_L0
LD  X09  →  OUT M309    // PRESSURE_SW_L_L0
LD  X0A  →  OUT M30A    // REFRIG_SUPPLY_OK_L0
LD  X0B  →  OUT M30B    // SAFETY_PLC_HEALTHY
LD  X0C~X0F → M30C~M30F  // SPARE_DI_L0

// D228≥2 (2 Line 모드) 일 때만 유효
LD  X10  →  OUT M310    // START_PB_L1
LD  X11  →  OUT M311    // STOP_PB_L1
LD  X13  →  OUT M313    // EMG_STOP_L1
LD  X14  →  OUT M314    // GUN_COUPLER_L1_G0
LD  X15  →  OUT M315    // GUN_COUPLER_L1_G1
LD  X16  →  OUT M316    // VAC_PUMP_FB_L1
LD  X17  →  OUT M317    // DOOR_SENSOR_L1
LD  X18  →  OUT M318    // PRESSURE_SW_H_L1
LD  X19  →  OUT M319    // PRESSURE_SW_L_L1
LD  X1A  →  OUT M31A    // REFRIG_SUPPLY_OK_L1
LD  X1B~X1F → M31B~M31F  // SPARE_DI_L1
```

### 5-2. M → Y Mapping (Output Scan)

매 스캔마다 내부 솔레노이드 코일 이미지를 물리적 출력에 복사.

```
// Line 0 — 진공
LD  M30  →  OUT Y10    // VAC_PUMP_RUN_L0
LD  M31  →  OUT Y11    // LINE_VAC_SOL_L0
LD  M32  →  OUT Y12    // LINE_STEM_SOL_L0
LD  M33  →  OUT Y1B    // EXHAUST_SOL_L0

// Line 0 — Gun 0 Injection
LD  M34  →  OUT Y13    // REFRIG_BASE_SOL_L0_G0
LD  M35  →  OUT Y14    // REFRIG_NORMAL_SOL_L0_G0
LD  M36  →  OUT Y15    // OIL_BASE_SOL_L0_G0
LD  M37  →  OUT Y16    // OIL_NORMAL_SOL_L0_G0

// Line 0 — Gun 1 Injection
LD  M38  →  OUT Y17    // REFRIG_BASE_SOL_L0_G1
LD  M39  →  OUT Y18    // REFRIG_NORMAL_SOL_L0_G1
LD  M3A  →  OUT Y19    // OIL_BASE_SOL_L0_G1
LD  M3B  →  OUT Y1A    // OIL_NORMAL_SOL_L0_G1

// Line 1 — 진공 (D270≥2)
LD  M40  →  OUT Y20    // VAC_PUMP_RUN_L1
LD  M41  →  OUT Y21    // LINE_VAC_SOL_L1
LD  M42  →  OUT Y22    // LINE_STEM_SOL_L1
LD  M43  →  OUT Y2B    // EXHAUST_SOL_L1

// Line 1 — Gun 0 Injection
LD  M44  →  OUT Y23    // REFRIG_BASE_SOL_L1_G0
LD  M45  →  OUT Y24    // REFRIG_NORMAL_SOL_L1_G0
LD  M46  →  OUT Y25    // OIL_BASE_SOL_L1_G0
LD  M47  →  OUT Y26    // OIL_NORMAL_SOL_L1_G0

// Line 1 — Gun 1 Injection
LD  M48  →  OUT Y27    // REFRIG_BASE_SOL_L1_G1
LD  M49  →  OUT Y28    // REFRIG_NORMAL_SOL_L1_G1
LD  M4A  →  OUT Y29    // OIL_BASE_SOL_L1_G1
LD  M4B  →  OUT Y2A    // OIL_NORMAL_SOL_L1_G1

// Global Outputs
LD  M4C  →  OUT Y30    // BUZZER
LD  M4D  →  OUT Y31    // LAMP_GREEN
LD  M4E  →  OUT Y32    // LAMP_RED
LD  M4F  →  OUT Y33    // LAMP_YELLOW
LD  M50  →  OUT Y1C    // SAFETY_RESET_ACK
```

### 5-3. System Flags

```
LD  SM400 → OUT M0    // AlwaysON
LD  SM401 → OUT M1    // AlwaysOFF
LD  SM402 → OUT M2    // Initial Pulse (1 scan)
```

---

## 6. Config Validation

매 스캔마다 D270, D272 값의 유효성을 확인.

| Check | Condition | Action |
|-------|:---------:|--------|
| D270 Range | 1 ≤ D270 ≤ 2 | NG → 강제 MOV 2 |
| D272 Range | 1 ≤ D272 ≤ 2 | NG → 강제 MOV 2 |
| D274 계산 | D274 ≠ D270 × D272 | D274 재계산 |
| Line-Gun 불일치 | D270=1인데 Line 1 I/O 사용 | CJ로 Skip |

---

## 7. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| X→M 복사 실패 | Physical I/O Error | System Error → Alarm |
| Config Mismatch | D270/D272 불일치 | L41 (Safety Fault) |

---

## 8. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | X/M bit 읽기 |
| `OUT` | M/Y bit 쓰기 |
| `MOV` | D register 복사 (Config Validation) |
| `SET` | L0 (InitDone) 설정 |
| `RST` | Step/Alarm 초기화 |
