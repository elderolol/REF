---
# gmes — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 100
**Blocks:** 6
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | PC COMM L1 | 0–39 | LD M0, LD M0, LD M0 | 20 |
| 2 | PC COMM L2 | 40–79 | LD M0, LD M0, LD M0 | 20 |
| 3 | GAS TYPE MAP | 80–84 | LD M0, LD M0 | 2 |
| 4 | AUTO BARCODE | 85–89 | LDD> D7001, LDD> D8001 | 2 |
| 5 | VAC SPC DATA | 90–94 | LD M18, LD M34 | 2 |
| 6 | RESULT CODE | 95–100 | LD M24, LD M40 | 3 |

## Block Detail

### Block 1: PC COMM L1 (Step 0–39)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD L3
- LDI L3
- LD M16
- LDI M16
- LD M18
- LD M19
- LD M20
- LD M21
- LD M16

**Actions:**
- MOV D7000
- MOV D7001
- DMOV D130
- MOV D142
- MOV D142
- MOV D140
- DMOV D160
- DMOV D22
- MOV K1
- MOV K0
- MOV K1
- MOV K2
- MOV K0
- MOV K1
- MOV K1
- MOV K2
- MOV K3
- OR M22
- MOV K4
- MOV K0

### Block 2: PC COMM L2 (Step 40–79)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD L3
- LDI L3
- LD M32
- LDI M32
- LD M34
- LD M35
- LD M36
- LD M37
- LD M32

**Actions:**
- MOV D8000
- MOV D8001
- DMOV D130
- MOV D148
- MOV D148
- MOV D146
- DMOV D172
- DMOV D50
- MOV K2
- MOV K0
- MOV K1
- MOV K2
- MOV K0
- MOV K1
- MOV K1
- MOV K2
- MOV K3
- OR M38
- MOV K4
- MOV K0

### Block 3: GAS TYPE MAP (Step 80–84)

**Trigger Condition:**
- LD M0
- LD M0

**Actions:**
- MOV D7000
- MOV D8000

### Block 4: AUTO BARCODE (Step 85–89)

**Trigger Condition:**
- LDD> D7001
- LDD> D8001

**Actions:**
- BMOV D6870
- BMOV D7870

### Block 5: VAC SPC DATA (Step 90–94)

**Trigger Condition:**
- LD M18
- LD M34

**Actions:**
- D* D160
- D* D172

### Block 6: RESULT CODE (Step 95–100)

**Trigger Condition:**
- LD M24
- LD M40

**Actions:**
- MOV K1
- MOV K1
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D130 | D | — | — | — | 6, 46 | DOUBLE_COIL_CANDIDATE |
| D140 | D | — | — | — | 12 |  |
| D142 | D | — | — | — | 8, 10 |  |
| D146 | D | — | — | — | 52 |  |
| D148 | D | — | — | — | 48, 50 |  |
| D160 | D | — | — | — | 14 | DOUBLE_COIL_CANDIDATE |
| D172 | D | — | — | — | 54 | DOUBLE_COIL_CANDIDATE |
| D22 | D | — | — | — | 16 |  |
| D50 | D | — | — | — | 56 |  |
| D6870 | D | — | — | — | 87 |  |
| D7000 | D | — | — | — | 2, 82 | DOUBLE_COIL_CANDIDATE |
| D7001 | D | — | — | — | 4, 86 | DOUBLE_COIL_CANDIDATE |
| D7870 | D | — | — | — | 89 |  |
| D8000 | D | — | — | — | 42, 84 | DOUBLE_COIL_CANDIDATE |
| D8001 | D | — | — | — | 44, 88 | DOUBLE_COIL_CANDIDATE |
| K0 | K | — | — | — | 20, 26, 39, 60, 66, 79 | DOUBLE_COIL_CANDIDATE |
| K1 | K | — | — | — | 18, 22, 28, 30, 62, 68, 70, 97, 99 | DOUBLE_COIL_CANDIDATE |
| K2 | K | — | — | — | 24, 32, 58, 64, 72 | DOUBLE_COIL_CANDIDATE |
| K3 | K | — | — | — | 34, 74 | DOUBLE_COIL_CANDIDATE |
| K4 | K | — | — | — | 37, 77 | DOUBLE_COIL_CANDIDATE |
| L3 | L | — | — | — | 21, 23, 61, 63 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| M0 | M | — | — | — | 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 81, 83 | DOUBLE_COIL_CANDIDATE |
| M16 | M | — | — | — | 25, 27, 38 |  |
| M18 | M | — | — | — | 29, 91 | DOUBLE_COIL_CANDIDATE |
| M19 | M | — | — | — | 31 |  |
| M20 | M | — | — | — | 33 |  |
| M21 | M | — | — | — | 35 |  |
| M22 | M | — | — | — | 36 |  |
| M24 | M | — | — | — | 96 |  |
| M32 | M | — | — | — | 65, 67, 78 |  |
| M34 | M | — | — | — | 69, 93 | DOUBLE_COIL_CANDIDATE |
| M35 | M | — | — | — | 71 |  |
| M36 | M | — | — | — | 73 |  |
| M37 | M | — | — | — | 75 |  |
| M38 | M | — | — | — | 76 |  |
| M40 | M | — | — | — | 98 |  |
