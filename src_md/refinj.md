---
# refinj — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 138
**Blocks:** 10
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 REFRIG FAST | 0–25 | LD M21, LD M21, LD= D62 | 17 |
| 2 | L0 REFRIG NORMAL | 26–35 | LD M22, LD M22, LDD>= D124 | 6 |
| 3 | L0 OIL FAST | 36–51 | LD M25, LD M25, LD= D62 | 9 |
| 4 | L0 OIL NORMAL | 52–59 | LD M26, LD M26, LDD>= D124 | 4 |
| 5 | L0 EXHAUST | 60–68 | LD M23, LD M23 | 6 |
| 6 | L1 REFRIG FAST | 69–94 | LD M37, LD M37, LD= D62 | 17 |
| 7 | L1 REFRIG NORMAL | 95–104 | LD M38, LD M38, LDD>= D124 | 6 |
| 8 | L1 OIL FAST | 105–120 | LD M41, LD M41, LD= D62 | 9 |
| 9 | L1 OIL NORMAL | 121–128 | LD M42, LD M42, LDD>= D124 | 4 |
| 10 | L1 EXHAUST | 129–138 | LD M39, LD M39 | 7 |

## Block Detail

### Block 1: L0 REFRIG FAST (Step 0–25)

**Trigger Condition:**
- LD M21
- LD M21
- LD= D62
- LDD>= D124
- LD M21
- LD= D62
- LDD>= D124
- LD M21

**Actions:**
- SET M52
- SET M96
- OUT T4
- ANB 
- ANB 
- RST M52
- SET M22
- ANB 
- ANB 
- RST M52
- RST M96
- SET M23
- AND T4
- RST M52
- RST M96
- SET M23
- SET L69

### Block 2: L0 REFRIG NORMAL (Step 26–35)

**Trigger Condition:**
- LD M22
- LD M22
- LDD>= D124

**Actions:**
- SET M53
- OUT T5
- ANB 
- RST M53
- RST M96
- SET M23

### Block 3: L0 OIL FAST (Step 36–51)

**Trigger Condition:**
- LD M25
- LD M25
- LD= D62
- LDD>= D124
- LD M25
- LDD>= D124

**Actions:**
- SET M54
- OUT T6
- ANB 
- ANB 
- RST M54
- SET M26
- ANB 
- RST M54
- SET M21

### Block 4: L0 OIL NORMAL (Step 52–59)

**Trigger Condition:**
- LD M26
- LD M26
- LDD>= D124

**Actions:**
- SET M55
- ANB 
- RST M55
- SET M21

### Block 5: L0 EXHAUST (Step 60–68)

**Trigger Condition:**
- LD M23
- LD M23

**Actions:**
- SET M51
- OUT T3
- AND T3
- RST M51
- SET L22
- RST M23

### Block 6: L1 REFRIG FAST (Step 69–94)

**Trigger Condition:**
- LD M37
- LD M37
- LD= D62
- LDD>= D124
- LD M37
- LD= D62
- LDD>= D124
- LD M37

**Actions:**
- SET M68
- SET M98
- OUT T4
- ANB 
- ANB 
- RST M68
- SET M38
- ANB 
- ANB 
- RST M68
- RST M98
- SET M39
- AND T4
- RST M68
- RST M98
- SET M39
- SET L69

### Block 7: L1 REFRIG NORMAL (Step 95–104)

**Trigger Condition:**
- LD M38
- LD M38
- LDD>= D124

**Actions:**
- SET M69
- OUT T5
- ANB 
- RST M69
- RST M98
- SET M39

### Block 8: L1 OIL FAST (Step 105–120)

**Trigger Condition:**
- LD M41
- LD M41
- LD= D62
- LDD>= D124
- LD M41
- LDD>= D124

**Actions:**
- SET M70
- OUT T6
- ANB 
- ANB 
- RST M70
- SET M42
- ANB 
- RST M70
- SET M37

### Block 9: L1 OIL NORMAL (Step 121–128)

**Trigger Condition:**
- LD M42
- LD M42
- LDD>= D124

**Actions:**
- SET M71
- ANB 
- RST M71
- SET M37

### Block 10: L1 EXHAUST (Step 129–138)

**Trigger Condition:**
- LD M39
- LD M39

**Actions:**
- SET M67
- OUT T3
- AND T3
- RST M67
- SET L38
- RST M39
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D124 | D | — | — | — | 8, 15, 31, 43, 48, 56, 77, 84, 100, 112, 117, 125 | DOUBLE_COIL_CANDIDATE |
| D62 | D | — | — | — | 6, 13, 41, 75, 82, 110 | DOUBLE_COIL_CANDIDATE |
| L22 | L | 67 | — | — | — | NO_RST, LATCH_DEVICE |
| L38 | L | 136 | — | — | — | NO_RST, LATCH_DEVICE |
| L69 | L | 25, 94 | — | — | — | NO_RST, LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| M21 | M | 51, 59 | — | — | 1, 5, 12, 20 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M22 | M | 11 | — | — | 27, 30 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M23 | M | 19, 24, 35 | 68 | — | 61, 64 | DOUBLE_COIL_CANDIDATE |
| M25 | M | — | — | — | 37, 40, 47 |  |
| M26 | M | 46 | — | — | 53, 55 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M37 | M | 120, 128 | — | — | 70, 74, 81, 89 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M38 | M | 80 | — | — | 96, 99 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M39 | M | 88, 93, 104 | 137 | — | 130, 133 | DOUBLE_COIL_CANDIDATE |
| M41 | M | — | — | — | 106, 109, 116 |  |
| M42 | M | 115 | — | — | 122, 124 | NO_RST, DOUBLE_COIL_CANDIDATE |
| M51 | M | 62 | 66 | — | — |  |
| M52 | M | 2 | 10, 17, 22 | — | — |  |
| M53 | M | 28 | 33 | — | — |  |
| M54 | M | 38 | 45, 50 | — | — |  |
| M55 | M | 54 | 58 | — | — |  |
| M67 | M | 131 | 135 | — | — |  |
| M68 | M | 71 | 79, 86, 91 | — | — |  |
| M69 | M | 97 | 102 | — | — |  |
| M70 | M | 107 | 114, 119 | — | — |  |
| M71 | M | 123 | 127 | — | — |  |
| M96 | M | 3 | 18, 23, 34 | — | — | DOUBLE_COIL_CANDIDATE |
| M98 | M | 72 | 87, 92, 103 | — | — | DOUBLE_COIL_CANDIDATE |
| T3 | T | — | — | 63, 132 | 65, 134 | DOUBLE_COIL_CANDIDATE |
| T4 | T | — | — | 4, 73 | 21, 90 | DOUBLE_COIL_CANDIDATE |
| T5 | T | — | — | 29, 98 | — | DOUBLE_COIL_CANDIDATE |
| T6 | T | — | — | 39, 108 | — | DOUBLE_COIL_CANDIDATE |
