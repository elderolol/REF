---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 101
**Blocks:** 6
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L1 REFRIG FAST | 1–18 | LD M15, LD M15, LD M15 ... (+1) | 14 |
| 2 | L1 REFRIG BASE | 20–41 | LD M16, LD M16, LD M16 ... (+3) | 16 |
| 3 | L1 EXHAUST | 43–50 | LD M17, LD M17, LD M17 | 5 |
| 4 | L2 REFRIG FAST | 52–69 | LD M35, LD M35, LD M35 ... (+1) | 14 |
| 5 | L2 REFRIG BASE | 71–92 | LD M36, LD M36, LD M36 ... (+3) | 16 |
| 6 | L2 EXHAUST | 94–101 | LD M37, LD M37, LD M37 | 5 |

## Block Detail

### Block 1: L1 REFRIG FAST (Step 1–18)

**Trigger Condition:**
- LD M15
- LD M15
- LD M15
- LD M15

**Actions:**
- OUT M62
- OUT M63
- OUT T4
- LDD>= D150
- RST M62
- SET M104
- SET M16
- AND T4
- RST M62
- RST M63
- SET M313
- SET M110
- SET M17
- RST M15

### Block 2: L1 REFRIG BASE (Step 20–41)

**Trigger Condition:**
- LD M16
- LD M16
- LD M16
- LD M16
- LD M16
- LD M17

**Actions:**
- OUT M63
- OUT T5
- LDD>= D150
- RST M63
- SET M105
- SET M17
- AND T5
- RST M63
- SET M313
- SET M110
- SET M17
- RST M16
- LDD> D150
- SET M314
- LDD< D150
- SET M314

### Block 3: L1 EXHAUST (Step 43–50)

**Trigger Condition:**
- LD M17
- LD M17
- LD M17

**Actions:**
- OUT M64
- OUT T6
- AND T6
- RST M64
- SET M106

### Block 4: L2 REFRIG FAST (Step 52–69)

**Trigger Condition:**
- LD M35
- LD M35
- LD M35
- LD M35

**Actions:**
- OUT M72
- OUT M73
- OUT T10
- LDD>= D170
- RST M72
- SET M120
- SET M36
- AND T10
- RST M72
- RST M73
- SET M333
- SET M126
- SET M37
- RST M35

### Block 5: L2 REFRIG BASE (Step 71–92)

**Trigger Condition:**
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M37

**Actions:**
- OUT M73
- OUT T11
- LDD>= D170
- RST M73
- SET M121
- SET M37
- AND T11
- RST M73
- SET M333
- SET M126
- SET M37
- RST M36
- LDD> D170
- SET M334
- LDD< D170
- SET M334

### Block 6: L2 EXHAUST (Step 94–101)

**Trigger Condition:**
- LD M37
- LD M37
- LD M37

**Actions:**
- OUT M74
- OUT T12
- AND T12
- RST M74
- SET M122

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D150 | D |  |  |  | 4 |
| D170 | D |  |  |  | 4 |
| M104 | M | 1 |  |  |  |
| M105 | M | 1 |  |  |  |
| M106 | M | 1 |  |  |  |
| M110 | M | 2 |  |  |  |
| M120 | M | 1 |  |  |  |
| M121 | M | 1 |  |  |  |
| M122 | M | 1 |  |  |  |
| M126 | M | 2 |  |  |  |
| M15 | M |  | 1 |  | 4 |
| M16 | M | 1 | 1 |  | 5 |
| M17 | M | 3 |  |  | 4 |
| M313 | M | 2 |  |  |  |
| M314 | M | 2 |  |  |  |
| M333 | M | 2 |  |  |  |
| M334 | M | 2 |  |  |  |
| M35 | M |  | 1 |  | 4 |
| M36 | M | 1 | 1 |  | 5 |
| M37 | M | 3 |  |  | 4 |
| M62 | M |  | 2 | 1 |  |
| M63 | M |  | 3 | 2 |  |
| M64 | M |  | 1 | 1 |  |
| M72 | M |  | 2 | 1 |  |
| M73 | M |  | 3 | 2 |  |
| M74 | M |  | 1 | 1 |  |
| T10 | T |  |  | 1 | 1 |
| T11 | T |  |  | 1 | 1 |
| T12 | T |  |  | 1 | 1 |
| T4 | T |  |  | 1 | 1 |
| T5 | T |  |  | 1 | 1 |
| T6 | T |  |  | 1 | 1 |
