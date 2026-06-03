---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 81
**Blocks:** 2
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | PC COMM L1 | 1–40 | LD M23, LD M23, LD M23 ... (+15) | 22 |
| 2 | PC COMM L2 | 42–81 | LD M39, LD M39, LD M39 ... (+15) | 22 |

## Block Detail

### Block 1: PC COMM L1 (Step 1–40)

**Trigger Condition:**
- LD M23
- LD M23
- LD M23
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M803
- LDI M803
- LD M16
- LDI M16
- LD M18
- LD M19
- LD M20
- LD M21
- LD M16

**Actions:**
- LD> D7001
- MOV D7000
- MOV D7001
- DMOV D130
- MOV D142
- MOV D142
- MOV D7007
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

### Block 2: PC COMM L2 (Step 42–81)

**Trigger Condition:**
- LD M39
- LD M39
- LD M39
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M803
- LDI M803
- LD M32
- LDI M32
- LD M34
- LD M35
- LD M36
- LD M37
- LD M32

**Actions:**
- LD> D8001
- MOV D8000
- MOV D8001
- DMOV D406
- MOV D148
- MOV D148
- MOV D8007
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

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D130 | D |  |  |  | 1 |
| D140 | D |  |  |  | 1 |
| D142 | D |  |  |  | 2 |
| D146 | D |  |  |  | 1 |
| D148 | D |  |  |  | 2 |
| D160 | D |  |  |  | 1 |
| D172 | D |  |  |  | 1 |
| D22 | D |  |  |  | 1 |
| D406 | D |  |  |  | 1 |
| D50 | D |  |  |  | 1 |
| D7000 | D |  |  |  | 1 |
| D7001 | D |  |  |  | 2 |
| D7007 | D |  |  |  | 1 |
| D8000 | D |  |  |  | 1 |
| D8001 | D |  |  |  | 2 |
| D8007 | D |  |  |  | 1 |
| K0 | K |  |  |  | 6 |
| K1 | K |  |  |  | 7 |
| K2 | K |  |  |  | 5 |
| K3 | K |  |  |  | 2 |
| K4 | K |  |  |  | 2 |
| M0 | M |  |  |  | 12 |
| M16 | M |  |  |  | 3 |
| M18 | M |  |  |  | 1 |
| M19 | M |  |  |  | 1 |
| M20 | M |  |  |  | 1 |
| M21 | M |  |  |  | 1 |
| M22 | M |  |  |  | 1 |
| M23 | M |  |  |  | 3 |
| M32 | M |  |  |  | 3 |
| M34 | M |  |  |  | 1 |
| M35 | M |  |  |  | 1 |
| M36 | M |  |  |  | 1 |
| M37 | M |  |  |  | 1 |
| M38 | M |  |  |  | 1 |
| M39 | M |  |  |  | 3 |
| M803 | M |  |  |  | 4 |
