# REF_DOCUMENT

> **PLC**: QCPU (Q mode) Q03UDV | **Tool**: GX Works2 IL | **HMI**: LS IXP2-1200
> 
> IL coding rules: `gx_works2_il_spec.md` | CSV format: see [CSV Format Reference](#csv-format-reference)

---

# Program Structure

## System Overview
Refrigerant injection equipment. Two independent lanes (L0, L1) with shared HMI.

## Operation Modes

### Mode Toggle
- M1038 toggles M801 (auto) ↔ M802 (manual). SET/RST flip-flop with PLS edge (M600) — no 1-scan overlap.

### Manual Mode (M802 = ON)
- Function selection via HMI momentary buttons M1039-M1042.
- Function btn + START → direct step entry. Chain continues automatically from entry point.

| Btn | + START | Step |
|-----|---------|------|
| M1039 | M1043 | M18 gunvac L0 |
| M1040 | M1043 | M19 unitvac L0 |
| M1041 | M1043 | M20 vacchec L0 |
| M1042 | M1043 | M21+M22 refrig L0 |
| M1039 | M1045 | M34 gunvac L1 |
| M1040 | M1045 | M35 unitvac L1 |
| M1041 | M1045 | M36 vacchec L1 |
| M1042 | M1045 | M37+M38 refrig L1 |

## Step Machine

### L0
```
M16(init) → M17(wait) → M18(gunvac) → M19(unitvac)
          → M20(vacchec) → M21+M22(refrig, parallel) → M23(exhaust) → M24(complete) → M16
```
- M25/M26: oil sub-cycles (refinj-owned).
- **Rung order** (release step before released): M24→M23→M21→M22→M20→M19→M18→M17→M16

### L1
```
M32(init) → M33(wait) → M34(gunvac) → M35(unitvac)
          → M36(vacchec) → M37+M38(refrig, parallel) → M39(exhaust) → M40(complete) → M32
```
- M41/M42: oil sub-cycles (refinj-owned).
- **Rung order**: M40→M39→M37→M38→M36→M35→M34→M33→M32

## Injection Quantity

### PC/Barcode Mode (M803 = ON)
```
D7001(L0)/D8001(L1) → D60-D84/D88-D112 lookup → D0/D30 model index → D128/D404 final setpoint
```
- M876 SET if D7000≠1 or D8000≠2 → PC data error alarm.

### Manual Mode (M803 = OFF)
- User sets D0(L0)/D30(L1) to model 1-25 → D60-D84/D88-D112 lookup → D128/D404.

### Refrig Process
- D62 = gas type. D124 = current injection amount.
- Gas type 1: D124 ≥ D10 → M22 normal refrig → D124 ≥ D64 → exhaust.
- Gas type 0: D124 ≥ D64 → exhaust (skip normal).
- D72 = oil target → trigger oil sub-cycle or restart refrig.

## Stop / Emergency

| Action | Bit | Behavior |
|--------|-----|----------|
| STOP (M1044) | M301(L0) / M317(L1) | Self-holding ON. All steps `ANI M301/M317` → release. Init reactivates → latch OFF. |
| EMG (M303 N/C) | M304, M330 | Self-holding ON. All steps `ANI M304` → release. Manual reset: M303 restored + M1027 → M330 → M304 OFF. (IEC 60204-1 compliant) |

## Interlock

| Lane | Inputs | All-OK | Fail Latch |
|------|--------|--------|------------|
| L0 | M881-M885 (5, N/C closed=OK) | M880 | M316 |
| L1 | M897-M901 (5) | M896 | M332 |

- Interlock fail during M18/M19(L0) or M34/M35(L1): M316/M332 latches ON.
- `ANI M316` in M18/M19 ANI chain, `ANI M332` in M34/M35 ANI chain → immediate stop.
- **방폭** model: physical door sensors. **비방폭** model: inputs tied ON.

## Alarm System

| Item | Device | Detail |
|------|--------|--------|
| Latches | M864-M879 | Self-holding (M864-M874) or 1:1 SET/RST (M875-M879). Released by M1027. |
| Buzzer | M76 | Self-holding: any alarm AND not silenced → ON. OFF by M1028. |
| Silence | M500 | Self-holding: M1028→ON, M1027→OFF |
| Lamps | M77(green) / M78(red) / M79(yellow) | Step active / NG alarm / init+!interlock |
| Result codes | D7012(L0) / D8012(L1) | K1=OK, K2-K6=NG codes |

### Alarm Allocation (per Lane)

| Bit | Lane | Description | Type |
|----|------|-------------|------|
| M864 | Shared | Emergency Stop | self-hold |
| M865 | Shared | Door Open | self-hold |
| M866 | Shared | Vac Mismatch | self-hold |
| M867 | Shared | Unit Vac Mismatch | self-hold |
| M868 | Shared | Vac Leak | self-hold |
| M869 | Shared | Timeout Alarm | self-hold |
| M872 | Shared | Gas Check L1A | self-hold |
| M873 | Shared | Gas Check L1B | self-hold |
| M874 | Shared | Temp Out of Range | self-hold |
| M875 | **L0** | Bombe Count Exceed | 1:1 SET/RST |
| M876 | **L0** | PC Data Error | 1:1 SET/RST |
| M877 | **L1** | PC Data Error | 1:1 SET/RST |
| M878 | **L1** | Bombe Count Exceed | 1:1 SET/RST |
| M879 | **L1** | Interlock Fail | self-hold |

M870, M871 removed (were always-ON placeholders).

### ANI Chain

| Lane | Bits (in step ANI) |
|------|---------------------|
| L0 | M864-M869, M872-M874, M875, M876 (11) |
| L1 | M864-M869, M872-M874, M877, M878, M879 (12) |

## HMI Specification

> **Model**: LS IXP2-1200 (1024×768, XGA). All buttons momentary.

### Operation Screen Buttons

| Button | Device | Function |
|--------|--------|----------|
| MANUAL/AUTO | M1038 | Mode toggle → M801/M802 |
| GUN VACUUM | M1039 | Function select st0 |
| UNIT VACUUM | M1040 | Function select st1 |
| VACUUM CHECK | M1041 | Function select st2 |
| REFRIGER INJECTION | M1042 | Function select st3 |
| START | M1043(L0) / M1045(L1) | Initiate |
| STOP | M1044 | Stop |
| ALARM RESET | M1027 | Reset alarm latches |
| BUZZER STOP | M1028 | Silence buzzer |
| BARCODE USE/NOT USE | M803 | Toggle PC/barcode mode |
| MODEL SELECT | — | Set D0/D30 |

### Parameter ↔ PLC

| # | Parameter | Device | Unit |
|---|-----------|--------|------|
| 1 | Gun Vacuum Time | D2(L0) / D32(L1) | sec |
| 2 | Unit Vacuum Time | D4 / D34 | sec |
| 3 | Vacuum Check Time | D6 / D36 | sec |
| 4 | Exhaust Time | D8 / D38 | sec |
| 5 | Fast Stop Section | D10 | g |
| 6 | Bombe Alarm | D14 | Kg |
| 7 | Gas Used Amount | D280/D290 | Kg |
| 10 | Unit Vacuum Setting | D22 / D50 | Torr |
| 11 | Vacuum Check Setting | D24 / D52 | Torr |

### Screen Flow
```
POWER ON → OPERATION SCREEN
              ├── USER SETTING (per-gun model params)
              ├── PARAMETER SETTING (timers/limits)
              └── ALARM SCREEN
```

## File Map

| File | Sections | Content |
|------|----------|---------|
| MAIN.csv | 12 | Step machine, mode, stop/emg, interlock, lamps |
| alarm.csv | 3 | Alarm latches, buzzer, reset |
| refinj.csv | 14 | Refrig injection: fast/normal, oil cycles, exhaust |
| gunvac.csv | 2 | Gun vacuum: solenoids, OK/NG, timeout |
| unitvac.csv | 2 | Unit vacuum: solenoids, OK/NG |
| vacchec.csv | 2 | Vacuum check: delta calc, OK/NG |
| indexs.csv | 8 | PC data check, barcode lookup, manual model |
| spc.csv | 5 | Cycle counters, SPC logging, bombe alarm |
| gmes.csv | 2 | PC communication data packing |
| idata.csv | 8 | System flags, I/O mapping (X→M mirror) |
| setting.csv | 1 | Config sync |

## Device Address Map

### Step Machine
```
L0: M16-M26 (11)         L1: M32-M42 (11)          offset +16
```

### Solenoids / Outputs
```
L0: M49-M55 (7)          L1: M65-M71 (7)           offset +16
M96 L0 pump              M112 L1 pump              offset +16
M100 L0 vac aux          M116 L1 vac aux           offset +16
M102 L0 unit vac aux     M118 L1 unit vac aux      offset +16
```

### Control Flags
```
M301 L0 stop             M317 L1 stop              offset +16
M304 emergency latch (shared)
M312 L0 NG alarm OR      M328 L1 NG alarm OR       offset +16
M316 L0 interlock fail   M332 L1 interlock fail    offset +16
M320 L0 timeout          M336 L1 timeout           offset +16
M340 L0 oil restart      M356 L1 oil restart       offset +16
M330 EMG release permit (M303 AND M1027)
```

### HMI
```
M500 buzzer silence (shared)    M76 buzzer
M77 green  M78 red  M79 yellow
M530-M533 L0 lamps      M546-M549 L1 lamps         offset +16
M540 L0 run lamp        M556 L1 run lamp           offset +16
M1024-M1045 HMI buttons (hardware fixed)
M600-M601 PLS edge bits
```

### Results / Interlock / Direction
```
M816-M824 L0 results    M832-M840 L1 results       offset +16
M880-M885 L0 interlock  M896-M901 L1 interlock     offset +16
M864-M879 alarm latches (shared M864-M874, lane: M875-M879)
M912-M913 L0 direction  M928-M929 L1 direction     offset +16
M916 toggle (shared)
```

### Input Mapping
```
M768-M799 X→M mirror (hardware fixed)
M800 first-scan  M801 manual mode  M802 auto mode
```

### D-Registers
```
D0/D30   model index      D2-D38   timer presets
D60-D84  L0 model params  D88-D112 L1 model params
D124     current amount   D128/D404 final setpoint
D160/D172 vac current    D280-D298 SPC accumulators
D7000+   PC comm L0      D8000+   PC comm L1
```

---

# CSV Format Reference

## File Format
- **Encoding**: UTF-16 LE with BOM (`FF FE`)
- **Line ending**: CR+LF (`0D 00 0A 00`)
- **Field delimiter**: TAB (`09 00`)
- **No blank rows** anywhere
- **Structure**: Row1=Title, Row2=PLC info, Row3=Headers, Row4+=Data, Last=END

## Mnemonic Reference
Common mnemonics in this project:

| Category | Mnemonic | Operands | Usage |
|----------|----------|----------|-------|
| Contact | `LD`, `LDI`, `AND`, `ANI`, `OR`, `ORI` | 1 | Bit logic |
| Block | `ANB`, `ORB` | 0 | Block AND/OR |
| Output | `OUT`, `SET`, `RST`, `PLS` | 1 | Write actions |
| Comparison | `LD=`, `LD>`, `AND=`, `AND>=`, `LDD>=` | 2 | Compare |
| Transfer | `MOV`, `DMOV`, `BMOV`, `FMOV` | 2+ | Data move |
| Arithmetic | `D+`, `D-`, `D*`, `D/` | 3 | Math |
| Timer | `OUT Tn` + preset | 2 | Timer coil |
| Term | `END` | 0 | End of program |

## Device Prefix
| Prefix | Type | Index |
|--------|------|-------|
| `M` | Internal relay | **Decimal** (never hex) |
| `D` | Data register | Decimal |
| `T` | Timer | Decimal |
| `K` | Decimal constant | Literal |
| `X` | Digital input | Uppercase hex |
| `Y` | Digital output | Uppercase hex |
| `SM` | Special relay | Decimal |
| `L` | Latch relay | Decimal |
