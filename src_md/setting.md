---
# setting — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 25
**Blocks:** 3
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | CONFIG SYNC | 0–4 | LD M0, LD M0 | 2 |
| 2 | GUN SETTINGS SYNC | 5–11 | LD M0, LD M0, LD M0 | 3 |
| 3 | DISPLAY MIRROR | 12–25 | LD M0, LD M0, LD M0 | 7 |

## Block Detail

### Block 1: CONFIG SYNC (Step 0–4)

**Trigger Condition:**
- LD M0
- LD M0

**Actions:**
- MOV D270
- D* D274

### Block 2: GUN SETTINGS SYNC (Step 5–11)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0

**Actions:**
- MOV D62
- DMOV D64
- DMOV D72

### Block 3: DISPLAY MIRROR (Step 12–25)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D160
- MOV D156
- MOV D152
- DMOV D172
- MOV D168
- MOV D164
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D152 | D | — | — | — | 18 |  |
| D156 | D | — | — | — | 16 |  |
| D160 | D | — | — | — | 14 |  |
| D164 | D | — | — | — | 24 |  |
| D168 | D | — | — | — | 22 |  |
| D172 | D | — | — | — | 20 |  |
| D270 | D | — | — | — | 2 |  |
| D274 | D | — | — | — | — |  |
| D62 | D | — | — | — | 7 |  |
| D64 | D | — | — | — | 9 |  |
| D72 | D | — | — | — | 11 |  |
| M0 | M | — | — | — | 1, 3, 6, 8, 10, 13, 15, 17, 19, 21, 23 | DOUBLE_COIL_CANDIDATE |
