---
# idata — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 232
**Blocks:** 8
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | SYSTEM FLAGS | 1–6 | LD SM400, LD SM401, LD SM402 | 3 |
| 2 | INIT FIRST SCAN | 8–96 | LD M2, LD M2, LD M2 ... (+7) | 79 |
| 3 | INPUT MAPPING L0 | 98–129 | LD X0A0, LD X0A1, LD X0A2 ... (+13) | 16 |
| 4 | INPUT MAPPING L1 | 131–162 | LD X0B0, LD X0B1, LD X0B2 ... (+13) | 16 |
| 5 | OUTPUT MAPPING L0 | 164–189 | LD M48, LD M49, LD M50 ... (+10) | 13 |
| 6 | GLOBAL OUTPUTS | 191–198 | LD M76, LD M77, LD M78 ... (+1) | 4 |
| 7 | OUTPUT MAPPING L1 | 200–223 | LD M64, LD M65, LD M66 ... (+9) | 12 |
| 8 | CONFIG VALIDATION | 225–232 |  | 8 |

## Block Detail

### Block 1: SYSTEM FLAGS (Step 1–6)

**Trigger Condition:**
- LD SM400
- LD SM401
- LD SM402

**Actions:**
- OUT M0
- OUT M1
- OUT M2

### Block 2: INIT FIRST SCAN (Step 8–96)

**Trigger Condition:**
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2
- LD M2

**Actions:**
- SET L0
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
- RST L16
- RST L17
- RST L18
- RST L19
- RST L20
- RST L21
- RST L22
- RST L23
- RST L24
- RST L32
- RST L33
- RST L34
- RST L35
- RST L36
- RST L37
- RST L38
- RST L39
- RST L40
- RST L64
- RST L65
- RST L66
- RST L67
- RST L68
- RST L69
- RST L70
- RST L71
- RST L72
- RST L73
- RST L74
- RST L75
- RST L78

### Block 3: INPUT MAPPING L0 (Step 98–129)

**Trigger Condition:**
- LD X0A0
- LD X0A1
- LD X0A2
- LD X0A3
- LD X0A4
- LD X0A5
- LD X0A6
- LD X0A7
- LD X0A8
- LD X0A9
- LD X0AA
- LD X0AB
- LD X0AC
- LD X0AD
- LD X0AE
- LD X0AF

**Actions:**
- OUT M768
- OUT M769
- OUT M770
- OUT M771
- OUT M772
- OUT M773
- OUT M774
- OUT M775
- OUT M776
- OUT M777
- OUT M778
- OUT M779
- OUT M780
- OUT M781
- OUT M782
- OUT M783

### Block 4: INPUT MAPPING L1 (Step 131–162)

**Trigger Condition:**
- LD X0B0
- LD X0B1
- LD X0B2
- LD X0B3
- LD X0B4
- LD X0B5
- LD X0B6
- LD X0B7
- LD X0B8
- LD X0B9
- LD X0BA
- LD X0BB
- LD X0BC
- LD X0BD
- LD X0BE
- LD X0BF

**Actions:**
- OUT M784
- OUT M785
- OUT M786
- OUT M787
- OUT M788
- OUT M789
- OUT M790
- OUT M791
- OUT M792
- OUT M793
- OUT M794
- OUT M795
- OUT M796
- OUT M797
- OUT M798
- OUT M799

### Block 5: OUTPUT MAPPING L0 (Step 164–189)

**Trigger Condition:**
- LD M48
- LD M49
- LD M50
- LD M51
- LD M52
- LD M53
- LD M54
- LD M55
- LD M56
- LD M57
- LD M58
- LD M59
- LD M80

**Actions:**
- OUT Y010
- OUT Y011
- OUT Y012
- OUT Y01B
- OUT Y013
- OUT Y014
- OUT Y015
- OUT Y016
- OUT Y017
- OUT Y018
- OUT Y019
- OUT Y01A
- OUT Y01C

### Block 6: GLOBAL OUTPUTS (Step 191–198)

**Trigger Condition:**
- LD M76
- LD M77
- LD M78
- LD M79

**Actions:**
- OUT Y01D
- OUT Y01E
- OUT Y01F
- OUT Y02C

### Block 7: OUTPUT MAPPING L1 (Step 200–223)

**Trigger Condition:**
- LD M64
- LD M65
- LD M66
- LD M67
- LD M68
- LD M69
- LD M70
- LD M71
- LD M72
- LD M73
- LD M74
- LD M75

**Actions:**
- OUT Y020
- OUT Y021
- OUT Y022
- OUT Y02B
- OUT Y023
- OUT Y024
- OUT Y025
- OUT Y026
- OUT Y027
- OUT Y028
- OUT Y029
- OUT Y02A

### Block 8: CONFIG VALIDATION (Step 225–232)

**Trigger Condition:**

**Actions:**
- LD< D270
- MOV K1 D270
- LD> D270
- MOV K2 D270
- LD< D272
- MOV K1 D272
- LD> D272
- MOV K2 D272

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D270 | D |  |  |  | 2 |
| D272 | D |  |  |  | 2 |
| K1 D270 | K |  |  |  | 1 |
| K1 D272 | K |  |  |  | 1 |
| K2 D270 | K |  |  |  | 1 |
| K2 D272 | K |  |  |  | 1 |
| L0 | L | 1 |  |  |  |
| L16 | L |  | 1 |  |  |
| L17 | L |  | 1 |  |  |
| L18 | L |  | 1 |  |  |
| L19 | L |  | 1 |  |  |
| L20 | L |  | 1 |  |  |
| L21 | L |  | 1 |  |  |
| L22 | L |  | 1 |  |  |
| L23 | L |  | 1 |  |  |
| L24 | L |  | 1 |  |  |
| L32 | L |  | 1 |  |  |
| L33 | L |  | 1 |  |  |
| L34 | L |  | 1 |  |  |
| L35 | L |  | 1 |  |  |
| L36 | L |  | 1 |  |  |
| L37 | L |  | 1 |  |  |
| L38 | L |  | 1 |  |  |
| L39 | L |  | 1 |  |  |
| L40 | L |  | 1 |  |  |
| L64 | L |  | 1 |  |  |
| L65 | L |  | 1 |  |  |
| L66 | L |  | 1 |  |  |
| L67 | L |  | 1 |  |  |
| L68 | L |  | 1 |  |  |
| L69 | L |  | 1 |  |  |
| L70 | L |  | 1 |  |  |
| L71 | L |  | 1 |  |  |
| L72 | L |  | 1 |  |  |
| L73 | L |  | 1 |  |  |
| L74 | L |  | 1 |  |  |
| L75 | L |  | 1 |  |  |
| L78 | L |  | 1 |  |  |
| M0 | M |  |  | 1 |  |
| M1 | M |  |  | 1 |  |
| M16 | M |  | 1 |  |  |
| M17 | M |  | 1 |  |  |
| M18 | M |  | 1 |  |  |
| M19 | M |  | 1 |  |  |
| M2 | M |  |  | 1 | 10 |
| M20 | M |  | 1 |  |  |
| M21 | M |  | 1 |  |  |
| M22 | M |  | 1 |  |  |
| M23 | M |  | 1 |  |  |
| M24 | M |  | 1 |  |  |
| M32 | M |  | 1 |  |  |
| M33 | M |  | 1 |  |  |
| M34 | M |  | 1 |  |  |
| M35 | M |  | 1 |  |  |
| M36 | M |  | 1 |  |  |
| M37 | M |  | 1 |  |  |
| M38 | M |  | 1 |  |  |
| M39 | M |  | 1 |  |  |
| M40 | M |  | 1 |  |  |
| M48 | M |  | 1 |  | 1 |
| M49 | M |  | 1 |  | 1 |
| M50 | M |  | 1 |  | 1 |
| M51 | M |  | 1 |  | 1 |
| M52 | M |  | 1 |  | 1 |
| M53 | M |  | 1 |  | 1 |
| M54 | M |  | 1 |  | 1 |
| M55 | M |  | 1 |  | 1 |
| M56 | M |  | 1 |  | 1 |
| M57 | M |  | 1 |  | 1 |
| M58 | M |  | 1 |  | 1 |
| M59 | M |  | 1 |  | 1 |
| M64 | M |  | 1 |  | 1 |
| M65 | M |  | 1 |  | 1 |
| M66 | M |  | 1 |  | 1 |
| M67 | M |  | 1 |  | 1 |
| M68 | M |  | 1 |  | 1 |
| M69 | M |  | 1 |  | 1 |
| M70 | M |  | 1 |  | 1 |
| M71 | M |  | 1 |  | 1 |
| M72 | M |  | 1 |  | 1 |
| M73 | M |  | 1 |  | 1 |
| M74 | M |  | 1 |  | 1 |
| M75 | M |  | 1 |  | 1 |
| M76 | M |  | 1 |  | 1 |
| M768 | M |  |  | 1 |  |
| M769 | M |  |  | 1 |  |
| M77 | M |  | 1 |  | 1 |
| M770 | M |  |  | 1 |  |
| M771 | M |  |  | 1 |  |
| M772 | M |  |  | 1 |  |
| M773 | M |  |  | 1 |  |
| M774 | M |  |  | 1 |  |
| M775 | M |  |  | 1 |  |
| M776 | M |  |  | 1 |  |
| M777 | M |  |  | 1 |  |
| M778 | M |  |  | 1 |  |
| M779 | M |  |  | 1 |  |
| M78 | M |  | 1 |  | 1 |
| M780 | M |  |  | 1 |  |
| M781 | M |  |  | 1 |  |
| M782 | M |  |  | 1 |  |
| M783 | M |  |  | 1 |  |
| M784 | M |  |  | 1 |  |
| M785 | M |  |  | 1 |  |
| M786 | M |  |  | 1 |  |
| M787 | M |  |  | 1 |  |
| M788 | M |  |  | 1 |  |
| M789 | M |  |  | 1 |  |
| M79 | M |  | 1 |  | 1 |
| M790 | M |  |  | 1 |  |
| M791 | M |  |  | 1 |  |
| M792 | M |  |  | 1 |  |
| M793 | M |  |  | 1 |  |
| M794 | M |  |  | 1 |  |
| M795 | M |  |  | 1 |  |
| M796 | M |  |  | 1 |  |
| M797 | M |  |  | 1 |  |
| M798 | M |  |  | 1 |  |
| M799 | M |  |  | 1 |  |
| M80 | M |  | 1 |  | 1 |
| SM400 | ? |  |  |  | 1 |
| SM401 | ? |  |  |  | 1 |
| SM402 | ? |  |  |  | 1 |
| X0A0 | X |  |  |  | 1 |
| X0A1 | X |  |  |  | 1 |
| X0A2 | X |  |  |  | 1 |
| X0A3 | X |  |  |  | 1 |
| X0A4 | X |  |  |  | 1 |
| X0A5 | X |  |  |  | 1 |
| X0A6 | X |  |  |  | 1 |
| X0A7 | X |  |  |  | 1 |
| X0A8 | X |  |  |  | 1 |
| X0A9 | X |  |  |  | 1 |
| X0AA | X |  |  |  | 1 |
| X0AB | X |  |  |  | 1 |
| X0AC | X |  |  |  | 1 |
| X0AD | X |  |  |  | 1 |
| X0AE | X |  |  |  | 1 |
| X0AF | X |  |  |  | 1 |
| X0B0 | X |  |  |  | 1 |
| X0B1 | X |  |  |  | 1 |
| X0B2 | X |  |  |  | 1 |
| X0B3 | X |  |  |  | 1 |
| X0B4 | X |  |  |  | 1 |
| X0B5 | X |  |  |  | 1 |
| X0B6 | X |  |  |  | 1 |
| X0B7 | X |  |  |  | 1 |
| X0B8 | X |  |  |  | 1 |
| X0B9 | X |  |  |  | 1 |
| X0BA | X |  |  |  | 1 |
| X0BB | X |  |  |  | 1 |
| X0BC | X |  |  |  | 1 |
| X0BD | X |  |  |  | 1 |
| X0BE | X |  |  |  | 1 |
| X0BF | X |  |  |  | 1 |
| Y010 | Y |  |  | 1 |  |
| Y011 | Y |  |  | 1 |  |
| Y012 | Y |  |  | 1 |  |
| Y013 | Y |  |  | 1 |  |
| Y014 | Y |  |  | 1 |  |
| Y015 | Y |  |  | 1 |  |
| Y016 | Y |  |  | 1 |  |
| Y017 | Y |  |  | 1 |  |
| Y018 | Y |  |  | 1 |  |
| Y019 | Y |  |  | 1 |  |
| Y01A | Y |  |  | 1 |  |
| Y01B | Y |  |  | 1 |  |
| Y01C | Y |  |  | 1 |  |
| Y01D | Y |  |  | 1 |  |
| Y01E | Y |  |  | 1 |  |
| Y01F | Y |  |  | 1 |  |
| Y020 | Y |  |  | 1 |  |
| Y021 | Y |  |  | 1 |  |
| Y022 | Y |  |  | 1 |  |
| Y023 | Y |  |  | 1 |  |
| Y024 | Y |  |  | 1 |  |
| Y025 | Y |  |  | 1 |  |
| Y026 | Y |  |  | 1 |  |
| Y027 | Y |  |  | 1 |  |
| Y028 | Y |  |  | 1 |  |
| Y029 | Y |  |  | 1 |  |
| Y02A | Y |  |  | 1 |  |
| Y02B | Y |  |  | 1 |  |
| Y02C | Y |  |  | 1 |  |
