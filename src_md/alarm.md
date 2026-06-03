---
# alarm — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 86
**Blocks:** 3
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | ALARM LATCH | 1–57 | LDI M771, LDI M779, LD L17 ... (+9) | 45 |
| 2 | BUZZER | 59–79 | LD L64, LD M1028, LD M1028 | 18 |
| 3 | ALARM RESET | 81–86 | LD M1027, LD M750, LD M750 | 3 |

## Block Detail

### Block 1: ALARM LATCH (Step 1–57)

**Trigger Condition:**
- LDI M771
- LDI M779
- LD L17
- LD L19
- LD L21
- LD L23
- LD M0
- LD M0
- LD M776
- LD M777
- LD M0
- LD M791

**Actions:**
- SET L64
- OR L65
- ANI M750
- OUT L65
- OR L33
- OR L66
- ANI M750
- OUT L66
- OR L35
- OR L67
- ANI M750
- OUT L67
- OR L37
- OR L68
- ANI M750
- OUT L68
- OR L39
- OR L69
- ANI M750
- OUT L69
- OR L70
- ANI M750
- OUT L70
- OR L71
- ANI M750
- OUT L71
- OR M792
- OR L72
- ANI M750
- OUT L72
- OR M793
- OR L73
- ANI M750
- OUT L73
- LD< D156
- OR> D156
- OR L74
- ANI M750
- OUT L74
- OR L78
- ANI M750
- OUT L78
- OR L79
- ANI M750
- OUT L79

### Block 2: BUZZER (Step 59–79)

**Trigger Condition:**
- LD L64
- LD M1028
- LD M1028

**Actions:**
- OR L65
- OR L66
- OR L67
- OR L68
- OR L69
- OR L70
- OR L71
- OR L72
- OR L73
- OR L74
- OR L76
- OR L77
- OR L78
- OR L79
- ANI M500
- OUT M76
- SET M500
- RST M76

### Block 3: ALARM RESET (Step 81–86)

**Trigger Condition:**
- LD M1027
- LD M750
- LD M750

**Actions:**
- PLS M750
- RST L64
- RST L76

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D156 | D |  |  |  | 2 |
| L17 | L |  |  |  | 1 |
| L19 | L |  |  |  | 1 |
| L21 | L |  |  |  | 1 |
| L23 | L |  |  |  | 1 |
| L33 | L |  |  |  | 1 |
| L35 | L |  |  |  | 1 |
| L37 | L |  |  |  | 1 |
| L39 | L |  |  |  | 1 |
| L64 | L | 1 | 1 |  | 1 |
| L65 | L |  |  | 1 | 2 |
| L66 | L |  |  | 1 | 2 |
| L67 | L |  |  | 1 | 2 |
| L68 | L |  |  | 1 | 2 |
| L69 | L |  |  | 1 | 2 |
| L70 | L |  |  | 1 | 2 |
| L71 | L |  |  | 1 | 2 |
| L72 | L |  |  | 1 | 2 |
| L73 | L |  |  | 1 | 2 |
| L74 | L |  |  | 1 | 2 |
| L76 | L |  | 1 |  | 1 |
| L77 | L |  |  |  | 1 |
| L78 | L |  |  | 1 | 2 |
| L79 | L |  |  | 1 | 2 |
| M0 | M |  |  |  | 3 |
| M1027 | M |  |  |  | 1 |
| M1028 | M |  |  |  | 2 |
| M500 | M | 1 |  |  | 1 |
| M750 | M |  |  |  | 15 |
| M76 | M |  | 1 | 1 |  |
| M771 | M |  |  |  | 1 |
| M776 | M |  |  |  | 1 |
| M777 | M |  |  |  | 1 |
| M779 | M |  |  |  | 1 |
| M791 | M |  |  |  | 1 |
| M792 | M |  |  |  | 1 |
| M793 | M |  |  |  | 1 |
