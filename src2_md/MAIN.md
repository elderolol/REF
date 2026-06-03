---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 638
**Blocks:** 10
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | MODE CONTROL | 1–34 | LD M1038, LD M600, LD M600 ... (+7) | 24 |
| 2 | INTERLOCK CHECK | 36–47 | LD M881, LD M897 | 10 |
| 3 | STOP / EMG LATCH | 49–127 | LD M1044, LD M1044, LD M303 ... (+21) | 55 |
| 4 | NG ALARM GROUP | 129–153 | LD M864, LD M864 | 23 |
| 5 | STEP L0 | 155–343 | LD M23, LD M23, LD M24 ... (+13) | 173 |
| 6 | STEP L1 | 345–542 | LD M39, LD M39, LD M40 ... (+13) | 182 |
| 7 | NG RESULT CODE | 544–555 | LD M817, LD M819, LD M821 ... (+1) | 8 |
| 8 | EXHAUST TIMER | 557–560 | LD M23, LD M39 | 2 |
| 9 | LAMP CONTROL | 562–603 | LD M16, LD M864, LD M16 | 39 |
| 10 | HMI LAMP | 605–638 | LD M18, LD M19, LD M20 ... (+7) | 24 |

## Block Detail

### Block 1: MODE CONTROL (Step 1-34)

**Trigger Condition:**
- LD M1038
- LD M600
- LD M600
- LD M1024
- LD M1025
- LD M1032
- LD M1033
- LD M1026
- LD M601
- LD M916

**Actions:**
- PLS M600
- AND M802
- SET M801
- RST M802
- AND M801
- SET M802
- RST M801
- OR M912
- ANI M1025
- OUT M912
- OR M913
- ANI M1024
- OUT M913
- OR M928
- ANI M1033
- OUT M928
- OR M929
- ANI M1032
- OUT M929
- PLS M601
- ANI M916
- ANI M601
- ORB 
- OUT M916

### Block 2: INTERLOCK CHECK (Step 36-47)

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

### Block 3: STOP / EMG LATCH (Step 49-127)

**Trigger Condition:**
- LD M1044
- LD M1044
- LD M303
- LDI M303
- LD M18
- LD M18
- LD M18
- LD M18
- LD M18
- LD M19
- LD M19
- LD M19
- LD M19
- LD M19
- LD M34
- LD M34
- LD M34
- LD M34
- LD M34
- LD M35
- LD M35
- LD M35
- LD M35
- LD M35

**Actions:**
- OR M301
- ANI M16
- OUT M301
- OR M317
- ANI M32
- OUT M317
- AND M1027
- OUT M330
- OR M304
- ANI M330
- OUT M304
- ANI M881
- ANI M882
- ORB 
- ANI M883
- ORB 
- ANI M884
- ORB 
- ANI M885
- ORB 
- ANI M881
- ORB 
- ANI M882
- ORB 
- ANI M883
- ORB 
- ANI M884
- ORB 
- ANI M885
- ORB 
- OR M316
- ANI M16
- OUT M316
- ANI M897
- ANI M898
- ORB 
- ANI M899
- ORB 
- ANI M900
- ORB 
- ANI M901
- ORB 
- ANI M897
- ORB 
- ANI M898
- ORB 
- ANI M899
- ORB 
- ANI M900
- ORB 
- ANI M901
- ORB 
- OR M332
- ANI M32
- OUT M332

### Block 4: NG ALARM GROUP (Step 129-153)

**Trigger Condition:**
- LD M864
- LD M864

**Actions:**
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M872
- OR M873
- OR M874
- OR M875
- OR M876
- OUT M312
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M872
- OR M873
- OR M874
- OR M877
- OR M878
- OR M879
- OUT M328

### Block 5: STEP L0 (Step 155-343)

**Trigger Condition:**
- LD M23
- LD M23
- LD M24
- LD M21
- LD M20
- LD M1042
- LD M20
- LD M1042
- LD M19
- LD M1041
- LD M18
- LD M1040
- LD M17
- LD M1039
- LD M16
- LD M24

**Actions:**
- AND T3
- OR M24
- ANI M16
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M24
- AND T3
- SET M824
- MOV K1
- OR M22
- AND M822
- OR M23
- ANI M24
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M23
- AND M820
- OR M340
- AND M1043
- ORB 
- OR M21
- ANI M23
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M21
- AND M820
- AND M1043
- ORB 
- OR M22
- ANI M23
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M22
- AND M818
- AND M1043
- ORB 
- OR M20
- ANI M21
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M20
- AND M816
- AND M1043
- ORB 
- OR M19
- ANI M316
- ANI M20
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M19
- AND M1043
- ORB 
- OR M18
- ANI M316
- ANI M19
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M18
- AND M800
- AND M880
- AND M1043
- AND M801
- OR M17
- ANI M18
- ANI M301
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M17
- OR M301
- OR M312
- OR M316
- OR M16
- ANI M17
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- OUT M16

### Block 6: STEP L1 (Step 345-542)

**Trigger Condition:**
- LD M39
- LD M39
- LD M40
- LD M37
- LD M36
- LD M1042
- LD M36
- LD M1042
- LD M35
- LD M1041
- LD M34
- LD M1040
- LD M33
- LD M1039
- LD M32
- LD M40

**Actions:**
- AND T3
- OR M40
- ANI M32
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M40
- AND T3
- SET M840
- MOV K1
- OR M38
- AND M838
- OR M39
- ANI M40
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M39
- AND M836
- OR M356
- AND M1045
- ORB 
- OR M37
- ANI M39
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M37
- AND M836
- AND M1045
- ORB 
- OR M38
- ANI M39
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M38
- AND M834
- AND M1045
- ORB 
- OR M36
- ANI M37
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M36
- AND M832
- AND M1045
- ORB 
- OR M35
- ANI M332
- ANI M36
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M35
- AND M1045
- ORB 
- OR M34
- ANI M332
- ANI M35
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M34
- AND M800
- AND M896
- AND M1045
- AND M801
- OR M33
- ANI M34
- ANI M317
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M33
- OR M317
- OR M328
- OR M332
- OR M32
- ANI M33
- ANI M304
- ANI M864
- ANI M865
- ANI M866
- ANI M867
- ANI M868
- ANI M869
- ANI M872
- ANI M873
- ANI M874
- ANI M877
- ANI M878
- ANI M879
- OUT M32

### Block 7: NG RESULT CODE (Step 544-555)

**Trigger Condition:**
- LD M817
- LD M819
- LD M821
- LD M823

**Actions:**
- MOV K3
- MOV K3
- MOV K4
- MOV K4
- MOV K5
- MOV K5
- MOV K2
- MOV K2

### Block 8: EXHAUST TIMER (Step 557-560)

**Trigger Condition:**
- LD M23
- LD M39

**Actions:**
- OUT T3
- OUT T3

### Block 9: LAMP CONTROL (Step 562-603)

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
- ANI M872
- ANI M873
- ANI M874
- ANI M875
- ANI M876
- ANI M877
- ANI M878
- ANI M879
- OUT M77
- OR M865
- OR M866
- OR M867
- OR M868
- OR M869
- OR M872
- OR M873
- OR M874
- OR M875
- OR M876
- OR M877
- OR M878
- OR M879
- OUT M78
- ANI M880
- OUT M79

### Block 10: HMI LAMP (Step 605-638)

**Trigger Condition:**
- LD M18
- LD M19
- LD M20
- LD M21
- LD M34
- LD M35
- LD M36
- LD M37
- LD M18
- LD M34

**Actions:**
- OUT M530
- OUT M531
- OUT M532
- OR M22
- OUT M533
- OUT M546
- OUT M547
- OUT M548
- OR M38
- OUT M549
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
- OUT M556

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| K1 | K |  |  |  | 2 |
| K2 | K |  |  |  | 2 |
| K3 | K |  |  |  | 2 |
| K4 | K |  |  |  | 2 |
| K5 | K |  |  |  | 2 |
| M1024 | M |  |  |  | 2 |
| M1025 | M |  |  |  | 2 |
| M1026 | M |  |  |  | 1 |
| M1027 | M |  |  |  | 1 |
| M1032 | M |  |  |  | 2 |
| M1033 | M |  |  |  | 2 |
| M1038 | M |  |  |  | 1 |
| M1039 | M |  |  |  | 2 |
| M1040 | M |  |  |  | 2 |
| M1041 | M |  |  |  | 2 |
| M1042 | M |  |  |  | 4 |
| M1043 | M |  |  |  | 6 |
| M1044 | M |  |  |  | 2 |
| M1045 | M |  |  |  | 6 |
| M16 | M |  |  | 1 | 7 |
| M17 | M |  |  | 1 | 4 |
| M18 | M |  |  | 1 | 11 |
| M19 | M |  |  | 1 | 11 |
| M20 | M |  |  | 1 | 7 |
| M21 | M |  |  | 1 | 6 |
| M22 | M |  |  | 1 | 5 |
| M23 | M |  |  | 1 | 8 |
| M24 | M |  |  | 1 | 6 |
| M301 | M |  |  | 1 | 10 |
| M303 | M |  |  |  | 2 |
| M304 | M |  |  | 1 | 19 |
| M312 | M |  |  | 1 | 1 |
| M316 | M |  |  | 1 | 4 |
| M317 | M |  |  | 1 | 10 |
| M32 | M |  |  | 1 | 5 |
| M328 | M |  |  | 1 | 1 |
| M33 | M |  |  | 1 | 3 |
| M330 | M |  |  | 1 | 1 |
| M332 | M |  |  | 1 | 4 |
| M34 | M |  |  | 1 | 10 |
| M340 | M |  |  |  | 1 |
| M35 | M |  |  | 1 | 10 |
| M356 | M |  |  |  | 1 |
| M36 | M |  |  | 1 | 6 |
| M37 | M |  |  | 1 | 5 |
| M38 | M |  |  | 1 | 4 |
| M39 | M |  |  | 1 | 7 |
| M40 | M |  |  | 1 | 5 |
| M530 | M |  |  | 1 |  |
| M531 | M |  |  | 1 |  |
| M532 | M |  |  | 1 |  |
| M533 | M |  |  | 1 |  |
| M540 | M |  |  | 1 |  |
| M546 | M |  |  | 1 |  |
| M547 | M |  |  | 1 |  |
| M548 | M |  |  | 1 |  |
| M549 | M |  |  | 1 |  |
| M556 | M |  |  | 1 |  |
| M600 | M |  |  |  | 3 |
| M601 | M |  |  |  | 3 |
| M77 | M |  |  | 1 |  |
| M78 | M |  |  | 1 |  |
| M79 | M |  |  | 1 |  |
| M800 | M |  |  |  | 2 |
| M801 | M | 1 | 1 |  | 3 |
| M802 | M | 1 | 1 |  | 1 |
| M816 | M |  |  |  | 1 |
| M817 | M |  |  |  | 1 |
| M818 | M |  |  |  | 1 |
| M819 | M |  |  |  | 1 |
| M820 | M |  |  |  | 2 |
| M821 | M |  |  |  | 1 |
| M822 | M |  |  |  | 1 |
| M823 | M |  |  |  | 1 |
| M824 | M | 1 |  |  |  |
| M832 | M |  |  |  | 1 |
| M834 | M |  |  |  | 1 |
| M836 | M |  |  |  | 2 |
| M838 | M |  |  |  | 1 |
| M840 | M | 1 |  |  |  |
| M864 | M |  |  |  | 22 |
| M865 | M |  |  |  | 22 |
| M866 | M |  |  |  | 22 |
| M867 | M |  |  |  | 22 |
| M868 | M |  |  |  | 22 |
| M869 | M |  |  |  | 22 |
| M872 | M |  |  |  | 22 |
| M873 | M |  |  |  | 22 |
| M874 | M |  |  |  | 22 |
| M875 | M |  |  |  | 12 |
| M876 | M |  |  |  | 12 |
| M877 | M |  |  |  | 12 |
| M878 | M |  |  |  | 12 |
| M879 | M |  |  |  | 12 |
| M880 | M |  |  | 1 | 2 |
| M881 | M |  |  |  | 3 |
| M882 | M |  |  |  | 3 |
| M883 | M |  |  |  | 3 |
| M884 | M |  |  |  | 3 |
| M885 | M |  |  |  | 3 |
| M896 | M |  |  | 1 | 1 |
| M897 | M |  |  |  | 3 |
| M898 | M |  |  |  | 3 |
| M899 | M |  |  |  | 3 |
| M900 | M |  |  |  | 3 |
| M901 | M |  |  |  | 3 |
| M912 | M |  |  | 1 | 1 |
| M913 | M |  |  | 1 | 1 |
| M916 | M |  |  | 1 | 2 |
| M928 | M |  |  | 1 | 1 |
| M929 | M |  |  | 1 | 1 |
| T3 | T |  |  | 2 | 4 |
