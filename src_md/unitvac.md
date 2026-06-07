---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 51
**Blocks:** 2
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | UNIT VAC L1 | 1–25 | LD M13, LD M13, LD M13 ... (+2) | 20 |
| 2 | UNIT VAC L2 | 27–51 | LD M33, LD M33, LD M33 ... (+2) | 20 |

## Block Detail

### Block 1: UNIT VAC L1 (Step 1–25)

**Trigger Condition:**
- LD M13
- LD M13
- LD M13
- LD T15
- LD M13

**Actions:**
- OUT M60
- OUT M61
- OUT T2
- AND T2
- LDD<= D30
- OUT M102
- AND T2
- LDD> D30
- OUT T15
- SET M109
- SET M311
- RST M13
- RST M60
- RST M61
- ANI M80
- SET M109
- SET M311
- RST M13
- RST M60
- RST M61

### Block 2: UNIT VAC L2 (Step 27–51)

**Trigger Condition:**
- LD M33
- LD M33
- LD M33
- LD T16
- LD M33

**Actions:**
- OUT M70
- OUT M71
- OUT T8
- AND T8
- LDD<= D62
- OUT M118
- AND T8
- LDD> D62
- OUT T16
- SET M125
- SET M331
- RST M33
- RST M70
- RST M71
- ANI M90
- SET M125
- SET M331
- RST M33
- RST M70
- RST M71

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D30 | D |  |  |  | 2 |
| D62 | D |  |  |  | 2 |
| M102 | M |  |  | 1 |  |
| M109 | M | 2 |  |  |  |
| M118 | M |  |  | 1 |  |
| M125 | M | 2 |  |  |  |
| M13 | M |  | 2 |  | 4 |
| M311 | M | 2 |  |  |  |
| M33 | M |  | 2 |  | 4 |
| M331 | M | 2 |  |  |  |
| M60 | M |  | 2 | 1 |  |
| M61 | M |  | 2 | 1 |  |
| M70 | M |  | 2 | 1 |  |
| M71 | M |  | 2 | 1 |  |
| M80 | M |  |  |  | 1 |
| M90 | M |  |  |  | 1 |
| T15 | T |  |  | 1 | 1 |
| T16 | T |  |  | 1 | 1 |
| T2 | T |  |  | 1 | 2 |
| T8 | T |  |  | 1 | 2 |
