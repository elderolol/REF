---
# gunvac — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 71
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | GUN VACUUM (Line 0) | 1–35 | LD M18, LD M18, LD M18 ... (+6) | 26 |
| 2 | GUN VACUUM (Line 1) | 37–71 | LD M34, LD M34, LD M34 ... (+6) | 26 |

## Block Detail

### Block 1: GUN VACUUM (Line 0) (Step 1–35)

**Trigger Condition:**
- LD M18
- LD M18
- LD M18
- LD M18
- LD L114
- LD L115
- LD M18
- LD M18
- LD T7

**Actions:**
- OUT T0
- OUT M49
- ANI L81
- SET M16
- RST M18
- RST M49
- ANI M772
- ANI M773
- ORB 
- ANB 
- SET L17
- RST M49
- RST M18
- AND T0
- ANDD<= D160
- RST M49
- SET L16
- RST M18
- AND T0
- ANDD> D160
- OUT T7
- SET L17
- SET L66
- SET M76
- RST M49
- RST M18

### Block 2: GUN VACUUM (Line 1) (Step 37–71)

**Trigger Condition:**
- LD M34
- LD M34
- LD M34
- LD M34
- LD L114
- LD L115
- LD M34
- LD M34
- LD T17

**Actions:**
- OUT T8
- OUT M65
- ANI L97
- SET M32
- RST M34
- RST M65
- ANI M788
- ANI M789
- ORB 
- ANB 
- SET L33
- RST M65
- RST M34
- AND T8
- ANDD<= D172
- RST M65
- SET L32
- RST M34
- AND T8
- ANDD> D172
- OUT T17
- SET L33
- SET L66
- SET M76
- RST M65
- RST M34

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 2 |
| D172 | D |  |  |  | 2 |
| L114 | L |  |  |  | 2 |
| L115 | L |  |  |  | 2 |
| L16 | L | 1 |  |  |  |
| L17 | L | 2 |  |  |  |
| L32 | L | 1 |  |  |  |
| L33 | L | 2 |  |  |  |
| L66 | L | 2 |  |  |  |
| L81 | L |  |  |  | 1 |
| L97 | L |  |  |  | 1 |
| M16 | M | 1 |  |  |  |
| M18 | M |  | 4 |  | 6 |
| M32 | M | 1 |  |  |  |
| M34 | M |  | 4 |  | 6 |
| M49 | M |  | 4 | 1 |  |
| M65 | M |  | 4 | 1 |  |
| M76 | M | 2 |  |  |  |
| M772 | M |  |  |  | 1 |
| M773 | M |  |  |  | 1 |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| T0 | T |  |  | 1 | 2 |
| T17 | T |  |  | 1 | 1 |
| T7 | T |  |  | 1 | 1 |
| T8 | T |  |  | 1 | 2 |
