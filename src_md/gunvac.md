---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 41
**Blocks:** 2
**Generated:** 2026-06-08
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | GUN VAC L1 | 1–20 | LD M12, LD M12, LD M12 ... (+2) | 15 |
| 2 | GUN VAC L2 | 22–41 | LD M32, LD M32, LD M32 ... (+2) | 15 |

## Block Detail

### Block 1: GUN VAC L1 (Step 1–20)

**Trigger Condition:**
- LD M12
- LD M12
- LD M12
- LD T15
- LD M12

**Actions:**
- OUT M60
- OUT T1
- AND T1
- OUT M101
- AND T1
- OUT T15
- SET M108
- SET M310
- RST M12
- RST M60
- ANI M80
- SET M108
- SET M310
- RST M12
- RST M60

### Block 2: GUN VAC L2 (Step 22–41)

**Trigger Condition:**
- LD M32
- LD M32
- LD M32
- LD T16
- LD M32

**Actions:**
- OUT M70
- OUT T7
- AND T7
- OUT M117
- AND T7
- OUT T16
- SET M124
- SET M330
- RST M32
- RST M70
- ANI M90
- SET M124
- SET M330
- RST M32
- RST M70

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| M101 | M |  |  | 1 |  |
| M108 | M | 2 |  |  |  |
| M117 | M |  |  | 1 |  |
| M12 | M |  | 2 |  | 4 |
| M124 | M | 2 |  |  |  |
| M310 | M | 2 |  |  |  |
| M32 | M |  | 2 |  | 4 |
| M330 | M | 2 |  |  |  |
| M60 | M |  | 2 | 1 |  |
| M70 | M |  | 2 | 1 |  |
| M80 | M |  |  |  | 1 |
| M90 | M |  |  |  | 1 |
| T1 | T |  |  | 1 | 2 |
| T15 | T |  |  | 1 | 1 |
| T16 | T |  |  | 1 | 1 |
| T7 | T |  |  | 1 | 2 |
