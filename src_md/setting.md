---
# setting — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 4
**Blocks:** 1
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | CONFIG SYNC | 1–4 | LD M0, LD M0 | 2 |

## Block Detail

### Block 1: CONFIG SYNC (Step 1–4)

**Trigger Condition:**
- LD M0
- LD M0

**Actions:**
- MOV D270
- D* D274

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D270 | D |  |  |  | 1 |
| D274 | D |  |  |  | 1 |
| M0 | M |  |  |  | 2 |
