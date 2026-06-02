---
# unitvac — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 80
**Blocks:** 2
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | UNIT VACUUM (Line 0) | 0–39 | LD M19, LD M19, LD M19 | 30 |
| 2 | UNIT VACUUM (Line 1) | 40–80 | LD M35, LD M35, LD M35 | 31 |

## Block Detail

### Block 1: UNIT VACUUM (Line 0) (Step 0–39)

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

### Block 2: UNIT VACUUM (Line 1) (Step 40–80)

**Trigger Condition:**
- LD M35
- LD M35
- LD M35
- LD M35
- LD L114
- LD L115
- LD M35
- LD M35
- LD T7

**Actions:**
- OUT T1
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
- AND T1
- ANDD<= D172
- RST M65
- RST M66
- SET L34
- RST M35
- AND T1
- ANDD> D172
- OUT T7
- SET L35
- SET L67
- RST M65
- RST M66
- RST M35
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D160 | D | — | — | — | 25, 32 |  |
| D172 | D | — | — | — | 65, 72 |  |
| L114 | L | — | — | — | 13, 53 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L115 | L | — | — | — | 15, 55 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L18 | L | 28 | — | — | — | NO_RST, LATCH_DEVICE |
| L19 | L | 19, 35 | — | — | — | NO_RST, LATCH_DEVICE |
| L34 | L | 68 | — | — | — | NO_RST, LATCH_DEVICE |
| L35 | L | 59, 75 | — | — | — | NO_RST, LATCH_DEVICE |
| L67 | L | 36, 76 | — | — | — | NO_RST, LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L81 | L | — | — | — | 7 | LATCH_DEVICE |
| L97 | L | — | — | — | 47 | LATCH_DEVICE |
| M16 | M | 8 | — | — | — | NO_RST |
| M19 | M | — | 9, 22, 29, 39 | — | 1, 3, 6, 12, 23, 30 | NO_SET |
| M32 | M | 48 | — | — | — | NO_RST |
| M35 | M | — | 49, 62, 69, 79 | — | 41, 43, 46, 52, 63, 70 | NO_SET |
| M49 | M | 4 | 10, 20, 26, 37 | — | — |  |
| M50 | M | 5 | 11, 21, 27, 38 | — | — |  |
| M65 | M | 44 | 50, 60, 66, 77 | — | — |  |
| M66 | M | 45 | 51, 61, 67, 78 | — | — |  |
| M772 | M | — | — | — | 14 |  |
| M773 | M | — | — | — | 16 |  |
| M788 | M | — | — | — | 54 |  |
| M789 | M | — | — | — | 56 |  |
| T1 | T | — | — | 2, 42 | 24, 31, 64, 71 | DOUBLE_COIL_CANDIDATE |
| T7 | T | — | — | 33, 73 | 34, 74 | DOUBLE_COIL_CANDIDATE |
