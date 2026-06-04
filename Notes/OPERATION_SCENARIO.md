# REFRIGER CHARGING MACHINE — Operation Scenario

> 작성일: 2026-06-05
> Re-planned from scratch (Session 1). This document supersedes all prior versions.
> **PLC**: Mitsubishi QCPU (Q mode) Q03UDV | **Tool**: GX Works2 IL

---

## 1. Equipment

| Line | Gun | Function | Steps |
|:----:|:---:|----------|:-----:|
| L1 | A | Refrig injection | M10–M18 (9) |
| L2 | B | Refrig injection | M30–M38 (9) |
| L3 | — | Oil injection (shared) | M50–M53 (4) |

- Only one line operates at a time (serial operation).
- Gun select determines active line: Gun A → L1, Gun B → L2.
- L3 is a shared oil line used by both L1 and L2.
- H+L solenoid structure only (FAST + BASE). No Gun Type branching.
- If a customer uses 1 solenoid, they leave the second output unwired.

---

## 2. Power-On Default State

| Setting | Default |
|---------|:------:|
| Mode | MANUAL |
| Active Gun | A |
| Barcode | Used |

---

## 3. Step Machine

| # | L1 (Gun A) | L2 (Gun B) | L3 (Oil) | Step Name |
|:-:|:--:|:--:|:--:|------|
| 1 | M10 | M30 | M50 | IDLE |
| 2 | M11 | M31 | — | PRECHECK |
| 3 | M12 | M32 | — | GUN VAC |
| 4 | M13 | M33 | — | UNIT VAC |
| 5 | M14 | M34 | — | VAC CHECK |
| 6 | M15 | M35 | M51 | REFRIG FAST INJ / OIL FAST INJ |
| 7 | M16 | M36 | M52 | REFRIG BASE INJ / OIL BASE INJ |
| 8 | M17 | M37 | M53 | EXHAUST / OIL COMPLETE |
| 9 | M18 | M38 | — | COMPLETE |

- Offset: L1→L2 = +20, L1→L3 = +40.
- Step self-holding: `LD set_cond OR self ANI release_cond OUT self`.
- Warmup delay (0.5s, T0) before EVERY step entry (auto and manual).
- Rung order: release step BEFORE released step (no 1-scan overlap).

### Solenoid activation by step:

| Step | VAC SOL | STEM SOL | FAST SOL | BASE SOL | EXHAUST SOL |
|------|:-------:|:--------:|:--------:|:--------:|:-----------:|
| GUN VAC (M12/M32) | ON | | | | |
| UNIT VAC (M13/M33) | ON | ON | | | |
| VAC CHECK (M14/M34) | OFF | OFF | | | |
| REFRIG FAST (M15/M35) | | | ON | ON | |
| REFRIG BASE (M16/M36) | | | OFF | ON | |
| OIL FAST (M51) | | | ON | ON | |
| OIL BASE (M52) | | | OFF | ON | |
| EXHAUST (M17/M37) | | | | | ON |

---

## 4. Auto Mode Sequence

```
IDLE (M10)
  ↓ Gun select + START + 0.5s warmup (T0)
PRECHECK (M11)
  ├── Interlock OK? Model# ≠ 0? Target > 0?
  ↓ 0.5s warmup
GUN VAC (M12)
  ├── VAC SOL ON
  ├── Timer T1 ≥ D_gun_vac_time
  ↓ Done → 0.5s warmup
UNIT VAC (M13)
  ├── VAC SOL ON + STEM SOL ON
  ├── Timer T2 ≥ D_unit_vac_time
  │   AND Vacuum ≤ D_unit_vac_setting
  ↓ Done → 0.5s warmup
VAC CHECK (M14)
  ├── SOL OFF, Δ vacuum over time T3
  │   Δ ≤ D_vac_check_setting → OK
  │   Δ > limit → Vac Leak NG, alarm latch
  ↓ OK → 0.5s warmup
OIL FAST (M51, L3)
  ├── OIL FAST SOL ON + OIL BASE SOL ON
  ├── Flow meter HSC count
  ├── Pulse ≥ D_oil_fast_stop → FAST OFF
  ↓ → OIL BASE (M52)
OIL BASE (M52, L3)
  ├── OIL BASE SOL ON
  ├── Pulse ≥ D_oil_target ± D_oil_tolerance → OK
  │   ├── Over: alarm latch
  │   └── Under: alarm latch
  ├── Timeout → alarm latch
  ↓ → OIL COMPLETE (M53)
  ↓ → 0.5s warmup
REFRIG FAST (M15)
  ├── REFRIG FAST SOL ON + REFRIG BASE SOL ON
  ├── Flow meter HSC count
  ├── Pulse ≥ D_refrig_fast_stop → FAST OFF
  ↓ → REFRIG BASE (M16)
REFRIG BASE (M16)
  ├── REFRIG BASE SOL ON
  ├── Pulse ≥ D_refrig_target ± D_refrig_tolerance → OK
  │   ├── Over: alarm latch
  │   └── Under: alarm latch
  ├── Timeout → alarm latch
  ↓ → 0.5s warmup
EXHAUST (M17)
  ├── EXHAUST SOL ON
  ├── Timer T4 ≥ D_exhaust_time
  ↓ → 0.5s warmup
COMPLETE (M18)
  ├── SPC update (usage, count, cycle data)
  ├── Cycle count++
  ↓ → IDLE (M10)
  ├── Barcode Used: Model# = 0
  └── Barcode Not Used: Model# maintained
```

---

## 5. Manual Mode Sequence

- Function button press → READY flag SET, lamp ON.
- Same button press again → READY flag RST, lamp OFF (toggle cancel).
- START + READY → 0.5s warmup → **single step only**. No chain continuation.

| Button | Executes |
|--------|----------|
| GUN VAC | M12 |
| UNIT VAC | M13 |
| VAC CHECK | M14 |
| OIL INJ | M51 → M52 → M53 (L3 chain) |
| REFRIG INJ | M15 → M16 |

---

## 6. Mode Control

```
// Power-on default
SM402 → SET M_MANUAL, RST M_AUTO

// AUTO/MANUAL toggle (IDLE only, M10)
LD  AUTO_MANUAL_BTN_edge AND M_MANUAL AND M10 → SET M_AUTO, RST M_MANUAL
LD  AUTO_MANUAL_BTN_edge AND M_AUTO    AND M10 → SET M_MANUAL, RST M_AUTO
```

- SET/RST exclusive pair ensures atomic transition (no 1-scan overlap).
- Toggle locked during M11–M18 active.

---

## 7. Gun Select

```
// Power-on default
SM402 → SET M_GUN_A, RST M_GUN_B

// Gun A button (IDLE only)
LD  GUN_A_BTN_edge AND M10 → SET M_GUN_A, RST M_GUN_B

// Gun B button (IDLE only)
LD  GUN_B_BTN_edge AND M10 → SET M_GUN_B, RST M_GUN_A
```

- SET/RST exclusive pair. Locked during M11–M20 active.

---

## 8. STOP / EMG

| Action | Behavior |
|--------|----------|
| STOP (HMI button) | Halt current step immediately → exhaust → IDLE |
| EMG (N/C OPEN) | All outputs OFF, all steps RST, alarm latch. Manual reset only (IEC 60204-1). |
| Door Left/Right OPEN | EMG-level alarm latch. Stop both lines. |

---

## 9. HMI Buttons

All buttons momentary — rising edge, 1 scan ON. Used directly in logic; no PLS wrapper.

### Operation Screen

| Button | Action |
|--------|--------|
| GUN A | Gun select (IDLE only) |
| GUN B | Gun select (IDLE only) |
| AUTO/MANUAL | Mode toggle (IDLE only) |
| GUN VAC | Manual function select |
| UNIT VAC | Manual function select |
| VAC CHECK | Manual function select |
| OIL INJ | Manual function select |
| REFRIG INJ | Manual function select |
| START | Initiate operation |
| STOP | Halt operation immediately |
| ALARM RESET | Clear alarm latches + unmute buzzer |
| BUZZER STOP | Mute buzzer only |
| VACUUM PUMP ON/OFF | Toggle vacuum pump |
| USER SETTING | Navigate to USER SETTING screen |
| PARAM SETTING | Navigate to PARAMETER SETTING screen |
| ALARM | Navigate to ALARM screen |

---

## 10. HMI Lamp Backlight

| Lamp | ON Condition |
|------|-------------|
| GUN A | M_GUN_A selected |
| GUN B | M_GUN_B selected |
| AUTO | M_AUTO active |
| MANUAL | M_MANUAL active |
| GUN VAC | READY OR M12 (GUN VAC step) |
| UNIT VAC | READY OR M13 (UNIT VAC step) |
| VAC CHECK | READY OR M14 (VAC CHECK step) |
| OIL INJ | READY OR M51/M52 (OIL step) |
| REFRIG INJ | READY OR M15/M16 (REFRIG step) |
| START | Any M11–M18 step active |
| GREEN | Running + no alarm |
| RED | Any alarm latch active |
| YELLOW | IDLE + interlock not OK |

---

## 11. Alarm System

### Structure

- **Self-holding OUT**: `LD trigger OR self ANI alarm_reset ANI init OUT self`.
- **Edge detect**: Each alarm has a companion prev-state bit for buzzer re-trigger.
- **All alarms stop the process** (step RST → exhaust → IDLE).

### Shared Alarms (system-wide)

| Alarm | Trigger |
|-------|---------|
| EMG Stop | EMG N/C OPEN |
| Door Open | Door Left OPEN OR Door Right OPEN |
| Bombe Low | Total usage ≥ Bombe alarm setting |
| Pump Trip | Vacuum pump fault |

### Per-Line Alarms (L1 / L2)

| Alarm | Trigger |
|-------|---------|
| Gun Vac Timeout | T ≥ preset + grace time |
| Unit Vac Timeout | T ≥ preset + grace time |
| Vac Leak | Δ vacuum > limit during VAC CHECK |
| Inj Timeout | No flow meter pulse change over timeout |
| Inj Over | Actual > Target + Tolerance |
| Inj Under | Actual < Target - Tolerance |
| Pressure High | Pressure > upper limit |
| Pressure Low | Pressure < lower limit |
| Temp Out of Range | Temperature < min or > max |
| Model Not Selected | Model# = 0 at PRECHECK |
| Target Amount Not Set | Target = 0 at PRECHECK |

### L3 Oil Alarms

| Alarm | Trigger |
|-------|---------|
| Oil Timeout | No flow meter pulse change |
| Oil Over | Actual > Target + Tolerance |
| Oil Under | Actual < Target - Tolerance |

### Buzzer Control

```
// Buzzer output
LD  any_alarm_latch AND NOT buzzer_mute → OUT buzzer

// BUZZER STOP button → mute only (latches untouched)
LD  BUZZER_STOP_btn → SET buzzer_mute

// New alarm rising edge → unmute (buzzer re-triggers)
LD  alarm_N AND NOT alarm_N_prev → RST buzzer_mute

// ALARM RESET → unmute + clear all latches (if source cleared)
LD  ALARM_RESET_btn → RST buzzer_mute
```

### ANI Chain in Step Rungs

All alarm latches (L1 + L2 + L3 + shared) are included in step rung ANI chains. Inactive line alarms are OFF → no false blocking.

---

## 12. Interlock

### Per-Line OK (AND chain)

| Condition | Source |
|-----------|--------|
| Gun coupler | DI sensor = ON |
| Pressure in range | Analog EU vs D parameter limits |
| Temperature in range | Analog EU vs D parameter limits |
| Vacuum valid | Analog EU valid |
| Model# ≠ 0 | D register |
| Target amount > 0 | D register |

All OK → `M_INTLK_OK` = ON (per line).

### EMG-Level (OR → stops both lines)

| Condition | Effect |
|-----------|--------|
| Door Left OFF | EMG alarm latch |
| Door Right OFF | EMG alarm latch |
| Vacuum pump trip | EMG alarm latch |

---

## 13. Injection Quantity

### Model Table (25 models per gun)

| Per Row | Width |
|---------|:-----:|
| Model# | 16-bit |
| Refrig Base Target | 32-bit (g) |
| Refrig User Correction | 16-bit (±g) |
| Refrig Display Correction | 16-bit (±g) |
| Oil Base Target | 32-bit (g) |
| Oil User Correction | 16-bit (±g) |
| Oil Display Correction | 16-bit (±g) |

- Gun A and Gun B each have independent 25-model tables.
- All D registers: even address + next odd reserved for 32-bit upgrade.

### Barcode Used (power-on default)

1. PC writes target amount to PLC via gmes.
2. PLC scans lookup table → find matching Base Target.
3. Match found → model# assigned, corrections applied.
4. No match → Model Not Selected alarm, stop.
5. Real injection target = Base Target + User Correction.
6. HMI display target = Base Target + User Correction + Display Correction.
7. On IDLE entry (after COMPLETE / STOP / NG): Model# reset to 0.

### Barcode Not Used

1. Operator selects model# on HMI.
2. Lookup table → target + corrections applied.
3. On IDLE entry: Model# maintained (persists across cycles).

---

## 14. Flow Meter (HSC)

- Counts during injection steps only.
- L1/L2: counts during M15–M16 (REFRIG FAST / BASE INJ).
- L3: counts during M51–M52 (OIL FAST / BASE INJ).
- Oil count vs refrig count separated by which step is active.

---

## 15. Solenoids & Motor

| L1 | L2 | L3 | Signal | Type |
|:--:|:--:|:--:|--------|:----:|
| ✓ | ✓ | | VAC SOL | Solenoid |
| ✓ | ✓ | | STEM SOL | Solenoid |
| ✓ | ✓ | | REFRIG FAST SOL | Solenoid |
| ✓ | ✓ | | REFRIG BASE SOL | Solenoid |
| | | ✓ | OIL FAST SOL | Solenoid |
| | | ✓ | OIL BASE SOL | Solenoid |
| ✓ | ✓ | | EXHAUST SOL | Solenoid |
| ✓ | ✓ | | VACUUM PUMP RUN | Motor |

---

## 16. Digital Inputs (DI)

| Qty | Signal | Type | Scope |
|:---:|--------|:----:|:-----:|
| 1 | EMG | N/C | Shared |
| 1 | Door Left | N/C | Shared |
| 1 | Door Right | N/C | Shared |
| 1 | Gun Coupler | — | L1 |
| 1 | Gun Coupler | — | L2 |

---

## 17. Analog Inputs

| L1 | L2 | L3 | Signal | Width |
|:--:|:--:|:--:|--------|:-----:|
| ✓ | ✓ | | Pressure | 16-bit |
| ✓ | ✓ | ✓ | Temperature | 16-bit |
| ✓ | ✓ | | Vacuum | 32-bit |

### Analog EU Destination Registers

| Signal | L1 | L2 | L3 |
|--------|:--:|:--:|:--:|
| Pressure | D100 | D110 | — |
| Temperature | D102 | D112 | D120 |
| Vacuum | D104–D105 | D114–D115 | — |

- User MOVs final scaled values into these registers.
- All other modules read from these addresses.

---

## 18. SPC (merged into gmes.csv)

- spc.csv removed; logic merged into gmes.csv.
- Vacuum SPC data logged during GUN VAC / UNIT VAC / VAC CHECK in auto mode.
- 0.08s interval (T18 10ms timer × K8).
- Cycle counters, cumulative usage, per-cycle injection amounts.

---

## 19. File Structure (11 CSVs)

| Module | Content |
|--------|---------|
| MAIN.csv | Step machine, mode control, gun select, ready flags, interlock, lamps |
| alarm.csv | Alarm latches, buzzer, lamp colors |
| gunvac.csv | Gun vacuum (M12/M32): VAC SOL, timer, OK/NG |
| unitvac.csv | Unit vacuum (M13/M33): VAC+STEM SOL, timer, OK/NG |
| vacchec.csv | Vacuum check (M14/M34): delta calc, OK/NG |
| refinj.csv | Refrig injection (M15–M18 / M35–M38): FAST→BASE, HSC, tolerance |
| oilinj.csv | Oil injection (M51–M53): FAST→BASE, HSC, tolerance |
| gmes.csv | PC communication + SPC logging |
| idata.csv | DI → M mirror, M → DO mirror, system flags |
| ad.csv | Analog raw → EU scaling |
| setting.csv | Configuration (line count, oil mode, HMI parameters) |

---

## 20. Key Design Rules

| Rule | Detail |
|------|--------|
| State bits | Self-holding OUT: `LD set_cond OR self ANI release_cond OUT self` |
| Exclusive pairs | SET/RST allowed (gun select, mode toggle, alarm mute, ready toggle) |
| HMI buttons | Momentary 1-scan. Used directly in logic — no PLS wrapper. |
| X/Y isolation | idata.csv only. All logic code references M/D registers. |
| D registers | Even address + next odd reserved for 32-bit upgrade (all registers). |
| Solenoid | H+L only (FAST + BASE). No type branching. Single-sol users leave BASE unwired. |
| Edge detection | Prev-state compare: `LD signal AND NOT signal_prev`. No PLS. |
| Warmup | 0.5s delay before EVERY step entry (auto chain and manual single-step). |
| STOP | Available in all modes. Immediate halt → exhaust → IDLE. |
| Lamp progress | Auto mode: function lamp driven by step bit (no READY). Operator sees progress. |
| Naming | Device names as clear as possible within GX Works2 comment character limits. |

---

## 21. Pending / Next Session

- Complete device map (M, D, T, X, Y address allocation).
- Detailed parameter list for USER SETTING and PARAMETER SETTING screens.
- PC communication protocol (gmes data layout).
- Rung order specification.
- Detailed module-by-module IL logic design.
