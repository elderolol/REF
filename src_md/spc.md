---
# spc — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 54
**Blocks:** 5
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 CYCLE DONE | 1–10 | LD L24, LD L24, LD L24 ... (+2) | 5 |
| 2 | L1 CYCLE DONE | 12–21 | LD L40, LD L40, LD L40 ... (+2) | 5 |
| 3 | DISPLAY BOMBE | 23–26 | LD M0 | 3 |
| 4 | VAC SPC LOGGING | 28–49 | LD M18, LD M34, LD T18 ... (+4) | 15 |
| 5 | VAC SPC CLEAR | 51–54 | LD M17 | 3 |

## Block Detail

### Block 1: L0 CYCLE DONE (Step 1–10)

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

### Block 2: L1 CYCLE DONE (Step 12–21)

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
- DMOV D406
- DMOV D128

### Block 3: DISPLAY BOMBE (Step 23–26)

**Trigger Condition:**
- LD M0

**Actions:**
- MOV D282
- LDD>= D280
- SET L75

### Block 4: VAC SPC LOGGING (Step 28–49)

**Trigger Condition:**
- LD M18
- LD M34
- LD T18
- LD T18
- LD M18
- LD T19
- LD M34

**Actions:**
- OR M19
- OR M20
- OUTH T18
- OR M35
- OR M36
- OUTH T19
- BMOV D7020
- OR M19
- OR M20
- ANB 
- DMOV D160
- OR M35
- OR M36
- ANB 
- DMOV D172

### Block 5: VAC SPC CLEAR (Step 51–54)

**Trigger Condition:**
- LD M17

**Actions:**
- OR M33
- FMOV K0
- FMOV K0

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D128 | D |  |  |  | 2 |
| D130 | D |  |  |  | 1 |
| D160 | D |  |  |  | 1 |
| D172 | D |  |  |  | 1 |
| D280 | D |  |  |  | 2 |
| D282 | D |  |  |  | 2 |
| D284 | D |  |  |  | 1 |
| D290 | D |  |  |  | 1 |
| D292 | D |  |  |  | 1 |
| D294 | D |  |  |  | 1 |
| D406 | D |  |  |  | 1 |
| D7020 | D |  |  |  | 1 |
| K0 | K |  |  |  | 2 |
| L24 | L |  |  |  | 5 |
| L40 | L |  |  |  | 5 |
| L75 | L | 1 |  |  |  |
| M0 | M |  |  |  | 1 |
| M17 | M |  |  |  | 1 |
| M18 | M |  |  |  | 2 |
| M19 | M |  |  |  | 2 |
| M20 | M |  |  |  | 2 |
| M33 | M |  |  |  | 1 |
| M34 | M |  |  |  | 2 |
| M35 | M |  |  |  | 2 |
| M36 | M |  |  |  | 2 |
| T18 | T |  |  |  | 3 |
| T19 | T |  |  |  | 2 |
