---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 51
**Blocks:** 2
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | UNIT VACUUM (Line 0) | 1–19 | LD M19, LD T1, LD M19 ... (+2) | 14 |
| 2 | UNIT VACUUM (Line 1) | 21–51 | LD M35, LD T9, LD M35 ... (+6) | 22 |

## Block Detail

### Block 1: UNIT VACUUM (Line 0) (Step 1-19)

**Trigger Condition:**
- LD M19
- LD T1
- LD M19
- LD M19
- LD M20

**Actions:**
- OUT T1
- AND<= D160
- OUT M102
- ANI M881
- ANI T7
- ANI M102
- ANI M818
- ANI M819
- OUT M50
- AND T1
- AND<= D160
- SET M818
- OR M16
- RST M818

### Block 2: UNIT VACUUM (Line 1) (Step 21-51)

**Trigger Condition:**
- LD M35
- LD T9
- LD M35
- LD M35
- LD M928
- LD M929
- LD T17
- LD M35
- LD M36

**Actions:**
- OUT T9
- AND<= D172
- OUT M118
- ANI M897
- ANI T17
- ANI M118
- ANI M834
- ANI M835
- OUT M66
- ANI M788
- ANI M789
- ORB 
- ANB 
- ORB 
- OR M835
- ANI M36
- OUT M835
- AND T9
- AND<= D172
- SET M834
- OR M32
- RST M834

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 2 |
| D172 | D |  |  |  | 2 |
| M102 | M |  |  | 1 | 1 |
| M118 | M |  |  | 1 | 1 |
| M16 | M |  |  |  | 1 |
| M19 | M |  |  |  | 3 |
| M20 | M |  |  |  | 1 |
| M32 | M |  |  |  | 1 |
| M35 | M |  |  |  | 4 |
| M36 | M |  |  |  | 2 |
| M50 | M |  |  | 1 |  |
| M66 | M |  |  | 1 |  |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| M818 | M | 1 | 1 |  | 1 |
| M819 | M |  |  |  | 1 |
| M834 | M | 1 | 1 |  | 1 |
| M835 | M |  |  | 1 | 2 |
| M881 | M |  |  |  | 1 |
| M897 | M |  |  |  | 1 |
| M928 | M |  |  |  | 1 |
| M929 | M |  |  |  | 1 |
| T1 | T |  |  | 1 | 2 |
| T17 | T |  |  |  | 2 |
| T7 | T |  |  |  | 1 |
| T9 | T |  |  | 1 | 2 |
