---
# unitvac — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 79
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | UNIT VACUUM (Line 0) | 1–39 | LD M19, LD M19, LD M19 ... (+6) | 30 |
| 2 | UNIT VACUUM (Line 1) | 41–79 | LD M35, LD M35, LD M35 ... (+6) | 30 |

## Block Detail

### Block 1: UNIT VACUUM (Line 0) (Step 1–39)

**Trigger Condition:**
- LD M19
- LD M19
- LD M19
- LD M19
- LD L114
- LD L115
- LD M19
- LD M19
- LD T7

**Actions:**
- OUT T1
- SET M49
- SET M50
- ANI L81
- SET M16
- RST M19
- RST M49
- RST M50
- ANI M772
- ANI M773
- ORB 
- ANB 
- SET L19
- RST M49
- RST M50
- RST M19
- AND T1
- ANDD<= D160
- RST M49
- RST M50
- SET L18
- RST M19
- AND T1
- ANDD> D160
- OUT T7
- SET L19
- SET L67
- RST M49
- RST M50
- RST M19

### Block 2: UNIT VACUUM (Line 1) (Step 41–79)

**Trigger Condition:**
- LD M35
- LD M35
- LD M35
- LD M35
- LD L114
- LD L115
- LD M35
- LD M35
- LD T17

**Actions:**
- OUT T9
- SET M65
- SET M66
- ANI L97
- SET M32
- RST M35
- RST M65
- RST M66
- ANI M788
- ANI M789
- ORB 
- ANB 
- SET L35
- RST M65
- RST M66
- RST M35
- AND T9
- ANDD<= D172
- RST M65
- RST M66
- SET L34
- RST M35
- AND T9
- ANDD> D172
- OUT T17
- SET L35
- SET L67
- RST M65
- RST M66
- RST M35

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 2 |
| D172 | D |  |  |  | 2 |
| L114 | L |  |  |  | 2 |
| L115 | L |  |  |  | 2 |
| L18 | L | 1 |  |  |  |
| L19 | L | 2 |  |  |  |
| L34 | L | 1 |  |  |  |
| L35 | L | 2 |  |  |  |
| L67 | L | 2 |  |  |  |
| L81 | L |  |  |  | 1 |
| L97 | L |  |  |  | 1 |
| M16 | M | 1 |  |  |  |
| M19 | M |  | 4 |  | 6 |
| M32 | M | 1 |  |  |  |
| M35 | M |  | 4 |  | 6 |
| M49 | M | 1 | 4 |  |  |
| M50 | M | 1 | 4 |  |  |
| M65 | M | 1 | 4 |  |  |
| M66 | M | 1 | 4 |  |  |
| M772 | M |  |  |  | 1 |
| M773 | M |  |  |  | 1 |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| T1 | T |  |  | 1 | 2 |
| T17 | T |  |  | 1 | 1 |
| T7 | T |  |  | 1 | 1 |
| T9 | T |  |  | 1 | 2 |
