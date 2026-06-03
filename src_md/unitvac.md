---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 101
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | UNIT VACUUM (Line 0) | 1–50 | LD M19, LD T1, LD M19 ... (+9) | 38 |
| 2 | UNIT VACUUM (Line 1) | 52–101 | LD M35, LD T9, LD M35 ... (+9) | 38 |

## Block Detail

### Block 1: UNIT VACUUM (Line 0) (Step 1–50)

**Trigger Condition:**
- LD M19
- LD T1
- LD M19
- LD M19
- LD M19
- LD M19
- LD M914
- LD M915
- LD M19
- LD M19
- LD M19
- LD T7

**Actions:**
- OUT T1
- AND<= D160
- OUT M102
- ANI M881
- ANI T7
- ANI M102
- OUT M50
- ANI M881
- ANI T7
- ANI M102
- OUT M49
- ANI M881
- SET M16
- RST M19
- RST M49
- RST M50
- ANI M772
- ANI M773
- ORB 
- ANB 
- SET M819
- AND T1
- AND<= D160
- OUT M818
- AND T1
- AND<= D160
- RST M19
- RST M49
- RST M50
- AND T1
- AND> D160
- OUT T7
- SET M819
- OUT M867
- SET M76
- RST M19
- RST M49
- RST M50

### Block 2: UNIT VACUUM (Line 1) (Step 52–101)

**Trigger Condition:**
- LD M35
- LD T9
- LD M35
- LD M35
- LD M35
- LD M35
- LD M914
- LD M915
- LD M35
- LD M35
- LD M35
- LD T17

**Actions:**
- OUT T9
- AND<= D172
- OUT M103
- ANI M897
- ANI T17
- ANI M103
- OUT M66
- ANI M897
- ANI T17
- ANI M103
- OUT M65
- ANI M897
- SET M32
- RST M35
- RST M65
- RST M66
- ANI M788
- ANI M789
- ORB 
- ANB 
- SET M835
- AND T9
- AND<= D172
- OUT M834
- AND T9
- AND<= D172
- RST M35
- RST M65
- RST M66
- AND T9
- AND> D172
- OUT T17
- SET M835
- OUT M867
- SET M76
- RST M35
- RST M65
- RST M66

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 4 |
| D172 | D |  |  |  | 4 |
| M102 | M |  |  | 1 | 2 |
| M103 | M |  |  | 1 | 2 |
| M16 | M | 1 |  |  |  |
| M19 | M |  | 3 |  | 8 |
| M32 | M | 1 |  |  |  |
| M35 | M |  | 3 |  | 8 |
| M49 | M |  | 3 | 1 |  |
| M50 | M |  | 3 | 1 |  |
| M65 | M |  | 3 | 1 |  |
| M66 | M |  | 3 | 1 |  |
| M76 | M | 2 |  |  |  |
| M772 | M |  |  |  | 1 |
| M773 | M |  |  |  | 1 |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| M818 | M |  |  | 1 |  |
| M819 | M | 2 |  |  |  |
| M834 | M |  |  | 1 |  |
| M835 | M | 2 |  |  |  |
| M867 | M |  |  | 2 |  |
| M881 | M |  |  |  | 3 |
| M897 | M |  |  |  | 3 |
| M914 | M |  |  |  | 2 |
| M915 | M |  |  |  | 2 |
| T1 | T |  |  | 1 | 4 |
| T17 | T |  |  | 1 | 3 |
| T7 | T |  |  | 1 | 3 |
| T9 | T |  |  | 1 | 4 |
