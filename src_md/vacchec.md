---
# vacchec — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 43
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | VAC CHECK L0 | 1–21 | LD M20, LD M20, LD M20 ... (+3) | 15 |
| 2 | VAC CHECK L1 | 23–43 | LD M36, LD M36, LD M36 ... (+3) | 15 |

## Block Detail

### Block 1: VAC CHECK L0 (Step 1–21)

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

### Block 2: VAC CHECK L1 (Step 23–43)

**Trigger Condition:**
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36
- LD M36

**Actions:**
- DMOV D172
- OUT T11
- AND M791
- SET L79
- SET L37
- RST M36
- D- D306
- AND T11
- ANDD<= D308
- SET L36
- RST M36
- ANDD> D308
- SET L37
- SET L68
- RST M36

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D160 | D |  |  |  | 1 |
| D172 | D |  |  |  | 1 |
| D300 | D |  |  |  | 1 |
| D304 | D |  |  |  | 2 |
| D306 | D |  |  |  | 1 |
| D308 | D |  |  |  | 2 |
| L20 | L | 1 |  |  |  |
| L21 | L | 2 |  |  |  |
| L36 | L | 1 |  |  |  |
| L37 | L | 2 |  |  |  |
| L68 | L | 2 |  |  |  |
| L78 | L | 1 |  |  |  |
| L79 | L | 1 |  |  |  |
| M20 | M |  | 3 |  | 6 |
| M36 | M |  | 3 |  | 6 |
| M775 | M |  |  |  | 1 |
| M791 | M |  |  |  | 1 |
| T11 | T |  |  | 1 | 1 |
| T2 | T |  |  | 1 | 1 |
