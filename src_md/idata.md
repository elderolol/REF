---
# idata — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 233
**Blocks:** 8
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | SYSTEM FLAGS | 0–6 | LD SM400, LD SM401, LD SM402 | 3 |
| 2 | INIT FIRST SCAN | 7–96 | LD M2, LD M2, LD M2 | 79 |
| 3 | INPUT MAPPING L0 | 97–129 | LD X0A0, LD X0A1, LD X0A2 | 16 |
| 4 | INPUT MAPPING L1 | 130–162 | LD X0B0, LD X0B1, LD X0B2 | 16 |
| 5 | OUTPUT MAPPING L0 | 163–189 | LD M48, LD M49, LD M50 | 13 |
| 6 | GLOBAL OUTPUTS | 190–198 | LD M76, LD M77, LD M78 | 4 |
| 7 | OUTPUT MAPPING L1 | 199–223 | LD M64, LD M65, LD M66 | 12 |
| 8 | CONFIG VALIDATION | 224–233 | LD< D270, LD> D270, LD< D272 | 5 |

## Block Detail

### Block 1: SYSTEM FLAGS (Step 0–6)

**Trigger Condition:**
- LD SM400
- LD SM401
- LD SM402

**Actions:**
- OUT M0
- OUT M1
- OUT M2

### Block 2: INIT FIRST SCAN (Step 7–96)

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

### Block 3: INPUT MAPPING L0 (Step 97–129)

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

### Block 4: INPUT MAPPING L1 (Step 130–162)

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

### Block 5: OUTPUT MAPPING L0 (Step 163–189)

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

### Block 6: GLOBAL OUTPUTS (Step 190–198)

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

### Block 7: OUTPUT MAPPING L1 (Step 199–223)

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

### Block 8: CONFIG VALIDATION (Step 224–233)

**Trigger Condition:**
- LD< D270
- LD> D270
- LD< D272
- LD> D272

**Actions:**
- MOV K1 D270
- MOV K2 D270
- MOV K1 D272
- MOV K2 D272
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D270 | D | 226, 228 | — | — | 225, 227 | NO_RST |
| D272 | D | 230, 232 | — | — | 229, 231 | NO_RST |
| K1 | K | — | — | — | 226, 230 |  |
| K2 | K | — | — | — | 228, 232 |  |
| L0 | L | 9 | — | — | — | NO_RST, LATCH_DEVICE |
| L16 | L | — | 63 | — | — | NO_SET, LATCH_DEVICE |
| L17 | L | — | 64 | — | — | NO_SET, LATCH_DEVICE |
| L18 | L | — | 65 | — | — | NO_SET, LATCH_DEVICE |
| L19 | L | — | 66 | — | — | NO_SET, LATCH_DEVICE |
| L20 | L | — | 67 | — | — | NO_SET, LATCH_DEVICE |
| L21 | L | — | 68 | — | — | NO_SET, LATCH_DEVICE |
| L22 | L | — | 69 | — | — | NO_SET, LATCH_DEVICE |
| L23 | L | — | 70 | — | — | NO_SET, LATCH_DEVICE |
| L24 | L | — | 72 | — | — | NO_SET, LATCH_DEVICE |
| L32 | L | — | 73 | — | — | NO_SET, LATCH_DEVICE |
| L33 | L | — | 74 | — | — | NO_SET, LATCH_DEVICE |
| L34 | L | — | 75 | — | — | NO_SET, LATCH_DEVICE |
| L35 | L | — | 76 | — | — | NO_SET, LATCH_DEVICE |
| L36 | L | — | 77 | — | — | NO_SET, LATCH_DEVICE |
| L37 | L | — | 78 | — | — | NO_SET, LATCH_DEVICE |
| L38 | L | — | 79 | — | — | NO_SET, LATCH_DEVICE |
| L39 | L | — | 81 | — | — | NO_SET, LATCH_DEVICE |
| L40 | L | — | 82 | — | — | NO_SET, LATCH_DEVICE |
| L64 | L | — | 83 | — | — | NO_SET, LATCH_DEVICE |
| L65 | L | — | 84 | — | — | NO_SET, LATCH_DEVICE |
| L66 | L | — | 85 | — | — | NO_SET, LATCH_DEVICE |
| L67 | L | — | 86 | — | — | NO_SET, LATCH_DEVICE |
| L68 | L | — | 87 | — | — | NO_SET, LATCH_DEVICE |
| L69 | L | — | 88 | — | — | NO_SET, LATCH_DEVICE |
| L70 | L | — | 90 | — | — | NO_SET, LATCH_DEVICE |
| L71 | L | — | 91 | — | — | NO_SET, LATCH_DEVICE |
| L72 | L | — | 92 | — | — | NO_SET, LATCH_DEVICE |
| L73 | L | — | 93 | — | — | NO_SET, LATCH_DEVICE |
| L74 | L | — | 94 | — | — | NO_SET, LATCH_DEVICE |
| L75 | L | — | 95 | — | — | NO_SET, LATCH_DEVICE |
| L78 | L | — | 96 | — | — | NO_SET, LATCH_DEVICE |
| M0 | M | — | — | 2 | — |  |
| M1 | M | — | — | 4 | — |  |
| M16 | M | — | 10 | — | — | NO_SET |
| M17 | M | — | 11 | — | — | NO_SET |
| M18 | M | — | 12 | — | — | NO_SET |
| M19 | M | — | 13 | — | — | NO_SET |
| M2 | M | — | — | 6 | 8, 17, 26, 35, 44, 53, 62, 71, 80, 89 | DOUBLE_COIL_CANDIDATE |
| M20 | M | — | 14 | — | — | NO_SET |
| M21 | M | — | 15 | — | — | NO_SET |
| M22 | M | — | 16 | — | — | NO_SET |
| M23 | M | — | 18 | — | — | NO_SET |
| M24 | M | — | 19 | — | — | NO_SET |
| M32 | M | — | 20 | — | — | NO_SET |
| M33 | M | — | 21 | — | — | NO_SET |
| M34 | M | — | 22 | — | — | NO_SET |
| M35 | M | — | 23 | — | — | NO_SET |
| M36 | M | — | 24 | — | — | NO_SET |
| M37 | M | — | 25 | — | — | NO_SET |
| M38 | M | — | 27 | — | — | NO_SET |
| M39 | M | — | 28 | — | — | NO_SET |
| M40 | M | — | 29 | — | — | NO_SET |
| M48 | M | — | 30 | — | 164 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M49 | M | — | 31 | — | 166 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M50 | M | — | 32 | — | 168 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M51 | M | — | 33 | — | 170 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M52 | M | — | 34 | — | 172 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M53 | M | — | 36 | — | 174 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M54 | M | — | 37 | — | 176 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M55 | M | — | 38 | — | 178 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M56 | M | — | 39 | — | 180 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M57 | M | — | 40 | — | 182 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M58 | M | — | 41 | — | 184 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M59 | M | — | 42 | — | 186 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M64 | M | — | 43 | — | 200 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M65 | M | — | 45 | — | 202 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M66 | M | — | 46 | — | 204 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M67 | M | — | 47 | — | 206 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M68 | M | — | 48 | — | 208 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M69 | M | — | 49 | — | 210 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M70 | M | — | 50 | — | 212 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M71 | M | — | 51 | — | 214 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M72 | M | — | 52 | — | 216 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M73 | M | — | 54 | — | 218 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M74 | M | — | 55 | — | 220 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M75 | M | — | 56 | — | 222 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M76 | M | — | 57 | — | 191 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M768 | M | — | — | 99 | — |  |
| M769 | M | — | — | 101 | — |  |
| M77 | M | — | 58 | — | 193 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M770 | M | — | — | 103 | — |  |
| M771 | M | — | — | 105 | — |  |
| M772 | M | — | — | 107 | — |  |
| M773 | M | — | — | 109 | — |  |
| M774 | M | — | — | 111 | — |  |
| M775 | M | — | — | 113 | — |  |
| M776 | M | — | — | 115 | — |  |
| M777 | M | — | — | 117 | — |  |
| M778 | M | — | — | 119 | — |  |
| M779 | M | — | — | 121 | — |  |
| M78 | M | — | 59 | — | 195 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M780 | M | — | — | 123 | — |  |
| M781 | M | — | — | 125 | — |  |
| M782 | M | — | — | 127 | — |  |
| M783 | M | — | — | 129 | — |  |
| M784 | M | — | — | 132 | — |  |
| M785 | M | — | — | 134 | — |  |
| M786 | M | — | — | 136 | — |  |
| M787 | M | — | — | 138 | — |  |
| M788 | M | — | — | 140 | — |  |
| M789 | M | — | — | 142 | — |  |
| M79 | M | — | 60 | — | 197 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M790 | M | — | — | 144 | — |  |
| M791 | M | — | — | 146 | — |  |
| M792 | M | — | — | 148 | — |  |
| M793 | M | — | — | 150 | — |  |
| M794 | M | — | — | 152 | — |  |
| M795 | M | — | — | 154 | — |  |
| M796 | M | — | — | 156 | — |  |
| M797 | M | — | — | 158 | — |  |
| M798 | M | — | — | 160 | — |  |
| M799 | M | — | — | 162 | — |  |
| M80 | M | — | 61 | — | 188 | NO_SET, DOUBLE_COIL_CANDIDATE |
| SM400 | SM | — | — | — | 1 |  |
| SM401 | SM | — | — | — | 3 |  |
| SM402 | SM | — | — | — | 5 |  |
| X0A0 | X | — | — | — | 98 |  |
| X0A1 | X | — | — | — | 100 |  |
| X0A2 | X | — | — | — | 102 |  |
| X0A3 | X | — | — | — | 104 |  |
| X0A4 | X | — | — | — | 106 |  |
| X0A5 | X | — | — | — | 108 |  |
| X0A6 | X | — | — | — | 110 |  |
| X0A7 | X | — | — | — | 112 |  |
| X0A8 | X | — | — | — | 114 |  |
| X0A9 | X | — | — | — | 116 |  |
| X0AA | X | — | — | — | 118 |  |
| X0AB | X | — | — | — | 120 |  |
| X0AC | X | — | — | — | 122 |  |
| X0AD | X | — | — | — | 124 |  |
| X0AE | X | — | — | — | 126 |  |
| X0AF | X | — | — | — | 128 |  |
| X0B0 | X | — | — | — | 131 |  |
| X0B1 | X | — | — | — | 133 |  |
| X0B2 | X | — | — | — | 135 |  |
| X0B3 | X | — | — | — | 137 |  |
| X0B4 | X | — | — | — | 139 |  |
| X0B5 | X | — | — | — | 141 |  |
| X0B6 | X | — | — | — | 143 |  |
| X0B7 | X | — | — | — | 145 |  |
| X0B8 | X | — | — | — | 147 |  |
| X0B9 | X | — | — | — | 149 |  |
| X0BA | X | — | — | — | 151 |  |
| X0BB | X | — | — | — | 153 |  |
| X0BC | X | — | — | — | 155 |  |
| X0BD | X | — | — | — | 157 |  |
| X0BE | X | — | — | — | 159 |  |
| X0BF | X | — | — | — | 161 |  |
| Y010 | Y | — | — | 165 | — |  |
| Y011 | Y | — | — | 167 | — |  |
| Y012 | Y | — | — | 169 | — |  |
| Y013 | Y | — | — | 173 | — |  |
| Y014 | Y | — | — | 175 | — |  |
| Y015 | Y | — | — | 177 | — |  |
| Y016 | Y | — | — | 179 | — |  |
| Y017 | Y | — | — | 181 | — |  |
| Y018 | Y | — | — | 183 | — |  |
| Y019 | Y | — | — | 185 | — |  |
| Y01A | Y | — | — | 187 | — |  |
| Y01B | Y | — | — | 171 | — |  |
| Y01C | Y | — | — | 189 | — |  |
| Y01D | Y | — | — | 192 | — |  |
| Y01E | Y | — | — | 194 | — |  |
| Y01F | Y | — | — | 196 | — |  |
| Y020 | Y | — | — | 201 | — |  |
| Y021 | Y | — | — | 203 | — |  |
| Y022 | Y | — | — | 205 | — |  |
| Y023 | Y | — | — | 209 | — |  |
| Y024 | Y | — | — | 211 | — |  |
| Y025 | Y | — | — | 213 | — |  |
| Y026 | Y | — | — | 215 | — |  |
| Y027 | Y | — | — | 217 | — |  |
| Y028 | Y | — | — | 219 | — |  |
| Y029 | Y | — | — | 221 | — |  |
| Y02A | Y | — | — | 223 | — |  |
| Y02B | Y | — | — | 207 | — |  |
| Y02C | Y | — | — | 198 | — |  |
