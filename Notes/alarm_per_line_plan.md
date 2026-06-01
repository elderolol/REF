# Alarm Per-Line Separation Plan

## Terminology
- NG (not "fail")

## Current Problem

Shared latches violate **Line Independence Principle**:

| Shared Latch | Sources | Problem |
|---|---|---|
| L42 = L11 OR L21 | GunVac L0/L1 | Line 1 GunVac NG → L0 injection also blocked |
| L43 = L13 OR L23 | UnitVac L0/L1 | Same |
| L44 = L15 OR L25 | VacLeak L0/L1 | Same |
| L45~L47 = L17 | Inj NG L0 only | L27 (L1 Inj NG) not even wired |
| L48 = M308 OR M318 | Press High L0/L1 | Same |
| L49 = M309 OR M319 | Press Low L0/L1 | Same |
| L4A = D156 OR D168 | Temp L0/L1 | Same |

## Latch Device Map (existing)

| Range | Usage | Details |
|---|---|---|
| L40 | EMG Stop | Global alarm latch |
| L41 | Safety Fault | Global alarm latch |
| L42-L4A | Process/Sensor latches | Shared L0+L1 (problem) |
| L4B | Bombe Low | Global (one refrigerant tank) |
| L4C | Door Open | Machine-level, explosion-proof only |
| L4D-L4F | Reserved | |
| L50-L5F | L0 Interlock Status | L50=Active, L51=SafetyOK, L52=VacFB, ... NOT available |
| L60-L6F | L1 Interlock Status | L60=Active, L61=SafetyOK, L62=VacFB, ... NOT available |

L50-L5F and L60-L6F are **interlock chains** (defined in gmes.csv), not available for alarm latches.

## Proposed Latch Allocation

### Line 0 latches (keep existing L42-L4A)
| Latch | Source | Condition |
|---|---|---|
| L42 | L11 | GunVac NG L0 |
| L43 | L13 | UnitVac NG L0 |
| L44 | L15 | VacLeak L0 |
| L45 | L17 + TOUT | Inj Timeout L0 |
| L46 | L17 + OVER | Inj Over L0 |
| L47 | L17 + UNDER | Inj Under L0 |
| L48 | M308 | Pressure High L0 |
| L49 | M309 | Pressure Low L0 |
| L4A | D156 | Temp Abnormal L0 |

### Line 1 latches (L70-L7F)
| Latch | Source | Condition |
|---|---|---|
| L70 | L21 | GunVac NG L1 |
| L71 | L23 | UnitVac NG L1 |
| L72 | L25 | VacLeak L1 |
| L73 | L27 + TOUT | Inj Timeout L1 |
| L74 | L27 + OVER | Inj Over L1 |
| L75 | L27 + UNDER | Inj Under L1 |
| L76 | M318 | Pressure High L1 |
| L77 | M319 | Pressure Low L1 |
| L78 | D168 | Temp Abnormal L1 |

### Bombe — configurable (depends on D330)
| Lines | L0 Latch | L0 Source | L1 Latch | L1 Source |
|---|---|---|---|---|
| 1-line (D330=1) | L4B | D16 >= D14 | — (shared) | — |
| 2-line (D330≥2) | L4B | D16 >= D14 | **L79** | D46 >= D44 |

L1 bombe params at D44 (setting), D46 (usage) — per DESIGN_REPORT D30~D59 = L1 param area.

### Keep shared (unconditional)
| Latch | Reason |
|---|---|
| L40 | EMG Stop — one for machine |
| L41 | Safety Fault — one safety PLC |
| L4C | Door Open — machine-level |

## Impact Analysis

### Physical Lamps removed
M4D/M4E/M4F → Y31/Y32/Y33 (Green/Red/Yellow) eliminated entirely. LAMP_CONTROL section deleted.
HMI button internal lamps (M420~M423 driven) are unaffected — these are software indicators on the HMI screen, not physical Y outputs.

### Buzzer (M4C → Y30) — single, shared
Single physical buzzer (Y30). Any line alarm → buzzer ON. Either line's BUZZER STOP (M404 or M406) stops it.

```
L40 OR L41 OR L42 OR L43 OR L44 OR L45 OR L46 OR L47
OR L48 OR L49 OR L4A OR L4B OR L4C
OR L70 OR L71 OR L72 OR L73 OR L74 OR L75 OR L76 OR L77 OR L78
→ OUT M4C

M404 OR M406 → RST M4C
```

### ALARM RESET (per-line)
HMI has separate Alarm Reset and Buzzer Stop buttons per line.

| Button | Line 0 | Line 1 |
|---|---|---|
| ALARM RESET | M403 | M405 |
| BUZZER STOP | M404 | M406 |

M403 resets L0 latches (L42-L4A, +L4B if 1-line). M405 resets L1 latches (L70-L79, +L79 if 2-line).
M404 OR M406 → RST M4C (single buzzer, either button stops it).

### Output Interlock
Per-line latches enable true per-line blocking:
- L42-L4A (L0) → block L0 injection only
- L70-L78 (L1) → block L1 injection only
- L40/L41 → global ALL OUT RST (unchanged)
- L4B/L4C → block both lines (shared)

### GMES Result Code (D7012 L0 / D8012 L1)
| Code | Meaning |
|:----:|---------|
| 1 | OK |
| 2 | Vacuum NG |
| 3 | Gun Vacuum NG |
| 4 | Unit Vacuum NG |
| 5 | Vacuum check NG |
| 6 | Operator stop |
| 7 | Refrig none flow NG |
| 8 | Charging time over |
| 9 | Refrig back flow |
| 10 | GMES data not match model |
| 11 | GMES data receive time over |

GunVac NG → `MOV K3 D7012` (L0) / `MOV K3 D8012` (L1)

## HMI-PLC Integration

### Screen Navigation
HMI (XP-Builder) 자체 Screen Change Button 사용 → PLC M bit 불필요.
M405/M406/M407 (USER SETTING / PARAMETER SETTING / ALARM SCREEN) → **삭제**.

### Alarm Page Navigation by D Register
Alarm 발생 시 PLC가 특정 D register에 alarm code를 쓰면 HMI가 해당 페이지로 전환.

| D | Direction | Format | Description |
|---|---|---|---|
| D500 | PLC → HMI | 16-bit (0=no alarm) | Alarm page navigation code |

Alarm code mapping (예시):
| Code | Page |
|:----:|------|
| 0 | No alarm — current page |
| 1 | EMG Stop page |
| 2 | GunVac NG |
| 3 | UnitVac NG |
| 4 | VacLeak NG |
| 5 | Inj NG |
| ... | (할당 예정) |

### Per-line ALARM RESET / BUZZER STOP (충돌 해결됨)
| 버튼 | L0 | L1 |
|---|---|---|
| ALARM RESET | M403 | M405 |
| BUZZER STOP | M404 | M406 |
| (화면 이동) | — (HMI 자체 기능으로 대체) |

### Injection Source Select (ex-BARCODE)

| Line | HMI Button | M | Toggle Flag | ON | OFF |
|:----:|------------|:-:|:-----------:|----|-----|
| L0 | INJECTION SOURCE | M40D | L3 | PC mode (Ethernet data) | Local mode (Model# preset) |
| L1 | INJECTION SOURCE | M41D | L4 | PC mode | Local mode |

## Resolved

1. **L27 (Inj NG L1)** — injection pulse count missing → L27 ON. Same logic as L17 for L0.
2. **Buzzer** — single Y30 shared. M404 OR M406 → RST M4C.
3. **L1 latch range** — L70-L7F (confirmed).
4. **Per-line ALARM RESET** — M403 (L0), M405 (L1) on HMI (confirmed).
5. **No lamps** — removed entirely (confirmed).

All open questions resolved. Ready for implementation.

## Manual Mode Change: Select → START

### Current (direct execute)
| HMI Button | Action |
|---|---|
| GUN VAC (M40F) | → SET M12 (즉시 실행) |
| UNIT VAC (M410) | → SET M13 |
| VAC CHECK (M411) | → SET M14 |
| INJECTION (M412) | → SET M15 |

### New (select → START)
| HMI Button | Action |
|---|---|
| GUN VAC (M40F) | → SET M420, RST M421~M423 |
| UNIT VAC (M410) | → SET M421, RST M420/M422/M423 |
| VAC CHECK (M411) | → SET M422, RST M420/M421/M423 |
| INJECTION (M412) | → SET M423, RST M420~M422 |
| START (M413 L0 / M415 L1) | → Check M420~M423 → SET corresponding step bit → RST M420~M423 |

### Function Status Bits (M420~M423 → HMI Button Lamp)

Dual mode: **Manual** = selected function waiting for START. **Auto** = current active step.

| Bit | Manual (L2=1) | Auto (L1=1) | Lamp |
|:---:|---|---|:----:|
| M420 | M40F chosen (selected) | M12/M22 (GUN VAC step active) | GUN VAC button |
| M421 | M410 chosen | M13/M23 (UNIT VAC step active) | UNIT VAC button |
| M422 | M411 chosen | M14/M24 (VAC CHECK step active) | VAC CHECK button |
| M423 | M412 chosen | M15/M16/M25/M26 (INJ step active) | INJECTION button |

**Manual mode (L2=1):** M420~M423 = function selection (mutual exclusive RST). Cleared on START/Done/NG/IDLE/STOP/EMG.

**Auto mode (L1=1):** M420 = M12 OR M22, M421 = M13 OR M23, M422 = M14 OR M24, M423 = M15 OR M16 OR M25 OR M26. Auto-cleared when step advances.
