---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 14
**Blocks:** 1
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | ANALOG RAW TO EU | 1–14 | LD M0, LD M0, LD M0 ... (+4) | 7 |

## Block Detail

### Block 1: ANALOG RAW TO EU (Step 1–14)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- MOV D100
- MOV D102
- DMOV D104
- MOV D110
- MOV D112
- DMOV D114
- MOV D120

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D100 | D |  |  |  | 1 |
| D102 | D |  |  |  | 1 |
| D104 | D |  |  |  | 1 |
| D110 | D |  |  |  | 1 |
| D112 | D |  |  |  | 1 |
| D114 | D |  |  |  | 1 |
| D120 | D |  |  |  | 1 |
| M0 | M |  |  |  | 7 |
