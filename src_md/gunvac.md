---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 85
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | GUN VACUUM (Line 0) | 1–42 | LD M18, LD T0, LD M18 ... (+8) | 31 |
| 2 | GUN VACUUM (Line 1) | 44–85 | LD M34, LD T8, LD M34 ... (+8) | 31 |

## Block Detail

### Block 1: GUN VACUUM (Line 0) (Step 1–42)

**Trigger Condition:**
- LD M18
- LD T0
- LD M18
- LD M18
- LD M18
- LD M914
- LD M915
- LD M18
- LD M18
- LD M18
- LD T7

**Actions:**
- OUT T0
- AND<= D160
- OUT M100
- ANI M881
- ANI T7
- ANI M100
- OUT M49
- ANI M881
- SET M16
- RST M18
- RST M49
- ANI M772
- ANI M773
- ORB 
- ANB 
- SET M817
- AND T0
- AND<= D160
- OUT M816
- AND T0
- AND<= D160
- RST M18
- RST M49
- AND T0
- AND> D160
- OUT T7
- SET M817
- OUT M866
- SET M76
- RST M18
- RST M49

### Block 2: GUN VACUUM (Line 1) (Step 44–85)

**Trigger Condition:**
- LD M34
- LD T8
- LD M34
- LD M34
- LD M34
- LD M914
- LD M915
- LD M34
- LD M34
- LD M34
- LD T17

**Actions:**
- OUT T8
- AND<= D172
- OUT M101
- ANI M897
- ANI T17
- ANI M101
- OUT M65
- ANI M897
- SET M32
- RST M34
- RST M65
- ANI M788
- ANI M789
- ORB 
- ANB 
- SET M833
- AND T8
- AND<= D172
- OUT M832
- AND T8
- AND<= D172
- RST M34
- RST M65
- AND T8
- AND> D172
- OUT T17
- SET M833
- OUT M866
- SET M76
- RST M34
- RST M65

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 4 |
| D172 | D |  |  |  | 4 |
| M100 | M |  |  | 1 | 1 |
| M101 | M |  |  | 1 | 1 |
| M16 | M | 1 |  |  |  |
| M18 | M |  | 3 |  | 7 |
| M32 | M | 1 |  |  |  |
| M34 | M |  | 3 |  | 7 |
| M49 | M |  | 3 | 1 |  |
| M65 | M |  | 3 | 1 |  |
| M76 | M | 2 |  |  |  |
| M772 | M |  |  |  | 1 |
| M773 | M |  |  |  | 1 |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| M816 | M |  |  | 1 |  |
| M817 | M | 2 |  |  |  |
| M832 | M |  |  | 1 |  |
| M833 | M | 2 |  |  |  |
| M866 | M |  |  | 2 |  |
| M881 | M |  |  |  | 2 |
| M897 | M |  |  |  | 2 |
| M914 | M |  |  |  | 2 |
| M915 | M |  |  |  | 2 |
| T0 | T |  |  | 1 | 4 |
| T17 | T |  |  | 1 | 2 |
| T7 | T |  |  | 1 | 2 |
| T8 | T |  |  | 1 | 4 |
