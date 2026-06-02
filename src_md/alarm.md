---
# alarm — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 85
**Blocks:** 3
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | ALARM LATCH | 0–32 | LDI M771, LDI M779, LD L17 | 20 |
| 2 | BUZZER | 33–49 | LD L64, LD M1028 | 14 |
| 3 | ALARM RESET | 50–85 | LD M1027, LD M1872, LD M1872 | 24 |

## Block Detail

### Block 1: ALARM LATCH (Step 0–32)

**Trigger Condition:**
- LDI M771
- LDI M779
- LD L17
- LD L19
- LD L21
- LD L23
- LD M776
- LD M777
- LD< D156
- LD> D156
- LD M775
- LD M791

**Actions:**
- SET L64
- SET L65
- OR L33
- SET L66
- OR L35
- SET L67
- OR L37
- SET L68
- OR L39
- SET L69
- SET L70
- SET L71
- OR M792
- SET L72
- OR M793
- SET L73
- SET L74
- SET L74
- SET L78
- SET L79

### Block 2: BUZZER (Step 33–49)

**Trigger Condition:**
- LD L64
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
- OR L78
- OR L79
- OUT M76
- RST M76

### Block 3: ALARM RESET (Step 50–85)

**Trigger Condition:**
- LD M1027
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872
- LD M1872

**Actions:**
- PLS M1872
- ANI M771
- RST L64
- ANI M779
- RST L65
- RST L66
- RST L67
- RST L68
- RST L69
- RST L70
- RST L71
- ANI M776
- ANI M792
- RST L72
- ANI M777
- ANI M793
- RST L73
- RST L74
- ANI M775
- RST L78
- ANI M791
- RST L79
- RST M76
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D156 | D | — | — | — | 25, 27 |  |
| L17 | L | — | — | — | 5 | LATCH_DEVICE |
| L19 | L | — | — | — | 8 | LATCH_DEVICE |
| L21 | L | — | — | — | 11 | LATCH_DEVICE |
| L23 | L | — | — | — | 14 | LATCH_DEVICE |
| L33 | L | — | — | — | 6 | LATCH_DEVICE |
| L35 | L | — | — | — | 9 | LATCH_DEVICE |
| L37 | L | — | — | — | 12 | LATCH_DEVICE |
| L39 | L | — | — | — | 15 | LATCH_DEVICE |
| L64 | L | 2 | 55 | — | 34 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L65 | L | 4 | 58 | — | 35 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L66 | L | 7 | 60 | — | 36 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L67 | L | 10 | 61 | — | 37 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L68 | L | 13 | 62 | — | 38 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L69 | L | 16 | 64 | — | 39 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L70 | L | 17 | 65 | — | 40 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L71 | L | 18 | 66 | — | 41 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L72 | L | 21 | 70 | — | 42 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L73 | L | 24 | 74 | — | 43 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L74 | L | 26, 28 | 76 | — | 44 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L78 | L | 30 | 79 | — | 45 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L79 | L | 32 | 82 | — | 46 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| M1027 | M | — | — | — | 51 |  |
| M1028 | M | — | — | — | 48 |  |
| M1872 | M | — | — | — | 53, 56, 59, 63, 67, 71, 75, 77, 80, 83 |  |
| M76 | M | — | 49, 84 | 47 | — | DOUBLE_COIL_CANDIDATE |
| M771 | M | — | — | — | 1, 54 | DOUBLE_COIL_CANDIDATE |
| M775 | M | — | — | — | 29, 78 | DOUBLE_COIL_CANDIDATE |
| M776 | M | — | — | — | 19, 68 | DOUBLE_COIL_CANDIDATE |
| M777 | M | — | — | — | 22, 72 | DOUBLE_COIL_CANDIDATE |
| M779 | M | — | — | — | 3, 57 | DOUBLE_COIL_CANDIDATE |
| M791 | M | — | — | — | 31, 81 | DOUBLE_COIL_CANDIDATE |
| M792 | M | — | — | — | 20, 69 | DOUBLE_COIL_CANDIDATE |
| M793 | M | — | — | — | 23, 73 | DOUBLE_COIL_CANDIDATE |
