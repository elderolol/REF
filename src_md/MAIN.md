---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 713
**Blocks:** 14
**Generated:** 2026-06-03
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | MODE CONTROL | 1–38 | LD M1038, LD M1536, LD M801 ... (+9) | 26 |
| 2 | INTERLOCK CHECK | 40–51 | LD M881, LD M897 | 10 |
| 3 | READY SET L0 | 53–68 | LD M1039, LD M1040, LD M1041 ... (+1) | 12 |
| 4 | READY SET L1 | 70–85 | LD M1039, LD M1040, LD M1041 ... (+1) | 12 |
| 5 | START EXEC L0 | 87–102 | LD M1043, LD M1043, LD M1043 ... (+1) | 12 |
| 6 | START EXEC L1 | 104–119 | LD M1045, LD M1045, LD M1045 ... (+1) | 12 |
| 7 | STEP L0 | 121–289 | LD M24, LD M16, LD M17 ... (+8) | 158 |
| 8 | STEP L1 | 291–459 | LD M40, LD M32, LD M33 ... (+8) | 158 |
| 9 | NG ALARM STOP | 461–506 | LD M817, LD M819, LD M821 ... (+3) | 40 |
| 10 | STOP | 508–567 | LD M1044, LD M0, LD M0 ... (+5) | 52 |
| 11 | EMERGENCY STOP | 569–624 | LDI M771, LD M0, LD M0 ... (+4) | 49 |
| 12 | EXHAUST TIMER | 626–629 | LD M23, LD M39 | 2 |
| 13 | LAMP CONTROL | 631–670 | LD M16, LD M864, LD M16 | 37 |
| 14 | HMI LAMP | 672–713 | LD M502, LD M503, LD M504 ... (+7) | 32 |

## Block Detail

### Block 1: MODE CONTROL (Step 1–38)

**Trigger Condition:**
- LD M1038
- LD M1536
- LD M801
- LD M1536
- LD M802
- LD M1024
- LD M1025
- LD M1032
- LD M1033
- LD M1026
- LD M1537
- LD M916

**Actions:**
- PLS M1536
- AND M802
- ANI M1536
- ORB 
- OUT M801
- AND M801
- ANI M1536
- ORB 
- OUT M802
- OR M912
- ANI M1025
- OUT M912
- OR M913
- ANI M1024
- OUT M913
- OR M914
- ANI M1033
- OUT M914
- OR M915
- ANI M1032
- OUT M915
- PLS M1537
- ANI M916
- ANI M1537
- ORB 
- OUT M916

### Block 2: INTERLOCK CHECK (Step 40–51)

**Trigger Condition:**
- LD M881
- LD M897

**Actions:**
- AND M882
- AND M883
- AND M884
- AND M885
- OUT M880
- AND M898
- AND M899
- AND M900
- AND M901
- OUT M896

### Block 3: READY SET L0 (Step 53–68)

**Trigger Condition:**
- LD M1039
- LD M1040
- LD M1041
- LD M1042

**Actions:**
- AND M802
- ANI M18
- SET M502
- AND M802
- ANI M19
- SET M503
- AND M802
- ANI M20
- SET M504
- AND M802
- ANI M21
- SET M505

### Block 4: READY SET L1 (Step 70–85)

**Trigger Condition:**
- LD M1039
- LD M1040
- LD M1041
- LD M1042

**Actions:**
- AND M802
- ANI M34
- SET M506
- AND M802
- ANI M35
- SET M507
- AND M802
- ANI M36
- SET M508
- AND M802
- ANI M37
- SET M509

### Block 5: START EXEC L0 (Step 87–102)

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

### Block 6: START EXEC L1 (Step 104–119)

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

### Block 7: STEP L0 (Step 121–289)

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
- ANI M864
- OUT M16
- AND M800
- AND M880
- AND M1043
- AND M801
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OR M17
- ANI M18
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M17
- OR M18
- ANI M19
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M18
- AND M816
- OR M19
- ANI M20
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M19
- AND M818
- OR M20
- ANI M21
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M20
- AND M820
- OR M21
- ANI M23
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M21
- AND M820
- OR M22
- ANI M23
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M22
- OR M22
- AND M822
- OR M23
- ANI M24
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M23
- AND T3
- OR M24
- ANI M16
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- OUT M24
- AND T3
- SET M824
- MOV K1

### Block 8: STEP L1 (Step 291–459)

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
- ANI M864
- OUT M32
- AND M800
- AND M896
- AND M1045
- AND M801
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OR M33
- ANI M34
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M33
- OR M34
- ANI M35
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M34
- AND M832
- OR M35
- ANI M36
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M35
- AND M834
- OR M36
- ANI M37
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M36
- AND M836
- OR M37
- ANI M39
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M37
- AND M836
- OR M38
- ANI M39
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M38
- OR M38
- AND M838
- OR M39
- ANI M40
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M39
- AND T3
- OR M40
- ANI M32
- ANI M864
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M879
- OUT M40
- AND T3
- SET M840
- MOV K1

### Block 9: NG ALARM STOP (Step 461–506)

**Trigger Condition:**
- LD M817
- LD M819
- LD M821
- LD M823
- LD M817
- LD M817

**Actions:**
- MOV K3
- MOV K3
- MOV K4
- MOV K4
- MOV K5
- MOV K5
- MOV K2
- MOV K2
- OR M819
- OR M821
- OR M823
- OR M864
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M870
- OR M871
- OR M872
- OR M873
- OR M874
- OR M878
- SET M16
- OR M819
- OR M821
- OR M823
- OR M864
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M870
- OR M871
- OR M872
- OR M873
- OR M874
- OR M879
- SET M32

### Block 10: STOP (Step 508–567)

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

### Block 11: EMERGENCY STOP (Step 569–624)

**Trigger Condition:**
- LDI M771
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
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

### Block 12: EXHAUST TIMER (Step 626–629)

**Trigger Condition:**
- LD M23
- LD M39

**Actions:**
- OUT T3
- OUT T3

### Block 13: LAMP CONTROL (Step 631–670)

**Trigger Condition:**
- LD M16
- LD M864
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
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M870
- ANI M871
- ANI M872
- ANI M873
- ANI M874
- ANI M878
- ANI M879
- OUT M77
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M870
- OR M871
- OR M872
- OR M873
- OR M874
- OR M878
- OR M879
- OUT M78
- ANI M880
- OUT M79

### Block 14: HMI LAMP (Step 672–713)

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
| M1536 | M |  |  |  | 5 |
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
| M800 | M |  |  |  | 2 |
| M801 | M |  |  | 1 | 4 |
| M802 | M |  |  | 1 | 10 |
| M816 | M |  |  |  | 1 |
| M817 | M |  |  |  | 3 |
| M818 | M |  |  |  | 1 |
| M819 | M |  |  |  | 3 |
| M820 | M |  |  |  | 2 |
| M821 | M |  |  |  | 3 |
| M822 | M |  |  |  | 1 |
| M823 | M |  |  |  | 3 |
| M824 | M | 1 |  |  |  |
| M832 | M |  |  |  | 1 |
| M834 | M |  |  |  | 1 |
| M836 | M |  |  |  | 2 |
| M838 | M |  |  |  | 1 |
| M840 | M | 1 |  |  |  |
| M864 | M |  |  |  | 40 |
| M865 | M |  |  |  | 22 |
| M866 | M |  |  |  | 22 |
| M867 | M |  |  |  | 22 |
| M868 | M |  |  |  | 22 |
| M869 | M |  |  |  | 22 |
| M870 | M |  |  |  | 22 |
| M871 | M |  |  |  | 22 |
| M872 | M |  |  |  | 22 |
| M873 | M |  |  |  | 22 |
| M874 | M |  |  |  | 22 |
| M878 | M |  |  |  | 12 |
| M879 | M |  |  |  | 12 |
| M880 | M |  |  | 1 | 2 |
| M881 | M |  |  |  | 1 |
| M882 | M |  |  |  | 1 |
| M883 | M |  |  |  | 1 |
| M884 | M |  |  |  | 1 |
| M885 | M |  |  |  | 1 |
| M896 | M |  |  | 1 | 1 |
| M897 | M |  |  |  | 1 |
| M898 | M |  |  |  | 1 |
| M899 | M |  |  |  | 1 |
| M900 | M |  |  |  | 1 |
| M901 | M |  |  |  | 1 |
| M912 | M |  |  | 1 | 1 |
| M913 | M |  |  | 1 | 1 |
| M914 | M |  |  | 1 | 1 |
| M915 | M |  |  | 1 | 1 |
| M916 | M |  |  | 1 | 2 |
| T3 | T |  |  | 2 | 4 |
