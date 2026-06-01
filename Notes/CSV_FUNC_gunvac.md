# REFRIGER CHARGING MACHINE — Function Spec: gunvac.csv

> **Module**: `gunvac.csv`  
> **Execution**: Step 진입 시 (M12=L0, M22=L1)  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

건 진공 (Gun Vacuum) 공정 수행. 선택된 Gun 라인의 진공 배관을 감압하여 다음 공정(Unit Vacuum)을 준비.
LINE VACUUM SOL을 ON 하여 해당 Gun의 진공 라인을 진공 펌프에 연결.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| M12 | Step: GUN VAC (Line 0) |
| M22 | Step: GUN VAC (Line 1) |
| L51 | Safety OK (Line 0) |
| L61 | Safety OK (Line 1) |
| D2 | Gun Vacuum Time Setting (Line 0, 0.1 sec) |
| D32 | Gun Vacuum Time Setting (Line 1, 0.1 sec) |
| D22 | Unit Vacuum Setting Value (32-bit Torr, Line 0) |
| D50 | Unit Vacuum Setting Value (32-bit Torr, Line 1) |
| D160~D161 | Current Vacuum EU (32-bit Torr, Line 0) |
| D172~D173 | Current Vacuum EU (32-bit Torr, Line 1) |
| M304 | Gun Coupler Sensor L0 G0 (→ input.csv) |
| M305 | Gun Coupler Sensor L0 G1 |
| M314 | Gun Coupler Sensor L1 G0 |
| M315 | Gun Coupler Sensor L1 G1 |
| L72 | Active Gun A |
| L73 | Active Gun B |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| M31 | LINE VACUUM SOL ON (Line 0) → output.csv → Y11 |
| M41 | LINE VACUUM SOL ON (Line 1) → output.csv → Y21 |
| T0 | Gun Vacuum Timer (100ms base) |
| L10 | GunVac Done (Line 0) |
| L20 | GunVac Done (Line 1) |
| L11 | GunVac NG (Line 0) |
| L21 | GunVac NG (Line 1) |
| L42 | GunVac Timeout Alarm (Latch) |
| M4C | Buzzer (NG 시) |

---

## 4. Sequence Logic (Line 0 기준, Line 1은 +10 offset)

```
M12 (Step Entry) ─── Rising Edge
    │
    ├── Safety OK? (L51=1)
    │   ├── YES → SET M31 (LINE VAC SOL ON), T0 RST, T0 Start
    │   └── NO  → Abort, SET M10 (IDLE), Alarm
    │
    ├── Gun Coupler OK? (M304=CLOSE or M305=CLOSE)
    │   ├── YES → Continue
    │   └── NO  → Abort, Alarm, 모든 Sol OFF
    │
    ▼
[GUN VAC 진행 중]
    │
    ├── STOP (M414) 발생? → 즉시 종료, RST M31, SET M10
    ├── EMG (M303) 발생? → 즉시 종료, SET L40
    ├── Coupler OFF 감지? → 즉시 Alarm + 모든 Sol OFF
    │
    ├── 정상 완료 조건:
    │   T0 ≥ D2 AND D160 ≤ D22
    │   → RST M31, SET L10 (Done), RST M12
    │
    └── 타임아웃 조건:
        T0 ≥ D2 + 100 (D2+10초)
        → RST M31, SET L11 (NG), SET L42 (Timeout Alarm), SET M4C (Buzzer)
```

---

## 5. Step Transition

| From | To | Condition |
|:----:|:--:|:---------:|
| PRECHECK (M11) | GUN VAC (M12) | gmes에서 PRECHECK OK → SET M12 |
| GUN VAC (M12) | UNIT VAC (M13) | L10 Done → gmes에서 SET M13 |
| GUN VAC (M12) | IDLE (M10) | L11 NG → gmes에서 Alarm + IDLE |
| GUN VAC (M12) | IDLE (M10) | STOP 감지 → gmes에서 RST ALL |

---

## 6. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| Vacuum Timeout | T0 ≥ D2+10s | SET L11, SET L42 Alarm, Buzzer |
| Safety Lost | L51/L61 OFF during step | Abort → IDLE, SET L41 |
| Coupler Disconnect | M304 OFF during step | 즉시 Alarm + All Sol OFF |
| EMG Stop | M303 OFF | 즉시 All Stop, L40 Latch |

---

## 7. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Step bit / Input read |
| `AND` | Safety + Coupler 조건 확인 |
| `OUT` | Solenoid Control (M31) |
| `MOV` | Timer Preset (D2 → T0) |
| `DMOV` | Vacuum Compare (32-bit) |
| `LDD<=` | Vacuum ≤ Setting (Done 조건) |
| `SET` | Done/NG Flag |
| `RST` | Step Bit 해제 |
| `TMR` | Timer Start |
