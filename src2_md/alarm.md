---
# REF_self_holding -- IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 81
**Blocks:** 3
**Generated:** 2026-06-04
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | ALARM LATCH | 1–49 | LDI M771, LDI M779, LD M817 ... (+6) | 40 |
| 2 | BUZZER | 51–72 | LD M1028, LD M864 | 20 |
| 3 | ALARM RESET | 74–81 | LD M1027, LD M1027, LD M1027 ... (+1) | 4 |

## Block Detail

### Block 1: ALARM LATCH (Step 1-49)

**Trigger Condition:**
- LDI M771
- LDI M779
- LD M817
- LD M819
- LD M821
- LD M823
- LD M776
- LD M777
- LD M791

**Actions:**
- OR M864
- ANI M1027
- OUT M864
- OR M865
- ANI M1027
- OUT M865
- OR M833
- OR M866
- ANI M1027
- OUT M866
- OR M835
- OR M867
- ANI M1027
- OUT M867
- OR M837
- OR M868
- ANI M1027
- OUT M868
- OR M839
- OR M320
- OR M336
- OR M869
- ANI M1027
- OUT M869
- OR M792
- OR M872
- ANI M1027
- OUT M872
- OR M793
- OR M873
- ANI M1027
- OUT M873
- LD< D156
- OR> D156
- OR M874
- ANI M1027
- OUT M874
- OR M879
- ANI M1027
- OUT M879

### Block 2: BUZZER (Step 51-72)

**Trigger Condition:**
- LD M1028
- LD M864

**Actions:**
- OR M500
- ANI M1027
- OUT M500
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
- ANI M500
- OR M76
- ANI M1028
- OUT M76

### Block 3: ALARM RESET (Step 74-81)

**Trigger Condition:**
- LD M1027
- LD M1027
- LD M1027
- LD M1027

**Actions:**
- RST M875
- RST M876
- RST M877
- RST M878

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D156 | D |  |  |  | 2 |
| M1027 | M |  |  |  | 15 |
| M1028 | M |  |  |  | 2 |
| M320 | M |  |  |  | 1 |
| M336 | M |  |  |  | 1 |
| M500 | M |  |  | 1 | 2 |
| M76 | M |  |  | 1 | 1 |
| M771 | M |  |  |  | 1 |
| M776 | M |  |  |  | 1 |
| M777 | M |  |  |  | 1 |
| M779 | M |  |  |  | 1 |
| M791 | M |  |  |  | 1 |
| M792 | M |  |  |  | 1 |
| M793 | M |  |  |  | 1 |
| M817 | M |  |  |  | 1 |
| M819 | M |  |  |  | 1 |
| M821 | M |  |  |  | 1 |
| M823 | M |  |  |  | 1 |
| M833 | M |  |  |  | 1 |
| M835 | M |  |  |  | 1 |
| M837 | M |  |  |  | 1 |
| M839 | M |  |  |  | 1 |
| M864 | M |  |  | 1 | 2 |
| M865 | M |  |  | 1 | 2 |
| M866 | M |  |  | 1 | 2 |
| M867 | M |  |  | 1 | 2 |
| M868 | M |  |  | 1 | 2 |
| M869 | M |  |  | 1 | 2 |
| M872 | M |  |  | 1 | 2 |
| M873 | M |  |  | 1 | 2 |
| M874 | M |  |  | 1 | 2 |
| M875 | M |  | 1 |  | 1 |
| M876 | M |  | 1 |  | 1 |
| M877 | M |  | 1 |  | 1 |
| M878 | M |  | 1 |  | 1 |
| M879 | M |  |  | 1 | 2 |
