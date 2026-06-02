---
# ad — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 59
**Blocks:** 7
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 PRESSURE | 0–6 | LD M0, LD M0, LD M0 | 3 |
| 2 | L0 TEMPERATURE | 7–15 | LD M0, LD M0, LD M0 | 4 |
| 3 | L0 VACUUM | 16–22 | LD M0, LD M0, LD M0 | 3 |
| 4 | L1 PRESSURE | 23–29 | LD M0, LD M0, LD M0 | 3 |
| 5 | L1 TEMPERATURE | 30–38 | LD M0, LD M0, LD M0 | 4 |
| 6 | L1 VACUUM | 39–45 | LD M0, LD M0, LD M0 | 3 |
| 7 | DISPLAY MIRROR | 46–59 | LD M0, LD M0, LD M0 | 7 |

## Block Detail

### Block 1: L0 PRESSURE (Step 0–6)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D150
- D* D300
- D/ D302

### Block 2: L0 TEMPERATURE (Step 7–15)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D154
- D* D310
- D/ D312
- D- D314

### Block 3: L0 VACUUM (Step 16–22)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D158
- D* D320
- D/ D322

### Block 4: L1 PRESSURE (Step 23–29)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D162
- D* D330
- D/ D332

### Block 5: L1 TEMPERATURE (Step 30–38)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D166
- D* D340
- D/ D342
- D- D344

### Block 6: L1 VACUUM (Step 39–45)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D170
- D* D350
- D/ D352

### Block 7: DISPLAY MIRROR (Step 46–59)

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
| D150 | D | — | — | — | 2 |  |
| D152 | D | — | — | — | 52 |  |
| D154 | D | — | — | — | 9 |  |
| D156 | D | — | — | — | 50 |  |
| D158 | D | — | — | — | 18 |  |
| D160 | D | — | — | — | 48 |  |
| D162 | D | — | — | — | 25 |  |
| D164 | D | — | — | — | 58 |  |
| D166 | D | — | — | — | 32 |  |
| D168 | D | — | — | — | 56 |  |
| D170 | D | — | — | — | 41 |  |
| D172 | D | — | — | — | 54 |  |
| D300 | D | — | — | — | — |  |
| D302 | D | — | — | — | — |  |
| D310 | D | — | — | — | — |  |
| D312 | D | — | — | — | — |  |
| D314 | D | — | — | — | — |  |
| D320 | D | — | — | — | — |  |
| D322 | D | — | — | — | — |  |
| D330 | D | — | — | — | — |  |
| D332 | D | — | — | — | — |  |
| D340 | D | — | — | — | — |  |
| D342 | D | — | — | — | — |  |
| D344 | D | — | — | — | — |  |
| D350 | D | — | — | — | — |  |
| D352 | D | — | — | — | — |  |
| M0 | M | — | — | — | 1, 3, 5, 8, 10, 12, 14, 17, 19, 21, 24, 26, 28, 31, 33, 35, 37, 40, 42, 44, 47, 49, 51, 53, 55, 57 | DOUBLE_COIL_CANDIDATE |
