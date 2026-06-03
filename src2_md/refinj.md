---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 215
**Blocks:** 14
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | L0 REFRIG FAST | 1–6 | LD M21, LD M21, LD M21 | 3 |
| 2 | L0 REFRIG NORMAL | 8–11 | LD M22, LD M22 | 2 |
| 3 | L0 OIL FAST | 13–27 | LD M23, LD M25, LD M25 | 12 |
| 4 | L0 OIL NORMAL | 29–40 | LD M25, LD M26 | 10 |
| 5 | L0 EXHAUST | 42–43 | LD M23 | 1 |
| 6 | L1 REFRIG FAST | 45–50 | LD M37, LD M37, LD M37 | 3 |
| 7 | L1 REFRIG NORMAL | 52–55 | LD M38, LD M38 | 2 |
| 8 | L1 OIL FAST | 57–71 | LD M39, LD M41, LD M41 | 12 |
| 9 | L1 OIL NORMAL | 73–90 | LD M41, LD M872, LD M873 ... (+1) | 14 |
| 10 | L1 EXHAUST | 92–95 | LD M39, LD M39 | 2 |
| 11 | COMPLETION L0 (M822) | 97–126 | LD M21, LD M21, LD M21 ... (+5) | 22 |
| 12 | COMPLETION L1 (M838) | 128–169 | LD M37, LD M872, LD M873 ... (+9) | 30 |
| 13 | TIMEOUT ALARM TRIGGERS | 171–198 | LD M21, LD M22, LD M25 ... (+5) | 20 |
| 14 | OIL RESTART FLAGS | 200–215 | LD M25, LD M26, LD M41 ... (+1) | 12 |

## Block Detail

### Block 1: L0 REFRIG FAST (Step 1-6)

**Trigger Condition:**
- LD M21
- LD M21
- LD M21

**Actions:**
- OUT M52
- OUT M96
- OUT T4

### Block 2: L0 REFRIG NORMAL (Step 8-11)

**Trigger Condition:**
- LD M22
- LD M22

**Actions:**
- OUT M53
- OUT T5

### Block 3: L0 OIL FAST (Step 13-27)

**Trigger Condition:**
- LD M23
- LD M25
- LD M25

**Actions:**
- ANI T3
- ANI M822
- OR M25
- ANI M26
- ANI M340
- ANI M320
- ANI M301
- ANI M304
- OUT M25
- OUT M54
- OR M26
- OUT T6

### Block 4: L0 OIL NORMAL (Step 29-40)

**Trigger Condition:**
- LD M25
- LD M26

**Actions:**
- LD= D62
- AND>= D124
- ANB 
- OR M26
- ANI M340
- ANI M320
- ANI M301
- ANI M304
- OUT M26
- OUT M55

### Block 5: L0 EXHAUST (Step 42-43)

**Trigger Condition:**
- LD M23

**Actions:**
- OUT M51

### Block 6: L1 REFRIG FAST (Step 45-50)

**Trigger Condition:**
- LD M37
- LD M37
- LD M37

**Actions:**
- OUT M68
- OUT M112
- OUT T13

### Block 7: L1 REFRIG NORMAL (Step 52-55)

**Trigger Condition:**
- LD M38
- LD M38

**Actions:**
- OUT M69
- OUT T14

### Block 8: L1 OIL FAST (Step 57-71)

**Trigger Condition:**
- LD M39
- LD M41
- LD M41

**Actions:**
- ANI T12
- ANI M838
- OR M41
- ANI M42
- ANI M356
- ANI M336
- ANI M317
- ANI M304
- OUT M41
- OUT M70
- OR M42
- OUT T15

### Block 9: L1 OIL NORMAL (Step 73-90)

**Trigger Condition:**
- LD M41
- LD M872
- LD M873
- LD M42

**Actions:**
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- OR M42
- ANI M356
- ANI M336
- ANI M317
- ANI M304
- OUT M42
- OUT M71

### Block 10: L1 EXHAUST (Step 92-95)

**Trigger Condition:**
- LD M39
- LD M39

**Actions:**
- OUT M67
- OUT T12

### Block 11: COMPLETION L0 (M822) (Step 97-126)

**Trigger Condition:**
- LD M21
- LD M21
- LD M21
- LD M22
- LD M22
- LD M25
- LD M26
- LD M23

**Actions:**
- LD= D62
- AND>= D124
- ANB 
- LD= D62
- AND>= D124
- ANB 
- ORB 
- AND T4
- ORB 
- AND>= D124
- ORB 
- AND T5
- ORB 
- AND T6
- ORB 
- AND T6
- ORB 
- AND T3
- ORB 
- OR M822
- ANI M24
- OUT M822

### Block 12: COMPLETION L1 (M838) (Step 128-169)

**Trigger Condition:**
- LD M37
- LD M872
- LD M873
- LD M37
- LD M872
- LD M873
- LD M37
- LD M38
- LD M38
- LD M41
- LD M42
- LD M39

**Actions:**
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- LD= D90
- ANB 
- LD= D104
- ANB 
- ORB 
- ANB 
- AND>= D400
- ORB 
- AND T13
- ORB 
- AND>= D400
- ORB 
- AND T14
- ORB 
- AND T15
- ORB 
- AND T15
- ORB 
- AND T12
- ORB 
- OR M838
- ANI M40
- OUT M838

### Block 13: TIMEOUT ALARM TRIGGERS (Step 171-198)

**Trigger Condition:**
- LD M21
- LD M22
- LD M25
- LD M26
- LD M37
- LD M38
- LD M41
- LD M42

**Actions:**
- AND T4
- AND T5
- ORB 
- AND T6
- ORB 
- AND T6
- ORB 
- OR M320
- ANI M1027
- OUT M320
- AND T13
- AND T14
- ORB 
- AND T15
- ORB 
- AND T15
- ORB 
- OR M336
- ANI M1027
- OUT M336

### Block 14: OIL RESTART FLAGS (Step 200-215)

**Trigger Condition:**
- LD M25
- LD M26
- LD M41
- LD M42

**Actions:**
- AND>= D124
- AND>= D124
- ORB 
- OR M340
- ANI M21
- OUT M340
- AND>= D400
- AND>= D400
- ORB 
- OR M356
- ANI M37
- OUT M356

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D104 | D |  |  |  | 3 |
| D124 | D |  |  |  | 6 |
| D400 | D |  |  |  | 6 |
| D62 | D |  |  |  | 3 |
| D90 | D |  |  |  | 3 |
| M1027 | M |  |  |  | 2 |
| M112 | M |  |  | 1 |  |
| M21 | M |  |  |  | 8 |
| M22 | M |  |  |  | 5 |
| M23 | M |  |  |  | 3 |
| M24 | M |  |  |  | 1 |
| M25 | M |  |  | 1 | 7 |
| M26 | M |  |  | 1 | 7 |
| M301 | M |  |  |  | 2 |
| M304 | M |  |  |  | 4 |
| M317 | M |  |  |  | 2 |
| M320 | M |  |  | 1 | 3 |
| M336 | M |  |  | 1 | 3 |
| M340 | M |  |  | 1 | 3 |
| M356 | M |  |  | 1 | 3 |
| M37 | M |  |  |  | 8 |
| M38 | M |  |  |  | 5 |
| M39 | M |  |  |  | 4 |
| M40 | M |  |  |  | 1 |
| M41 | M |  |  | 1 | 7 |
| M42 | M |  |  | 1 | 7 |
| M51 | M |  |  | 1 |  |
| M52 | M |  |  | 1 |  |
| M53 | M |  |  | 1 |  |
| M54 | M |  |  | 1 |  |
| M55 | M |  |  | 1 |  |
| M67 | M |  |  | 1 |  |
| M68 | M |  |  | 1 |  |
| M69 | M |  |  | 1 |  |
| M70 | M |  |  | 1 |  |
| M71 | M |  |  | 1 |  |
| M822 | M |  |  | 1 | 2 |
| M838 | M |  |  | 1 | 2 |
| M872 | M |  |  |  | 3 |
| M873 | M |  |  |  | 3 |
| M96 | M |  |  | 1 |  |
| T12 | T |  |  | 1 | 2 |
| T13 | T |  |  | 1 | 2 |
| T14 | T |  |  | 1 | 2 |
| T15 | T |  |  | 1 | 4 |
| T3 | T |  |  |  | 2 |
| T4 | T |  |  | 1 | 2 |
| T5 | T |  |  | 1 | 2 |
| T6 | T |  |  | 1 | 4 |
