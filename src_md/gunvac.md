---
# gunvac — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 72
**Blocks:** 2
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | GUN VACUUM (Line 0) | 0–35 | LD M18, LD M18, LD M18 | 26 |
| 2 | GUN VACUUM (Line 1) | 36–72 | LD M34, LD M34, LD M34 | 27 |

## Block Detail

### Block 1: GUN VACUUM (Line 0) (Step 0–35)

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

### Block 2: GUN VACUUM (Line 1) (Step 36–72)

**Trigger Condition:**
- LD M34
- LD M34
- LD M34
- LD M34
- LD L114
- LD L115
- LD M34
- LD M34
- LD T7

**Actions:**
- OUT T0
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
- AND T0
- ANDD<= D172
- RST M65
- SET L32
- RST M34
- AND T0
- ANDD> D172
- OUT T7
- SET L33
- SET L66
- SET M76
- RST M65
- RST M34
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D160 | D | — | — | — | 22, 28 |  |
| D172 | D | — | — | — | 58, 64 |  |
| L114 | L | — | — | — | 11, 47 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L115 | L | — | — | — | 13, 49 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L16 | L | 24 | — | — | — | NO_RST, LATCH_DEVICE |
| L17 | L | 17, 31 | — | — | — | NO_RST, LATCH_DEVICE |
| L32 | L | 60 | — | — | — | NO_RST, LATCH_DEVICE |
| L33 | L | 53, 67 | — | — | — | NO_RST, LATCH_DEVICE |
| L66 | L | 32, 68 | — | — | — | NO_RST, LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L81 | L | — | — | — | 6 | LATCH_DEVICE |
| L97 | L | — | — | — | 42 | LATCH_DEVICE |
| M16 | M | 7 | — | — | — | NO_RST |
| M18 | M | — | 8, 19, 25, 35 | — | 1, 3, 5, 10, 20, 26 | NO_SET |
| M32 | M | 43 | — | — | — | NO_RST |
| M34 | M | — | 44, 55, 61, 71 | — | 37, 39, 41, 46, 56, 62 | NO_SET |
| M49 | M | — | 9, 18, 23, 34 | 4 | — |  |
| M65 | M | — | 45, 54, 59, 70 | 40 | — |  |
| M76 | M | 33, 69 | — | — | — | NO_RST, DOUBLE_COIL_CANDIDATE |
| M772 | M | — | — | — | 12 |  |
| M773 | M | — | — | — | 14 |  |
| M788 | M | — | — | — | 48 |  |
| M789 | M | — | — | — | 50 |  |
| T0 | T | — | — | 2, 38 | 21, 27, 57, 63 | DOUBLE_COIL_CANDIDATE |
| T7 | T | — | — | 29, 65 | 30, 66 | DOUBLE_COIL_CANDIDATE |
