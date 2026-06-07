---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 160
**Blocks:** 7
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L1 CYCLE DONE SPC | 1–16 | LD M107, LD M107, LD M107 ... (+4) | 9 |
| 2 | L2 CYCLE DONE SPC | 18–29 | LD M123, LD M123, LD M123 ... (+2) | 7 |
| 3 | VAC SPC LOGGING | 31–78 | LD M12, LD M470, LD M14 ... (+15) | 30 |
| 4 | VAC SPC CLEAR | 80–83 | LD M11, LD M31 | 2 |
| 5 | PC COMM STATUS | 85–150 | LD M10, LD M11, LD M12 ... (+29) | 34 |
| 6 | INJECTION COUNT RESET | 152–155 | LD M414, LD M416 | 2 |
| 7 | REFRIGERANT USAGE RESET | 157–160 | LD M417, LD M418 | 2 |

## Block Detail

### Block 1: L1 CYCLE DONE SPC (Step 1–16)

**Trigger Condition:**
- LD M107
- LD M107
- LD M107
- LD M107
- LD M107
- LD M107
- LD M123

**Actions:**
- D+ D300
- D+ D202
- D+ D204
- DMOV D130
- DMOV D12
- LDD>= D300
- SET M302
- D+ D240
- D+ D242

### Block 2: L2 CYCLE DONE SPC (Step 18–29)

**Trigger Condition:**
- LD M123
- LD M123
- LD M123
- LD M123
- LD M123

**Actions:**
- D+ D220
- D+ D222
- D+ D224
- DMOV D160
- DMOV D44
- LDD>= D220
- SET M302

### Block 3: VAC SPC LOGGING (Step 31–78)

**Trigger Condition:**
- LD M12
- LD M470
- LD M14
- LD M480
- LD M481
- LD M450
- LD M452
- LD T18
- LD T18
- LD M32
- LD M471
- LD M34
- LD M482
- LD M483
- LD M451
- LD M452
- LD T19
- LD T19

**Actions:**
- AND M201
- SET M470
- OUTH T18
- PLS M480
- SET M481
- OUT T20
- AND T20
- RST M470
- RST M481
- RST M470
- RST M481
- RST M470
- RST M481
- BMOV D7020
- DMOV D30
- AND M201
- SET M471
- OUTH T19
- PLS M482
- SET M483
- OUT T21
- AND T21
- RST M471
- RST M483
- RST M471
- RST M483
- RST M471
- RST M483
- BMOV D8020
- DMOV D62

### Block 4: VAC SPC CLEAR (Step 80–83)

**Trigger Condition:**
- LD M11
- LD M31

**Actions:**
- FMOV K0
- FMOV K0

### Block 5: PC COMM STATUS (Step 85–150)

**Trigger Condition:**
- LD M10
- LD M11
- LD M12
- LD M13
- LD M14
- LD M15
- LD M17
- LD M18
- LD M30
- LD M31
- LD M32
- LD M33
- LD M34
- LD M35
- LD M37
- LD M38
- LD M50
- LD M51
- LD M52
- LD M53
- LD M520
- LDI M520
- LD M210
- LD M211
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- MOV K0
- MOV K1
- MOV K2
- MOV K3
- MOV K4
- OR M16
- MOV K5
- MOV K6
- MOV K7
- MOV K0
- MOV K1
- MOV K2
- MOV K3
- MOV K4
- OR M36
- MOV K5
- MOV K6
- MOV K7
- MOV K0
- MOV K1
- MOV K2
- MOV K3
- MOV K1
- MOV K2
- MOV K1
- MOV K2
- DMOV D30
- DMOV D62
- MOV D0
- MOV D32
- DMOV D12
- DMOV D44
- DMOV D150
- DMOV D170

### Block 6: INJECTION COUNT RESET (Step 152–155)

**Trigger Condition:**
- LD M414
- LD M416

**Actions:**
- MOV K0
- MOV K0

### Block 7: REFRIGERANT USAGE RESET (Step 157–160)

**Trigger Condition:**
- LD M417
- LD M418

**Actions:**
- DMOV K0
- DMOV K0

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D0 | D |  |  |  | 1 |
| D12 | D |  |  |  | 2 |
| D130 | D |  |  |  | 1 |
| D150 | D |  |  |  | 1 |
| D160 | D |  |  |  | 1 |
| D170 | D |  |  |  | 1 |
| D202 | D |  |  |  | 1 |
| D204 | D |  |  |  | 1 |
| D220 | D |  |  |  | 2 |
| D222 | D |  |  |  | 1 |
| D224 | D |  |  |  | 1 |
| D240 | D |  |  |  | 1 |
| D242 | D |  |  |  | 1 |
| D30 | D |  |  |  | 2 |
| D300 | D |  |  |  | 2 |
| D32 | D |  |  |  | 1 |
| D44 | D |  |  |  | 2 |
| D62 | D |  |  |  | 2 |
| D7020 | D |  |  |  | 1 |
| D8020 | D |  |  |  | 1 |
| K0 | K |  |  |  | 9 |
| K1 | K |  |  |  | 5 |
| K2 | K |  |  |  | 5 |
| K3 | K |  |  |  | 3 |
| K4 | K |  |  |  | 2 |
| K5 | K |  |  |  | 2 |
| K6 | K |  |  |  | 2 |
| K7 | K |  |  |  | 2 |
| M0 | M |  |  |  | 8 |
| M10 | M |  |  |  | 1 |
| M107 | M |  |  |  | 6 |
| M11 | M |  |  |  | 2 |
| M12 | M |  |  |  | 2 |
| M123 | M |  |  |  | 6 |
| M13 | M |  |  |  | 1 |
| M14 | M |  |  |  | 2 |
| M15 | M |  |  |  | 1 |
| M16 | M |  |  |  | 1 |
| M17 | M |  |  |  | 1 |
| M18 | M |  |  |  | 1 |
| M201 | M |  |  |  | 2 |
| M210 | M |  |  |  | 1 |
| M211 | M |  |  |  | 1 |
| M30 | M |  |  |  | 1 |
| M302 | M | 2 |  |  |  |
| M31 | M |  |  |  | 2 |
| M32 | M |  |  |  | 2 |
| M33 | M |  |  |  | 1 |
| M34 | M |  |  |  | 2 |
| M35 | M |  |  |  | 1 |
| M36 | M |  |  |  | 1 |
| M37 | M |  |  |  | 1 |
| M38 | M |  |  |  | 1 |
| M414 | M |  |  |  | 1 |
| M416 | M |  |  |  | 1 |
| M417 | M |  |  |  | 1 |
| M418 | M |  |  |  | 1 |
| M450 | M |  |  |  | 1 |
| M451 | M |  |  |  | 1 |
| M452 | M |  |  |  | 2 |
| M470 | M | 1 | 3 |  | 1 |
| M471 | M | 1 | 3 |  | 1 |
| M480 | M |  |  |  | 2 |
| M481 | M | 1 | 3 |  | 1 |
| M482 | M |  |  |  | 2 |
| M483 | M | 1 | 3 |  | 1 |
| M50 | M |  |  |  | 1 |
| M51 | M |  |  |  | 1 |
| M52 | M |  |  |  | 1 |
| M520 | M |  |  |  | 2 |
| M53 | M |  |  |  | 1 |
| T18 | T |  |  |  | 3 |
| T19 | T |  |  |  | 3 |
| T20 | T |  |  | 1 | 1 |
| T21 | T |  |  | 1 | 1 |
