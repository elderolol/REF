---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 1048
**Blocks:** 20
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | SYSTEM FLAGS | 1–6 | LD SM400, LD SM401, LD SM402 | 3 |
| 2 | POWER-ON DEFAULTS | 8–23 | LD M2, LD M2, LD M2 ... (+3) | 10 |
| 3 | MODE CONTROL | 25–36 | LD M402, LD M600, LD M600 | 9 |
| 4 | GUN SELECT | 38–51 | LD M400, LD M601, LD M401 ... (+1) | 10 |
| 5 | OIL+REFRIG ENABLE | 53–60 | LD M415, LD M621, LD M621 | 5 |
| 6 | INTERLOCK ENABLE | 62–69 | LD M413, LD M622, LD M622 | 5 |
| 7 | READY SET | 71–122 | LD M403, LD M603, LD M603 ... (+12) | 37 |
| 8 | MANUAL START ENTRY | 124–200 | LD M408, LD M408, LD M408 ... (+13) | 61 |
| 9 | AUTO START | 202–227 | LD M408, LD M408, LD M615 ... (+4) | 19 |
| 10 | AUTO CHAIN WARMUP | 229–390 | LD M11, LD M460, LD M460 ... (+34) | 125 |
| 11 | STEP L1 | 392–583 | LD M17, LD M17, LD M18 ... (+10) | 179 |
| 12 | STEP L2 | 585–776 | LD M37, LD M37, LD M38 ... (+10) | 179 |
| 13 | STEP L3 | 778–820 | LD M52, LD M52, LD M51 ... (+2) | 38 |
| 14 | INTERLOCK CHECK | 822–833 | LD M81, LD M91 | 10 |
| 15 | NG ALARM STOP | 835–873 | LD M108, LD M310, LD M124 ... (+4) | 32 |
| 16 | STOP | 875–888 | LD M409, LD M409, LD M10 ... (+3) | 8 |
| 17 | EMERGENCY STOP | 890–940 | LDI M770, LD M452, LD M452 ... (+5) | 43 |
| 18 | LAMP CONTROL | 942–1025 | LD M12, LD M32, LD M51 ... (+3) | 78 |
| 19 | STOPWATCH | 1027–1039 | LD M490, LD T22, LD M10 ... (+2) | 8 |
| 20 | VACUUM PUMP | 1041–1048 | LD M412, LD M620, LD M620 | 5 |

## Block Detail

### Block 1: SYSTEM FLAGS (Step 1–6)

**Trigger Condition:**
- LD SM400
- LD SM401
- LD SM402

**Actions:**
- OUT M0
- OUT M1
- OUT M2

### Block 2: POWER-ON DEFAULTS (Step 8–23)

**Trigger Condition:**
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2

**Actions:**
- SET M200
- RST M201
- SET M210
- RST M211
- SET M520
- SET M521
- SET M522
- SET M10
- SET M30
- SET M50

### Block 3: MODE CONTROL (Step 25–36)

**Trigger Condition:**
- LD M402
- LD M600
- LD M600

**Actions:**
- PLS M600
- AND M200
- AND M10
- SET M201
- RST M200
- AND M201
- AND M10
- SET M200
- RST M201

### Block 4: GUN SELECT (Step 38–51)

**Trigger Condition:**
- LD M400
- LD M601
- LD M401
- LD M602

**Actions:**
- PLS M601
- AND M10
- AND M30
- SET M210
- RST M211
- PLS M602
- AND M10
- AND M30
- SET M211
- RST M210

### Block 5: OIL+REFRIG ENABLE (Step 53–60)

**Trigger Condition:**
- LD M415
- LD M621
- LD M621

**Actions:**
- PLS M621
- ANI M521
- SET M521
- AND M521
- RST M521

### Block 6: INTERLOCK ENABLE (Step 62–69)

**Trigger Condition:**
- LD M413
- LD M622
- LD M622

**Actions:**
- PLS M622
- ANI M522
- SET M522
- AND M522
- RST M522

### Block 7: READY SET (Step 71–122)

**Trigger Condition:**
- LD M403
- LD M603
- LD M603
- LD M404
- LD M604
- LD M604
- LD M405
- LD M605
- LD M605
- LD M406
- LD M606
- LD M606
- LD M407
- LD M607
- LD M607

**Actions:**
- PLS M603
- AND M200
- ANI M220
- SET M220
- AND M200
- AND M220
- RST M220
- PLS M604
- AND M200
- ANI M221
- SET M221
- AND M200
- AND M221
- RST M221
- PLS M605
- AND M200
- ANI M222
- SET M222
- AND M200
- AND M222
- RST M222
- PLS M606
- AND M200
- ANI M520
- ANI M223
- SET M223
- AND M200
- AND M223
- RST M223
- PLS M607
- AND M200
- ANI M520
- ANI M224
- SET M224
- AND M200
- AND M224
- RST M224

### Block 8: MANUAL START ENTRY (Step 124–200)

**Trigger Condition:**
- LD M408
- LD M408
- LD M408
- LD M408
- LD M408
- LD M610
- LD M453
- LD M610
- LD M610
- LD M611
- LD M611
- LD M612
- LD M612
- LD M613
- LD M613
- LD M614

**Actions:**
- AND M220
- PLS M610
- AND M221
- PLS M611
- AND M222
- PLS M612
- AND M223
- PLS M613
- AND M224
- PLS M614
- OR M611
- OR M612
- OR M613
- OR M614
- SET M453
- OUT T0
- AND T0
- AND M210
- RST M220
- SET M12
- RST M453
- AND T0
- AND M211
- RST M220
- SET M32
- RST M453
- AND T0
- AND M210
- RST M221
- SET M13
- RST M453
- AND T0
- AND M211
- RST M221
- SET M33
- RST M453
- AND T0
- AND M210
- RST M222
- SET M14
- RST M453
- AND T0
- AND M211
- RST M222
- SET M34
- RST M453
- AND T0
- AND M210
- RST M223
- SET M15
- RST M453
- AND T0
- AND M211
- RST M223
- SET M35
- RST M453
- AND T0
- AND M521
- RST M224
- SET M51
- RST M453

### Block 9: AUTO START (Step 202–227)

**Trigger Condition:**
- LD M408
- LD M408
- LD M615
- LD M616
- LD M615
- LD M616
- LD M615

**Actions:**
- AND M201
- AND M210
- AND M10
- PLS M615
- AND M201
- AND M211
- AND M30
- PLS M616
- SET M453
- SET M453
- AND T0
- SET M11
- RST M453
- AND T0
- SET M31
- RST M453
- OR M616
- SET M490
- MOV K0

### Block 10: AUTO CHAIN WARMUP (Step 229–390)

**Trigger Condition:**
- LD M11
- LD M460
- LD M460
- LD M31
- LD M467
- LD M467
- LD M12
- LD M461
- LD M461
- LD M32
- LD M468
- LD M468
- LD M13
- LD M462
- LD M462
- LD M33
- LD M469
- LD M469
- LD M14
- LD M34
- LD M463
- LD M463
- LD M463
- LD M463
- LD M463
- LD M463
- LD M463
- LD M53
- LD M464
- LD M464
- LD M464
- LD M16
- LD M465
- LD M465
- LD M36
- LD M466
- LD M466

**Actions:**
- AND M100
- AND M201
- SET M460
- OUT T0
- AND T0
- SET M12
- RST M11
- RST M460
- AND M116
- AND M201
- SET M467
- OUT T0
- AND T0
- SET M32
- RST M31
- RST M467
- AND M101
- AND M201
- SET M461
- OUT T0
- AND T0
- SET M13
- RST M12
- RST M461
- AND M117
- AND M201
- SET M468
- OUT T0
- AND T0
- SET M33
- RST M32
- RST M468
- AND M102
- AND M201
- SET M462
- OUT T0
- AND T0
- SET M14
- RST M13
- RST M462
- AND M118
- AND M201
- SET M469
- OUT T0
- AND T0
- SET M34
- RST M33
- RST M469
- AND M103
- AND M201
- AND M119
- AND M201
- ORB 
- SET M463
- OUT T0
- AND T0
- AND M210
- AND M521
- LDD>= D18
- SET M51
- RST M14
- RST M463
- AND T0
- AND M211
- AND M521
- LDD>= D50
- SET M51
- RST M34
- RST M463
- AND T0
- AND M210
- LDD>= D18
- ANI M0
- SET M15
- RST M14
- RST M463
- AND T0
- AND M211
- LDD>= D50
- ANI M0
- SET M35
- RST M34
- RST M463
- AND T0
- AND M210
- ANI M521
- SET M15
- RST M14
- RST M463
- AND T0
- AND M211
- ANI M521
- SET M35
- RST M34
- RST M463
- AND M201
- AND M521
- SET M464
- OUT T0
- AND T0
- AND M210
- SET M15
- RST M53
- RST M464
- AND T0
- AND M211
- SET M35
- RST M53
- RST M464
- AND M105
- AND M201
- SET M465
- OUT T0
- AND T0
- SET M17
- RST M16
- RST M465
- AND M121
- AND M201
- SET M466
- OUT T0
- AND T0
- SET M37
- RST M36
- RST M466

### Block 11: STEP L1 (Step 392–583)

**Trigger Condition:**
- LD M17
- LD M17
- LD M18
- LD M17
- LD M16
- LD M15
- LD M14
- LD M13
- LD M12
- LD M11
- LD M11
- LD M18
- LD M10

**Actions:**
- AND M106
- OR M18
- ANI M10
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M18
- AND M106
- SET M107
- MOV K1
- OR M17
- ANI M18
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M17
- OR M16
- ANI M17
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M16
- OR M15
- ANI M16
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M15
- OR M14
- ANI M15
- ANI M51
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M14
- OR M13
- ANI M14
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M13
- OR M12
- ANI M13
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M12
- OR M11
- ANI M12
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M11
- AND M80
- LD> D0
- ANB 
- LDD>= D12
- ANB 
- OUT M100
- OR M10
- ANI M11
- ANI M12
- ANI M13
- ANI M14
- ANI M15
- ANI M16
- ANI M450
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- OUT M10
- MOV K0

### Block 12: STEP L2 (Step 585–776)

**Trigger Condition:**
- LD M37
- LD M37
- LD M38
- LD M37
- LD M36
- LD M35
- LD M34
- LD M33
- LD M32
- LD M31
- LD M31
- LD M38
- LD M30

**Actions:**
- AND M122
- OR M38
- ANI M30
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M38
- AND M122
- SET M123
- MOV K1
- OR M37
- ANI M38
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M37
- OR M36
- ANI M37
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M36
- OR M35
- ANI M36
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M35
- OR M34
- ANI M35
- ANI M51
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M34
- OR M33
- ANI M34
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M33
- OR M32
- ANI M33
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M32
- OR M31
- ANI M32
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M31
- AND M90
- LD> D32
- ANB 
- LDD>= D44
- ANB 
- OUT M116
- OR M30
- ANI M31
- ANI M32
- ANI M33
- ANI M34
- ANI M35
- ANI M36
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- OUT M30
- MOV K0

### Block 13: STEP L3 (Step 778–820)

**Trigger Condition:**
- LD M52
- LD M52
- LD M51
- LD M51
- LD M53

**Actions:**
- AND M146
- OR M53
- ANI M50
- ANI M450
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M350
- ANI M351
- OUT M53
- AND M146
- SET M147
- AND M145
- OR M52
- ANI M53
- ANI M450
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M350
- ANI M351
- OUT M52
- OUT M51
- OR M50
- ANI M51
- ANI M450
- ANI M451
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M350
- ANI M351
- OUT M50

### Block 14: INTERLOCK CHECK (Step 822–833)

**Trigger Condition:**
- LD M81
- LD M91

**Actions:**
- AND M82
- AND M83
- AND M84
- AND M85
- OUT M80
- AND M92
- AND M93
- AND M94
- AND M95
- OUT M90

### Block 15: NG ALARM STOP (Step 835–873)

**Trigger Condition:**
- LD M108
- LD M310
- LD M124
- LD M330
- LD M450
- LD M451
- LD M450

**Actions:**
- OR M109
- OR M111
- OR M311
- OR M312
- ORB 
- SET M450
- OR M125
- OR M127
- OR M331
- OR M332
- ORB 
- SET M451
- RST M12
- RST M13
- RST M14
- RST M15
- RST M16
- SET M17
- RST M32
- RST M33
- RST M34
- RST M35
- RST M36
- SET M37
- OR M451
- RST M51
- RST M52
- SET M53
- RST M65
- RST M66
- RST M75
- RST M76

### Block 16: STOP (Step 875–888)

**Trigger Condition:**
- LD M409
- LD M409
- LD M10
- LD M30
- LD M450
- LD M451

**Actions:**
- AND M210
- SET M450
- AND M211
- SET M451
- RST M450
- RST M451
- MOV K6
- MOV K6

### Block 17: EMERGENCY STOP (Step 890–940)

**Trigger Condition:**
- LDI M770
- LD M452
- LD M452
- LD M452
- LD M452
- LD M452
- LD M452
- LD M452

**Actions:**
- OR M452
- ANI M410
- OUT M452
- RST M10
- RST M11
- RST M12
- RST M13
- RST M14
- RST M15
- RST M16
- RST M17
- RST M18
- RST M30
- RST M31
- RST M32
- RST M33
- RST M34
- RST M35
- RST M36
- RST M37
- RST M38
- RST M50
- RST M51
- RST M52
- RST M53
- RST M60
- RST M61
- RST M62
- RST M63
- RST M64
- RST M65
- RST M66
- RST M68
- RST M69
- RST M70
- RST M71
- RST M72
- RST M73
- RST M74
- RST M75
- RST M76
- MOV K6
- MOV K6

### Block 18: LAMP CONTROL (Step 942–1025)

**Trigger Condition:**
- LD M12
- LD M32
- LD M51
- LD M300
- LD M10
- LD M30

**Actions:**
- OR M13
- OR M14
- OR M15
- OR M16
- OR M17
- OR M33
- OR M34
- OR M35
- OR M36
- OR M37
- ORB 
- OR M52
- ORB 
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M310
- ANI M311
- ANI M312
- ANI M313
- ANI M314
- ANI M316
- ANI M317
- ANI M318
- ANI M319
- ANI M320
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M330
- ANI M331
- ANI M332
- ANI M333
- ANI M334
- ANI M336
- ANI M337
- ANI M338
- ANI M339
- ANI M340
- ANI M300
- ANI M301
- ANI M302
- ANI M303
- ANI M350
- ANI M351
- OUT M77
- OR M301
- OR M302
- OR M303
- OR M310
- OR M311
- OR M312
- OR M313
- OR M314
- OR M316
- OR M317
- OR M318
- OR M319
- OR M320
- OR M330
- OR M331
- OR M332
- OR M333
- OR M334
- OR M336
- OR M337
- OR M338
- OR M339
- OR M340
- OR M350
- OR M351
- OUT M78
- ORB 
- ANI M80
- ANI M90
- OUT M79

### Block 19: STOPWATCH (Step 1027–1039)

**Trigger Condition:**
- LD M490
- LD T22
- LD M10
- LD M450
- LD M452

**Actions:**
- ANI T22
- OUT T22
- D+ D244
- OR M30
- RST M490
- OR M451
- RST M490
- RST M490

### Block 20: VACUUM PUMP (Step 1041–1048)

**Trigger Condition:**
- LD M412
- LD M620
- LD M620

**Actions:**
- PLS M620
- ANI M67
- SET M67
- AND M67
- RST M67

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D0 | D |  |  |  | 1 |
| D12 | D |  |  |  | 1 |
| D18 | D |  |  |  | 2 |
| D244 | D |  |  |  | 1 |
| D32 | D |  |  |  | 1 |
| D44 | D |  |  |  | 1 |
| D50 | D |  |  |  | 2 |
| K0 | K |  |  |  | 3 |
| K1 | K |  |  |  | 2 |
| K6 | K |  |  |  | 4 |
| M0 | M |  |  | 1 | 2 |
| M1 | M |  |  | 1 |  |
| M10 | M | 1 | 1 | 1 | 11 |
| M100 | M |  |  | 1 | 1 |
| M101 | M |  |  |  | 1 |
| M102 | M |  |  |  | 1 |
| M103 | M |  |  |  | 1 |
| M105 | M |  |  |  | 1 |
| M106 | M |  |  |  | 2 |
| M107 | M | 1 |  |  |  |
| M108 | M |  |  |  | 1 |
| M109 | M |  |  |  | 1 |
| M11 | M | 1 | 2 | 1 | 5 |
| M111 | M |  |  |  | 1 |
| M116 | M |  |  | 1 | 1 |
| M117 | M |  |  |  | 1 |
| M118 | M |  |  |  | 1 |
| M119 | M |  |  |  | 1 |
| M12 | M | 2 | 3 | 1 | 6 |
| M121 | M |  |  |  | 1 |
| M122 | M |  |  |  | 2 |
| M123 | M | 1 |  |  |  |
| M124 | M |  |  |  | 1 |
| M125 | M |  |  |  | 1 |
| M127 | M |  |  |  | 1 |
| M13 | M | 2 | 3 | 1 | 6 |
| M14 | M | 2 | 5 | 1 | 6 |
| M145 | M |  |  |  | 1 |
| M146 | M |  |  |  | 2 |
| M147 | M | 1 |  |  |  |
| M15 | M | 4 | 2 | 1 | 5 |
| M16 | M |  | 3 | 1 | 6 |
| M17 | M | 2 | 1 | 1 | 6 |
| M18 | M |  | 1 | 1 | 4 |
| M2 | M |  |  | 1 | 6 |
| M200 | M | 2 | 1 |  | 11 |
| M201 | M | 1 | 2 |  | 14 |
| M210 | M | 2 | 1 |  | 10 |
| M211 | M | 1 | 2 |  | 10 |
| M220 | M | 1 | 3 |  | 3 |
| M221 | M | 1 | 3 |  | 3 |
| M222 | M | 1 | 3 |  | 3 |
| M223 | M | 1 | 3 |  | 3 |
| M224 | M | 1 | 2 |  | 3 |
| M30 | M | 1 | 1 | 1 | 9 |
| M300 | M |  |  |  | 25 |
| M301 | M |  |  |  | 25 |
| M302 | M |  |  |  | 25 |
| M303 | M |  |  |  | 25 |
| M31 | M | 1 | 2 | 1 | 5 |
| M310 | M |  |  |  | 12 |
| M311 | M |  |  |  | 12 |
| M312 | M |  |  |  | 12 |
| M313 | M |  |  |  | 11 |
| M314 | M |  |  |  | 11 |
| M316 | M |  |  |  | 11 |
| M317 | M |  |  |  | 11 |
| M318 | M |  |  |  | 11 |
| M319 | M |  |  |  | 11 |
| M32 | M | 2 | 3 | 1 | 6 |
| M320 | M |  |  |  | 11 |
| M33 | M | 2 | 3 | 1 | 6 |
| M330 | M |  |  |  | 12 |
| M331 | M |  |  |  | 12 |
| M332 | M |  |  |  | 12 |
| M333 | M |  |  |  | 11 |
| M334 | M |  |  |  | 11 |
| M336 | M |  |  |  | 11 |
| M337 | M |  |  |  | 11 |
| M338 | M |  |  |  | 11 |
| M339 | M |  |  |  | 11 |
| M34 | M | 2 | 5 | 1 | 6 |
| M340 | M |  |  |  | 11 |
| M35 | M | 4 | 2 | 1 | 5 |
| M350 | M |  |  |  | 5 |
| M351 | M |  |  |  | 5 |
| M36 | M |  | 3 | 1 | 6 |
| M37 | M | 2 | 1 | 1 | 6 |
| M38 | M |  | 1 | 1 | 4 |
| M400 | M |  |  |  | 1 |
| M401 | M |  |  |  | 1 |
| M402 | M |  |  |  | 1 |
| M403 | M |  |  |  | 1 |
| M404 | M |  |  |  | 1 |
| M405 | M |  |  |  | 1 |
| M406 | M |  |  |  | 1 |
| M407 | M |  |  |  | 1 |
| M408 | M |  |  |  | 7 |
| M409 | M |  |  |  | 2 |
| M410 | M |  |  |  | 1 |
| M412 | M |  |  |  | 1 |
| M413 | M |  |  |  | 1 |
| M415 | M |  |  |  | 1 |
| M450 | M | 2 | 1 |  | 16 |
| M451 | M | 2 | 1 |  | 16 |
| M452 | M |  |  | 1 | 9 |
| M453 | M | 3 | 11 |  | 1 |
| M460 | M | 1 | 1 |  | 2 |
| M461 | M | 1 | 1 |  | 2 |
| M462 | M | 1 | 1 |  | 2 |
| M463 | M | 1 | 6 |  | 7 |
| M464 | M | 1 | 2 |  | 3 |
| M465 | M | 1 | 1 |  | 2 |
| M466 | M | 1 | 1 |  | 2 |
| M467 | M | 1 | 1 |  | 2 |
| M468 | M | 1 | 1 |  | 2 |
| M469 | M | 1 | 1 |  | 2 |
| M490 | M | 1 | 3 |  | 1 |
| M50 | M | 1 | 1 | 1 | 2 |
| M51 | M | 3 | 2 | 1 | 6 |
| M52 | M |  | 2 | 1 | 4 |
| M520 | M | 1 |  |  | 2 |
| M521 | M | 2 | 1 |  | 8 |
| M522 | M | 2 | 1 |  | 2 |
| M53 | M | 1 | 3 | 1 | 4 |
| M60 | M |  | 1 |  |  |
| M600 | M |  |  |  | 3 |
| M601 | M |  |  |  | 2 |
| M602 | M |  |  |  | 2 |
| M603 | M |  |  |  | 3 |
| M604 | M |  |  |  | 3 |
| M605 | M |  |  |  | 3 |
| M606 | M |  |  |  | 3 |
| M607 | M |  |  |  | 3 |
| M61 | M |  | 1 |  |  |
| M610 | M |  |  |  | 4 |
| M611 | M |  |  |  | 4 |
| M612 | M |  |  |  | 4 |
| M613 | M |  |  |  | 4 |
| M614 | M |  |  |  | 3 |
| M615 | M |  |  |  | 4 |
| M616 | M |  |  |  | 4 |
| M62 | M |  | 1 |  |  |
| M620 | M |  |  |  | 3 |
| M621 | M |  |  |  | 3 |
| M622 | M |  |  |  | 3 |
| M63 | M |  | 1 |  |  |
| M64 | M |  | 1 |  |  |
| M65 | M |  | 2 |  |  |
| M66 | M |  | 2 |  |  |
| M67 | M | 1 | 1 |  | 2 |
| M68 | M |  | 1 |  |  |
| M69 | M |  | 1 |  |  |
| M70 | M |  | 1 |  |  |
| M71 | M |  | 1 |  |  |
| M72 | M |  | 1 |  |  |
| M73 | M |  | 1 |  |  |
| M74 | M |  | 1 |  |  |
| M75 | M |  | 2 |  |  |
| M76 | M |  | 2 |  |  |
| M77 | M |  |  | 1 |  |
| M770 | M |  |  |  | 1 |
| M78 | M |  |  | 1 |  |
| M79 | M |  |  | 1 |  |
| M80 | M |  |  | 1 | 2 |
| M81 | M |  |  |  | 1 |
| M82 | M |  |  |  | 1 |
| M83 | M |  |  |  | 1 |
| M84 | M |  |  |  | 1 |
| M85 | M |  |  |  | 1 |
| M90 | M |  |  | 1 | 2 |
| M91 | M |  |  |  | 1 |
| M92 | M |  |  |  | 1 |
| M93 | M |  |  |  | 1 |
| M94 | M |  |  |  | 1 |
| M95 | M |  |  |  | 1 |
| SM400 | ? |  |  |  | 1 |
| SM401 | ? |  |  |  | 1 |
| SM402 | ? |  |  |  | 1 |
| T0 | T |  |  | 11 | 27 |
| T22 | T |  |  | 1 | 2 |
