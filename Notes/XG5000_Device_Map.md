# XG5000 Device Address Map

> Generated from GX Works2 → XG5000 migration. M addresses decimal→hex. D/T/C zero-padded.

---

## I/O (P)
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| X0A0-X0BB | P0000-P001B | Physical inputs (28pt) |
| Y020-Y047 | P0020-P0047 | Physical outputs |

---

## Internal Relay (M) — Decimal GXW2 → Hex XG5000

### System Flags
| GXW2 (dec) | XG5000 (hex) | Purpose |
|-------------|---------------|---------|
| M0 | M00000 | Always ON mirror |
| M1 | M00001 | Always OFF mirror |
| M2 | M00002 | 0.1s clock mirror |
| M3 | M00003 | 1s clock mirror |

### Input Mirrors (28pt, P→M)
| GXW2 | XG5000 |
|------|--------|
| M768-M795 | M00300-M0031B |

### Interlock
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| M80-M85 | M00050-M00055 | L1 interlock door |
| M90-M95 | M0005A-M0005F | L2 interlock door |

### Step Machine
| Step | L1 (GXW2) | L1 (XG5000) | L2 (GXW2) | L2 (XG5000) | L3 (GXW2) | L3 (XG5000) |
|------|-----------|-------------|-----------|-------------|-----------|-------------|
| IDLE | M10 | M0000A | M30 | M0001E | M50 | M00032 |
| PRECHECK | M11 | M0000B | M31 | M0001F | — | — |
| GUN VAC | M12 | M0000C | M32 | M00020 | — | — |
| UNIT VAC | M13 | M0000D | M33 | M00021 | — | — |
| VAC CHECK | M14 | M0000E | M34 | M00022 | — | — |
| REFRIG FAST | M15 | M0000F | M35 | M00023 | — | — |
| REFRIG BASE | M16 | M00010 | M36 | M00024 | — | — |
| EXHAUST | M17 | M00011 | M37 | M00025 | — | — |
| COMPLETE | M18 | M00012 | M38 | M00026 | M53 | M00035 |
| OIL FAST | — | — | — | — | M51 | M00033 |
| OIL BASE | — | — | — | — | M52 | M00034 |

### Step Completion Flags
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| M100-M106 | M00064-M0006A | L1 step complete flags |
| M107 | M0006B | L1 cycle done |
| M108 | M0006C | L1 NG (gun vac TO) |
| M109 | M0006D | L1 NG (unit vac TO) |
| M110 | M0006E | L1 NG (refrig TO) |
| M116-M122 | M00074-M0007A | L2 step complete flags |
| M123 | M0007B | L2 cycle done |
| M124 | M0007C | L2 NG (gun vac TO) |
| M125 | M0007D | L2 NG (unit vac TO) |
| M126 | M0007E | L2 NG (refrig TO) |
| M145-M146 | M00091-M00092 | L3 step complete flags |

### Solenoids / Outputs
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| M60 | M0003C | L1 VAC SOL |
| M61 | M0003D | L1 STEM SOL |
| M62 | M0003E | L1 REFRIG FAST SOL |
| M63 | M0003F | L1 REFRIG BASE SOL |
| M64 | M00040 | L1 EXHAUST SOL |
| M65 | M00041 | OIL FAST GUN A |
| M66 | M00042 | OIL BASE GUN A |
| M67 | M00043 | VACUUM PUMP |
| M68 | M00044 | LINE VAC SOL (N/O) |
| M69 | M00045 | BUZZER |
| M70 | M00046 | L2 VAC SOL |
| M71 | M00047 | L2 STEM SOL |
| M72 | M00048 | L2 REFRIG FAST SOL |
| M73 | M00049 | L2 REFRIG BASE SOL |
| M74 | M0004A | L2 EXHAUST SOL |
| M75 | M0004B | OIL FAST GUN B |
| M76 | M0004C | OIL BASE GUN B |
| M77 | M0004D | LAMP GREEN (run) |
| M78 | M0004E | LAMP RED (alarm) |
| M79 | M0004F | LAMP YELLOW (idle) |
| M96 | M00060 | HYDRO PUMP L1 |
| M97 | M00061 | OIL LINE SOL |
| M98 | M00062 | HEATER RELAY |

### HMI Buttons
| GXW2 | XG5000 | Button |
|------|--------|--------|
| M400 | M00190 | GUN A |
| M401 | M00191 | GUN B |
| M402 | M00192 | AUTO/MANUAL |
| M403 | M00193 | GUN VACUUM |
| M404 | M00194 | UNIT VACUUM |
| M405 | M00195 | VACUUM CHECK |
| M406 | M00196 | REFRIG INJ |
| M407 | M00197 | OIL INJ |
| M408 | M00198 | START |
| M409 | M00199 | STOP |
| M410 | M0019A | ALARM RESET |
| M411 | M0019B | BUZZER STOP |
| M412 | M0019C | VAC PUMP ON/OFF |
| M413 | M0019D | INTERLOCK EN |
| M414 | M0019E | L1 COUNT RESET |
| M415 | M0019F | OIL+REFRIG EN |
| M416 | M001A0 | L2 COUNT RESET |
| M417 | M001A1 | L1 USAGE RESET |
| M418 | M001A2 | L2 USAGE RESET |
| M419 | M001A3 | HYDRO PUMP |

### Mode / Flags
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| M200 | M000C8 | MANUAL mode |
| M201 | M000C9 | AUTO mode |
| M210 | M000D2 | GUN A selected |
| M211 | M000D3 | GUN B selected |
| M220-M224 | M000DC-M000E0 | Manual ready flags |
| M450 | M001C2 | STOP latch |
| M451 | M001C3 | NG STOP latch |
| M452 | M001C4 | EMG self-hold |
| M453 | M001C5 | Start pulse |
| M460-M469 | M001CC-M001D5 | Warmup chain |
| M470-M471 | M001D6-M001D7 | VAC SPC flags |
| M480-M483 | M001E0-M001E3 | VAC SPC logging |
| M490 | M001EA | Stopwatch start |
| M500 | M001F4 | Buzzer mute |
| M520 | M00208 | Barcode used |
| M521 | M00209 | Oil+Refrig enabled |
| M522 | M0020A | Interlock enabled |
| M600-M623 | M00258-M0026F | PLS pulse flags |

### Alarm Latches
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| M300 | M0012C | EMG (shared) |
| M301 | M0012D | DOOR (shared) |
| M303 | M0012F | PUMP (shared) |
| M304 | M00130 | HYDRO TRIP (shared) |
| — | M0012E | (reserved) |
| M310 | M00136 | L1 GUN TO |
| M311 | M00137 | L1 UNIT TO |
| M312 | M00138 | L1 VAC LEAK |
| M313 | M00139 | L1 INJ TO |
| M314 | M0013A | L1 OVER |
| M315 | M0013B | L1 UNDER |
| M316 | M0013C | L1 PRESSURE |
| M317 | M0013D | L1 VACUUM LO |
| M318 | M0013E | L1 TEMP NG |
| M319 | M0013F | L1 MODEL=0 |
| M320 | M00140 | L1 TARGET=0 |
| M321 | M00141 | L1 BOMBE LOW |
| M330 | M0014A | L2 GUN TO |
| M331 | M0014B | L2 UNIT TO |
| M332 | M0014C | L2 VAC LEAK |
| M333 | M0014D | L2 INJ TO |
| M334 | M0014E | L2 OVER |
| M335 | M0014F | L2 UNDER |
| M336 | M00150 | L2 PRESSURE |
| M337 | M00151 | L2 VACUUM LO |
| M338 | M00152 | L2 TEMP NG |
| M339 | M00153 | L2 MODEL=0 |
| M340 | M00154 | L2 TARGET=0 |
| M341 | M00155 | L2 BOMBE LOW |
| M350 | M0015E | L3 OIL TO |
| M351 | M0015F | L3 OVER/UNDER |
| M352 | M00160 | L3 reserve |

---

## Special Flags (F)
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| SM400 | F00000 | Always ON |
| SM401 | F00001 | Always OFF |
| SM402 | F00002 | 0.1s clock |
| SM412 | F00004 | 1s clock |

---

## Data Registers (D) — 5-digit zero-padded
GXW2 decimal → XG5000 5-digit decimal (e.g. D0 → D00000, D300 → D00300)

### L1 Parameters (D00000-D00031)
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D0 | D00000 | L1 Model# |
| D2 | D00002 | Gun vac time |
| D4 | D00004 | Unit vac time |
| D6 | D00006 | Vac check time |
| D8 | D00008 | Exhaust time |
| D10-D11 | D00010-D00011 | Refrig fast stop (32b) |
| D12-D13 | D00012-D00013 | Refrig target (32b) |
| D14 | D00014 | Refrig tolerance |
| D16-D17 | D00016-D00017 | Oil fast stop (32b) |
| D18-D19 | D00018-D00019 | Oil target (32b) |
| D20 | D00020 | Oil tolerance |
| D22 | D00022 | Unit vac setting |
| D24 | D00024 | Vac check setting |
| D26 | D00026 | Pressure |
| D28 | D00028 | Temperature |
| D30-D31 | D00030-D00031 | Vacuum (32b) |

### L2 Parameters (D00032-D00063)
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D32 | D00032 | L2 Model# |
| D34 | D00034 | Gun vac time |
| ... | ... | (offset +32 from L1) |

### Counter / Statistics
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D200-D201 | D00200-D00201 | L1 Cumulative usage (32b) |
| D202 | D00202 | L1 Cycle count |
| D204-D205 | D00204-D00205 | L1 Cumulative inj amount (32b) |
| D210-D211 | D00210-D00211 | L1 Bombe alarm (32b) |
| D220-D221 | D00220-D00221 | L2 Cumulative usage (32b) |
| D222 | D00222 | L2 Cycle count |
| D224-D225 | D00224-D00225 | L2 Cumulative inj amount (32b) |
| D230-D231 | D00230-D00231 | L2 Bombe alarm (32b) |
| D240 | D00240 | L1 Total injection count |
| D242 | D00242 | L2 Total injection count |
| D244 | D00244 | Stopwatch (0.1s) |

### Analog Raw (D00100-D00120)
| GXW2 | XG5000 |
|------|--------|
| D100, D102, D104 | D00100, D00102, D00104 (L1) |
| D110, D112, D114 | D00110, D00112, D00114 (L2) |
| D120 | D00120 |

### Injection Flow (D00130-D00180)
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D130 | D00130 | L1 actual inj (32b copy) |
| D150 | D00150 | L1 HSC refrig flow |
| D160 | D00160 | L2 actual inj (32b copy) |
| D170 | D00170 | L2 HSC refrig flow |
| D180 | D00180 | HSC oil flow |

### Model Tables
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D300-D524 | D00300-D00524 | L1 model table (25×9) |
| D550-D774 | D00550-D00774 | L2 model table (25×9) |

### Vac Check Temp
| GXW2 | XG5000 |
|------|--------|
| D600, D602 | D00600, D00602 (L1) |
| D610, D612 | D00610, D00612 (L2) |

### Barcode / PC / SPC
| GXW2 | XG5000 | Content |
|------|--------|---------|
| D6980-D6999 | D06980-D06999 | L1 Barcode |
| D7000-D7001 | D07000-D07001 | L1 Model# result |
| D7020-D7219 | D07020-D07219 | L1 VAC SPC log |
| D7220-D7239 | D07220-D07239 | HMI display area |
| D7980-D7999 | D07980-D07999 | L2 Barcode |
| D8000-D8001 | D08000-D08001 | L2 Model# result |
| D8020-D8219 | D08020-D08219 | L2 VAC SPC log |

---

## Timer (T) — 4-digit zero-padded
| GXW2 | XG5000 | Purpose |
|------|--------|---------|
| T0 | T0000 | Warmup (0.5s) |
| T1 | T0001 | L1 Gun vac timeout |
| T2 | T0002 | L1 Unit vac timeout |
| T3 | T0003 | L1 Vac check timeout |
| T4 | T0004 | L1 Refrig fast TO |
| T5 | T0005 | L1 Refrig base TO |
| T6 | T0006 | L1 Exhaust time |
| T7 | T0007 | L2 Gun vac timeout |
| T8 | T0008 | L2 Unit vac timeout |
| T9 | T0009 | L2 Vac check timeout |
| T10 | T0010 | L2 Refrig fast TO |
| T11 | T0011 | L2 Refrig base TO |
| T12 | T0012 | L2 Exhaust time |
| T13 | T0013 | L3 Oil fast TO |
| T14 | T0014 | L3 Oil base TO |
| T15 | T0015 | L1 TO pulse |
| T16 | T0016 | L2 TO pulse |
| T18 | T0018 | VAC SPC trigger L1 |
| T19 | T0019 | VAC SPC trigger L2 |
| T20 | T0020 | VAC SPC delay L1 |
| T21 | T0021 | VAC SPC delay L2 |
| T22 | T0022 | Stopwatch timer |

---

## Counter (C) — Not used in current project
