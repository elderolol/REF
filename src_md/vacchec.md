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
| 1 | VAC CHECK L1 | 1–25 | LD M14, LD M14, LD M14 ... (+2) | 20 |
| 2 | VAC CHECK L2 | 27–51 | LD M34, LD M34, LD M34 ... (+2) | 20 |

## Block Detail

### Block 1: VAC CHECK L1 (Step 1–25)

**Trigger Condition:**
- LD M14
- LD M14
- LD M14
- LD M14
- LD M14

**Actions:**
- OUT M60
- OUT M61
- OUT M68
- DMOV D30
- OUT T3
- D- D600
- AND T3
- LDD<= D602
- OUT M103
- RST M60
- RST M61
- RST M68
- AND T3
- LDD> D602
- SET M109
- SET M312
- RST M14
- RST M60
- RST M61
- RST M68

### Block 2: VAC CHECK L2 (Step 27–51)

**Trigger Condition:**
- LD M34
- LD M34
- LD M34
- LD M34
- LD M34

**Actions:**
- OUT M70
- OUT M71
- OUT M68
- DMOV D62
- OUT T9
- D- D610
- AND T9
- LDD<= D612
- OUT M119
- RST M70
- RST M71
- RST M68
- AND T9
- LDD> D612
- SET M125
- SET M332
- RST M34
- RST M70
- RST M71
- RST M68

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D30 | D |  |  |  | 1 |
| D600 | D |  |  |  | 1 |
| D602 | D |  |  |  | 2 |
| D610 | D |  |  |  | 1 |
| D612 | D |  |  |  | 2 |
| D62 | D |  |  |  | 1 |
| M103 | M |  |  | 1 |  |
| M109 | M | 1 |  |  |  |
| M119 | M |  |  | 1 |  |
| M125 | M | 1 |  |  |  |
| M14 | M |  | 1 |  | 5 |
| M312 | M | 1 |  |  |  |
| M332 | M | 1 |  |  |  |
| M34 | M |  | 1 |  | 5 |
| M60 | M |  | 2 | 1 |  |
| M61 | M |  | 2 | 1 |  |
| M68 | M |  | 4 | 2 |  |
| M70 | M |  | 2 | 1 |  |
| M71 | M |  | 2 | 1 |  |
| T3 | T |  |  | 1 | 2 |
| T9 | T |  |  | 1 | 2 |
