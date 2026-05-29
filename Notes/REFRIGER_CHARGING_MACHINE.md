# REFRIGER CHARGING MACHINE — HMI Specification

> **Domain**: Factory Automation / Refrigerant Charging Equipment  
> **Platform**: HMI + PLC (Mitsubishi)  
> **Rule**: Hardware or HMI button is ON only when pressed (momentary).

---

## 1. Operation Screen

### 1-1. Display Items

| # | Item | Data Type | Unit | Display Example |
|---|---|---|---|---|
| 1 | Refrigerant Usage | 32-bit | Kg | 12345.6 |
| 2 | Number of Injections | 16-bit | — | 12345 |
| 3 | Injection Model | 16-bit | — | 123 |
| 4 | Charging Pulse | 32-bit | — | 123456 |
| 5 | Injection Time | 16-bit | sec | 123.4 |
| 6 | Injection Setting Amount | 32-bit | g | 12345 |
| 7 | Actual Injection Volume | 32-bit | g | 12345 |
| 8 | SCAN Injection Volume | 16-bit | g | 12345 |
| 9 | Current Vacuum Level | 32-bit | Torr | 123.456 |
| 10 | Temperature | 16-bit | ℃ | 12.3 |
| 11 | Pressure | 16-bit | kgf/㎠ | 12.3 |

### 1-2. Labels

| # | Label Text |
|---|---|
| 1 | OPERATION SCREEN |
| 2 | REFRIGER TYPE |
| 3 | (REFRIGER TYPE value) |
| 4 | EACH LINE REFRIGER USED AMOUNT |
| 5 | GUN SELECT |
| 6 | INJECTION TIME |
| 7 | Number of Injections |
| 8 | INJECTION MODEL |
| 9 | INJECTION SETTING AMOUNT |
| 10 | CHARGING PULSE |
| 11 | VACUUM PUMP |
| 12 | REAL INJECTION AMOUNT |
| 13 | INJECTION TIME |
| 14 | VACUUM (Torr) |
| 15 | SCAN INFO |
| 16 | PRESSURE |
| 17 | TEMPERATURE |

### 1-3. Buttons

| # | Button | Description |
|---|---|---|
| 1 | UNIT PASS | |
| 2 | INTERLOCK USE/NOT USE | Toggle |
| 3 | ALARM RESET | |
| 4 | BUZZER STOP | |
| 5 | USER SETTING SCREEN | Navigate |
| 6 | PARAMETER SETTING SCREEN | Navigate |
| 7 | ALARM SCREEN | Navigate |
| 8 | EACH GUN SELECT | Select injection gun |
| 9 | NUMBER OF INJECTIONS RESET | Reset counter |
| 10 | MODEL SELECT | Select injection model |
| 11 | VACUUM PUMP ON/OFF | Toggle |
| 12 | BARCODE USE/NOT USE | Toggle |
| 13 | MANUAL/AUTO | Mode toggle |
| 14 | GUN VACUUM | Start gun vacuum |
| 15 | UNIT VACUUM | Start unit vacuum |
| 16 | VACUUM CHECK | Start vacuum check |
| 17 | REFRIGER INJECTION | Start refrigerant injection |
| 18 | START | |
| 19 | STOP | |

---

## 2. Parameter Setting Screen

> All items are read from the PLC and recorded to the PLC upon user input.

| # | Parameter | Data Type | Unit | Display Example |
|---|---|---|---|---|
| 1 | Gun Vacuum Time | 16-bit | sec | 12.3 |
| 2 | Unit Vacuum Time | 16-bit | sec | 12.3 |
| 3 | Vacuum Check Time | 16-bit | sec | 12.3 |
| 4 | Refrigerant Gas Exhaust Time | 16-bit | sec | 12.3 |
| 5 | Refrigerant Gas High-Speed Injection Stop Section Setting | 16-bit | g | 1234 |
| 6 | Refrigerant Used Bombe Alarm Setting | 32-bit | Kg | 123456.7 |
| 7 | Refrigerant Gas Used Amount | 32-bit | Kg | 123456.7 |
| 8 | Refrigerant Gas Pressure High Limit | 16-bit | kgf/㎠ | -12.3 |
| 9 | Refrigerant Gas Pressure Low Limit | 16-bit | kgf/㎠ | -12.3 |
| 10 | Unit Vacuum Setting Value | 32-bit | Torr | -123.456 |
| 11 | Vacuum Check Setting Value | 32-bit | Torr | -123.456 |
| 12 | Injection Tolerance | 16-bit | ±g | 12.3 |

---

## 3. User Setting Screen — Per Injection Gun

> All items are read from the PLC and recorded to the PLC upon user input.

| # | Setting | Data Type |
|---|---|---|
| 1 | Injection Amount Model Number | 16-bit |
| 2 | Injection Amount Volume | 32-bit |
| 3 | Value that Corrects the Actual Measurement | 16-bit |
| 4 | HMI Display Calibration Value | 16-bit |
| 5 | Batch Correction Amount by Refrigerant Gas | 16-bit |

---

## 4. Safety PLC Reset

| Type | Method |
|---|---|
| Hard Reset | Physical RESET push button |
| Soft Reset | HMI any RESET button |

---

## 5. Vacuum Pump Operation

- Vacuum Pump Button ON for each line (momentary action).
- Individual vacuum pump control per injection line.

---

## 6. Screen Flow (Conceptual)

```
POWER ON
    │
    ▼
[OPERATION SCREEN] ←──── Main screen
    │
    ├── [USER SETTING SCREEN]    ← Per-gun settings
    ├── [PARAMETER SETTING SCREEN] ← System parameters
    └── [ALARM SCREEN]           ← Alarm display & reset
```
