# REF_DOCUMENT

> **PLC**: QCPU (Q mode) Q03UDV | **Tool**: GX Works2 IL | **HMI**: LS IXP2-1200
> **Re-planned**: OPERATION_SCENARIO.md (Session 1, 2026-06-05)

---

# 1. System Overview

Refrigerant charging machine. Two independent refrig lines (GUN A=L1, GUN B=L2) + shared oil line (L3).
Serial operation — one gun active at a time. Gun select determines active line.

## Equipment Structure

| | GUN A (L1) | GUN B (L2) | Shared |
|---|:---:|:---:|:---:|
| VAC SOL | M60 | M70 | — |
| STEM SOL | M61 | M71 | — |
| REFRIG FAST SOL | M62 | M72 | — |
| REFRIG BASE SOL | M63 | M73 | — |
| EXHAUST SOL | M64 | M74 | — |
| OIL FAST SOL | M65 | M75 | — |
| OIL BASE SOL | M66 | M76 | — |
| VACUUM PUMP | — | — | M67 |
| LINE VAC SOL (N/O) | — | — | M68 |
| BUZZER | — | — | M69 |
| LAMPS (G/R/Y) | — | — | M77/M78/M79 |

---

# 2. Step Machine

| Step | L1 | L2 | L3 | Solenoid Active |
|------|:--:|:--:|:--:|----------------|
| IDLE | M10 | M30 | M50 | — |
| PRECHECK | M11 | M31 | — | interlock, model>0, target>0 |
| GUN VAC | M12 | M32 | — | VAC SOL, timer only |
| UNIT VAC | M13 | M33 | — | VAC+STEM SOL, vac≤setting |
| VAC CHECK | M14 | M34 | — | VAC+STEM+LINE VAC, Δvac check |
| OIL FAST | — | — | M51 | OIL FAST+BASE, HSC≥fast_stop |
| OIL BASE | — | — | M52 | OIL BASE, HSC≥target |
| REFRIG FAST | M15 | M35 | — | FAST+BASE, HSC≥fast_stop |
| REFRIG BASE | M16 | M36 | — | BASE, HSC≥target |
| EXHAUST | M17 | M37 | — | EXHAUST SOL, timer |
| COMPLETE | M18 | M38 | M53 | SPC, result K1→IDLE |

- **Warmup**: T0 0.5s before every step entry (auto mode only)
- **Rung order**: COMPLETE→EXHAUST→...→IDLE (release before released)
- Offset: L1→L2 +20, L1→L3 +40

---

# 3. Operation Modes

## Power-On Defaults

| Setting | Value | Flag |
|---------|:-----:|------|
| Mode | MANUAL | M200 |
| Gun | A | M210 |
| Barcode | Used | M520 |
| Oil+Refrig | Enabled | M521 |
| Interlock | Used | M522 |
| Steps | IDLE | M10/M30/M50 |

## Mode Control

- **M402**: AUTO/MANUAL toggle (IDLE only). SET/RST flip-flop
- **M400/M401**: GUN A/B select (IDLE only)
- **M415**: OIL+REFRIG enable toggle
- **M413**: INTERLOCK USE/NOT USE toggle (door bypass)

## Auto Mode (M201)

```
START → [T0 0.5s] → PRECHECK → [T0] → GUN VAC → [T0] → UNIT VAC → [T0]
→ VAC CHECK → [T0] → (M521&D18>0: OIL FAST→BASE→COMPLETE → [T0])
→ REFRIG FAST → REFRIG BASE → [T0] → EXHAUST → COMPLETE → IDLE
```

- Warmup chain (M460-M469): auto mode only, M201 guarded
- Stopwatch (D244): starts on auto START, stops on IDLE

## Manual Mode (M200)

| Button | + START | Step |
|--------|---------|------|
| GUN VAC (M403) | — | M12 or M32 |
| UNIT VAC (M404) | — | M13 or M33 |
| VAC CHECK (M405) | — | M14 or M34 |
| REFRIG INJ (M406) | — | M15→M16→EXHAUST→COMPLETE |
| OIL INJ (M407) | — | M51→M52→M53 |

- READY toggle (press again to cancel)
- Single step only (warmup chain blocked by M201)
- REFRIG INJ/OIL INJ blocked when barcode used (M520)
- OIL INJ blocked when M521 OFF

---

# 4. HMI Buttons

| Button | Device | Function |
|--------|:-----:|----------|
| GUN A | M400 | Gun select |
| GUN B | M401 | Gun select |
| AUTO/MANUAL | M402 | Mode toggle |
| GUN VACUUM | M403 | Manual function |
| UNIT VACUUM | M404 | Manual function |
| VACUUM CHECK | M405 | Manual function |
| REFRIG INJ | M406 | Manual function |
| OIL INJ | M407 | Manual function |
| START | M408 | Initiate |
| STOP | M409 | Halt → EXHAUST → IDLE |
| ALARM RESET | M410 | Clear latches + unmute |
| BUZZER STOP | M411 | Mute buzzer |
| VAC PUMP ON/OFF | M412 | Toggle vacuum pump |
| INTERLOCK EN | M413 | Door interlock toggle (M522) |
| L1 COUNT RESET | M414 | D240 = 0 |
| OIL+REFRIG EN | M415 | Oil enable toggle (M521) |
| L2 COUNT RESET | M416 | D242 = 0 |
| L1 USAGE RESET | M417 | D200-D201 = 0 |
| L2 USAGE RESET | M418 | D220-D221 = 0 |

---

# 5. Model Table & Injection Amount

## Model Table (25 models per gun, 9 words/row)

| | GUN A | GUN B |
|---|:---:|:---:|
| Base | D300-D524 | D550-D774 |
| Stride | 9 words | 9 words |

Row layout: `Model# (16) | Refrig Target (32) | Refrig Correction (16) | Refrig Display Corr (16) | Oil Target (32) | Oil Correction (16) | Oil Display Corr (16)`

## Barcode Flow

```
PC → D6980-D6999 (L1) / D7980-D7999 (L2)   ← PC writes barcode
PLC → BMOV D6980 D7220 K20                  ← Copy to HMI display area
    → M520=ON: D7001 target → table scan → D0/D32 model#
    → M520=OFF: user sets D0/D32 directly
    → D12/D44 (final refrig target), D18/D50 (final oil target)
Cycle end → FMOV K0 D6980 K20, clear D7000/D7001
```

---

# 6. Stop / Emergency / NG

| Action | Trigger | Behavior |
|--------|---------|----------|
| STOP | M409 | M450/M451 latch → RST steps → EXHAUST → IDLE |
| NG Alarm | vac NG/TO/leak | Same as STOP |
| EMG | M770 N/C OPEN | M452 self-hold → all RST → M410 manual reset |
| Interlock fail | vac step + M80/M90 OFF | RST step → EXHAUST |

---

# 7. Alarm System

| Shared | L1 | L2 | L3 Oil |
|--------|------|------|--------|
| M300 EMG | M310 GUN TO | M330 GUN TO | M350 OIL TO |
| M301 DOOR* | M311 UNIT TO | M331 UNIT TO | M351 OVER |
| M302 BOMBE | M312 VAC LEAK | M332 VAC LEAK | M352 UNDER |
| M303 PUMP | M313 INJ TO | M333 INJ TO | |
| | M314 OVER | M334 OVER | |
| | M315 UNDER | M335 UNDER | |
| | M316-M320 | M336-M340 | |

\* M301 gated by M522 (interlock enable)

- All self-holding: `LD trigger OR self ANI M410`
- Buzzer (M69): any alarm AND NOT M500(mute)
- Lamps: M77(G=run), M78(R=alarm), M79(Y=idle+!interlock)

---

# 8. SPC & Counters

| Item | L1 | L2 |
|------|----|----|
| Cumulative usage | D200-D201 | D220-D221 |
| Cycle count | D202 | D222 |
| Cumulative inj amount | D204-D205 | D224-D225 |
| Total injection count | D240 | D242 |
| Bombe alarm setting | D210-D211 | D230-D231 |
| VAC SPC log | D7020-D7219 | D8020-D8219 |
| Stopwatch | D244 (shared, 0.1sec) | |

---

# 9. D-Register Map (32-bit ready, L1 D0-D31 / L2 D32-D63)

| Parameter | L1 | L2 | Unit |
|-----------|:--:|:--:|------|
| Model# | D0 | D32 | — |
| Gun vac time | D2 | D34 | sec |
| Unit vac time | D4 | D36 | sec |
| Vac check time | D6 | D38 | sec |
| Exhaust time | D8 | D40 | sec |
| Refrig fast stop | D10-D11 | D42-D43 | g |
| Refrig target | D12-D13 | D44-D45 | g |
| Refrig tolerance | D14 | D46 | g |
| Oil fast stop | D16-D17 | D48-D49 | g |
| Oil target | D18-D19 | D50-D51 | g |
| Oil tolerance | D20 | D52 | g |
| Unit vac setting | D22 | D54 | Torr |
| Vac check setting | D24 | D56 | delta |
| Pressure | D26 | D58 | — |
| Temperature | D28 | D60 | — |
| Vacuum | D30-D31 | D62-D63 | Torr |

---

# 10. File Map (12 CSV)

| File | Content |
|------|---------|
| MAIN.csv | Step machine, mode, gun, ready, stop/emg, interlock, lamps, stopwatch |
| alarm.csv | Alarm latches (shared+L1+L2+L3), buzzer, mute |
| refinj.csv | Refrig injection (H+L): FAST→BASE→EXHAUST |
| oilinj.csv | Oil injection (per-gun): FAST→BASE→COMPLETE |
| gunvac.csv | Gun vacuum: VAC SOL, timer (no vacuum check) |
| unitvac.csv | Unit vacuum: VAC+STEM SOL, timer, vac≤setting |
| vacchec.csv | Vacuum check: VAC+STEM+LINE VAC ON, Δvac check |
| gmes.csv | PC communication + SPC + counters |
| indexs.csv | Barcode copy + model lookup |
| ad.csv | Analog EU scaling (placeholder) |
| idata.csv | I/O mapping (X→M, M→Y), HMI button buffer |
| setting.csv | Config sync (placeholder for future expansion) |
