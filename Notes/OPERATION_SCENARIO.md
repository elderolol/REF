# REFRIGER CHARGING MACHINE — Operation Scenario

> 작성일: 2026-06-05 | 최종구현일: 2026-06-06 | XG5000 갱신: 2026-06-08
> Re-planned from scratch (Session 1). This document is the **design reference**.
> 실제 구현은 `src/*.il` 참조. Device map: `Notes/XG5000_Device_Map.md`
> **PLC**: LS Electric XGK-CPUE | **Tool**: XG5000 IL | **HMI**: LS IXP2-1200

---

## 1. Equipment

| Line | Gun | Function | Steps |
|:----:|:---:|----------|:-----:|
| L1 | A | Refrig injection | M0000A–M00012 (9) |
| L2 | B | Refrig injection | M0001E–M00026 (9) |
| L3 | — | Oil injection (per-gun) | M00032–M00035 (4) |

- Only one line operates at a time (serial operation).
- Gun select determines active line: Gun A → L1, Gun B → L2.
- L3 is per-gun oil (M00041/M00042 for Gun A, M0004B/M0004C for Gun B).
- H+L solenoid structure only (FAST + BASE). No Gun Type branching.
- If a customer uses 1 solenoid, they leave the second output unwired.

### Solenoid Assignment

| Signal | GUN A (L1) | GUN B (L2) |
|--------|:----------:|:----------:|
| VAC SOL | M0003C (P0032) | M00046 (P0048) |
| STEM SOL | M0003D (P0033) | M00047 (P0049) |
| REFRIG FAST SOL | M0003E (P0034) | M00048 (P0050) |
| REFRIG BASE SOL | M0003F (P0035) | M00049 (P0051) |
| EXHAUST SOL | M00040 (P0036) | M0004A (P0052) |
| OIL FAST SOL | M00041 (P0037) | M0004B (P0040) |
| OIL BASE SOL | M00042 (P0038) | M0004C (P0041) |
| LINE VAC SOL | — | — | (N/O, M00044 shared → P0039) |
| HYDRO PUMP | — | — | M00060 toggle/P0069 — auto during oil steps |
| OIL LINE SOL | — | — | M00061/P0070 — follows M00060 |
| VACUUM PUMP | — | — | M00043 toggle (M0019C) |
| BUZZER | — | — | M00045 |
| LAMPS (G/R/Y) | — | — | M0004D/M0004E/M0004F |

---

## 2. Power-On Default State

| Setting | Value | Flag |
|---------|:-----:|------|
| Mode | MANUAL | M000C8=ON, M000C9=OFF |
| Active Gun | A | M000D2=ON, M000D3=OFF |
| Barcode | Used | M00208=ON |
| Oil+Refrig | Enabled | M00209=ON |
| Interlock | Used | M0020A=ON |
| Steps | IDLE | M0000A/M0001E/M00032=ON |

F00002 (power-on 1-scan) sets all defaults.

---

## 3. Step Machine

| # | L1 (Gun A) | L2 (Gun B) | L3 (Oil) | Step Name |
|:-:|:--:|:--:|:--:|------|
| 1 | M0000A | M0001E | M00032 | IDLE |
| 2 | M0000B | M0001F | — | PRECHECK |
| 3 | M0000C | M00020 | — | GUN VAC |
| 4 | M0000D | M00021 | — | UNIT VAC |
| 5 | M0000E | M00022 | — | VAC CHECK |
| 6 | M0000F | M00023 | M00033 | REFRIG FAST INJ / OIL FAST INJ |
| 7 | M00010 | M00024 | M00034 | REFRIG BASE INJ / OIL BASE INJ |
| 8 | M00011 | M00025 | M00035 | EXHAUST / OIL COMPLETE |
| 9 | M00012 | M00026 | — | COMPLETE |

- Offset: L1→L2 = +20 (hex +0x14), L1→L3 = +40 (hex +0x28).
- Step self-holding: `LOAD set_cond OR self AND NOT release_cond OUT self`.
- Warmup delay (0.5s, T0000) before EVERY step entry (auto and manual).
- Rung order: COMPLETE→EXHAUST→...→IDLE (release step BEFORE released step).

### Step OK/Fail Flags

| L1 | L2 | L3 | Meaning |
|:--:|:--:|:--:|---------|
| M00064 | M00074 | — | PRECHECK OK |
| M00065 | M00075 | — | GUN VAC OK |
| M00066 | M00076 | — | UNIT VAC OK |
| M00067 | M00077 | — | VAC CHECK OK |
| M00069 | M00079 | — | REFRIG BASE OK |
| M0006A | M0007A | — | EXHAUST OK |
| M0006B | M0007B | — | COMPLETE reached |
| — | — | M00091 | OIL FAST OK |
| — | — | M00092 | OIL BASE OK |
| — | — | M00093 | OIL COMPLETE reached |
| M0006C | M0007C | — | GUN VAC NG |
| M0006D | M0007D | — | UNIT VAC NG |
| M0006F | M0007F | — | VAC CHECK NG |

### Solenoid Activation by Step

| Step | VAC SOL | STEM SOL | LINE VAC SOL | FAST SOL | BASE SOL | EXHAUST SOL |
|------|:-------:|:--------:|:------------:|:--------:|:--------:|:-----------:|
| GUN VAC (M0000C/M00020) | ON | | | | | |
| UNIT VAC (M0000D/M00021) | ON | ON | | | | |
| VAC CHECK (M0000E/M00022) | ON | ON | ON | | | |
| REFRIG FAST (M0000F/M00023) | | | | ON | ON | |
| REFRIG BASE (M00010/M00024) | | | | OFF | ON | |
| OIL FAST (M00033) | | | | ON | ON | |
| OIL BASE (M00034) | | | | OFF | ON | |
| EXHAUST (M00011/M00025) | | | | | | ON |

Note: VAC CHECK keeps VAC SOL, STEM SOL, and LINE VAC SOL all ON (active vacuum hold test).

---

## 4. Auto Mode Sequence

```
IDLE (M0000A)
  ↓ START (M00198) + Gun select + T0000 warmup
PRECHECK (M0000B)
  ├── M00050 (interlock AND chain: M00051 & M00052 & M00053 & M00054 & M00055)
  ├── D00000 > 0 (model selected)
  ├── D00012 >= 1 (target set)
  ↓ OK (M00064) → T0000 warmup
GUN VAC (M0000C)
  ├── VAC SOL ON (M0003C)
  ├── Timer T0001 ≥ D00002
  ↓ OK (M00065) → T0000 warmup
UNIT VAC (M0000D)
  ├── VAC SOL ON (M0003C) + STEM SOL ON (M0003D)
  ├── Timer T0002 ≥ D00004 AND Vacuum (D00030) ≤ D00022
  ↓ OK (M00066) → T0000 warmup
VAC CHECK (M0000E)
  ├── VAC SOL ON (M0003C) + STEM SOL ON (M0003D) + LINE VAC SOL ON (M00044)
  ├── Δ vacuum over time T0003 ≤ D00024 → OK
  │   Δ > D00024 → NG (M0006F), alarm latch
  ↓ OK (M00067) → T0000 warmup
  ├── IF M00209=ON AND D00018≥1 (Oil target > 0):
  │     OIL FAST (M00033) → OIL BASE (M00034) → OIL COMPLETE (M00035)
  │     ├── Flow meter HSC count
  │     ├── Pulse ≥ D00016-D00017 → FAST OK (M00091)
  │     ├── Pulse ≥ D00018-D00019 ± D00020 → BASE OK/NG (M00092/M0015F)
  │     ├── Timeout 30s on T0013/T0014 → alarm
  │     └── OIL COMPLETE → T0000 warmup
  │   IF M00209=OFF OR D00018<1: skip oil, go directly to Refrig
  └── T0000 warmup
REFRIG FAST (M0000F)
  ├── REFRIG FAST SOL ON (M0003E) + REFRIG BASE SOL ON (M0003F)
  ├── Flow meter HSC count
  ├── Pulse ≥ D00010-D00011 → FAST OK
  ↓ → REFRIG BASE (M00010)
REFRIG BASE (M00010)
  ├── REFRIG BASE SOL ON (M0003F), FAST SOL OFF
  ├── Pulse ≥ D00012-D00013 ± D00014 → OK/NG (M00069/M0013A)
  ├── Timeout 30s on T0004 → alarm
  ↓ OK → T0000 warmup
EXHAUST (M00011)
  ├── EXHAUST SOL ON (M00040)
  ├── Timer T0006 ≥ D00008
  ↓ OK (M0006A) → T0000 warmup
COMPLETE (M00012)
  ├── SPC update + cycle count++
  ├── D01000 = 1 (COMPLETE code)
  ↓ → IDLE (M0000A)
  └── Model# D00000 = 0 (always reset on IDLE)
```

### L2 Equivalent
Same sequence with offsets: M0001E-M00026, M00046-M0004A (solenoids), D00032-D00063 (parameters), M0005A-M0005F (interlock), M00074-M0007F (flags).

---

## 5. Manual Mode Sequence

- Function button press → READY flag SET, lamp ON.
- Same button press again → READY flag RST, lamp OFF (toggle cancel).
- START + READY → 0.5s warmup (T0000) → **single step only**. No chain continuation.

| Button | READY Bit | Executes (Gun A / Gun B) |
|--------|:---------:|---------------------------|
| GUN VAC (M00193) | M000DC | M0000C / M00020 |
| UNIT VAC (M00194) | M000DD | M0000D / M00021 |
| VAC CHECK (M00195) | M000DE | M0000E / M00022 |
| REFRIG INJ (M00196) | M000DF | M0000F→M00010 / M00023→M00024 |
| OIL INJ (M00197) | M000E0 | M00033→M00034→M00035 (L3 chain) |

- M000DF (REFRIG INJ) and M000E0 (OIL INJ) blocked when M00208=ON (barcode used).
- OIL INJ M000E0 also blocked when M00209=OFF (oil disabled).
- Manual mode uses T0000 warmup via PLS M001C5: `M001C5 → TON T0000 5 → SET target_step, RST M001C5`.

---

## 6. Mode Control

```
// Power-on default (F00002)
SET M000C8, RST M000C9    // MANUAL

// AUTO/MANUAL toggle (IDLE only, M0000A)
M00192 OUTP M00258
M00258 & M000C8 & M0000A → SET M000C9, RST M000C8    // → AUTO
M00258 & M000C9 & M0000A → SET M000C8, RST M000C9    // → MANUAL
```

- SET/RST exclusive pair ensures atomic transition (no 1-scan overlap).
- Toggle locked during M0000B–M00012 active (requires M0000A IDLE).

---

## 7. Gun Select

```
// Power-on default (F00002)
SET M000D2, RST M000D3    // GUN A

// Gun A button (BOTH lines IDLE required)
M00190 OUTP M00259
M00259 & M0000A & M0001E → SET M000D2, RST M000D3

// Gun B button (BOTH lines IDLE required)
M00191 OUTP M0025A
M0025A & M0000A & M0001E → SET M000D3, RST M000D2
```

- SET/RST exclusive pair.
- Requires M0000A AND M0001E both ON (both lines in IDLE) to change guns.

---

## 8. STOP / EMG

| Action | Behavior |
|--------|----------|
| STOP (M00199) | M001C2 (L1) or M001C3 (L2) latch → RST steps → SET EXHAUST(M00011/M00025) → IDLE. Code D01000/D01200=6 |
| NG Alarm | M0006C/M0006D/M0006F/M00136-M00138 → SET M001C2 (L1); M0007C/M0007D/M0007F/M0014A-M0014C → SET M001C3 (L2). Same flow as STOP. |
| EMG (M00302 N/C OPEN) | M001C4 self-holds → RST all steps M0000A-M00035 + all solenoids M0003C-M0004C → M0019A manual reset. D01000/D01200=6 |
| Interlock fail | step + M00050/M0005A OFF → RST step → EXHAUST |

STOP latch releases on IDLE: `LOAD M0000A → RST M001C2` / `LOAD M0001E → RST M001C3`.

---

## 8-1. Hydro Pump

| Item | Detail |
|------|--------|
| Control | M00060 (HYDRO PUMP) → P0069 |
| Oil Line Sol | M00061 → P0070, follows M00060 |
| HMI Button | M001A3 HYDRO PUMP ON/OFF (toggle) |
| Trip Input | M00304 (P0004, N/C) |
| Trip Alarm | M00130 (self-holding, resets via M0019A) |

### Operation

```
// HMI Toggle
M001A3 OUTP M0026F
M0026F & !M00060 → SET M00060, SET M00061
M0026F &  M00060 → RST M00060, RST M00061

// Auto ON during oil steps (pump not tripped)
M00033 & !M00130 → SET M00060, SET M00061
M00034 & !M00130 → SET M00060, SET M00061
```

- Two ways to activate: **HMI toggle** OR **auto during oil steps**.
- Oil charging step (M00033/M00034) is **blocked when M00130 is ON** (hydro pump tripped).
- M00130 stops both auto oil entry (AND NOT M00130 gate) and manual oil entry.
- M00060/M00061 are RST on: oil complete (M00035), oil timeout, STOP (M00199), NG alarm (M001C2/M001C3), EMG (M001C4).

---

## 9. HMI Buttons

All buttons momentary — rising edge, 1 scan ON. Used directly in logic with PLS edge detection.

### Operation Screen

| Button | Device | Action |
|--------|:------:|--------|
| GUN A | M00190 | Gun select (M0000A & M0001E IDLE required) |
| GUN B | M00191 | Gun select (M0000A & M0001E IDLE required) |
| AUTO/MANUAL | M00192 | Mode toggle (M0000A IDLE only) |
| GUN VACUUM | M00193 | Manual GUN VAC select (M000DC toggle) |
| UNIT VACUUM | M00194 | Manual UNIT VAC select (M000DD toggle) |
| VACUUM CHECK | M00195 | Manual VAC CHECK select (M000DE toggle) |
| REFRIG INJ | M00196 | Manual REFRIG INJ select (M000DF toggle) |
| OIL INJ | M00197 | Manual OIL INJ select (M000E0 toggle) |
| START | M00198 | Initiate operation |
| STOP | M00199 | Halt → EXHAUST → IDLE |
| ALARM RESET | M0019A | Clear alarm latches + unmute buzzer |
| BUZZER STOP | M0019B | Mute buzzer only (M001F4) |
| VAC PUMP ON/OFF | M0019C | Toggle vacuum pump M00043 |
| INTERLOCK EN | M0019D | Toggle M0020A (DOOR alarm gate) |
| L1 COUNT RESET | M0019E | D00240 = 0 |
| OIL+REFRIG EN | M0019F | Toggle M00209 (oil enable in auto) |
| L2 COUNT RESET | M001A0 | D00242 = 0 |
| L1 USAGE RESET | M001A1 | D00200-D00201 = 0 |
| L2 USAGE RESET | M001A2 | D00220-D00221 = 0 |
| HYDRO PUMP | M001A3 | Toggle M00060/M00061 (hydro pump + oil line sol) |

---

## 10. HMI Lamp Backlight

| Lamp | ON Condition |
|------|-------------|
| GUN A | M000D2 selected |
| GUN B | M000D3 selected |
| AUTO | M000C9 active |
| MANUAL | M000C8 active |
| GUN VAC | READY (M000DC) OR M0000C/M00020 step |
| UNIT VAC | READY (M000DD) OR M0000D/M00021 step |
| VAC CHECK | READY (M000DE) OR M0000E/M00022 step |
| REFRIG INJ | READY (M000DF) OR M0000F/M00010/M00023/M00024 step |
| OIL INJ | READY (M000E0) OR M00033/M00034 step |
| START | Any M0000B-M00012/M0001F-M00026/M00033-M00035 step active |
| GREEN (M0004D) | Running (M0000C-M00011/M00020-M00025/M00033-M00034) + no alarm |
| RED (M0004E) | Any alarm latch active |
| YELLOW (M0004F) | IDLE (M0000A/M0001E) + interlock not OK (AND NOT M00050/M0005A) |

---

## 11. Alarm System

### Structure

- **Self-holding OUT**: `LOAD trigger OR self AND NOT M0019A (alarm_reset) OUT self`.
- **Edge detect**: Each alarm has a companion prev-state bit for buzzer re-trigger.
- **All alarms stop the process** (step RST → exhaust → IDLE).

### Shared Alarms (system-wide)

| Alarm | Bit | Trigger |
|-------|:---:|---------|
| EMG Stop | M0012C | M00302 N/C OPEN |
| Door Open | M0012D | M00303 OFF, gated by M0020A (interlock enable) |
| Pump Trip | M0012F | Vacuum pump fault |
| Hydro Pump Trip | M00130 | M00304 (P0004) N/C OPEN |

### L1 Alarms

| Alarm | Bit | Trigger |
|-------|:---:|---------|
| Gun Vac Timeout | M00136 | T0001 ≥ D00002 + grace |
| Unit Vac Timeout | M00137 | T0002 ≥ D00004 + grace |
| Vac Leak | M00138 | Δ vacuum > D00024 during VAC CHECK |
| Inj Timeout | M00139 | No flow meter pulse change over 30s (T0004) |
| Inj Amount NG | M0013A | Actual ∉ [D00012-D00013 ± D00014] (over+under combined) |
| Pressure High | M0013C | D00026 > upper limit |
| Pressure Low | M0013D | D00026 <= lower limit |
| Temp Out of Range | M0013E | D00028 < -200 or D00028 > 800 |
| Model Not Selected | M0013F | D00000 = 0 at PRECHECK |
| Target Not Set | M00140 | D00012-D00013 = 0 at PRECHECK |
| Bombe Low | M00141 | L1 cumulative usage ≥ D00210-D00211 |

### L2 Alarms

| Alarm | Bit | Trigger |
|-------|:---:|---------|
| Gun Vac Timeout | M0014A | T0007 ≥ D00034 + grace |
| Unit Vac Timeout | M0014B | T0008 ≥ D00036 + grace |
| Vac Leak | M0014C | Δ vacuum > D00056 during VAC CHECK |
| Inj Timeout | M0014D | No flow meter pulse change over 30s (T0010) |
| Inj Amount NG | M0014E | Actual ∉ [D00044-D00045 ± D00046] |
| Pressure High | M00150 | D00058 > upper limit |
| Pressure Low | M00151 | D00058 <= lower limit |
| Temp Out of Range | M00152 | D00060 < -200 or D00060 > 800 |
| Model Not Selected | M00153 | D00032 = 0 at PRECHECK |
| Target Not Set | M00154 | D00044-D00045 = 0 at PRECHECK |
| Bombe Low | M00155 | L2 cumulative usage ≥ D00230-D00231 |

### L3 Oil Alarms

| Alarm | Bit | Trigger |
|-------|:---:|---------|
| Oil Timeout | M0015E | No HSC change over 30s (T0013/T0014) |
| Oil Amount NG | M0015F | Actual ∉ [D00018-D00019 ± D00020] |
| Hydro Pump Trip | M00130 | M00304 N/C OPEN — blocks oil steps |

### Buzzer Control

```
// Buzzer output
LOAD any_alarm_latch AND NOT M001F4 → OUT M00045

// BUZZER STOP button → mute only (latches untouched)
LOAD M0019B → SET M001F4

// New alarm rising edge → unmute (buzzer re-triggers)
LOAD alarm_N AND NOT alarm_N_prev → RST M001F4

// ALARM RESET → unmute + clear all latches (if source cleared)
LOAD M0019A → RST M001F4
```

---

## 12. Interlock

### L1 Interlock (AND chain M00050)

| Bit | Source |
|:---:|--------|
| M00051 | Interlock input 1 |
| M00052 | Interlock input 2 |
| M00053 | Interlock input 3 |
| M00054 | Interlock input 4 |
| M00055 | Always ON (spare, F00000) |

### L2 Interlock (AND chain M0005A)

| Bit | Source |
|:---:|--------|
| M0005B | Interlock input 1 |
| M0005C | Interlock input 2 |
| M0005D | Interlock input 3 |
| M0005E | Interlock input 4 |
| M0005F | Always ON (spare, F00000) |

- All 5 bits ANDed → M00050 (L1) / M0005A (L2).
- Violation during vacuum steps → RST step → EXHAUST.
- M0012D (Door alarm) gated by M0020A — suppressed when interlock "not used".

### EMG-Level Stops

| Condition | Effect |
|-----------|--------|
| M00302 N/C OPEN | EMG alarm latch M0012C |
| M00303 OFF (Door) | Door alarm latch M0012D (if M0020A=ON) |
| Vacuum pump trip | Pump alarm latch M0012F |

---

## 13. Injection Quantity

### Model Table (25 models per gun, 9 words/row)

| Per Row | Width | Gun A Base | Gun B Base |
|---------|:-----:|:----------:|:----------:|
| Model# | 16-bit | D00300 | D00550 |
| Refrig Base Target | 32-bit (g) | — | — |
| Refrig User Correction | 16-bit (±g) | — | — |
| Refrig Display Correction | 16-bit (±g) | — | — |
| Oil Base Target | 32-bit (g) | — | — |
| Oil User Correction | 16-bit (±g) | — | — |
| Oil Display Correction | 16-bit (±g) | — | — |

- Gun A: D00300-D00524 (stride 9). Gun B: D00550-D00774 (stride 9).
- All D registers: even address + next odd reserved for 32-bit upgrade.

### Barcode Used (M00208=ON, power-on default)

1. PC writes target amount to PLC via gmes (D06980-D06999 L1 / D07980-D07999 L2).
2. PLC BMOV D06980 to D07220 (L1) / D07980 to D08220 (L2) — HMI display area.
3. PLC scans lookup table → find matching Base Target.
4. Match found → D00000/D00032 (model#) assigned, corrections applied.
5. No match → Model Not Selected alarm (M0013F/M00153), stop.
6. Real injection target (D00012-D00013) = Base Target + User Correction.
7. HMI display target = Base Target + User Correction + Display Correction.
8. On IDLE entry: D00000/D00032 = 0 (model# reset). FMOV 0 D06980 20 (clear barcode area).

### Barcode Not Used (M00208=OFF)

1. Operator sets D00000/D00032 directly on HMI.
2. Lookup table → target + corrections applied.
3. On IDLE entry: D00000/D00032 = 0 (always reset).

---

## 14. Flow Meter (HSC)

- Counts during injection steps only.
- L1/L2 refrig: counts during M0000F–M00010 / M00023–M00024.
- L1/L2 oil: counts during M00033–M00034.
- Per-gun: M00041/M00042 (Gun A) and M0004B/M0004C (Gun B) on separate P outputs.
- Timeout: 30.0s (3000 on 10ms timer T0004/T0005/T0010/T0011/T0013/T0014).

---

## 15. Solenoids & Motor

| L1 | L2 | Signal | Type | M Bit | P Output |
|:--:|:--:|--------|:----:|:-----:|:--------:|
| ✓ | ✓ | VAC SOL | Solenoid | M0003C/M00046 | P0032/P0048 |
| ✓ | ✓ | STEM SOL | Solenoid | M0003D/M00047 | P0033/P0049 |
| ✓ | ✓ | REFRIG FAST SOL | Solenoid | M0003E/M00048 | P0034/P0050 |
| ✓ | ✓ | REFRIG BASE SOL | Solenoid | M0003F/M00049 | P0035/P0051 |
| ✓ | ✓ | EXHAUST SOL | Solenoid | M00040/M0004A | P0036/P0052 |
| ✓ | ✓ | OIL FAST SOL | Solenoid | M00041/M0004B | P0037/P0040 |
| ✓ | ✓ | OIL BASE SOL | Solenoid | M00042/M0004C | P0038/P0041 |
| — | — | LINE VAC SOL (N/O) | Solenoid | M00044 | P0039 |
| — | — | VACUUM PUMP RUN | Motor | M00043 toggle | — |
| — | — | BUZZER | — | M00045 | — |
| ✓ | ✓ | LAMPS G/R/Y | — | M0004D/M0004E/M0004F | — |
| — | — | HYDRO PUMP | Motor | M00060 toggle | P0069 |
| — | — | OIL LINE SOL | Solenoid | M00061 | P0070 |

---

## 16. Digital Inputs (DI)

| Qty | Signal | P Addr | M Mirror | Scope |
|:---:|--------|:------:|:--------:|:-----:|
| 1 | EMG (N/C) | P0002 | M00302 | Shared |
| 1 | Door (N/C) | P0003 | M00303 | Shared |
| 1 | Pump fault (N/C) | P0004 | M00304 | Shared |
| 4 | Interlock L1 | P000C-P000F | M0030C-M0030F | L1 |
| 5 | Interlock L2 | P0017-P001B | M00317-M0031B | L2 |
| 2 | HSC L1/L2 | HSC | — | L1/L2 |
| 2 | HSC Oil L1/L2 | HSC | — | L1/L2 |

---

## 17. Analog Inputs

| L1 | L2 | Signal | Width | EU Register L1 | EU Register L2 |
|:--:|:--:|--------|:-----:|:--------------:|:--------------:|
| ✓ | ✓ | Pressure | 16-bit | D00026 | D00058 |
| ✓ | ✓ | Temperature | 16-bit | D00028 | D00060 |
| ✓ | ✓ | Vacuum | 32-bit | D00030-D00031 | D00062-D00063 |

### Analog EU Destination Registers

| Signal | L1 | L2 |
|--------|:--:|:--:|
| Pressure (setpoint) | D00026 | D00058 |
| Temperature (setpoint) | D00028 | D00060 |
| Vacuum reading | D00030-D00031 | D00062-D00063 |
| Pressure high alarm limit | D00026 | D00058 |
| Pressure low alarm limit | D00030 (shared with vacuum) | D00062 (shared with vacuum) |

Note: ad.il is a placeholder. Analog scaling is done externally; values are MOV'd into the above registers by the user/HMI.

---

## 18. SPC

- Actual SPC merged into gmes.il: vacuum SPC logged during GUN VAC/UNIT VAC/VAC CHECK.
- 0.08s interval sampling.
- Counters: D00240 (L1 inj count), D00242 (L2 inj count), D00200-D00201 (L1 usage), D00220-D00221 (L2 usage).
- Cycle count: D00202 (L1), D00222 (L2). Cumulative inj: D00204-D00205 (L1), D00224-D00225 (L2).
- Stopwatch D00244: 0.1s resolution, starts on auto START, stops on IDLE/STOP/NG/EMG.

---

## 19. D-Register Map (L1 D00000-D00031 / L2 D00032-D00063)

| Parameter | L1 | L2 | Unit |
|-----------|:--:|:--:|------|
| Model# | D00000 | D00032 | — |
| Gun vac time | D00002 | D00034 | sec |
| Unit vac time | D00004 | D00036 | sec |
| Vac check time | D00006 | D00038 | sec |
| Exhaust time | D00008 | D00040 | sec |
| Refrig fast stop | D00010-D00011 | D00042-D00043 | g |
| Refrig target | D00012-D00013 | D00044-D00045 | g |
| Refrig tolerance | D00014 | D00046 | g |
| Oil fast stop | D00016-D00017 | D00048-D00049 | g |
| Oil target | D00018-D00019 | D00050-D00051 | g |
| Oil tolerance | D00020 | D00052 | g |
| Unit vac setting | D00022 | D00054 | Torr |
| Vac check setting | D00024 | D00056 | delta |
| Pressure | D00026 | D00058 | — |
| Temperature | D00028 | D00060 | — |
| Vacuum | D00030-D00031 | D00062-D00063 | Torr |
| Result Code | D01000 | D01200 | 1=OK, 6=STOP/EMG |

### Additional Register Blocks

| Range | Use |
|-------|-----|
| D00200-D00211 | L1 SPC (usage, cycle, cum inj, bombe alarm) |
| D00220-D00231 | L2 SPC |
| D00240 | L1 injection count |
| D00242 | L2 injection count |
| D00244 | Stopwatch (0.1s, shared) |
| D00300-D00524 | Gun A model table (25 x 9) |
| D00550-D00774 | Gun B model table (25 x 9) |
| D06980-D06999 | L1 barcode area (PC write) |
| D07980-D07999 | L2 barcode area (PC write) |
| D07000-D07001 | L1 barcode target |
| D08000-D08001 | L2 barcode target |
| D07220-D07239 | L1 HMI barcode display (BMOV from D06980) |
| D08220-D08239 | L2 HMI barcode display (BMOV from D07980) |
| D07020-D07219 | L1 VAC SPC log |
| D08020-D08219 | L2 VAC SPC log |

---

## 20. File Structure (12 .il files)

| Module | Content |
|--------|---------|
| MAIN.il | Step machine, mode/gun control, ready flags, interlock, STOP/EMG, lamps, stopwatch, vacuum pump |
| alarm.il | Alarm latches (shared+L1+L2+L3), buzzer M00045, mute M001F4 |
| gunvac.il | Gun vacuum (M0000C/M00020): VAC SOL, timer T0001/T0007, OK/NG |
| unitvac.il | Unit vacuum (M0000D/M00021): VAC+STEM SOL, timer T0002/T0008, vac≤setting, OK/NG |
| vacchec.il | Vacuum check (M0000E/M00022): VAC+STEM+LINE VAC SOL ON, delta calc, OK/NG |
| refinj.il | Refrig injection (M0000F-M00011/M00023-M00025): FAST→BASE→EXHAUST, HSC, tolerance |
| oilinj.il | Oil injection (M00033-M00035): per-gun oil, HSC, tolerance |
| gmes.il | PC communication + SPC logging |
| idata.il | DI → M mirror, M → DO mirror, system flags, HMI button buffer |
| indexs.il | Barcode copy + model lookup (25-model table scan) |
| ad.il | Analog EU scaling (placeholder) |
| setting.il | Configuration placeholder (no-op MOVs) |

---

## 21. Key Design Rules

| Rule | Detail |
|------|--------|
| State bits | Self-holding OUT: `LOAD set_cond OR self AND NOT release_cond OUT self` |
| Exclusive pairs | SET/RST allowed (gun select M000D2/M000D3, mode toggle M000C8/M000C9, alarm mute M001F4, ready toggle M000DC-M000E0, oil enable M00209, interlock enable M0020A) |
| HMI buttons | Momentary 1-scan, edge-detect via OUTP M00258-M0026F before use |
| P isolation | idata.il only. All logic code references M/D registers. |
| D registers | Even address + next odd reserved for 32-bit upgrade (all registers). |
| Solenoid | H+L only (FAST + BASE). No type branching. Single-sol users leave BASE unwired. |
| Edge detection | OUTP instruction used for button edges (M00258-M0026F). No manual prev-state compare for buttons. |
| Warmup | T0000 0.5s delay before EVERY step entry (auto chain via M001CC-M001D5, manual via M001C5). |
| STOP | Available in all modes. Immediate halt → EXHAUST → IDLE. M001C2/M001C3 latch. |
| Lamp progress | GREEN M0004D: running + no alarm. RED M0004E: any alarm. YELLOW M0004F: IDLE + !interlock. |
| Naming | Device names as clear as possible within XG5000 comment character limits. |
| Barcode reset | FMOV 0 D06980 20 clears barcode area on cycle end. Model# reset to 0 on every IDLE entry. |
