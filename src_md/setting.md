---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 16
**Blocks:** 1
**Generated:** 2026-06-08
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | CONFIG SYNC | 1–16 | LD M0, LD M0, LD M0 ... (+5) | 8 |

## Block Detail

### Block 1: CONFIG SYNC (Step 1–16)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- MOV D2
- MOV D4
- MOV D6
- MOV D8
- MOV D22
- MOV D24
- MOV D26
- MOV D28

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D2 | D |  |  |  | 1 |
| D22 | D |  |  |  | 1 |
| D24 | D |  |  |  | 1 |
| D26 | D |  |  |  | 1 |
| D28 | D |  |  |  | 1 |
| D4 | D |  |  |  | 1 |
| D6 | D |  |  |  | 1 |
| D8 | D |  |  |  | 1 |
| M0 | M |  |  |  | 8 |
