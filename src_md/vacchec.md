---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 47
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | VAC CHECK L0 | 1–23 | LD M20, LD M20, LD M20 ... (+5) | 15 |
| 2 | VAC CHECK L1 | 25–47 | LD M36, LD M36, LD M36 ... (+5) | 15 |

## Block Detail

### Block 1: VAC CHECK L0 (Step 1–23)

**Trigger Condition:**
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20

**Actions:**
- DMOV D160
- OUT T2
- D- D300
- AND M775
- OUT M878
- AND M775
- AND> D304
- ORB 
- OUT M821
- AND> D304
- OUT M868
- ANI M775
- AND T2
- AND<= D304
- OUT M820

### Block 2: VAC CHECK L1 (Step 25–47)

**Trigger Condition:**
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36

**Actions:**
- DMOV D172
- OUT T11
- D- D306
- AND M791
- OUT M879
- AND M791
- AND> D308
- ORB 
- OUT M837
- AND> D308
- OUT M868
- ANI M791
- AND T11
- AND<= D308
- OUT M836

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 1 |
| D172 | D |  |  |  | 1 |
| D300 | D |  |  |  | 1 |
| D304 | D |  |  |  | 3 |
| D306 | D |  |  |  | 1 |
| D308 | D |  |  |  | 3 |
| M20 | M |  |  |  | 8 |
| M36 | M |  |  |  | 8 |
| M775 | M |  |  |  | 3 |
| M791 | M |  |  |  | 3 |
| M820 | M |  |  | 1 |  |
| M821 | M |  |  | 1 |  |
| M836 | M |  |  | 1 |  |
| M837 | M |  |  | 1 |  |
| M868 | M |  |  | 2 |  |
| M878 | M |  |  | 1 |  |
| M879 | M |  |  | 1 |  |
| T11 | T |  |  | 1 | 1 |
| T2 | T |  |  | 1 | 1 |
