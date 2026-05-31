# REF — GX Works2 PLC IL CSV Processing

> **Domain**: Factory Automation / Mitsubishi Electric PLC  
> **Toolchain**: GX Works2 → Ladder Logic → IL (Instruction List) → CSV export → LLM Analysis  
> **Strict Constraint**: Design and code MUST strictly follow `Notes/GX_WORKS2_IL_Spec.md`

---

## Overview

REF is a workspace for analyzing, parsing, generating, and modifying CSV files exported from **Mitsubishi Electric GX Works2**. The exported CSV represents PLC Ladder Logic converted to IL (Instruction List) format.

The core specification (`Notes/GX_WORKS2_IL_Spec.md`) was reverse-engineered from real PLC export files (`F:\WorkSpace\MC_26074_DS\MAIN.csv`, 3,607 lines) and defines byte-level encoding rules. Violating even one rule causes GX Works2 import failure or abnormal PLC behavior.

---

## Target CSV Files

### Main Program

| File | Description |
|---|---|
| `main.csv` | Project-wide master program — orchestrates all individual functional modules. Contains the overall control flow, initialization, and global logic for the entire system. |

### Functional Modules

| File | Description |
|---|---|
| `gunvac.csv` | Gun vacuum control |
| `unitvac.csv` | Unit vacuum control |
| `vacchec.csv` | Vacuum check |
| `refinj.csv` | Refrigerant injection |
| `alarm.csv` | Alarm handling |
| `gmes.csv` | GMES (General-purpose) |
| `ad.csv` | Analog-to-Digital conversion |
| `485.csv` | RS-485 communication |
| `setting.csv` | System settings / configuration |
| `spc.csv` | SPC (Statistical Process Control) |
| `idata.csv` | Input data |

---

## Key Technical Constraints

### File Format (GX Works2 IL CSV)
- **Encoding**: UTF-16 LE with BOM (FF FE)
- **Line ending**: CR+LF (0D 00 0A 00 hex)
- **Field delimiter**: TAB (09 00)
- **No blank rows** anywhere in the file
- **Fixed file structure**:
  - Row 1: Program name (title)
  - Row 2: PLC information record
  - Row 3: Column header record
  - Row 4+: Data records
  - Last: END instruction record

### Non-compliance Consequence
- Import into GX Works2 fails or produces abnormal PLC behavior

---

## Directory Structure

```
REF/
├── AGENTS.md                                    # OpenCode agent config (graphify rules)
├── Notes/
│   ├── REF_DOCUMENT.md                          # This file — project documentation & reference data
│   └── GX_WORKS2_IL_Spec.md         # Strict IL CSV format specification
├── graphify-out/                                # Knowledge graph output
│   └── .graphify_detect.json
├── .opencode/                                   # OpenCode runtime config
└── .sisyphus/                                   # Sisyphus session data
```

### External Reference
- `F:\WorkSpace\MC_26074_DS\MAIN.csv` — Source-of-truth PLC export file (3,607 lines)
- `F:\WorkSpace\MC_26074_DS\L1_MAIN.csv`, `L2_MAIN.csv` — Additional reference exports

---

## Development Rules

1. All CSV read/write must strictly conform to `Notes/GX_WORKS2_IL_Spec.md` (IL writing rules). See [Reference Data](#reference-data) below for frequency evidence.
2. After code changes, run `graphify update .` to keep the knowledge graph current
3. For codebase questions, use `graphify query`, `graphify path`, or `graphify explain` when `graphify-out/graph.json` exists

---

## Reference Data

### Source Materials

| Source | Description |
|---|---|
| `F:\WorkSpace\MC_26074_DS\MAIN.csv` | Original PLC export (3,607 lines). Reverse-engineered for format rules. Now being reconstructed as the project's `main.csv`. |
| `F:\WorkSpace\MC_26074_DS\L1_MAIN.csv`, `L2_MAIN.csv` | Additional partial-exports confirming format variants. |
| `Notes/MELSEC_QL_Programming_Manual(Common_Instruction).pdf` | Mitsubishi official manual (1,096 pages). Documents the complete MELSEC-Q/L instruction set and List Mode (IL) format. Used to validate and extend the spec. |

> **Purpose**: This specification defines the mandatory format rules for CSV files exported from GX-Works2 by converting Ladder Logic to IL (Instruction List).
>
> **Non-compliance = failure**: Violating even one rule will cause GX-Works2 import to fail or produce abnormal PLC behavior.

### Hex Prefix Evidence (MAIN.csv)

```
FF FE  4D 00 43 00 5F 00 …      ← BOM, then "MC_..." in UTF-16 LE
… 5F 00 44 00 53 00  0D 00 0A 00  ← end of row 1 with CRLF
22 00 50 00 4C 00 43 00 …       ← start of row 2: "PLC...
```

### Verified Counts (MAIN.csv)

- Total lines: 3,607
- Blank lines: **0**
- Lines with exactly 7 TAB-separated fields: 3,605 (= rows 3 … 3,607, i.e. the column header + all data rows)
- Row 1: 1 field (title only)
- Row 2: 2 TAB-separated fields (PLC info)

### Mnemonic Frequency (MAIN.csv)

A total of **46 distinct mnemonics** are observed. All mnemonics are UPPERCASE, contain no internal whitespace.

| Category | Mnemonic | Count | Operands |
|---|---|---|---|
| Contact load | `LD` | 505 | 1 |
| | `LDI` | 53 | 1 |
| | `LDP` | 23 | 1 |
| | `LDF` | (rare) | 1 |
| AND series | `AND` | 359 | 1 |
| | `ANI` | 483 | 1 |
| | `ANDP` | (rare) | 1 |
| OR series | `OR` | 223 | 1 |
| | `ORI` | (rare) | 1 |
| | `ORP` | 13 | 1 |
| Block | `ANB` | 113 | 0 |
| | `ORB` | 35 | 0 |
| Inversion | `INV` | 24 | 0 |
| Stack | `MPS` | 35 | 0 |
| | `MPP` | 35 | 0 |
| | `MRD` | 22 | 0 |
| Output | `OUT` | 364 | 1 |
| | `SET` | 17 | 1 |
| | `RST` | 21 | 1 |
| | `PLS` | 15 | 1 |
| Word comparison (load/AND/OR) | `LD=` | 48 | 2 |
| | `LD<` | (rare) | 2 |
| | `LD<>` | 6 | 2 |
| | `AND=` | (rare) | 2 |
| | `OR=` | 10 | 2 |
| Double-word comparison | `LDD=` | 48 | 2 |
| | `LDD<` | (rare) | 2 |
| | `LDD>` | (rare) | 2 |
| | `ANDD<` | (rare) | 2 |
| | `ANDD<=` | (rare) | 2 |
| | `ANDD<>` | (rare) | 2 |
| | `ANDD=` | (rare) | 2 |
| | `ANDD>` | 6 | 2 |
| | `ORD=` | 36 | 2 |
| | `ORD<` | (rare) | 2 |
| Transfer (word / double-word) | `MOV` | 108 | 2 |
| | `MOVP` | 49 | 2 |
| | `DMOV` | 22 | 2 |
| | `DMOVP` | (rare) | 2 |
| Arithmetic (double-word) | `D+` | 68 | 3 |
| | `D-` | 48 | 3 |
| | `D*` | 8 | 3 |
| | `D/` | 7 | 3 |
| Increment | `INCP` | (rare) | 1 |
| Conversion | `FLT` | (rare) | 2 |
| Termination | `END` | 1 | 0 |

> Counts marked "(rare)" mean fewer than 6 occurrences; they are still confirmed present.

> For mnemonics not present in MAIN.csv but documented in the official MELSEC-Q/L manual, see `GX_WORKS2_IL_Spec.md` §6-1 and §6-2.

### Device Prefix Frequency (MAIN.csv)

| Prefix | Type | Count | Notation |
|---|---|---|---|
| `M` | Internal relay | 1,579 | `M0`, `M731`, `M1000`, `M1020`, … (decimal index) |
| `D` | Data register | 863 | `D0`, `D4`, `D780`, `D1230`, … (decimal index) |
| `K` | Decimal constant | 352 | `K0`, `K1`, `K2`, `K3` (literal decimal) |
| `T` | Timer | 209 | `T0`, `T1`, … (decimal index) |
| `L` | Latch relay | 168 | `L31`, `L32`, `L33`, … (decimal index) |
| `SM` | Special relay | 59 | `SM400`, … |
| `X` | Digital input | 44 | `X0BA`, `X0BB`, `X2F`, … (**uppercase hex** index) |
| `Y` | Digital output | 33 | `Y15`, `Y2F`, … (**uppercase hex** index) |

### Additional Device Types (not in MAIN.csv)

These are common in MELSEC-Q IL exports and may appear in sibling files: `SD` (special data register), `W` (link register, hex index), `B` (link relay, hex index), `R` / `ZR` (file register), `Z` (index register), `C` (counter), `H` (hex constant — `H300`, `H31A`), `E` (floating-point constant — `E1000`), `U<n>` / `U<n>\G<addr>` (intelligent module / buffer memory — the backslash is written literally, not escaped).
