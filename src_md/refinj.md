---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 189
**Blocks:** 10
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 REFRIG FAST | 1–25 | LD M21, LD M21, LD M21 ... (+3) | 19 |
| 2 | L0 REFRIG NORMAL | 27–41 | LD M22, LD M22, LD M22 ... (+1) | 11 |
| 3 | L0 OIL FAST | 43–61 | LD M25, LD M25, LD M25 ... (+2) | 14 |
| 4 | L0 OIL NORMAL | 63–75 | LD M26, LD M26, LD M26 ... (+1) | 9 |
| 5 | L0 EXHAUST | 77–85 | LD M23, LD M23, LD M23 | 6 |
| 6 | L1 REFRIG FAST | 87–123 | LD M37, LD M37, LD M37 ... (+7) | 27 |
| 7 | L1 REFRIG NORMAL | 125–139 | LD M38, LD M38, LD M38 ... (+1) | 11 |
| 8 | L1 OIL FAST | 141–165 | LD M41, LD M41, LD M41 ... (+4) | 18 |
| 9 | L1 OIL NORMAL | 167–179 | LD M42, LD M42, LD M42 ... (+1) | 9 |
| 10 | L1 EXHAUST | 181–189 | LD M39, LD M39, LD M39 | 6 |

## Block Detail

### Block 1: L0 REFRIG FAST (Step 1–25)

**Trigger Condition:**
- LD M21
- LD M21
- LD M21
- LD M21
- LD M21
- LD M21

**Actions:**
- OUT M52
- OUT M96
- OUT T4
- LD= D62
- AND>= D124
- ANB 
- RST M52
- SET M22
- LD= D62
- AND>= D124
- ANB 
- RST M52
- RST M96
- SET M23
- AND T4
- RST M52
- RST M96
- SET M23
- SET M869

### Block 2: L0 REFRIG NORMAL (Step 27–41)

**Trigger Condition:**
- LD M22
- LD M22
- LD M22
- LD M22

**Actions:**
- OUT M53
- OUT T5
- AND>= D124
- RST M53
- RST M96
- SET M23
- AND T5
- RST M53
- RST M96
- SET M23
- SET M869

### Block 3: L0 OIL FAST (Step 43–61)

**Trigger Condition:**
- LD M25
- LD M25
- LD M25
- LD M25
- LD M25

**Actions:**
- OUT M54
- OUT T6
- LD= D62
- AND>= D124
- ANB 
- RST M54
- SET M26
- AND>= D124
- RST M54
- SET M21
- AND T6
- RST M54
- SET M23
- SET M869

### Block 4: L0 OIL NORMAL (Step 63–75)

**Trigger Condition:**
- LD M26
- LD M26
- LD M26
- LD M26

**Actions:**
- OUT M55
- OUT T6
- AND>= D124
- RST M55
- SET M21
- AND T6
- RST M55
- SET M23
- SET M869

### Block 5: L0 EXHAUST (Step 77–85)

**Trigger Condition:**
- LD M23
- LD M23
- LD M23

**Actions:**
- OUT M51
- OUT T3
- AND T3
- RST M51
- SET M822
- RST M23

### Block 6: L1 REFRIG FAST (Step 87–123)

**Trigger Condition:**
- LD M37
- LD M37
- LD M37
- LD M37
- LD M872
- LD M873
- LD M37
- LD M872
- LD M873
- LD M37

**Actions:**
- OUT M68
- OUT M98
- OUT T13
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- RST M68
- SET M38
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- RST M68
- RST M98
- SET M39
- AND T13
- RST M68
- RST M98
- SET M39
- SET M869

### Block 7: L1 REFRIG NORMAL (Step 125–139)

**Trigger Condition:**
- LD M38
- LD M38
- LD M38
- LD M38

**Actions:**
- OUT M69
- OUT T14
- AND>= D400
- RST M69
- RST M98
- SET M39
- AND T14
- RST M69
- RST M98
- SET M39
- SET M869

### Block 8: L1 OIL FAST (Step 141–165)

**Trigger Condition:**
- LD M41
- LD M41
- LD M41
- LD M872
- LD M873
- LD M41
- LD M41

**Actions:**
- OUT M70
- OUT T15
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- RST M70
- SET M42
- AND>= D400
- RST M70
- SET M37
- AND T15
- RST M70
- SET M39
- SET M869

### Block 9: L1 OIL NORMAL (Step 167–179)

**Trigger Condition:**
- LD M42
- LD M42
- LD M42
- LD M42

**Actions:**
- OUT M71
- OUT T15
- AND>= D400
- RST M71
- SET M37
- AND T15
- RST M71
- SET M39
- SET M869

### Block 10: L1 EXHAUST (Step 181–189)

**Trigger Condition:**
- LD M39
- LD M39
- LD M39

**Actions:**
- OUT M67
- OUT T12
- AND T12
- RST M67
- SET M838
- RST M39

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D104 | D |  |  |  | 3 |
| D124 | D |  |  |  | 6 |
| D400 | D |  |  |  | 6 |
| D62 | D |  |  |  | 3 |
| D90 | D |  |  |  | 3 |
| M21 | M | 2 |  |  | 6 |
| M22 | M | 1 |  |  | 4 |
| M23 | M | 6 | 1 |  | 3 |
| M25 | M |  |  |  | 5 |
| M26 | M | 1 |  |  | 4 |
| M37 | M | 2 |  |  | 6 |
| M38 | M | 1 |  |  | 4 |
| M39 | M | 6 | 1 |  | 3 |
| M41 | M |  |  |  | 5 |
| M42 | M | 1 |  |  | 4 |
| M51 | M |  | 1 | 1 |  |
| M52 | M |  | 3 | 1 |  |
| M53 | M |  | 2 | 1 |  |
| M54 | M |  | 3 | 1 |  |
| M55 | M |  | 2 | 1 |  |
| M67 | M |  | 1 | 1 |  |
| M68 | M |  | 3 | 1 |  |
| M69 | M |  | 2 | 1 |  |
| M70 | M |  | 3 | 1 |  |
| M71 | M |  | 2 | 1 |  |
| M822 | M | 1 |  |  |  |
| M838 | M | 1 |  |  |  |
| M869 | M | 8 |  |  |  |
| M872 | M |  |  |  | 3 |
| M873 | M |  |  |  | 3 |
| M96 | M |  | 4 | 1 |  |
| M98 | M |  | 4 | 1 |  |
| T12 | T |  |  | 1 | 1 |
| T13 | T |  |  | 1 | 1 |
| T14 | T |  |  | 1 | 1 |
| T15 | T |  |  | 2 | 2 |
| T3 | T |  |  | 1 | 1 |
| T4 | T |  |  | 1 | 1 |
| T5 | T |  |  | 1 | 1 |
| T6 | T |  |  | 2 | 2 |
