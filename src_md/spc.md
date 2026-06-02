---
# spc — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 27
**Blocks:** 3
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 CYCLE DONE | 0–10 | LD L24, LD L24, LD L24 | 5 |
| 2 | L1 CYCLE DONE | 11–21 | LD L40, LD L40, LD L40 | 5 |
| 3 | DISPLAY BOMBE | 22–27 | LD M0, LDD>= D280 | 3 |

## Block Detail

### Block 1: L0 CYCLE DONE (Step 0–10)

**Trigger Condition:**
- LD L24
- LD L24
- LD L24
- LD L24
- LD L24

**Actions:**
- D+ D280
- D+ D282
- D+ D284
- DMOV D130
- DMOV D128

### Block 2: L1 CYCLE DONE (Step 11–21)

**Trigger Condition:**
- LD L40
- LD L40
- LD L40
- LD L40
- LD L40

**Actions:**
- D+ D290
- D+ D292
- D+ D294
- DMOV D130
- DMOV D128

### Block 3: DISPLAY BOMBE (Step 22–27)

**Trigger Condition:**
- LD M0
- LDD>= D280

**Actions:**
- MOV D282
- SET L75
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D128 | D | — | — | — | 10, 21 | DOUBLE_COIL_CANDIDATE |
| D130 | D | — | — | — | 8, 19 | DOUBLE_COIL_CANDIDATE |
| D280 | D | — | — | — | 25 | DOUBLE_COIL_CANDIDATE |
| D282 | D | — | — | — | 24 | DOUBLE_COIL_CANDIDATE |
| D284 | D | — | — | — | — |  |
| D290 | D | — | — | — | — |  |
| D292 | D | — | — | — | — |  |
| D294 | D | — | — | — | — |  |
| L24 | L | — | — | — | 1, 3, 5, 7, 9 | LATCH_DEVICE |
| L40 | L | — | — | — | 12, 14, 16, 18, 20 | LATCH_DEVICE |
| L75 | L | 26 | — | — | — | NO_RST, LATCH_DEVICE |
| M0 | M | — | — | — | 23 |  |
