---
# MAIN — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 710
**Blocks:** 14
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | MODE CONTROL | 1–34 | LD M1038, LD M1536, LD M1536 ... (+7) | 24 |
| 2 | INTERLOCK CHECK | 36–47 | LD L81, LD L97 | 10 |
| 3 | READY SET L0 | 49–64 | LD M1039, LD M1040, LD M1041 ... (+1) | 12 |
| 4 | READY SET L1 | 66–81 | LD M1039, LD M1040, LD M1041 ... (+1) | 12 |
| 5 | START EXEC L0 | 83–98 | LD M1043, LD M1043, LD M1043 ... (+1) | 12 |
| 6 | START EXEC L1 | 100–115 | LD M1045, LD M1045, LD M1045 ... (+1) | 12 |
| 7 | STEP L0 | 117–285 | LD M24, LD M16, LD M17 ... (+8) | 158 |
| 8 | STEP L1 | 287–455 | LD M40, LD M32, LD M33 ... (+8) | 158 |
| 9 | NG ALARM STOP | 457–502 | LD L17, LD L19, LD L21 ... (+3) | 40 |
| 10 | STOP | 504–563 | LD M1044, LD M0, LD M0 ... (+5) | 52 |
| 11 | EMERGENCY STOP | 565–621 | LDI M771, LD M0, LD M0 ... (+4) | 50 |
| 12 | EXHAUST TIMER | 623–626 | LD M23, LD M39 | 2 |
| 13 | LAMP CONTROL | 628–667 | LD M16, LD L64, LD M16 | 37 |
| 14 | HMI LAMP | 669–710 | LD M502, LD M503, LD M504 ... (+7) | 32 |

## Block Detail

### Block 1: MODE CONTROL (Step 1–34)

**Trigger Condition:**
- LD M1038
- LD M1536
- LD M1536
- LD M1024
- LD M1025
- LD M1032
- LD M1033
- LD M1026
- LD M1537
- LD M1537

**Actions:**
- PLS M1536
- AND L1
- SET L2
- RST L1
- ANI L1
- SET L1
- RST L2
- OR L112
- ANI M1025
- OUT L112
- OR L113
- ANI M1024
- OUT L113
- OR L114
- ANI M1033
- OUT L114
- OR L115
- ANI M1032
- OUT L115
- PLS M1537
- AND L116
- RST L116
- ANI L116
- SET L116

### Block 2: INTERLOCK CHECK (Step 36–47)

**Trigger Condition:**
- LD L81
- LD L97

**Actions:**
- AND L82
- AND L83
- AND L84
- AND L85
- OUT L80
- AND L98
- AND L99
- AND L100
- AND L101
- OUT L96

### Block 3: READY SET L0 (Step 49–64)

**Trigger Condition:**
- LD M1039
- LD M1040
- LD M1041
- LD M1042

**Actions:**
- AND L2
- ANI M18
- SET M502
- AND L2
- ANI M19
- SET M503
- AND L2
- ANI M20
- SET M504
- AND L2
- ANI M21
- SET M505

### Block 4: READY SET L1 (Step 66–81)

**Trigger Condition:**
- LD M1039
- LD M1040
- LD M1041
- LD M1042

**Actions:**
- AND L2
- ANI M34
- SET M506
- AND L2
- ANI M35
- SET M507
- AND L2
- ANI M36
- SET M508
- AND L2
- ANI M37
- SET M509

### Block 5: START EXEC L0 (Step 83–98)

**Trigger Condition:**
- LD M1043
- LD M1043
- LD M1043
- LD M1043

**Actions:**
- AND M502
- SET M18
- RST M502
- AND M503
- SET M19
- RST M503
- AND M504
- SET M20
- RST M504
- AND M505
- SET M21
- RST M505

### Block 6: START EXEC L1 (Step 100–115)

**Trigger Condition:**
- LD M1045
- LD M1045
- LD M1045
- LD M1045

**Actions:**
- AND M506
- SET M34
- RST M506
- AND M507
- SET M35
- RST M507
- AND M508
- SET M36
- RST M508
- AND M509
- SET M37
- RST M509

### Block 7: STEP L0 (Step 117–285)

**Trigger Condition:**
- LD M24
- LD M16
- LD M17
- LD M18
- LD M19
- LD M20
- LD M20
- LD M21
- LD M23
- LD M23
- LD M24

**Actions:**
- OR M16
- ANI M17
- ANI L64
- OUT M16
- AND L0
- AND L80
- AND M1043
- AND L1
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OR M17
- ANI M18
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M17
- OR M18
- ANI M19
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M18
- AND L16
- OR M19
- ANI M20
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M19
- AND L18
- OR M20
- ANI M21
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M20
- AND L20
- OR M21
- ANI M23
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M21
- AND L20
- OR M22
- ANI M23
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M22
- OR M22
- AND L22
- OR M23
- ANI M24
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M23
- AND T3
- OR M24
- ANI M16
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- OUT M24
- AND T3
- SET L24
- MOV K1

### Block 8: STEP L1 (Step 287–455)

**Trigger Condition:**
- LD M40
- LD M32
- LD M33
- LD M34
- LD M35
- LD M36
- LD M36
- LD M37
- LD M39
- LD M39
- LD M40

**Actions:**
- OR M32
- ANI M33
- ANI L64
- OUT M32
- AND L0
- AND L96
- AND M1045
- AND L1
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OR M33
- ANI M34
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M33
- OR M34
- ANI M35
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M34
- AND L32
- OR M35
- ANI M36
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M35
- AND L34
- OR M36
- ANI M37
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M36
- AND L36
- OR M37
- ANI M39
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M37
- AND L36
- OR M38
- ANI M39
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M38
- OR M38
- AND L38
- OR M39
- ANI M40
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M39
- AND T3
- OR M40
- ANI M32
- ANI L64
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L79
- OUT M40
- AND T3
- SET L40
- MOV K1

### Block 9: NG ALARM STOP (Step 457–502)

**Trigger Condition:**
- LD L17
- LD L19
- LD L21
- LD L23
- LD L17
- LD L17

**Actions:**
- MOV K3
- MOV K3
- MOV K4
- MOV K4
- MOV K5
- MOV K5
- MOV K2
- MOV K2
- OR L19
- OR L21
- OR L23
- OR L64
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
- SET M16
- OR L19
- OR L21
- OR L23
- OR L64
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
- OR L79
- SET M32

### Block 10: STOP (Step 504–563)

**Trigger Condition:**
- LD M1044
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- OR M769
- RST M16
- RST M17
- RST M18
- RST M19
- RST M20
- RST M21
- RST M22
- RST M23
- RST M24
- RST M32
- RST M33
- RST M34
- RST M35
- RST M36
- RST M37
- RST M38
- RST M39
- RST M40
- RST M48
- RST M49
- RST M50
- RST M51
- RST M52
- RST M53
- RST M54
- RST M55
- RST M56
- RST M57
- RST M58
- RST M59
- RST M64
- RST M65
- RST M66
- RST M67
- RST M68
- RST M69
- RST M70
- RST M71
- RST M72
- RST M73
- RST M74
- RST M75
- RST M76
- RST M77
- RST M78
- RST M79
- RST M80
- SET M16
- SET M32
- MOV K6 D7012
- MOV K6 D8012

### Block 11: EMERGENCY STOP (Step 565–621)

**Trigger Condition:**
- LDI M771
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- SET L64
- MOV K6 D7012
- MOV K6 D8012
- RST M16
- RST M17
- RST M18
- RST M19
- RST M20
- RST M21
- RST M22
- RST M23
- RST M24
- RST M32
- RST M33
- RST M34
- RST M35
- RST M36
- RST M37
- RST M38
- RST M39
- RST M40
- RST M48
- RST M49
- RST M50
- RST M51
- RST M52
- RST M53
- RST M54
- RST M55
- RST M56
- RST M57
- RST M58
- RST M59
- RST M64
- RST M65
- RST M66
- RST M67
- RST M68
- RST M69
- RST M70
- RST M71
- RST M72
- RST M73
- RST M74
- RST M75
- RST M76
- RST M77
- RST M78
- RST M79
- RST M80

### Block 12: EXHAUST TIMER (Step 623–626)

**Trigger Condition:**
- LD M23
- LD M39

**Actions:**
- OUT T3
- OUT T3

### Block 13: LAMP CONTROL (Step 628–667)

**Trigger Condition:**
- LD M16
- LD L64
- LD M16

**Actions:**
- OR M17
- OR M18
- OR M19
- OR M20
- OR M21
- OR M22
- OR M23
- OR M24
- ANI L64
- ANI L65
- ANI L66
- ANI L67
- ANI L68
- ANI L69
- ANI L70
- ANI L71
- ANI L72
- ANI L73
- ANI L74
- ANI L78
- ANI L79
- OUT M77
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
- OUT M78
- ANI L80
- OUT M79

### Block 14: HMI LAMP (Step 669–710)

**Trigger Condition:**
- LD M502
- LD M503
- LD M504
- LD M505
- LD M506
- LD M507
- LD M508
- LD M509
- LD M18
- LD M34

**Actions:**
- OR M18
- OUT M530
- OR M19
- OUT M531
- OR M20
- OUT M532
- OR M21
- OR M22
- OUT M533
- OR M34
- OUT M534
- OR M35
- OUT M535
- OR M36
- OUT M536
- OR M37
- OR M38
- OUT M537
- OR M19
- OR M20
- OR M21
- OR M22
- OR M23
- OR M24
- OUT M540
- OR M35
- OR M36
- OR M37
- OR M38
- OR M39
- OR M40
- OUT M541

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| K1 | K |  |  |  | 2 |
| K2 | K |  |  |  | 2 |
| K3 | K |  |  |  | 2 |
| K4 | K |  |  |  | 2 |
| K5 | K |  |  |  | 2 |
| K6 D7012 | K |  |  |  | 2 |
| K6 D8012 | K |  |  |  | 2 |
| L0 | L |  |  |  | 2 |
| L1 | L | 1 | 1 |  | 4 |
| L100 | L |  |  |  | 1 |
| L101 | L |  |  |  | 1 |
| L112 | L |  |  | 1 | 1 |
| L113 | L |  |  | 1 | 1 |
| L114 | L |  |  | 1 | 1 |
| L115 | L |  |  | 1 | 1 |
| L116 | L | 1 | 1 |  | 2 |
| L16 | L |  |  |  | 1 |
| L17 | L |  |  |  | 3 |
| L18 | L |  |  |  | 1 |
| L19 | L |  |  |  | 3 |
| L2 | L | 1 | 1 |  | 8 |
| L20 | L |  |  |  | 2 |
| L21 | L |  |  |  | 3 |
| L22 | L |  |  |  | 1 |
| L23 | L |  |  |  | 3 |
| L24 | L | 1 |  |  |  |
| L32 | L |  |  |  | 1 |
| L34 | L |  |  |  | 1 |
| L36 | L |  |  |  | 2 |
| L38 | L |  |  |  | 1 |
| L40 | L | 1 |  |  |  |
| L64 | L | 1 |  |  | 40 |
| L65 | L |  |  |  | 22 |
| L66 | L |  |  |  | 22 |
| L67 | L |  |  |  | 22 |
| L68 | L |  |  |  | 22 |
| L69 | L |  |  |  | 22 |
| L70 | L |  |  |  | 22 |
| L71 | L |  |  |  | 22 |
| L72 | L |  |  |  | 22 |
| L73 | L |  |  |  | 22 |
| L74 | L |  |  |  | 22 |
| L78 | L |  |  |  | 12 |
| L79 | L |  |  |  | 12 |
| L80 | L |  |  | 1 | 2 |
| L81 | L |  |  |  | 1 |
| L82 | L |  |  |  | 1 |
| L83 | L |  |  |  | 1 |
| L84 | L |  |  |  | 1 |
| L85 | L |  |  |  | 1 |
| L96 | L |  |  | 1 | 1 |
| L97 | L |  |  |  | 1 |
| L98 | L |  |  |  | 1 |
| L99 | L |  |  |  | 1 |
| M0 | M |  |  |  | 13 |
| M1024 | M |  |  |  | 2 |
| M1025 | M |  |  |  | 2 |
| M1026 | M |  |  |  | 1 |
| M1032 | M |  |  |  | 2 |
| M1033 | M |  |  |  | 2 |
| M1038 | M |  |  |  | 1 |
| M1039 | M |  |  |  | 2 |
| M1040 | M |  |  |  | 2 |
| M1041 | M |  |  |  | 2 |
| M1042 | M |  |  |  | 2 |
| M1043 | M |  |  |  | 5 |
| M1044 | M |  |  |  | 1 |
| M1045 | M |  |  |  | 5 |
| M1536 | M |  |  |  | 3 |
| M1537 | M |  |  |  | 3 |
| M16 | M | 2 | 2 | 1 | 5 |
| M17 | M |  | 2 | 1 | 4 |
| M18 | M | 1 | 2 | 1 | 7 |
| M19 | M | 1 | 2 | 1 | 7 |
| M20 | M | 1 | 2 | 1 | 8 |
| M21 | M | 1 | 2 | 1 | 7 |
| M22 | M |  | 2 | 1 | 5 |
| M23 | M |  | 2 | 1 | 8 |
| M24 | M |  | 2 | 1 | 6 |
| M32 | M | 2 | 2 | 1 | 3 |
| M33 | M |  | 2 | 1 | 3 |
| M34 | M | 1 | 2 | 1 | 6 |
| M35 | M | 1 | 2 | 1 | 6 |
| M36 | M | 1 | 2 | 1 | 7 |
| M37 | M | 1 | 2 | 1 | 6 |
| M38 | M |  | 2 | 1 | 4 |
| M39 | M |  | 2 | 1 | 7 |
| M40 | M |  | 2 | 1 | 5 |
| M48 | M |  | 2 |  |  |
| M49 | M |  | 2 |  |  |
| M50 | M |  | 2 |  |  |
| M502 | M | 1 | 1 |  | 2 |
| M503 | M | 1 | 1 |  | 2 |
| M504 | M | 1 | 1 |  | 2 |
| M505 | M | 1 | 1 |  | 2 |
| M506 | M | 1 | 1 |  | 2 |
| M507 | M | 1 | 1 |  | 2 |
| M508 | M | 1 | 1 |  | 2 |
| M509 | M | 1 | 1 |  | 2 |
| M51 | M |  | 2 |  |  |
| M52 | M |  | 2 |  |  |
| M53 | M |  | 2 |  |  |
| M530 | M |  |  | 1 |  |
| M531 | M |  |  | 1 |  |
| M532 | M |  |  | 1 |  |
| M533 | M |  |  | 1 |  |
| M534 | M |  |  | 1 |  |
| M535 | M |  |  | 1 |  |
| M536 | M |  |  | 1 |  |
| M537 | M |  |  | 1 |  |
| M54 | M |  | 2 |  |  |
| M540 | M |  |  | 1 |  |
| M541 | M |  |  | 1 |  |
| M55 | M |  | 2 |  |  |
| M56 | M |  | 2 |  |  |
| M57 | M |  | 2 |  |  |
| M58 | M |  | 2 |  |  |
| M59 | M |  | 2 |  |  |
| M64 | M |  | 2 |  |  |
| M65 | M |  | 2 |  |  |
| M66 | M |  | 2 |  |  |
| M67 | M |  | 2 |  |  |
| M68 | M |  | 2 |  |  |
| M69 | M |  | 2 |  |  |
| M70 | M |  | 2 |  |  |
| M71 | M |  | 2 |  |  |
| M72 | M |  | 2 |  |  |
| M73 | M |  | 2 |  |  |
| M74 | M |  | 2 |  |  |
| M75 | M |  | 2 |  |  |
| M76 | M |  | 2 |  |  |
| M769 | M |  |  |  | 1 |
| M77 | M |  | 2 | 1 |  |
| M771 | M |  |  |  | 1 |
| M78 | M |  | 2 | 1 |  |
| M79 | M |  | 2 | 1 |  |
| M80 | M |  | 2 |  |  |
| T3 | T |  |  | 2 | 4 |
