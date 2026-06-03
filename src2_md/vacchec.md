---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 43
**Blocks:** 2
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | VAC CHECK L0 | 1–21 | LD M20, LD M20, LD M20 ... (+5) | 13 |
| 2 | VAC CHECK L1 | 23–43 | LD M36, LD M36, LD M36 ... (+5) | 13 |

## Block Detail

### Block 1: VAC CHECK L0 (Step 1-21)

**Trigger Condition:**
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20
- LD M21
- LD M20
- LD M21

**Actions:**
- DMOV D160
- OUT T2
- D- D300
- AND M775
- AND> D304
- ORB 
- OUT M821
- RST M821
- ANI M775
- AND T2
- AND<= D304
- OUT M820
- RST M820

### Block 2: VAC CHECK L1 (Step 23-43)

**Trigger Condition:**
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M37
- LD M36
- LD M37

**Actions:**
- DMOV D172
- OUT T11
- D- D306
- AND M791
- AND> D308
- ORB 
- OUT M837
- RST M837
- ANI M791
- AND T11
- AND<= D308
- OUT M836
- RST M836

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 1 |
| D172 | D |  |  |  | 1 |
| D300 | D |  |  |  | 1 |
| D304 | D |  |  |  | 2 |
| D306 | D |  |  |  | 1 |
| D308 | D |  |  |  | 2 |
| M20 | M |  |  |  | 6 |
| M21 | M |  |  |  | 2 |
| M36 | M |  |  |  | 6 |
| M37 | M |  |  |  | 2 |
| M775 | M |  |  |  | 2 |
| M791 | M |  |  |  | 2 |
| M820 | M |  | 1 | 1 |  |
| M821 | M |  | 1 | 1 |  |
| M836 | M |  | 1 | 1 |  |
| M837 | M |  | 1 | 1 |  |
| T11 | T |  |  | 1 | 1 |
| T2 | T |  |  | 1 | 1 |
