# REF_DOCUMENT

> **PLC**: XGK-CPUE | **Tool**: XG5000 IL | **HMI**: LS IXP2-1200
> **Re-planned**: OPERATION_SCENARIO.md (Session 1, 2026-06-05) | **XG5000 갱신**: 2026-06-08

---

# 1. System Overview

Refrigerant charging machine. Two independent refrig lines (GUN A=L1, GUN B=L2) + shared oil line (L3).
Serial operation — one gun active at a time. Gun select determines active line.

## Equipment Structure

| | GUN A (L1) | GUN B (L2) | Shared |
|---|:---:|:---:|:---:|
| VAC SOL | M0003C | M00046 | — |
| STEM SOL | M0003D | M00047 | — |
| REFRIG FAST SOL | M0003E | M00048 | — |
| REFRIG BASE SOL | M0003F | M00049 | — |
| EXHAUST SOL | M00040 | M0004A | — |
| OIL FAST SOL | M00041 | M0004B | — |
| OIL BASE SOL | M00042 | M0004C | — |
| VACUUM PUMP | — | — | M00043 |
| LINE VAC SOL (N/O) | — | — | M00044 |
| BUZZER | — | — | M00045 |
| LAMPS (G/R/Y) | — | — | M0004D/M0004E/M0004F |

---

# 2. Step Machine

| Step | L1 | L2 | L3 | Solenoid Active |
|------|:--:|:--:|:--:|----------------|
| IDLE | M0000A | M0001E | M00032 | — |
| PRECHECK | M0000B | M0001F | — | interlock, model>0, target>0 |
| GUN VAC | M0000C | M00020 | — | VAC SOL, timer only |
| UNIT VAC | M0000D | M00021 | — | VAC+STEM SOL, vac≤setting |
| VAC CHECK | M0000E | M00022 | — | VAC+STEM+LINE VAC, Δvac check |
| OIL FAST | — | — | M00033 | OIL FAST+BASE, HSC≥fast_stop |
| OIL BASE | — | — | M00034 | OIL BASE, HSC≥target |
| REFRIG FAST | M0000F | M00023 | — | FAST+BASE, HSC≥fast_stop |
| REFRIG BASE | M00010 | M00024 | — | BASE, HSC≥target |
| EXHAUST | M00011 | M00025 | — | EXHAUST SOL, timer |
| COMPLETE | M00012 | M00026 | M00035 | SPC, result 1→IDLE |

- **Warmup**: T0000 0.5s before every step entry (auto mode only)
- **Rung order**: COMPLETE→EXHAUST→...→IDLE (release before released)
- Offset: L1→L2 +20 (hex +0x14), L1→L3 +40 (hex +0x28)

---

# 3. Operation Modes

## Power-On Defaults

| Setting | Value | Flag |
|---------|:-----:|------|
| Mode | MANUAL | M000C8 |
| Gun | A | M000D2 |
| Barcode | Used | M00208 |
| Oil+Refrig | Enabled | M00209 |
| Interlock | Used | M0020A |
| Steps | IDLE | M0000A/M0001E/M00032 |

## Mode Control

- **M00192**: AUTO/MANUAL toggle (IDLE only). SET/RST flip-flop
- **M00190/M00191**: GUN A/B select (IDLE only)
- **M0019F**: OIL+REFRIG enable toggle
- **M0019D**: INTERLOCK USE/NOT USE toggle (door bypass)

## Auto Mode (M000C9)

```
START → [T0000 0.5s] → PRECHECK → [T0000] → GUN VAC → [T0000] → UNIT VAC → [T0000]
→ VAC CHECK → [T0000] → (M00209&D00018>0: OIL FAST→BASE→COMPLETE → [T0000])
→ REFRIG FAST → REFRIG BASE → [T0000] → EXHAUST → COMPLETE → IDLE
```

- Warmup chain (M001CC-M001D5): auto mode only, M000C9 guarded
- Stopwatch (D00244): starts on auto START, stops on IDLE

## Manual Mode (M000C8)

| Button | + START | Step |
|--------|---------|------|
| GUN VAC (M00193) | — | M0000C or M00020 |
| UNIT VAC (M00194) | — | M0000D or M00021 |
| VAC CHECK (M00195) | — | M0000E or M00022 |
| REFRIG INJ (M00196) | — | M0000F→M00010→EXHAUST→COMPLETE |
| OIL INJ (M00197) | — | M00033→M00034→M00035 |

- READY toggle (press again to cancel)
- Single step only (warmup chain blocked by M000C9)
- REFRIG INJ/OIL INJ blocked when barcode used (M00208)
- OIL INJ blocked when M00209 OFF

---

# 4. HMI Buttons

| Button | Device | Function |
|--------|:-----:|----------|
| GUN A | M00190 | Gun select |
| GUN B | M00191 | Gun select |
| AUTO/MANUAL | M00192 | Mode toggle |
| GUN VACUUM | M00193 | Manual function |
| UNIT VACUUM | M00194 | Manual function |
| VACUUM CHECK | M00195 | Manual function |
| REFRIG INJ | M00196 | Manual function |
| OIL INJ | M00197 | Manual function |
| START | M00198 | Initiate |
| STOP | M00199 | Halt → EXHAUST → IDLE |
| ALARM RESET | M0019A | Clear latches + unmute |
| BUZZER STOP | M0019B | Mute buzzer |
| VAC PUMP ON/OFF | M0019C | Toggle vacuum pump |
| INTERLOCK EN | M0019D | Door interlock toggle (M0020A) |
| L1 COUNT RESET | M0019E | D00240 = 0 |
| OIL+REFRIG EN | M0019F | Oil enable toggle (M00209) |
| L2 COUNT RESET | M001A0 | D00242 = 0 |
| L1 USAGE RESET | M001A1 | D00200-D00201 = 0 |
| L2 USAGE RESET | M001A2 | D00220-D00221 = 0 |

---

# 5. Model Table & Injection Amount

## Model Table (25 models per gun, 9 words/row)

| | GUN A | GUN B |
|---|:---:|:---:|
| Base | D00300-D00524 | D00550-D00774 |
| Stride | 9 words | 9 words |

Row layout: `Model# (16) | Refrig Target (32) | Refrig Correction (16) | Refrig Display Corr (16) | Oil Target (32) | Oil Correction (16) | Oil Display Corr (16)`

## Barcode Flow

```
PC → D06980-D06999 (L1) / D07980-D07999 (L2)   ← PC writes barcode
PLC → BMOV D06980 D07220 20                      ← Copy to HMI display area
    → M00208=ON: D07001 target → table scan → D00000/D00032 model#
    → M00208=OFF: user sets D00000/D00032 directly
    → D00012/D00044 (final refrig target), D00018/D00050 (final oil target)
Cycle end → FMOV 0 D06980 20, clear D07000/D07001
```

---

# 6. Stop / Emergency / NG

| Action | Trigger | Behavior |
|--------|---------|----------|
| STOP | M00199 | M001C2/M001C3 latch → RST steps → EXHAUST → IDLE |
| NG Alarm | vac NG/TO/leak | Same as STOP |
| EMG | M00302 N/C OPEN | M001C4 self-hold → all RST → M0019A manual reset |
| Interlock fail | vac step + M00050/M0005A OFF | RST step → EXHAUST |

---

# 7. Alarm System

| Shared | L1 | L2 | L3 Oil |
|--------|------|------|--------|
| M0012C EMG | M00136 GUN TO | M0014A GUN TO | M0015E OIL TO |
| M0012D DOOR* | M00137 UNIT TO | M0014B UNIT TO | M0015F OVER |
| M0012F PUMP | M00138 VAC LEAK | M0014C VAC LEAK | M00160 UNDER |
| M00130 HYDRO TRIP | M00139 INJ TO | M0014D INJ TO | |
| | M0013A OVER | M0014E OVER | |
| | M0013B UNDER | M0014F UNDER | |
| | M0013C PRES↑ | M00150 PRES↑ | |
| | M0013D PRES↓ | M00151 PRES↓ | |
| | M0013E TEMP NG | M00152 TEMP NG | |
| | M0013F MODEL=0 | M00153 MODEL=0 | |
| | M00140 TARGET=0 | M00154 TARGET=0 | |
| | M00141 BOMBE LOW | M00155 BOMBE LOW | |

\* M0012D gated by M0020A (interlock enable)

- All self-holding: `LOAD trigger OR self AND NOT M0019A`
- Buzzer (M00045): any alarm AND NOT M001F4(mute)
- Lamps: M0004D(G=run), M0004E(R=alarm), M0004F(Y=idle+!interlock)

---

# 8. SPC & Counters

| Item | L1 | L2 |
|------|----|----|
| Cumulative usage | D00200-D00201 | D00220-D00221 |
| Cycle count | D00202 | D00222 |
| Cumulative inj amount | D00204-D00205 | D00224-D00225 |
| Total injection count | D00240 | D00242 |
| Bombe alarm setting | D00210-D00211 | D00230-D00231 |
| VAC SPC log | D07020-D07219 | D08020-D08219 |
| Stopwatch | D00244 (shared, 0.1sec) | |

---

# 9. D-Register Map (32-bit ready, L1 D00000-D00031 / L2 D00032-D00063)

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

---

# 10. File Map (12 .il)

| File | Content |
|------|---------|
| MAIN.il | Step machine, mode, gun, ready, stop/emg, interlock, lamps, stopwatch |
| alarm.il | Alarm latches (shared+L1+L2+L3), buzzer, mute |
| refinj.il | Refrig injection (H+L): FAST→BASE→EXHAUST |
| oilinj.il | Oil injection (per-gun): FAST→BASE→COMPLETE |
| gunvac.il | Gun vacuum: VAC SOL, timer (no vacuum check) |
| unitvac.il | Unit vacuum: VAC+STEM SOL, timer, vac≤setting |
| vacchec.il | Vacuum check: VAC+STEM+LINE VAC ON, Δvac check |
| gmes.il | PC communication + SPC + counters |
| indexs.il | Barcode copy + model lookup |
| ad.il | Analog EU scaling (placeholder) |
| idata.il | I/O mapping (P→M, M→P), HMI button buffer |
| setting.il | Config sync (placeholder for future expansion) |
