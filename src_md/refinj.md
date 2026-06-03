---
# refinj — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 189
**Blocks:** 10
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 REFRIG FAST | 1–25 | LD M21, LD M21, LD M21 ... (+1) | 21 |
| 2 | L0 REFRIG NORMAL | 27–41 | LD M22, LD M22, LD M22 | 12 |
| 3 | L0 OIL FAST | 43–62 | LD M25, LD M25, LD M25 ... (+1) | 16 |
| 4 | L0 OIL NORMAL | 64–76 | LD M26, LD M26, LD M26 | 10 |
| 5 | L0 EXHAUST | 78–85 | LD M23, LD M23 | 6 |
| 6 | L1 REFRIG FAST | 87–123 | LD M37, LD M37, LD L72 ... (+5) | 29 |
| 7 | L1 REFRIG NORMAL | 125–139 | LD M38, LD M38, LD M38 | 12 |
| 8 | L1 OIL FAST | 141–166 | LD M41, LD M41, LD L72 ... (+3) | 20 |
| 9 | L1 OIL NORMAL | 168–180 | LD M42, LD M42, LD M42 | 10 |
| 10 | L1 EXHAUST | 182–189 | LD M39, LD M39 | 6 |

## Block Detail

### Block 1: L0 REFRIG FAST (Step 1–25)

**Trigger Condition:**
- LD M21
- LD M21
- LD M21
- LD M21

**Actions:**
- SET M52
- SET M96
- OUT T4
- LD= D62
- ANB 
- LDD>= D124
- ANB 
- RST M52
- SET M22
- LD= D62
- ANB 
- LDD>= D124
- ANB 
- RST M52
- RST M96
- SET M23
- AND T4
- RST M52
- RST M96
- SET M23
- SET L69

### Block 2: L0 REFRIG NORMAL (Step 27–41)

**Trigger Condition:**
- LD M22
- LD M22
- LD M22

**Actions:**
- SET M53
- OUT T5
- LDD>= D124
- ANB 
- RST M53
- RST M96
- SET M23
- AND T5
- RST M53
- RST M96
- SET M23
- SET L69

### Block 3: L0 OIL FAST (Step 43–62)

**Trigger Condition:**
- LD M25
- LD M25
- LD M25
- LD M25

**Actions:**
- SET M54
- OUT T6
- LD= D62
- ANB 
- LDD>= D124
- ANB 
- RST M54
- SET M26
- LDD>= D124
- ANB 
- RST M54
- SET M21
- AND T6
- RST M54
- SET M23
- SET L69

### Block 4: L0 OIL NORMAL (Step 64–76)

**Trigger Condition:**
- LD M26
- LD M26
- LD M26

**Actions:**
- SET M55
- OUT T6
- LDD>= D124
- ANB 
- RST M55
- SET M21
- AND T6
- RST M55
- SET M23
- SET L69

### Block 5: L0 EXHAUST (Step 78–85)

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

### Block 6: L1 REFRIG FAST (Step 87–123)

**Trigger Condition:**
- LD M37
- LD M37
- LD L72
- LD L73
- LD M37
- LD L72
- LD L73
- LD M37

**Actions:**
- SET M68
- SET M98
- OUT T13
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- LDD>= D400
- ANB 
- RST M68
- SET M38
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- LDD>= D400
- ANB 
- RST M68
- RST M98
- SET M39
- AND T13
- RST M68
- RST M98
- SET M39
- SET L69

### Block 7: L1 REFRIG NORMAL (Step 125–139)

**Trigger Condition:**
- LD M38
- LD M38
- LD M38

**Actions:**
- SET M69
- OUT T14
- LDD>= D400
- ANB 
- RST M69
- RST M98
- SET M39
- AND T14
- RST M69
- RST M98
- SET M39
- SET L69

### Block 8: L1 OIL FAST (Step 141–166)

**Trigger Condition:**
- LD M41
- LD M41
- LD L72
- LD L73
- LD M41
- LD M41

**Actions:**
- SET M70
- OUT T15
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- LDD>= D400
- ANB 
- RST M70
- SET M42
- LDD>= D400
- ANB 
- RST M70
- SET M37
- AND T15
- RST M70
- SET M39
- SET L69

### Block 9: L1 OIL NORMAL (Step 168–180)

**Trigger Condition:**
- LD M42
- LD M42
- LD M42

**Actions:**
- SET M71
- OUT T15
- LDD>= D400
- ANB 
- RST M71
- SET M37
- AND T15
- RST M71
- SET M39
- SET L69

### Block 10: L1 EXHAUST (Step 182–189)

**Trigger Condition:**
- LD M39
- LD M39

**Actions:**
- SET M67
- OUT T12
- AND T12
- RST M67
- SET L38
- RST M39

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D104 | D |  |  |  | 3 |
| D124 | D |  |  |  | 6 |
| D400 | D |  |  |  | 6 |
| D62 | D |  |  |  | 3 |
| D90 | D |  |  |  | 3 |
| L22 | L | 1 |  |  |  |
| L38 | L | 1 |  |  |  |
| L69 | L | 8 |  |  |  |
| L72 | L |  |  |  | 3 |
| L73 | L |  |  |  | 3 |
| M21 | M | 2 |  |  | 4 |
| M22 | M | 1 |  |  | 3 |
| M23 | M | 6 | 1 |  | 2 |
| M25 | M |  |  |  | 4 |
| M26 | M | 1 |  |  | 3 |
| M37 | M | 2 |  |  | 4 |
| M38 | M | 1 |  |  | 3 |
| M39 | M | 6 | 1 |  | 2 |
| M41 | M |  |  |  | 4 |
| M42 | M | 1 |  |  | 3 |
| M51 | M | 1 | 1 |  |  |
| M52 | M | 1 | 3 |  |  |
| M53 | M | 1 | 2 |  |  |
| M54 | M | 1 | 3 |  |  |
| M55 | M | 1 | 2 |  |  |
| M67 | M | 1 | 1 |  |  |
| M68 | M | 1 | 3 |  |  |
| M69 | M | 1 | 2 |  |  |
| M70 | M | 1 | 3 |  |  |
| M71 | M | 1 | 2 |  |  |
| M96 | M | 1 | 4 |  |  |
| M98 | M | 1 | 4 |  |  |
| T12 | T |  |  | 1 | 1 |
| T13 | T |  |  | 1 | 1 |
| T14 | T |  |  | 1 | 1 |
| T15 | T |  |  | 2 | 2 |
| T3 | T |  |  | 1 | 1 |
| T4 | T |  |  | 1 | 1 |
| T5 | T |  |  | 1 | 1 |
| T6 | T |  |  | 2 | 2 |
