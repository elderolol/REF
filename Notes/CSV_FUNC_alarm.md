# REFRIGER CHARGING MACHINE — Function Spec: alarm.csv

> **Module**: `alarm.csv`  
> **Execution**: Always ON  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

모든 알람 조건을 감시하고, 알람 발생 시 Latch, Buzzer/Lamp 출력 제어,
Alarm Reset 처리, 출력 Interlock (알람 중 모든 출력 차단) 담당.

---

## 2. Inputs

| Device | Source | Description |
|:------:|:------:|-------------|
| M303 | input.csv | EMG_STOP (NC Open = EMG) |
| M30B | input.csv | SAFETY_PLC_HEALTHY |
| L11/L21 | gunvac | GunVac NG |
| L13/L23 | unitvac | UnitVac NG |
| L15/L25 | vacchec | Vacuum Leak |
| L17/L27 | refinj | Injection NG (Timeout/Over/Under) |
| M308 | input.csv | PRESSURE_SW_H_L0 |
| M318 | input.csv | PRESSURE_SW_H_L1 |
| M309 | input.csv | PRESSURE_SW_L_L0 |
| M319 | input.csv | PRESSURE_SW_L_L1 |
| D156/D168 | ad.csv | Temperature EU (L0/L1) |
| D16 | setting | Refriger Used Amount (32-bit) |
| D14 | setting | Bombe Alarm Setting (32-bit) |
| M307 | input.csv | DOOR_SENSOR_L0 (방폭) |
| M317 | input.csv | DOOR_SENSOR_L1 (방폭) |
| M403 | HMI | ALARM RESET Button |
| M404 | HMI | BUZZER STOP Button |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| L40 | EMG Stop Alarm Latch |
| L41 | Safety PLC Fault Latch |
| L42 | Gun Vacuum Timeout Latch |
| L43 | Unit Vacuum Timeout Latch |
| L44 | Vacuum Leak Latch |
| L45 | Injection Timeout Latch |
| L46 | Injection Over Latch |
| L47 | Injection Under Latch |
| L48 | Pressure High Latch |
| L49 | Pressure Low Latch |
| L4A | Temperature Abnormal Latch |
| L4B | Refriger Bombe Low Latch |
| L4C | SPARE |
| L4D | SPARE |
| L4E | Door Open Latch (방폭 전용) |
| L4F | 예비 |
| M4C | BUZZER (→ output.csv → Y30) |
| M4D | LAMP_GREEN (→ Y31) |
| M4E | LAMP_RED (→ Y32) |
| M4F | LAMP_YELLOW (→ Y33) |

---

## 4. Alarm Detection & Latch Logic

| Latch | Source Condition | SET Logic |
|:-----:|:----------------:|:---------:|
| **L40** | EMG Stop | M303 OFF (NC Open) → SET L40 |
| **L41** | Safety Fault | M30B OFF → SET L41 |
| **L42** | GunVac Timeout | L11 OR L21 → SET L42 |
| **L43** | UnitVac Timeout | L13 OR L23 → SET L43 |
| **L44** | Vacuum Leak | L15 OR L25 → SET L44 |
| **L45** | Injection Timeout | L17(L7) + Timeout Flag → SET L45 |
| **L46** | Injection Over | L17(L7) + Over Flag → SET L46 |
| **L47** | Injection Under | L17(L7) + Under Flag → SET L47 |
| **L48** | Pressure High | M308 OR M318 ON → SET L48 |
| **L49** | Pressure Low | M309 OR M319 ON → SET L49 |
| **L4A** | Temp Abnormal | D156 < -200 OR D156 > 800 (L0) OR D168 범위外 → SET L4A |
| **L4B** | Bombe Low | D16 ≥ D14 (32-bit compare) → SET L4B |
| **L4C** | SPARE | — |
| **L4D** | SPARE | — |
| **L4E** | Door Open | M307 ON OR M317 ON (방폭 only) → SET L4E |

> **모든 Latch는 SET 후 M403(ALARM RESET) Rising Edge로만 RST 가능**  
> 단, RST 조건: Source Condition이 해소되어 있어야 함.

---

## 5. Buzzer Control

```
// Alarm 발생 시 Buzzer ON
LD  L40    // EMG
OR  L41    // Safety
OR  L42    // GunVac
OR  L43    // UnitVac
OR  L44    // Leak
OR  L45    // Inj Timeout
OR  L46    // Inj Over
OR  L47    // Inj Under
OR  L48    // Press High
OR  L49    // Press Low
OR  L4A    // Temp
OR  L4B    // Bombe
OR  L4E    // Door
OUT M4C    // Buzzer ON

// BUZZER STOP (M404) → Buzzer만 OFF (Alarm Latch는 유지)
LD  M404   // Buzzer Stop Button
RST M4C
```

---

## 6. Lamp Control

```
// GREEN Lamp: Running + No Alarm
LD  M10 OR M11 OR M12 OR M13 OR M14 OR M15 OR M16 OR M17 OR M18
    (Any L0 Step Active)
AND L40 NOT (No Alarm)
OUT M4D    // LAMP_GREEN

// RED Lamp: Any Alarm
LD  L40 OR L41 OR ... OR L4E  (Any Alarm)
OUT M4E    // LAMP_RED

// YELLOW Lamp: Interlock Not OK
LD  L50 NOT (L0 Interlock)
OR  L60 NOT (L1 Interlock, D270≥2)
AND M10 (IDLE 상태에서)
OUT M4F    // LAMP_YELLOW
```

---

## 7. Alarm Reset Logic

```
M403 (ALARM RESET) ─── Rising Edge (PLS)
    │
    ├── Source Condition Check
    │   ├── M303=ON? (EMG 해소) → RST L40
    │   ├── M30B=ON? (Safety OK) → RST L41
    │   ├── (각 Latch Source 조건 확인 후 RST)
    │   └── 조건 미해소 → 해당 Latch 유지
    │
    └── RST M4C (Buzzer 추가 정지)
```

---

## 8. Output Interlock

> 알람 발생 중에는 모든 출력 강제 차단.

```
// L40(EMG) 또는 L41(Safety) 발생 시
// 모든 Solenoid Coil Image 강제 RST (idata.csv와 연동)

LD  L40
OR  L41
    → (Alarm.csv 내에서) 모든 M30~M4F를 RST
    → gmes.csv와 연동하여 Step Bit RST

// 기타 알람(L42~L4E)은 해당 Line/Gun의 Injection만 차단
```

---

## 9. EMG Priority

```
L40 (EMG Stop)은 모든 것보다 최우선:

1. 동일 스캔 내에서 즉시 M30~M4F 전부 RST
2. M10~M28 전부 RST (IDLE 강제)
3. Buzzer ON
4. Lamp RED ON
5. 모든 Timer RST
```

---

## 10. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Alarm source read |
| `OR` | Multiple alarm OR |
| `SET` | Alarm Latch |
| `RST` | Alarm Latch Clear |
| `OUT` | Buzzer / Lamp |
| `TMR` | Alarm delay timer |
| `LDD>=` | Bombe compare (32-bit) |
