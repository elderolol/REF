---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 93
**Blocks:** 2
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | GUN VACUUM (Line 0) | 1–46 | LD M18, LD T0, LD M18 ... (+9) | 34 |
| 2 | GUN VACUUM (Line 1) | 48–93 | LD M34, LD T8, LD M34 ... (+9) | 34 |

## Block Detail

### Block 1: GUN VACUUM (Line 0) (Step 1-46)

**Trigger Condition:**
- LD M18
- LD T0
- LD M18
- LD M19
- LD M18
- LD M928
- LD M929
- LD T7
- LD M18
- LD M19
- LD M18
- LD M19

**Actions:**
- OUT T0
- AND<= D160
- OUT M100
- ANI M881
- ANI T7
- ANI M100
- ANI M816
- ANI M817
- ANI M881
- ANI T7
- ANI M102
- ANI M818
- ANI M819
- ORB 
- OUT M49
- ANI M772
- ANI M773
- ORB 
- ANB 
- ORB 
- OR M817
- ANI M19
- OUT M817
- AND T0
- AND<= D160
- SET M816
- OR M16
- RST M816
- AND T0
- AND> D160
- AND T1
- AND> D160
- ORB 
- OUT T7

### Block 2: GUN VACUUM (Line 1) (Step 48-93)

**Trigger Condition:**
- LD M34
- LD T8
- LD M34
- LD M35
- LD M34
- LD M928
- LD M929
- LD T17
- LD M34
- LD M35
- LD M34
- LD M35

**Actions:**
- OUT T8
- AND<= D172
- OUT M116
- ANI M897
- ANI T17
- ANI M116
- ANI M832
- ANI M833
- ANI M897
- ANI T17
- ANI M118
- ANI M834
- ANI M835
- ORB 
- OUT M65
- ANI M788
- ANI M789
- ORB 
- ANB 
- ORB 
- OR M833
- ANI M35
- OUT M833
- AND T8
- AND<= D172
- SET M832
- OR M32
- RST M832
- AND T8
- AND> D172
- AND T9
- AND> D172
- ORB 
- OUT T17

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 4 |
| D172 | D |  |  |  | 4 |
| M100 | M |  |  | 1 | 1 |
| M102 | M |  |  |  | 1 |
| M116 | M |  |  | 1 | 1 |
| M118 | M |  |  |  | 1 |
| M16 | M |  |  |  | 1 |
| M18 | M |  |  |  | 5 |
| M19 | M |  |  |  | 4 |
| M32 | M |  |  |  | 1 |
| M34 | M |  |  |  | 5 |
| M35 | M |  |  |  | 4 |
| M49 | M |  |  | 1 |  |
| M65 | M |  |  | 1 |  |
| M772 | M |  |  |  | 1 |
| M773 | M |  |  |  | 1 |
| M788 | M |  |  |  | 1 |
| M789 | M |  |  |  | 1 |
| M816 | M | 1 | 1 |  | 1 |
| M817 | M |  |  | 1 | 2 |
| M818 | M |  |  |  | 1 |
| M819 | M |  |  |  | 1 |
| M832 | M | 1 | 1 |  | 1 |
| M833 | M |  |  | 1 | 2 |
| M834 | M |  |  |  | 1 |
| M835 | M |  |  |  | 1 |
| M881 | M |  |  |  | 2 |
| M897 | M |  |  |  | 2 |
| M928 | M |  |  |  | 2 |
| M929 | M |  |  |  | 2 |
| T0 | T |  |  | 1 | 3 |
| T1 | T |  |  |  | 1 |
| T17 | T |  |  | 1 | 3 |
| T7 | T |  |  | 1 | 3 |
| T8 | T |  |  | 1 | 3 |
| T9 | T |  |  |  | 1 |
