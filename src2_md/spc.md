---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 60
**Blocks:** 5
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 CYCLE DONE | 1–12 | LD M824, LD M824, LD M824 ... (+3) | 6 |
| 2 | L1 CYCLE DONE | 14–25 | LD M840, LD M840, LD M840 ... (+3) | 6 |
| 3 | DISPLAY BOMBE | 27–32 | LD M0 | 5 |
| 4 | VAC SPC LOGGING | 34–55 | LD M18, LD M34, LD T18 ... (+4) | 15 |
| 5 | VAC SPC CLEAR | 57–60 | LD M17 | 3 |

## Block Detail

### Block 1: L0 CYCLE DONE (Step 1-12)

**Trigger Condition:**
- LD M824
- LD M824
- LD M824
- LD M824
- LD M824
- LD M824

**Actions:**
- D+ D280
- D+ D282
- D+ D284
- DMOV D130
- DMOV D128
- RST M824

### Block 2: L1 CYCLE DONE (Step 14-25)

**Trigger Condition:**
- LD M840
- LD M840
- LD M840
- LD M840
- LD M840
- LD M840

**Actions:**
- D+ D290
- D+ D292
- D+ D294
- DMOV D406
- DMOV D128
- RST M840

### Block 3: DISPLAY BOMBE (Step 27-32)

**Trigger Condition:**
- LD M0

**Actions:**
- MOV D282
- LDD>= D280
- SET M875
- LDD>= D290
- SET M878

### Block 4: VAC SPC LOGGING (Step 34-55)

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

### Block 5: VAC SPC CLEAR (Step 57-60)

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
| D290 | D |  |  |  | 2 |
| D292 | D |  |  |  | 1 |
| D294 | D |  |  |  | 1 |
| D406 | D |  |  |  | 1 |
| D7020 | D |  |  |  | 1 |
| K0 | K |  |  |  | 2 |
| M0 | M |  |  |  | 1 |
| M17 | M |  |  |  | 1 |
| M18 | M |  |  |  | 2 |
| M19 | M |  |  |  | 2 |
| M20 | M |  |  |  | 2 |
| M33 | M |  |  |  | 1 |
| M34 | M |  |  |  | 2 |
| M35 | M |  |  |  | 2 |
| M36 | M |  |  |  | 2 |
| M824 | M |  | 1 |  | 6 |
| M840 | M |  | 1 |  | 6 |
| M875 | M | 1 |  |  |  |
| M878 | M | 1 |  |  |  |
| T18 | T |  |  |  | 3 |
| T19 | T |  |  |  | 2 |
