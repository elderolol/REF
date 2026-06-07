---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 166
**Blocks:** 5
**Generated:** 2026-06-06
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | SYSTEM FLAGS | 1–8 | LD SM400, LD SM401, LD SM402 ... (+1) | 4 |
| 2 | INPUT MAPPING (X → M) | 10–65 | LD X0A0, LD X0A1, LD X0A2 ... (+25) | 28 |
| 3 | INTERLOCK WIRING | 67–86 | LD M780, LD M781, LD M782 ... (+7) | 10 |
| 4 | OUTPUT MAPPING (M → Y) | 88–127 | LD M60, LD M61, LD M62 ... (+17) | 20 |
| 5 | HMI BUTTON BUFFER | 129–166 | LD M400, LD M401, LD M402 ... (+16) | 19 |

## Block Detail

### Block 1: SYSTEM FLAGS (Step 1–8)

**Trigger Condition:**
- LD SM400
- LD SM401
- LD SM402
- LD SM412

**Actions:**
- OUT M0
- OUT M1
- OUT M2
- OUT M3

### Block 2: INPUT MAPPING (X → M) (Step 10–65)

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

### Block 3: INTERLOCK WIRING (Step 67–86)

**Trigger Condition:**
- LD M780
- LD M781
- LD M782
- LD M783
- LD M0
- LD M791
- LD M792
- LD M793
- LD M794
- LD M0

**Actions:**
- OUT M81
- OUT M82
- OUT M83
- OUT M84
- OUT M85
- OUT M91
- OUT M92
- OUT M93
- OUT M94
- OUT M95

### Block 4: OUTPUT MAPPING (M → Y) (Step 88–127)

**Trigger Condition:**
- LD M60
- LD M61
- LD M62
- LD M63
- LD M64
- LD M70
- LD M71
- LD M72
- LD M73
- LD M74
- LD M65
- LD M66
- LD M75
- LD M76
- LD M69
- LD M77
- LD M78
- LD M79
- LD M67
- LD M68

**Actions:**
- OUT Y020
- OUT Y021
- OUT Y022
- OUT Y023
- OUT Y024
- OUT Y030
- OUT Y031
- OUT Y032
- OUT Y033
- OUT Y034
- OUT Y025
- OUT Y026
- OUT Y028
- OUT Y029
- OUT Y040
- OUT Y041
- OUT Y042
- OUT Y043
- OUT Y044
- OUT Y027

### Block 5: HMI BUTTON BUFFER (Step 129–166)

**Trigger Condition:**
- LD M400
- LD M401
- LD M402
- LD M403
- LD M404
- LD M405
- LD M406
- LD M407
- LD M408
- LD M409
- LD M410
- LD M411
- LD M412
- LD M413
- LD M414
- LD M415
- LD M416
- LD M417
- LD M418

**Actions:**
- OUT M400
- OUT M401
- OUT M402
- OUT M403
- OUT M404
- OUT M405
- OUT M406
- OUT M407
- OUT M408
- OUT M409
- OUT M410
- OUT M411
- OUT M412
- OUT M413
- OUT M414
- OUT M415
- OUT M416
- OUT M417
- OUT M418

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| M0 | M |  |  | 1 | 2 |
| M1 | M |  |  | 1 |  |
| M2 | M |  |  | 1 |  |
| M3 | M |  |  | 1 |  |
| M400 | M |  |  | 1 | 1 |
| M401 | M |  |  | 1 | 1 |
| M402 | M |  |  | 1 | 1 |
| M403 | M |  |  | 1 | 1 |
| M404 | M |  |  | 1 | 1 |
| M405 | M |  |  | 1 | 1 |
| M406 | M |  |  | 1 | 1 |
| M407 | M |  |  | 1 | 1 |
| M408 | M |  |  | 1 | 1 |
| M409 | M |  |  | 1 | 1 |
| M410 | M |  |  | 1 | 1 |
| M411 | M |  |  | 1 | 1 |
| M412 | M |  |  | 1 | 1 |
| M413 | M |  |  | 1 | 1 |
| M414 | M |  |  | 1 | 1 |
| M415 | M |  |  | 1 | 1 |
| M416 | M |  |  | 1 | 1 |
| M417 | M |  |  | 1 | 1 |
| M418 | M |  |  | 1 | 1 |
| M60 | M |  |  |  | 1 |
| M61 | M |  |  |  | 1 |
| M62 | M |  |  |  | 1 |
| M63 | M |  |  |  | 1 |
| M64 | M |  |  |  | 1 |
| M65 | M |  |  |  | 1 |
| M66 | M |  |  |  | 1 |
| M67 | M |  |  |  | 1 |
| M68 | M |  |  |  | 1 |
| M69 | M |  |  |  | 1 |
| M70 | M |  |  |  | 1 |
| M71 | M |  |  |  | 1 |
| M72 | M |  |  |  | 1 |
| M73 | M |  |  |  | 1 |
| M74 | M |  |  |  | 1 |
| M75 | M |  |  |  | 1 |
| M76 | M |  |  |  | 1 |
| M768 | M |  |  | 1 |  |
| M769 | M |  |  | 1 |  |
| M77 | M |  |  |  | 1 |
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
| M78 | M |  |  |  | 1 |
| M780 | M |  |  | 1 | 1 |
| M781 | M |  |  | 1 | 1 |
| M782 | M |  |  | 1 | 1 |
| M783 | M |  |  | 1 | 1 |
| M784 | M |  |  | 1 |  |
| M785 | M |  |  | 1 |  |
| M786 | M |  |  | 1 |  |
| M787 | M |  |  | 1 |  |
| M788 | M |  |  | 1 |  |
| M789 | M |  |  | 1 |  |
| M79 | M |  |  |  | 1 |
| M790 | M |  |  | 1 |  |
| M791 | M |  |  | 1 | 1 |
| M792 | M |  |  | 1 | 1 |
| M793 | M |  |  | 1 | 1 |
| M794 | M |  |  | 1 | 1 |
| M795 | M |  |  | 1 |  |
| M81 | M |  |  | 1 |  |
| M82 | M |  |  | 1 |  |
| M83 | M |  |  | 1 |  |
| M84 | M |  |  | 1 |  |
| M85 | M |  |  | 1 |  |
| M91 | M |  |  | 1 |  |
| M92 | M |  |  | 1 |  |
| M93 | M |  |  | 1 |  |
| M94 | M |  |  | 1 |  |
| M95 | M |  |  | 1 |  |
| SM400 | ? |  |  |  | 1 |
| SM401 | ? |  |  |  | 1 |
| SM402 | ? |  |  |  | 1 |
| SM412 | ? |  |  |  | 1 |
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
| Y030 | Y |  |  | 1 |  |
| Y031 | Y |  |  | 1 |  |
| Y032 | Y |  |  | 1 |  |
| Y033 | Y |  |  | 1 |  |
| Y034 | Y |  |  | 1 |  |
| Y040 | Y |  |  | 1 |  |
| Y041 | Y |  |  | 1 |  |
| Y042 | Y |  |  | 1 |  |
| Y043 | Y |  |  | 1 |  |
| Y044 | Y |  |  | 1 |  |
