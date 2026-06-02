---
# MAIN — IL Logic Map
**CPU:** Q03UDV
**Total Steps:** 402
**Blocks:** 10
**Generated:** 2026-06-02
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | MODE CONTROL | 0–34 | LD M1038, LD M1536, LD M1536 | 24 |
| 2 | INTERLOCK CHECK | 35–47 | LD L81, LD L97 | 10 |
| 3 | STEP L0 | 48–95 | LD M16, LD M17, LD M18 | 39 |
| 4 | STEP L1 | 96–143 | LD M32, LD M33, LD M34 | 39 |
| 5 | NG ALARM STOP | 144–206 | LD L17, LD L64, LD L64 | 59 |
| 6 | MANUAL MODE | 207–239 | LD M1039, LD M1039, LD M1040 | 24 |
| 7 | STOP | 240–300 | LD M1044, LD M0, LD M0 | 52 |
| 8 | EMERGENCY STOP | 301–356 | LDI M771, LD M0, LD M0 | 48 |
| 9 | EXHAUST TIMER | 357–360 | LD M23 | 2 |
| 10 | LAMP CONTROL | 361–402 | LD M16, LD L64, LD M16 | 38 |

## Block Detail

### Block 1: MODE CONTROL (Step 0–34)

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

### Block 2: INTERLOCK CHECK (Step 35–47)

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

### Block 3: STEP L0 (Step 48–95)

**Trigger Condition:**
- LD M16
- LD M17
- LD M18
- LD M19
- LD M20
- LD M21
- LD M23
- LD M24

**Actions:**
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
- SET M17
- RST M16
- SET M18
- RST M17
- AND L16
- SET M19
- RST M18
- AND L18
- SET M20
- RST M19
- AND L20
- SET M21
- RST M20
- OR M22
- AND L22
- SET M23
- RST M21
- RST M22
- AND T3
- SET M24
- RST M23
- SET M16
- RST M24

### Block 4: STEP L1 (Step 96–143)

**Trigger Condition:**
- LD M32
- LD M33
- LD M34
- LD M35
- LD M36
- LD M37
- LD M39
- LD M40

**Actions:**
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
- SET M33
- RST M32
- SET M34
- RST M33
- AND L32
- SET M35
- RST M34
- AND L34
- SET M36
- RST M35
- AND L36
- SET M37
- RST M36
- OR M38
- AND L38
- SET M39
- RST M37
- RST M38
- AND T3
- SET M40
- RST M39
- SET M32
- RST M40

### Block 5: NG ALARM STOP (Step 144–206)

**Trigger Condition:**
- LD L17
- LD L64
- LD L64

**Actions:**
- OR L19
- OR L21
- OR L23
- RST M18
- RST M34
- RST M19
- RST M35
- RST M20
- RST M36
- RST M21
- RST M37
- RST M22
- RST M38
- RST M23
- RST M39
- SET M16
- SET M32
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
- RST M16
- RST M17
- RST M18
- RST M19
- RST M20
- RST M21
- RST M22
- RST M23
- RST M24
- SET M16
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
- RST M32
- RST M33
- RST M34
- RST M35
- RST M36
- RST M37
- RST M38
- RST M39
- RST M40
- SET M32

### Block 6: MANUAL MODE (Step 207–239)

**Trigger Condition:**
- LD M1039
- LD M1039
- LD M1040
- LD M1040
- LD M1041
- LD M1041
- LD M1042
- LD M1042

**Actions:**
- AND L2
- SET M18
- RST M16
- AND L2
- SET M34
- RST M32
- AND L2
- SET M19
- RST M16
- AND L2
- SET M35
- RST M32
- AND L2
- SET M20
- RST M16
- AND L2
- SET M36
- RST M32
- AND L2
- SET M21
- RST M16
- AND L2
- SET M37
- RST M32

### Block 7: STOP (Step 240–300)

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

### Block 8: EMERGENCY STOP (Step 301–356)

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

### Block 9: EXHAUST TIMER (Step 357–360)

**Trigger Condition:**
- LD M23

**Actions:**
- OR M39
- OUT T3

### Block 10: LAMP CONTROL (Step 361–402)

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
- END 

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps | Warnings |
|--------|------|-----------|-----------|-----------|------------|----------|
| D7012 | D | 299 | — | — | — | NO_RST |
| D8012 | D | 300 | — | — | — | NO_RST |
| K6 | K | — | — | — | 299, 300 |  |
| L0 | L | — | — | — | 50, 98 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L1 | L | 9 | 6 | — | 4, 8, 53, 101 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L100 | L | — | — | — | 45 | LATCH_DEVICE |
| L101 | L | — | — | — | 46 | LATCH_DEVICE |
| L112 | L | — | — | 14 | 12 | LATCH_DEVICE |
| L113 | L | — | — | 18 | 16 | LATCH_DEVICE |
| L114 | L | — | — | 22 | 20 | LATCH_DEVICE |
| L115 | L | — | — | 26 | 24 | LATCH_DEVICE |
| L116 | L | 34 | 31 | — | 30, 33 | LATCH_DEVICE |
| L16 | L | — | — | — | 72 | LATCH_DEVICE |
| L17 | L | — | — | — | 145 | LATCH_DEVICE |
| L18 | L | — | — | — | 76 | LATCH_DEVICE |
| L19 | L | — | — | — | 146 | LATCH_DEVICE |
| L2 | L | 5 | 10 | — | 209, 213, 217, 221, 225, 229, 233, 237 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L20 | L | — | — | — | 80 | LATCH_DEVICE |
| L21 | L | — | — | — | 147 | LATCH_DEVICE |
| L22 | L | — | — | — | 85 | LATCH_DEVICE |
| L23 | L | — | — | — | 148 | LATCH_DEVICE |
| L32 | L | — | — | — | 120 | LATCH_DEVICE |
| L34 | L | — | — | — | 124 | LATCH_DEVICE |
| L36 | L | — | — | — | 128 | LATCH_DEVICE |
| L38 | L | — | — | — | 133 | LATCH_DEVICE |
| L64 | L | 303 | — | — | 54, 102, 163, 185, 371, 385 | NO_RST, LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L65 | L | — | — | — | 55, 103, 164, 186, 372, 386 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L66 | L | — | — | — | 56, 104, 165, 187, 373, 387 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L67 | L | — | — | — | 57, 105, 166, 188, 374, 388 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L68 | L | — | — | — | 58, 106, 167, 189, 375, 389 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L69 | L | — | — | — | 59, 107, 168, 190, 376, 390 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L70 | L | — | — | — | 60, 108, 169, 191, 377, 391 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L71 | L | — | — | — | 61, 109, 170, 192, 378, 392 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L72 | L | — | — | — | 62, 110, 171, 193, 379, 393 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L73 | L | — | — | — | 63, 111, 172, 194, 380, 394 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L74 | L | — | — | — | 64, 112, 173, 195, 381, 395 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L78 | L | — | — | — | 65, 174, 382, 396 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L79 | L | — | — | — | 113, 196, 383, 397 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L80 | L | — | — | 41 | 51, 400 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L81 | L | — | — | — | 36 | LATCH_DEVICE |
| L82 | L | — | — | — | 37 | LATCH_DEVICE |
| L83 | L | — | — | — | 38 | LATCH_DEVICE |
| L84 | L | — | — | — | 39 | LATCH_DEVICE |
| L85 | L | — | — | — | 40 | LATCH_DEVICE |
| L96 | L | — | — | 47 | 99 | LATCH_DEVICE, DOUBLE_COIL_CANDIDATE |
| L97 | L | — | — | — | 42 | LATCH_DEVICE |
| L98 | L | — | — | — | 43 | LATCH_DEVICE |
| L99 | L | — | — | — | 44 | LATCH_DEVICE |
| M0 | M | — | — | — | 251, 260, 263, 272, 281, 290, 296, 312, 321, 324, 333, 342, 351 | DOUBLE_COIL_CANDIDATE |
| M1024 | M | — | — | — | 11, 17 |  |
| M1025 | M | — | — | — | 13, 15 |  |
| M1026 | M | — | — | — | 27 |  |
| M1032 | M | — | — | — | 19, 25 |  |
| M1033 | M | — | — | — | 21, 23 |  |
| M1038 | M | — | — | — | 1 |  |
| M1039 | M | — | — | — | 208, 212 |  |
| M1040 | M | — | — | — | 216, 220 |  |
| M1041 | M | — | — | — | 224, 228 |  |
| M1042 | M | — | — | — | 232, 236 |  |
| M1043 | M | — | — | — | 52 |  |
| M1044 | M | — | — | — | 241 |  |
| M1045 | M | — | — | — | 100 |  |
| M1536 | M | — | — | — | 3, 7 |  |
| M1537 | M | — | — | — | 29, 32 |  |
| M16 | M | 94, 161, 184, 297 | 67, 175, 211, 219, 227, 235, 243, 304 | — | 49, 362, 399 | DOUBLE_COIL_CANDIDATE |
| M17 | M | 66 | 70, 176, 244, 305 | — | 68, 363 | DOUBLE_COIL_CANDIDATE |
| M18 | M | 69, 210 | 74, 149, 177, 245, 306 | — | 71, 364 | DOUBLE_COIL_CANDIDATE |
| M19 | M | 73, 218 | 78, 151, 178, 246, 307 | — | 75, 365 | DOUBLE_COIL_CANDIDATE |
| M20 | M | 77, 226 | 82, 153, 179, 247, 308 | — | 79, 366 | DOUBLE_COIL_CANDIDATE |
| M21 | M | 81, 234 | 87, 155, 180, 248, 309 | — | 83, 367 | DOUBLE_COIL_CANDIDATE |
| M22 | M | — | 88, 157, 181, 249, 310 | — | 84, 368 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M23 | M | 86 | 92, 159, 182, 250, 311 | — | 89, 358, 369 | DOUBLE_COIL_CANDIDATE |
| M24 | M | 91 | 95, 183, 252, 313 | — | 93, 370 | DOUBLE_COIL_CANDIDATE |
| M32 | M | 142, 162, 206, 298 | 115, 197, 215, 223, 231, 239, 253, 314 | — | 97 | DOUBLE_COIL_CANDIDATE |
| M33 | M | 114 | 118, 198, 254, 315 | — | 116 | DOUBLE_COIL_CANDIDATE |
| M34 | M | 117, 214 | 122, 150, 199, 255, 316 | — | 119 | DOUBLE_COIL_CANDIDATE |
| M35 | M | 121, 222 | 126, 152, 200, 256, 317 | — | 123 | DOUBLE_COIL_CANDIDATE |
| M36 | M | 125, 230 | 130, 154, 201, 257, 318 | — | 127 | DOUBLE_COIL_CANDIDATE |
| M37 | M | 129, 238 | 135, 156, 202, 258, 319 | — | 131 | DOUBLE_COIL_CANDIDATE |
| M38 | M | — | 136, 158, 203, 259, 320 | — | 132 | NO_SET, DOUBLE_COIL_CANDIDATE |
| M39 | M | 134 | 140, 160, 204, 261, 322 | — | 137, 359 | DOUBLE_COIL_CANDIDATE |
| M40 | M | 139 | 143, 205, 262, 323 | — | 141 | DOUBLE_COIL_CANDIDATE |
| M48 | M | — | 264, 325 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M49 | M | — | 265, 326 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M50 | M | — | 266, 327 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M51 | M | — | 267, 328 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M52 | M | — | 268, 329 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M53 | M | — | 269, 330 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M54 | M | — | 270, 331 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M55 | M | — | 271, 332 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M56 | M | — | 273, 334 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M57 | M | — | 274, 335 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M58 | M | — | 275, 336 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M59 | M | — | 276, 337 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M64 | M | — | 277, 338 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M65 | M | — | 278, 339 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M66 | M | — | 279, 340 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M67 | M | — | 280, 341 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M68 | M | — | 282, 343 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M69 | M | — | 283, 344 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M70 | M | — | 284, 345 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M71 | M | — | 285, 346 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M72 | M | — | 286, 347 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M73 | M | — | 287, 348 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M74 | M | — | 288, 349 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M75 | M | — | 289, 350 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M76 | M | — | 291, 352 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| M769 | M | — | — | — | 242 |  |
| M77 | M | — | 292, 353 | 384 | — | DOUBLE_COIL_CANDIDATE |
| M771 | M | — | — | — | 302 |  |
| M78 | M | — | 293, 354 | 398 | — | DOUBLE_COIL_CANDIDATE |
| M79 | M | — | 294, 355 | 401 | — | DOUBLE_COIL_CANDIDATE |
| M80 | M | — | 295, 356 | — | — | NO_SET, DOUBLE_COIL_CANDIDATE |
| T3 | T | — | — | 360 | 90, 138 | DOUBLE_COIL_CANDIDATE |
