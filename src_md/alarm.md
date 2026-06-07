---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 159
**Blocks:** 6
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | SHARED ALARMS | 1–17 | LDI M770, LDI M771, LDI M772 | 14 |
| 2 | L1 ALARMS | 19–65 | LD M12, LD M13, LD M109 ... (+4) | 40 |
| 3 | L2 ALARMS | 67–113 | LD M32, LD M33, LD M125 ... (+4) | 40 |
| 4 | L3 OIL ALARMS | 115–123 | LD M51, LD M351 | 7 |
| 5 | BUZZER | 125–156 | LD M300, LD M411, LD M411 | 29 |
| 6 | ALARM RESET | 158–159 | LD M410 | 1 |

## Block Detail

### Block 1: SHARED ALARMS (Step 1–17)

**Trigger Condition:**
- LDI M770
- LDI M771
- LDI M772

**Actions:**
- OR M300
- ANI M410
- OUT M300
- AND M522
- OR M301
- ANI M410
- OUT M301
- LDD>= D300
- OR M302
- ANI M410
- OUT M302
- OR M303
- ANI M410
- OUT M303

### Block 2: L1 ALARMS (Step 19–65)

**Trigger Condition:**
- LD M12
- LD M13
- LD M109
- LD M110
- LD M314
- LD M11
- LD M11

**Actions:**
- AND T1
- OR M310
- ANI M410
- OUT M310
- AND T2
- OR M311
- ANI M410
- OUT M311
- OR M312
- ANI M410
- OUT M312
- OR M313
- ANI M410
- OUT M313
- OR M314
- ANI M410
- OUT M314
- LDD>= D26
- OR M316
- ANI M410
- OUT M316
- LDD<= D26
- OR M317
- ANI M410
- OUT M317
- LDD< D28
- OR> D28
- LDD> D28
- ORB 
- OR M318
- ANI M410
- OUT M318
- AND= D0
- OR M319
- ANI M410
- OUT M319
- LDD= D12
- OR M320
- ANI M410
- OUT M320

### Block 3: L2 ALARMS (Step 67–113)

**Trigger Condition:**
- LD M32
- LD M33
- LD M125
- LD M126
- LD M334
- LD M31
- LD M31

**Actions:**
- AND T7
- OR M330
- ANI M410
- OUT M330
- AND T8
- OR M331
- ANI M410
- OUT M331
- OR M332
- ANI M410
- OUT M332
- OR M333
- ANI M410
- OUT M333
- OR M334
- ANI M410
- OUT M334
- LDD>= D58
- OR M336
- ANI M410
- OUT M336
- LDD<= D58
- OR M337
- ANI M410
- OUT M337
- LDD< D60
- OR> D60
- LDD> D60
- ORB 
- OR M338
- ANI M410
- OUT M338
- AND= D32
- OR M339
- ANI M410
- OUT M339
- LDD= D44
- OR M340
- ANI M410
- OUT M340

### Block 4: L3 OIL ALARMS (Step 115–123)

**Trigger Condition:**
- LD M51
- LD M351

**Actions:**
- AND T13
- OR M350
- ANI M410
- OUT M350
- OR M351
- ANI M410
- OUT M351

### Block 5: BUZZER (Step 125–156)

**Trigger Condition:**
- LD M300
- LD M411
- LD M411

**Actions:**
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
- ANI M500
- OUT M69
- SET M500
- RST M69

### Block 6: ALARM RESET (Step 158–159)

**Trigger Condition:**
- LD M410

**Actions:**
- RST M500

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D0 | D |  |  |  | 1 |
| D12 | D |  |  |  | 1 |
| D26 | D |  |  |  | 2 |
| D28 | D |  |  |  | 3 |
| D300 | D |  |  |  | 1 |
| D32 | D |  |  |  | 1 |
| D44 | D |  |  |  | 1 |
| D58 | D |  |  |  | 2 |
| D60 | D |  |  |  | 3 |
| M109 | M |  |  |  | 1 |
| M11 | M |  |  |  | 2 |
| M110 | M |  |  |  | 1 |
| M12 | M |  |  |  | 1 |
| M125 | M |  |  |  | 1 |
| M126 | M |  |  |  | 1 |
| M13 | M |  |  |  | 1 |
| M300 | M |  |  | 1 | 2 |
| M301 | M |  |  | 1 | 2 |
| M302 | M |  |  | 1 | 2 |
| M303 | M |  |  | 1 | 2 |
| M31 | M |  |  |  | 2 |
| M310 | M |  |  | 1 | 2 |
| M311 | M |  |  | 1 | 2 |
| M312 | M |  |  | 1 | 2 |
| M313 | M |  |  | 1 | 2 |
| M314 | M |  |  | 1 | 3 |
| M316 | M |  |  | 1 | 2 |
| M317 | M |  |  | 1 | 2 |
| M318 | M |  |  | 1 | 2 |
| M319 | M |  |  | 1 | 2 |
| M32 | M |  |  |  | 1 |
| M320 | M |  |  | 1 | 2 |
| M33 | M |  |  |  | 1 |
| M330 | M |  |  | 1 | 2 |
| M331 | M |  |  | 1 | 2 |
| M332 | M |  |  | 1 | 2 |
| M333 | M |  |  | 1 | 2 |
| M334 | M |  |  | 1 | 3 |
| M336 | M |  |  | 1 | 2 |
| M337 | M |  |  | 1 | 2 |
| M338 | M |  |  | 1 | 2 |
| M339 | M |  |  | 1 | 2 |
| M340 | M |  |  | 1 | 2 |
| M350 | M |  |  | 1 | 2 |
| M351 | M |  |  | 1 | 3 |
| M410 | M |  |  |  | 27 |
| M411 | M |  |  |  | 2 |
| M500 | M | 1 | 1 |  | 1 |
| M51 | M |  |  |  | 1 |
| M522 | M |  |  |  | 1 |
| M69 | M |  | 1 | 1 |  |
| M770 | M |  |  |  | 1 |
| M771 | M |  |  |  | 1 |
| M772 | M |  |  |  | 1 |
| T1 | T |  |  |  | 1 |
| T13 | T |  |  |  | 1 |
| T2 | T |  |  |  | 1 |
| T7 | T |  |  |  | 1 |
| T8 | T |  |  |  | 1 |
