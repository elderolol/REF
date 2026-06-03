---
# indexs — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 647
**Blocks:** 8
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | PC DATA CHECK | 1–10 | LD L3, LD L3 | 8 |
| 2 | AUTO BARCODE | 12–15 |  | 4 |
| 3 | BARCODE L1 (D60~D84) | 17–166 | LD L3, LD L3, LD L3 ... (+22) | 125 |
| 4 | BARCODE L2 (D88~D112) | 168–317 | LD L3, LD L3, LD L3 ... (+22) | 125 |
| 5 | MANUAL MODEL L0 | 319–468 | LDI L3, LDI L3, LDI L3 ... (+22) | 125 |
| 6 | MANUAL MODEL L1 | 470–619 | LDI L3, LDI L3, LDI L3 ... (+22) | 125 |
| 7 | BARCODE RESET | 621–635 | LD L24, LD L40 | 13 |
| 8 | BARCODE MODEL CLEANUP | 637–647 | LD L3, LD L17 | 9 |

## Block Detail

### Block 1: PC DATA CHECK (Step 1–10)

**Trigger Condition:**
- LD L3
- LD L3

**Actions:**
- LDD> D7001
- LD<> D7000
- ANB 
- SET L76
- LDD> D8001
- LD<> D8000
- ANB 
- SET L76

### Block 2: AUTO BARCODE (Step 12–15)

**Trigger Condition:**

**Actions:**
- LDD> D7001
- BMOV D6980
- LDD> D8001
- BMOV D7980

### Block 3: BARCODE L1 (D60~D84) (Step 17–166)

**Trigger Condition:**
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3

**Actions:**
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K1
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K2
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K3
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K4
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K5
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K6
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K7
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K8
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K9
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K10
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K11
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K12
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K13
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K14
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K15
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K16
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K17
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K18
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K19
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K20
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K21
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K22
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K23
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K24
- LDD> D7001
- ANB 
- LDD= D7001
- ANB 
- MOV K25

### Block 4: BARCODE L2 (D88~D112) (Step 168–317)

**Trigger Condition:**
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3
- LD L3

**Actions:**
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K1
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K2
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K3
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K4
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K5
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K6
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K7
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K8
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K9
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K10
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K11
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K12
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K13
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K14
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K15
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K16
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K17
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K18
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K19
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K20
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K21
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K22
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K23
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K24
- LDD> D8001
- ANB 
- LDD= D8001
- ANB 
- MOV K25

### Block 5: MANUAL MODEL L0 (Step 319–468)

**Trigger Condition:**
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3

**Actions:**
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D60
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D61
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D62
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D63
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D64
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D65
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D66
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D67
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D68
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D69
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D70
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D71
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D72
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D73
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D74
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D75
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D76
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D77
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D78
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D79
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D80
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D81
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D82
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D83
- AND> D0
- AND<= D0
- LD= D0
- ANB 
- MOV D84

### Block 6: MANUAL MODEL L1 (Step 470–619)

**Trigger Condition:**
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3
- LDI L3

**Actions:**
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D88
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D89
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D90
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D91
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D92
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D93
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D94
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D95
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D96
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D97
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D98
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D99
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D100
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D101
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D102
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D103
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D104
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D105
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D106
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D107
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D108
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D109
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D110
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D111
- AND> D30
- AND<= D30
- LD= D30
- ANB 
- MOV D112

### Block 7: BARCODE RESET (Step 621–635)

**Trigger Condition:**
- LD L24
- LD L40

**Actions:**
- AND M16
- AND M32
- ORB 
- OR L17
- OR L19
- OR L21
- OR L23
- OR L64
- MOV K0
- MOV K0
- MOV K0
- MOV K0
- MOV K0

### Block 8: BARCODE MODEL CLEANUP (Step 637–647)

**Trigger Condition:**
- LD L3
- LD L17

**Actions:**
- OR L19
- OR L21
- OR L23
- OR L24
- OR L40
- OR L64
- ANB 
- RST D0
- RST D30

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D0 | D |  | 1 |  | 75 |
| D100 | D |  |  |  | 1 |
| D101 | D |  |  |  | 1 |
| D102 | D |  |  |  | 1 |
| D103 | D |  |  |  | 1 |
| D104 | D |  |  |  | 1 |
| D105 | D |  |  |  | 1 |
| D106 | D |  |  |  | 1 |
| D107 | D |  |  |  | 1 |
| D108 | D |  |  |  | 1 |
| D109 | D |  |  |  | 1 |
| D110 | D |  |  |  | 1 |
| D111 | D |  |  |  | 1 |
| D112 | D |  |  |  | 1 |
| D30 | D |  | 1 |  | 75 |
| D60 | D |  |  |  | 1 |
| D61 | D |  |  |  | 1 |
| D62 | D |  |  |  | 1 |
| D63 | D |  |  |  | 1 |
| D64 | D |  |  |  | 1 |
| D65 | D |  |  |  | 1 |
| D66 | D |  |  |  | 1 |
| D67 | D |  |  |  | 1 |
| D68 | D |  |  |  | 1 |
| D69 | D |  |  |  | 1 |
| D6980 | D |  |  |  | 1 |
| D70 | D |  |  |  | 1 |
| D7000 | D |  |  |  | 1 |
| D7001 | D |  |  |  | 52 |
| D71 | D |  |  |  | 1 |
| D72 | D |  |  |  | 1 |
| D73 | D |  |  |  | 1 |
| D74 | D |  |  |  | 1 |
| D75 | D |  |  |  | 1 |
| D76 | D |  |  |  | 1 |
| D77 | D |  |  |  | 1 |
| D78 | D |  |  |  | 1 |
| D79 | D |  |  |  | 1 |
| D7980 | D |  |  |  | 1 |
| D80 | D |  |  |  | 1 |
| D8000 | D |  |  |  | 1 |
| D8001 | D |  |  |  | 52 |
| D81 | D |  |  |  | 1 |
| D82 | D |  |  |  | 1 |
| D83 | D |  |  |  | 1 |
| D84 | D |  |  |  | 1 |
| D88 | D |  |  |  | 1 |
| D89 | D |  |  |  | 1 |
| D90 | D |  |  |  | 1 |
| D91 | D |  |  |  | 1 |
| D92 | D |  |  |  | 1 |
| D93 | D |  |  |  | 1 |
| D94 | D |  |  |  | 1 |
| D95 | D |  |  |  | 1 |
| D96 | D |  |  |  | 1 |
| D97 | D |  |  |  | 1 |
| D98 | D |  |  |  | 1 |
| D99 | D |  |  |  | 1 |
| K0 | K |  |  |  | 5 |
| K1 | K |  |  |  | 2 |
| K10 | K |  |  |  | 2 |
| K11 | K |  |  |  | 2 |
| K12 | K |  |  |  | 2 |
| K13 | K |  |  |  | 2 |
| K14 | K |  |  |  | 2 |
| K15 | K |  |  |  | 2 |
| K16 | K |  |  |  | 2 |
| K17 | K |  |  |  | 2 |
| K18 | K |  |  |  | 2 |
| K19 | K |  |  |  | 2 |
| K2 | K |  |  |  | 2 |
| K20 | K |  |  |  | 2 |
| K21 | K |  |  |  | 2 |
| K22 | K |  |  |  | 2 |
| K23 | K |  |  |  | 2 |
| K24 | K |  |  |  | 2 |
| K25 | K |  |  |  | 2 |
| K3 | K |  |  |  | 2 |
| K4 | K |  |  |  | 2 |
| K5 | K |  |  |  | 2 |
| K6 | K |  |  |  | 2 |
| K7 | K |  |  |  | 2 |
| K8 | K |  |  |  | 2 |
| K9 | K |  |  |  | 2 |
| L17 | L |  |  |  | 2 |
| L19 | L |  |  |  | 2 |
| L21 | L |  |  |  | 2 |
| L23 | L |  |  |  | 2 |
| L24 | L |  |  |  | 2 |
| L3 | L |  |  |  | 103 |
| L40 | L |  |  |  | 2 |
| L64 | L |  |  |  | 2 |
| L76 | L | 2 |  |  |  |
| M16 | M |  |  |  | 1 |
| M32 | M |  |  |  | 1 |
