# REFRIGER CHARGING MACHINE — Function Spec: unitvac.csv

> **Module**: `unitvac.csv`  
> **Execution**: Step 진입 시 (M13=L0, M23=L1)  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

유닛 진공 (Unit Vacuum) 공정 수행. Gun 진공에 더하여 LINE STEM SOL을 추가로 ON 하여
해당 Line의 전체 유닛(Unit) 배관까지 감압. 건 진공보다 더 넓은 범위의 진공을 형성.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| M13 | Step: UNIT VAC (Line 0) |
| M23 | Step: UNIT VAC (Line 1) |
| L51 | Safety OK (Line 0) |
| L61 | Safety OK (Line 1) |
| D4 | Unit Vacuum Time Setting (Line 0, 0.1 sec) |
| D34 | Unit Vacuum Time Setting (Line 1, 0.1 sec) |
| D22 | Unit Vacuum Setting Value (32-bit Torr, Line 0) |
| D50 | Unit Vacuum Setting Value (32-bit Torr, Line 1) |
| D160~D161 | Current Vacuum EU (32-bit Torr, Line 0) |
| D172~D173 | Current Vacuum EU (32-bit Torr, Line 1) |
| M304~M305 | Gun Coupler Sensors L0 |
| M314~M315 | Gun Coupler Sensors L1 |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| M31 | LINE VACUUM SOL ON (Line 0) |
| M32 | LINE STEM SOL ON (Line 0) |
| M41 | LINE VACUUM SOL ON (Line 1) |
| M42 | LINE STEM SOL ON (Line 1) |
| T1 | Unit Vacuum Timer (100ms base) |
| L12 | UnitVac Done (Line 0) |
| L22 | UnitVac Done (Line 1) |
| L13 | UnitVac Fail (Line 0) |
| L23 | UnitVac Fail (Line 1) |
| L43 | UnitVac Timeout Alarm |

---

## 4. Sequence Logic (Line 0 기준)

```
M13 (Step Entry) ─── Rising Edge
    │
    ├── Safety OK? (L51=1)
    │   └── YES → SET M31 + M32 (VAC + STEM SOL), T1 Start
    │
    └── Gun Coupler OK?
        └── NO → 즉시 Abort
    │
    ▼
[UNIT VAC 진행 중 — VAC SOL + STEM SOL 동시 ON]
    │
    ├── 정상 완료 조건:
    │   T1 ≥ D4 AND D160 ≤ D22 (진공도 도달)
    │   → RST M31, RST M32, SET L12 (Done), RST M13
    │
    └── 타임아웃:
        T1 ≥ D4 + 100 (D4+10초)
        → RST M31, RST M32, SET L13 (Fail), SET L43 (Alarm)
    │
    ├── STOP 발생 → RST M31, RST M32, SET M10 (IDLE)
    └── EMG 발생 → 즉시 All Sol OFF, L40 SET
```

**Key difference from gunvac**: LINE STEM SOL(M32/M42)도 함께 ON.
Unit Vacuum은 Gun 뿐만 아니라 Stem(샤프트/배관)까지 감압하므로 추가 SOL 필요.

---

## 5. Step Transition

| From | To | Condition |
|:----:|:--:|:---------:|
| GUN VAC (M12) | UNIT VAC (M13) | L10 Done → gmes SET M13 |
| UNIT VAC (M13) | VAC CHECK (M14) | L12 Done → gmes SET M14 |
| UNIT VAC (M13) | IDLE (M10) | Fail or STOP |

---

## 6. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| UnitVac Timeout | T1 ≥ D4+10s | SET L13, SET L43 Alarm |
| Safety Lost | L51/L61 OFF | 즉시 Abort |
| Coupler OFF | Sensor OFF | 즉시 All Sol OFF + Alarm |

---

## 7. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Step entry |
| `AND` | Safety + Coupler check |
| `OUT` | M31, M32 (VAC + STEM SOL) |
| `MOV` | Timer preset |
| `DMOV` | Vacuum compare |
| `LDD<=` | Vacuum ≤ Setting |
| `SET` | Done/Fail |
| `RST` | Step/Solenoid off |
| `TMR` | T1 Timer |
