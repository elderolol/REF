---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 495
**Blocks:** 8
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | PC DATA CHECK | 1–8 | LD M803, LD M803 | 6 |
| 2 | AUTO BARCODE | 10–13 |  | 4 |
| 3 | BARCODE L1 (D60~D84) | 15–114 | LD M803, LD M803, LD M803 ... (+22) | 75 |
| 4 | BARCODE L2 (D88~D112) | 116–215 | LD M803, LD M803, LD M803 ... (+22) | 75 |
| 5 | MANUAL MODEL L0 | 217–341 | LDI M803, LDI M803, LDI M803 ... (+22) | 100 |
| 6 | MANUAL MODEL L1 | 343–467 | LDI M803, LDI M803, LDI M803 ... (+22) | 100 |
| 7 | BARCODE RESET | 469–483 | LD M824, LD M840 | 13 |
| 8 | BARCODE MODEL CLEANUP | 485–495 | LD M803, LD M817 | 9 |

## Block Detail

### Block 1: PC DATA CHECK (Step 1–8)

**Trigger Condition:**
- LD M803
- LD M803

**Actions:**
- AND> D7001
- AND<> D7000
- AND> D8001
- AND<> D8000
- ORB 
- SET M876

### Block 2: AUTO BARCODE (Step 10–13)

**Trigger Condition:**

**Actions:**
- LD> D7001
- BMOV D6980
- LD> D8001
- BMOV D7980

### Block 3: BARCODE L1 (D60~D84) (Step 15–114)

**Trigger Condition:**
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803

**Actions:**
- AND> D7001
- AND= D7001
- MOV K1
- AND> D7001
- AND= D7001
- MOV K2
- AND> D7001
- AND= D7001
- MOV K3
- AND> D7001
- AND= D7001
- MOV K4
- AND> D7001
- AND= D7001
- MOV K5
- AND> D7001
- AND= D7001
- MOV K6
- AND> D7001
- AND= D7001
- MOV K7
- AND> D7001
- AND= D7001
- MOV K8
- AND> D7001
- AND= D7001
- MOV K9
- AND> D7001
- AND= D7001
- MOV K10
- AND> D7001
- AND= D7001
- MOV K11
- AND> D7001
- AND= D7001
- MOV K12
- AND> D7001
- AND= D7001
- MOV K13
- AND> D7001
- AND= D7001
- MOV K14
- AND> D7001
- AND= D7001
- MOV K15
- AND> D7001
- AND= D7001
- MOV K16
- AND> D7001
- AND= D7001
- MOV K17
- AND> D7001
- AND= D7001
- MOV K18
- AND> D7001
- AND= D7001
- MOV K19
- AND> D7001
- AND= D7001
- MOV K20
- AND> D7001
- AND= D7001
- MOV K21
- AND> D7001
- AND= D7001
- MOV K22
- AND> D7001
- AND= D7001
- MOV K23
- AND> D7001
- AND= D7001
- MOV K24
- AND> D7001
- AND= D7001
- MOV K25

### Block 4: BARCODE L2 (D88~D112) (Step 116–215)

**Trigger Condition:**
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803
- LD M803

**Actions:**
- AND> D8001
- AND= D8001
- MOV K1
- AND> D8001
- AND= D8001
- MOV K2
- AND> D8001
- AND= D8001
- MOV K3
- AND> D8001
- AND= D8001
- MOV K4
- AND> D8001
- AND= D8001
- MOV K5
- AND> D8001
- AND= D8001
- MOV K6
- AND> D8001
- AND= D8001
- MOV K7
- AND> D8001
- AND= D8001
- MOV K8
- AND> D8001
- AND= D8001
- MOV K9
- AND> D8001
- AND= D8001
- MOV K10
- AND> D8001
- AND= D8001
- MOV K11
- AND> D8001
- AND= D8001
- MOV K12
- AND> D8001
- AND= D8001
- MOV K13
- AND> D8001
- AND= D8001
- MOV K14
- AND> D8001
- AND= D8001
- MOV K15
- AND> D8001
- AND= D8001
- MOV K16
- AND> D8001
- AND= D8001
- MOV K17
- AND> D8001
- AND= D8001
- MOV K18
- AND> D8001
- AND= D8001
- MOV K19
- AND> D8001
- AND= D8001
- MOV K20
- AND> D8001
- AND= D8001
- MOV K21
- AND> D8001
- AND= D8001
- MOV K22
- AND> D8001
- AND= D8001
- MOV K23
- AND> D8001
- AND= D8001
- MOV K24
- AND> D8001
- AND= D8001
- MOV K25

### Block 5: MANUAL MODEL L0 (Step 217–341)

**Trigger Condition:**
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803

**Actions:**
- AND> D0
- AND<= D0
- AND= D0
- MOV D60
- AND> D0
- AND<= D0
- AND= D0
- MOV D61
- AND> D0
- AND<= D0
- AND= D0
- MOV D62
- AND> D0
- AND<= D0
- AND= D0
- MOV D63
- AND> D0
- AND<= D0
- AND= D0
- MOV D64
- AND> D0
- AND<= D0
- AND= D0
- MOV D65
- AND> D0
- AND<= D0
- AND= D0
- MOV D66
- AND> D0
- AND<= D0
- AND= D0
- MOV D67
- AND> D0
- AND<= D0
- AND= D0
- MOV D68
- AND> D0
- AND<= D0
- AND= D0
- MOV D69
- AND> D0
- AND<= D0
- AND= D0
- MOV D70
- AND> D0
- AND<= D0
- AND= D0
- MOV D71
- AND> D0
- AND<= D0
- AND= D0
- MOV D72
- AND> D0
- AND<= D0
- AND= D0
- MOV D73
- AND> D0
- AND<= D0
- AND= D0
- MOV D74
- AND> D0
- AND<= D0
- AND= D0
- MOV D75
- AND> D0
- AND<= D0
- AND= D0
- MOV D76
- AND> D0
- AND<= D0
- AND= D0
- MOV D77
- AND> D0
- AND<= D0
- AND= D0
- MOV D78
- AND> D0
- AND<= D0
- AND= D0
- MOV D79
- AND> D0
- AND<= D0
- AND= D0
- MOV D80
- AND> D0
- AND<= D0
- AND= D0
- MOV D81
- AND> D0
- AND<= D0
- AND= D0
- MOV D82
- AND> D0
- AND<= D0
- AND= D0
- MOV D83
- AND> D0
- AND<= D0
- AND= D0
- MOV D84

### Block 6: MANUAL MODEL L1 (Step 343–467)

**Trigger Condition:**
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803
- LDI M803

**Actions:**
- AND> D30
- AND<= D30
- AND= D30
- MOV D88
- AND> D30
- AND<= D30
- AND= D30
- MOV D89
- AND> D30
- AND<= D30
- AND= D30
- MOV D90
- AND> D30
- AND<= D30
- AND= D30
- MOV D91
- AND> D30
- AND<= D30
- AND= D30
- MOV D92
- AND> D30
- AND<= D30
- AND= D30
- MOV D93
- AND> D30
- AND<= D30
- AND= D30
- MOV D94
- AND> D30
- AND<= D30
- AND= D30
- MOV D95
- AND> D30
- AND<= D30
- AND= D30
- MOV D96
- AND> D30
- AND<= D30
- AND= D30
- MOV D97
- AND> D30
- AND<= D30
- AND= D30
- MOV D98
- AND> D30
- AND<= D30
- AND= D30
- MOV D99
- AND> D30
- AND<= D30
- AND= D30
- MOV D100
- AND> D30
- AND<= D30
- AND= D30
- MOV D101
- AND> D30
- AND<= D30
- AND= D30
- MOV D102
- AND> D30
- AND<= D30
- AND= D30
- MOV D103
- AND> D30
- AND<= D30
- AND= D30
- MOV D104
- AND> D30
- AND<= D30
- AND= D30
- MOV D105
- AND> D30
- AND<= D30
- AND= D30
- MOV D106
- AND> D30
- AND<= D30
- AND= D30
- MOV D107
- AND> D30
- AND<= D30
- AND= D30
- MOV D108
- AND> D30
- AND<= D30
- AND= D30
- MOV D109
- AND> D30
- AND<= D30
- AND= D30
- MOV D110
- AND> D30
- AND<= D30
- AND= D30
- MOV D111
- AND> D30
- AND<= D30
- AND= D30
- MOV D112

### Block 7: BARCODE RESET (Step 469–483)

**Trigger Condition:**
- LD M824
- LD M840

**Actions:**
- AND M16
- AND M32
- ORB 
- OR M817
- OR M819
- OR M821
- OR M823
- OR M864
- MOV K0
- MOV K0
- MOV K0
- MOV K0
- MOV K0

### Block 8: BARCODE MODEL CLEANUP (Step 485–495)

**Trigger Condition:**
- LD M803
- LD M817

**Actions:**
- OR M819
- OR M821
- OR M823
- OR M824
- OR M840
- OR M864
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
| M16 | M |  |  |  | 1 |
| M32 | M |  |  |  | 1 |
| M803 | M |  |  |  | 103 |
| M817 | M |  |  |  | 2 |
| M819 | M |  |  |  | 2 |
| M821 | M |  |  |  | 2 |
| M823 | M |  |  |  | 2 |
| M824 | M |  |  |  | 2 |
| M840 | M |  |  |  | 2 |
| M864 | M |  |  |  | 2 |
| M876 | M | 1 |  |  |  |
