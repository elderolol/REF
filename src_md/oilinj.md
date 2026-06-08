---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 130
**Blocks:** 2
**Generated:** 2026-06-08
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | OIL FAST | 1–57 | LD M51, LD M51, LD M51 ... (+9) | 45 |
| 2 | OIL BASE | 59–130 | LD M52, LD M52, LD M52 ... (+14) | 55 |

## Block Detail

### Block 1: OIL FAST (Step 1–57)

**Trigger Condition:**
- LD M51
- LD M51
- LD M51
- LD M51
- LD M51
- LD M210
- LD M211
- LD M51
- LD M210
- LD M211
- LD M51
- LD M51

**Actions:**
- AND M210
- OUT M65
- OUT M66
- AND M211
- OUT M75
- OUT M76
- SET M96
- SET M97
- OUT T13
- LDD>= D180
- LDD>= D180
- ORB 
- ANB 
- AND M210
- RST M65
- SET M145
- SET M52
- LDD>= D180
- LDD>= D180
- ORB 
- ANB 
- AND M211
- RST M75
- SET M145
- SET M52
- AND T13
- AND M210
- RST M65
- RST M66
- SET M350
- SET M145
- SET M53
- RST M51
- RST M96
- RST M97
- AND T13
- AND M211
- RST M75
- RST M76
- SET M350
- SET M145
- SET M53
- RST M51
- RST M96
- RST M97

### Block 2: OIL BASE (Step 59–130)

**Trigger Condition:**
- LD M52
- LD M52
- LD M52
- LD M52
- LD M52
- LD M210
- LD M211
- LD M52
- LD M210
- LD M211
- LD M52
- LD M52
- LD M52
- LD M210
- LD M211
- LD M53
- LD M53

**Actions:**
- AND M210
- OUT M66
- AND M211
- OUT M76
- SET M96
- SET M97
- OUT T14
- LDD>= D180
- LDD>= D180
- ORB 
- ANB 
- AND M210
- RST M66
- SET M146
- SET M53
- RST M96
- RST M97
- LDD>= D180
- LDD>= D180
- ORB 
- ANB 
- AND M211
- RST M76
- SET M146
- SET M53
- RST M96
- RST M97
- AND T14
- AND M210
- RST M66
- SET M350
- SET M146
- SET M53
- RST M52
- RST M96
- RST M97
- AND T14
- AND M211
- RST M76
- SET M350
- SET M146
- SET M53
- RST M52
- RST M96
- RST M97
- LDD> D180
- LDD> D180
- ORB 
- SET M351
- AND M210
- LDD< D180
- SET M351
- AND M211
- LDD< D180
- SET M351

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D180 | D |  |  |  | 12 |
| M145 | M | 4 |  |  |  |
| M146 | M | 4 |  |  |  |
| M210 | M |  |  |  | 12 |
| M211 | M |  |  |  | 12 |
| M350 | M | 4 |  |  |  |
| M351 | M | 3 |  |  |  |
| M51 | M |  | 2 |  | 8 |
| M52 | M | 2 | 2 |  | 9 |
| M53 | M | 6 |  |  | 2 |
| M65 | M |  | 2 | 1 |  |
| M66 | M |  | 3 | 2 |  |
| M75 | M |  | 2 | 1 |  |
| M76 | M |  | 3 | 2 |  |
| M96 | M | 2 | 6 |  |  |
| M97 | M | 2 | 6 |  |  |
| T13 | T |  |  | 1 | 2 |
| T14 | T |  |  | 1 | 2 |
