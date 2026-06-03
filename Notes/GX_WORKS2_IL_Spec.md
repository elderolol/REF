# GX Works2 IL Specification

> **PLC**: QCPU (Q mode) Q03UDV | **Program**: REF refrigerant charging machine

---

# Part 1 — IL CSV Format

## File Encoding
- **UTF-16 LE with BOM** (`FF FE`). CR+LF line ending (`0D 00 0A 00`).
- **TAB** (`09 00`) field delimiter. No blank rows anywhere.

## File Structure (fixed order)

| Row | Content |
|-----|---------|
| 1 | Program name (e.g. `REF`) — bare text, no quotes, no TAB |
| 2 | PLC Info: `"PLC Information:"` TAB `"QCPU (Q mode) Q03UDV"` |
| 3 | Column headers: `"Step No."` TAB `"Line Statement"` TAB `"Instruction"` TAB `"I/O(Device)"` TAB `"Blank"` TAB `"PI Statement"` TAB `"Note"` |
| 4+ | Data rows (7 TAB-delimited fields) |
| Last | `"XXX"` TAB `""` TAB `"END"` TAB `""` TAB `""` TAB `""` TAB `""` |

## Data Row Types

| Type | Step No. | Line Statement | Instruction | I/O(Device) | Purpose |
|------|----------|---------------|-------------|-------------|---------|
| **A** | step number | `">> SECTION"` | `""` | `""` | Section header |
| **B** | step number | `""` | mnemonic | device | Instruction |
| **C** | `""` | `""` | `""` | device | Continuation operand |

- Type C rows carry the 2nd/3rd operand for multi-operand instructions (`LD=`, `MOV`, `D+`, etc.).
- Type C must immediately follow its parent Type B row.

## Quoting
- All 7 fields are double-quoted: `"value"`.
- Empty fields: `""`. Step number must be quoted: `"0"`.
- Program name (Row 1) is bare text — NOT quoted.

## Step Number Rules
- Sequential integers starting from 0. No gaps, no duplicates.
- Type C rows: Step No. is `""` (inherits from preceding Type B).
- Section headers (Type A) consume a step number.

## Instruction Mnemonics
All mnemonics UPPERCASE, no internal whitespace.

| Category | Mnemonics | Operands |
|----------|-----------|----------|
| Contact load | `LD`, `LDI` | 1 |
| Contact AND | `AND`, `ANI` | 1 |
| Contact OR | `OR`, `ORI` | 1 |
| Block | `ANB`, `ORB` | 0 |
| Output | `OUT`, `SET`, `RST`, `PLS` | 1 |
| Comparison (word) | `LD=`, `LD>`, `LD<`, `LD<>`, `LD<=`, `LD>=`, `AND=`, `AND>`, `AND<>`, `AND>=`, `AND<=` | 2 |
| Comparison (dword) | `LDD=`, `LDD>`, `LDD<`, `LDD>=`, `LDD<=`, `ANDD=`, `ANDD>`, `ANDD<>`, `ANDD>=` | 2 |
| Transfer | `MOV`, `DMOV`, `BMOV`, `FMOV` | 2+ |
| Arithmetic | `D+`, `D-`, `D*`, `D/` | 3 |
| Timer | Use `OUT Tn` with preset on Type C row | 2 |
| Terminator | `END` | 0 |

**Prohibited**: `TMR` (use `OUT`), `CJ` (use conditional MOV), `INV` (avoid), non-empty `Note` column.

## Device Operand Notation

| Device | Index Notation | Example |
|--------|:------------:|---------|
| `M` relay | **Decimal** | M1038 (not M40E) |
| `L` latch | **Decimal** | — |
| `D` register | **Decimal** | D160 |
| `T` timer | **Decimal** | T3 |
| `K` constant | **Decimal** | K100 |
| `X` input | **Uppercase Hex** | X0A0 |
| `Y` output | **Uppercase Hex** | Y011 |
| `SM` special | **Decimal** | SM400 |

# Part 2 — Project IL Coding Rules (REF)

## Self-Holding
- All state bits: `LD set_condition OR self ANI release_condition OUT self`.
- SET/RST: only 1:1 pairs (one SET, one RST per bit across all files).
- Bits with SET/RST must not also use OUT.

## HMI Buttons
- HMI buttons are momentary (one scan ON). Use directly — no PLS wrapper.
- Exception: complement toggle (e.g. mode flip-flop) uses SET/RST pair with PLS edge.
- Mode toggle (M1038): SET/RST flip-flop ensures atomic transition, no 1-scan overlap.

## Intermediate Group Bits
- Rungs with 6+ contacts: group conditions into an intermediate bit.
- Control flags: M310–M399 range, descriptive comments required.

## Rung Order (No One-Scan Overlap)
- Step machine: releasing step evaluated BEFORE released step.
- L0: M24→M23→M21→M22→M20→M19→M18→M17→M16
- L1: M40→M39→M37→M38→M36→M35→M34→M33→M32

## L0/L1 Mirror Convention
- All mirrored pairs: `L1_addr = L0_addr + 16` (offset 0x10).
- 52 pairs conforming. Covers step machine, solenoids, results, interlock, direction.

## Interlock Fail
- 5 interlock inputs per lane: M881-M885 (L0), M897-M901 (L1).
- Fail latch: M316 (L0) / M332 (L1). Self-holding, releases on init.
- Every vac step (M18, M19, M34, M35) MUST have `ANI M316` / `ANI M332`.

## Emergency Stop
- M303 (N/C input, OPEN = EMG). Latch: M304 (self-holding).
- Release permit: M330 = M303 AND M1027. M304 releases on `ANI M330`.
- Manual reset required (IEC 60204-1 compliant). Power cycle alone does not reset.

## Alarm Allocation
- Shared alarms: M864-M874 (self-holding).
- Lane-specific: M875(L0 bombe), M876(L0 PC error), M877(L1 PC error), M878(L1 bombe), M879(L1 interlock).
- ANI chain: L0 blocks M875, M876. L1 blocks M877, M878, M879. Shared blocks both.
- M870, M871: reserved (removed from self-holding).

## Device Comments
- Note column must be empty. Device comments go in `src2/ref_comment.csv`.
- All device addresses in comments use decimal notation.
