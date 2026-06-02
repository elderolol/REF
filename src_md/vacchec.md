---
# vacchec — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 44
**Blocks:** 2
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | VAC CHECK L0 | 0–21 | LD M20, LD M20, LD M20 | 15 |
| 2 | VAC CHECK L1 | 22–44 | LD M36, LD M36, LD M36 | 16 |

## Block Detail

### Block 1: VAC CHECK L0 (Step 0–21)

**Trigger Condition:**
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20
- LD M20

**Actions:**
- DMOV D160
- OUT T2
- AND M775
- SET L78
- SET L21
- RST M20
- D- D300
- AND T2
- ANDD<= D304
- SET L20
- RST M20
- ANDD> D304
- SET L21
- SET L68
- RST M20

### Block 2: VAC CHECK L1 (Step 22–44)

**Trigger Condition:**
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36

**Actions:**
- DMOV D172
- OUT T2
- AND M791
- SET L79
- SET L37
- RST M36
- D- D306
- AND T2
- ANDD<= D308
- SET L36
- RST M36
- ANDD> D308
- SET L37
- SET L68
- RST M36
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D160 | D | — | — | — | 2 |  |
| D172 | D | — | — | — | 24 |  |
| D300 | D | — | — | — | — |  |
| D304 | D | — | — | — | 14, 18 |  |
| D306 | D | — | — | — | — |  |
| D308 | D | — | — | — | 36, 40 |  |
| L20 | L | 15 | — | — | — | NO_RST, LATCH_DEVICE |
| L21 | L | 8, 19 | — | — | — | NO_RST, LATCH_DEVICE |
| L36 | L | 37 | — | — | — | NO_RST, LATCH_DEVICE |
| L37 | L | 30, 41 | — | — | — | NO_RST, LATCH_DEVICE |
| L68 | L | 20, 42 | — | — | — | NO_RST, LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L78 | L | 7 | — | — | — | NO_RST, LATCH_DEVICE |
| L79 | L | 29 | — | — | — | NO_RST, LATCH_DEVICE |
| M20 | M | — | 9, 16, 21 | — | 1, 3, 5, 10, 12, 17 | NO_SET |
| M36 | M | — | 31, 38, 43 | — | 23, 25, 27, 32, 34, 39 | NO_SET |
| M775 | M | — | — | — | 6 |  |
| M791 | M | — | — | — | 28 |  |
| T2 | T | — | — | 4, 26 | 13, 35 | DOUBLE_COIL_CANDIDATE |
