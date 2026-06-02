# GX-Works2 Instruction List (IL) CSV Export — Strict Format Specification

> See `REF_DOCUMENT.md` → [Reference Data](#reference-data) for source-of-truth information and frequency evidence.

---

## 1. File Encoding and BOM

- **Encoding**: UTF-16 LE (Little Endian).
- **BOM**: The file MUST begin with the byte order mark `FF FE`.
- **Line ending**: CR+LF, which in UTF-16 LE is the four-byte sequence `0D 00 0A 00`.
- **Field delimiter (inside a record)**: a single TAB character (`\t`, i.e. `09 00` in UTF-16 LE).
- **Record separator (between records)**: CR+LF — there is **no** blank line between records.
- **Prohibited**: Do NOT save as UTF-8. UTF-16 BE or UTF-16 LE without BOM is also invalid.

**Verified hex prefix**: see `REF_DOCUMENT.md` → [Reference Data](#reference-data)

---

## 2. Overall File Structure (order is fixed, NO blank rows)

```
[Row 1]   Program name (title)        ← see §3-1
[Row 2]   PLC information record      ← see §3-2
[Row 3]   Column header record        ← see §3-3
[Row 4+]  Data records                ← Type A / B / C (see §4)
[Last]    END instruction record      ← see §9
```

> **Critical correction**: There are **no blank/separator rows anywhere** in the file — not between sections, not between data rows. The file is dense: every line is meaningful. An export with empty lines inserted between sections or between data rows is malformed.

Verified counts: see `REF_DOCUMENT.md` → [Reference Data](#reference-data)

---

## 3. Detailed Rules for Each Row

### 3-1. Row 1 — Program Name (title) record

This row carries the project / POU title and is **not** wrapped in the same way as data rows. Two observed variants depending on which CSV the user exported:

| Export | Row 1 literal content |
|---|---|
| Full program export (e.g. `gunvac.csv`, `unitvac.csv`, ...) | `REF` — bare text, no surrounding quotes, no TAB |
| Partial / per-line export | `"?""REF"""` — wrapped, with a leading `?` marker character |

**Rules:**
- **This project**: the program name is `REF` for all generated CSV files.
- The title contains the project / POU name and may include non-ASCII characters (Korean, Japanese, etc.). The encoding (UTF-16 LE) guarantees they survive intact.
- A parser MUST treat row 1 as a free-text label and not as a TAB-delimited record.
- The leading `?` in partial exports is a GX-Works2 marker and should be stripped or preserved as-is when round-tripping.

### 3-2. Row 2 — PLC Information record

A single record containing two TAB-separated fields, but **the entire record is itself wrapped in an outer pair of `"`** (see the universal quoting rules in §4 below).

**Literal bytes (as it appears in the file):**
```
"PLC Information:<TAB>""QCPU (Q mode) Q03UDV"""
```

**Logical content after decoding the outer wrapping:**

| Field 1 | Field 2 |
|---|---|
| `PLC Information:` | `QCPU (Q mode) Q03UDV` |

**Rules:**
- Field 1 is the fixed literal `PLC Information:` (with trailing colon, no quotes around it inside the wrapping).
- Field 2 is the PLC model string. Examples observed: `QCPU (Q mode) Q03UDV`.
- This row has **2 fields**, not 7. Do not pad to 7.

### 3-3. Row 3 — Column header record (exactly 7 fields)

**Literal bytes:**
```
"Step No.<TAB>""Line Statement""<TAB>""Instruction""<TAB>""I/O(Device)""<TAB>""Blank""<TAB>""PI Statement""<TAB>""Note"""
```

**Logical content after decoding:**

| # | Field | Description |
|---|-------|-------------|
| 1 | `Step No.` | IL step number (integer string, or empty for continuation rows) |
| 2 | `Line Statement` | Network / section comment (Type A only; empty otherwise) |
| 3 | `Instruction` | IL mnemonic |
| 4 | `I/O(Device)` | Device operand or constant |
| 5 | `Blank` | Reserved; **always empty in observed data** |
| 6 | `PI Statement` | Reserved; **always empty in observed data** |
| 7 | `Note` | Reserved; **always empty in observed data** |

**Rules:**
- The column count MUST be **exactly 7** for the header row and every data row.
- The column names and their order are fixed.
- Columns 5, 6, 7 are reserved by the exporter and are empty in all observed rows; a compliant generator MUST still emit them as empty fields so the column count stays at 7.

---

## 4. Universal Quoting Model (the most error-prone part)

GX-Works2 emits a **non-standard "wrapped TSV"** format. Each record uses three nested escaping conventions, NOT one quote per field. Misunderstanding this is the #1 cause of broken round-trips.

### 4-1. Rule

For every record from row 2 onward (row 1 is the special bare-title row, see §3-1):

1. The **entire record** is wrapped in **one outer pair of `"`** — i.e. the line begins with `"` and ends with `"` (immediately before CRLF).
2. **Inside** that outer wrapping, fields are separated by TAB characters.
3. **Inside** that outer wrapping, every `"` character that belongs to a field is doubled (`""`) per RFC 4180 CSV escaping.

Concretely:

| Logical field value | How it appears inside the outer wrapping |
|---|---|
| empty | `""`              (two double quotes — an escaped quote, treated as empty content) |
| `LD` | `""LD""`          (escaped quote + `LD` + escaped quote) |
| `M1000` | `""M1000""`    |
| `Step No.` (column 1 of header, special) | `Step No.`  (the FIRST inner field is **not** quoted-inside, only inherits the outer wrapping) |

> **Subtle case — the first inner field.** Because the outer wrapping already begins with `"`, the very first inner field is written without its own pair of doubled quotes. You can see this in row 3: `"Step No.<TAB>""Line Statement""…"` — `Step No.` has no leading `""` of its own, but every other inner field does. The same applies to data rows: the `Step No.` column is written as just the integer (or empty), e.g. `"0<TAB>""""<TAB>…` not `"""0""<TAB>…`.

### 4-2. Worked example — Type B row `LD M1000` at step 0

Logical fields: `[ "0", "", "LD", "M1000", "", "", "" ]`

After step (3) — doubling all inner `"`:
- Field 1: `0`            (first inner — no extra quote pair)
- Field 2: `""""`          (empty wrapped in `""…""`)
- Field 3: `""LD""`
- Field 4: `""M1000""`
- Field 5: `""""`
- Field 6: `""""`
- Field 7: `""""`

Joined with TAB and wrapped in outer `"…"`:

```
"0<TAB>""""<TAB>""LD""<TAB>""M1000""<TAB>""""<TAB>""""<TAB>"""""
```

Note the trailing `"""""` — that is the empty field 7 (`""""`) immediately followed by the closing outer `"`, yielding five `"` characters in a row.

### 4-3. Parsing algorithm (recommended)

```python
def decode_record(raw: str) -> list[str]:
    """Decode one wrapped-TSV record into a list of logical field values."""
    s = raw.rstrip('\r\n')
    # Strip the outer wrapping
    assert s.startswith('"') and s.endswith('"')
    inner = s[1:-1]
    # Un-double the inner quotes
    inner = inner.replace('""', '"')
    # Split on TAB
    fields = inner.split('\t')
    # Each non-first inner field still has a wrapping pair "...", strip it.
    # The first field never has its own pair, so leave it alone.
    out = [fields[0]]
    for f in fields[1:]:
        if f.startswith('"') and f.endswith('"'):
            out.append(f[1:-1])
        else:
            out.append(f)
    return out
```

This decoder handles row 2 (2 fields), row 3 (7 fields), and all data rows (7 fields) correctly.

### 4-4. Generating (encoding) algorithm

```python
def encode_record(fields: list[str]) -> str:
    parts = []
    for i, f in enumerate(fields):
        if i == 0:
            parts.append(f)                    # first inner field: bare
        else:
            parts.append('"' + f.replace('"', '""') + '"')
    return '"' + '\t'.join(parts) + '"'
```

---

## 5. Three Types of Data Rows

All data rows (from row 4 onward) have **exactly 7 logical fields** after decoding §4.

### 5-1. Type A — Label / Line Statement row

Carries a step number plus a network/section comment. The Instruction column is empty.

**Logical fields:** `[<step>, <label>, "", "", "", "", ""]`

**Examples (decoded):**
```
[90,   "<<<<< Q64RD Card Converting Setup Program >>>>>>>", "", "", "", "", ""]
[117,  "MODE ",                                              "", "", "", "", ""]
[337,  "INPUT PULSE VERIFY",                                 "", "", "", "", ""]
[1008, "BARCODE ERROR -- INPUT+OUTPUT",                      "", "", "", "", ""]
[1025, "BARCODE -- INPUT+OUTPUT",                            "", "", "", "", ""]
```

A Type A row does **not** execute. It only labels a logical section of the program.

### 5-2. Type B — Instruction row (head of an instruction, with step number)

Carries a step number, the IL mnemonic, and the first operand (if any).

**Logical fields:** `[<step>, "", <mnemonic>, <operand1>, "", "", ""]`

**Examples (decoded):**
```
[0,    "", "LD",   "M1000", "", "", ""]
[1,    "", "MOVP", "K0",    "", "", ""]
[17,   "", "LD=",  "K1",    "", "", ""]
[4373, "", "END",  "",      "", "", ""]
```

For zero-operand instructions (`END`, `INV`, `MPS`, `MPP`, `MRD`, `ANB`, `ORB`) the operand field is empty (`""`).

### 5-3. Type C — Continuation row (extra operands of the preceding instruction)

Multi-operand instructions place their **first** operand on the Type B row, then put each **additional** operand on its own Type C row with no step number and no mnemonic.

**Logical fields:** `["", "", "", <operandN>, "", "", ""]`

**Example — `MOVP K0 D0` at step 1:**
```
Row B: [1,  "", "MOVP", "K0", "", "", ""]
Row C: ["", "", "",     "D0", "", "", ""]
```

**Example — `LD= K1 D4` at step 17:** (comparison with 2 operands)
```
Row B: [17, "", "LD=",  "K1", "", "", ""]
Row C: ["", "", "",     "D4", "", "", ""]
```

**Rules for Type C:**
- Step No., Line Statement, and Instruction MUST all be empty.
- I/O(Device) holds exactly one operand.
- Multiple Type C rows can follow a single Type B row, one operand per row, in the order required by the instruction.
- Type C rows are **invisible** to Step No. monotonicity (they belong to the preceding step).

---

## 6. Instruction Mnemonics

All mnemonics are UPPERCASE, contain no internal whitespace, and — for comparison instructions — concatenate the comparison symbol directly to the prefix (e.g. `LD=`, `ANDD<=`). Frequency counts are in `REF_DOCUMENT.md` → [Reference Data](#reference-data).

### 6-1. Sequence Instructions (confirmed in MAIN.csv + MELSEC manual)

#### Contact Instructions (Load / AND / OR)

| Category | Mnemonic | Operands | Description |
|----------|----------|----------|-------------|
| **Load** | `LD` | 1 | Operation start (NO contact) |
| | `LDI` | 1 | Operation start (NC contact) |
| | `LDP` | 1 | Rising edge pulse operation start |
| | `LDF` | 1 | Falling edge pulse operation start |
| | `LDPI` | 1 | Rising edge pulse NOT operation start |
| | `LDFI` | 1 | Falling edge pulse NOT operation start |
| **AND** | `AND` | 1 | Series connection (NO contact) |
| | `ANI` | 1 | Series connection (NC contact) |
| | `ANDP` | 1 | Rising edge pulse series connection |
| | `ANDF` | 1 | Falling edge pulse series connection |
| | `ANDPI` | 1 | Rising edge pulse NOT series connection |
| | `ANDFI` | 1 | Falling edge pulse NOT series connection |
| **OR** | `OR` | 1 | Parallel connection (NO contact) |
| | `ORI` | 1 | Parallel connection (NC contact) |
| | `ORP` | 1 | Rising edge pulse parallel connection |
| | `ORF` | 1 | Falling edge pulse parallel connection |
| | `ORPI` | 1 | Rising edge pulse NOT parallel connection |
| | `ORFI` | 1 | Falling edge pulse NOT parallel connection |

#### Association Instructions

| Mnemonic | Operands | Description |
|----------|----------|-------------|
| `ANB` | 0 | AND block — ladder block series connection |
| `ORB` | 0 | OR block — ladder block parallel connection |
| `MPS` | 0 | Store operation result (push) |
| `MRD` | 0 | Read operation result |
| `MPP` | 0 | Pop operation result (restore) |
| `INV` | 0 | Invert operation result |

#### Output Instructions

| Mnemonic | Operands | Description |
|----------|----------|-------------|
| `OUT` | 1 | Bit device output |
| `SET` | 1 | Bit device set |
| `RST` | 1 | Bit device reset |
| `PLS` | 1 | Rising edge pulse output |
| `PLF` | 1 | Falling edge pulse output |
| `FF` | 1 | Output reversal (flip-flop) |

#### Shift / Master Control / Termination

| Mnemonic | Operands | Description |
|----------|----------|-------------|
| `SFT` / `SFTP` | 2 | Bit device shift (SFT: always, SFTP: rising edge) |
| `SFR` / `SFRP` | 2 | n-bit right shift |
| `SFL` / `SFLP` | 2 | n-bit left shift |
| `MC` | 1 | Master control start |
| `MCR` | 1 | Master control reset |
| `FEND` | 0 | Subroutine program end |
| `END` | 0 | Program end (mandatory, last row) |
| `STOP` | 0 | Program stop |
| `NOP` | 0 | No operation |
| `NOPLF` | 0 | No operation (line feed for printing) |
| `PAGE` | 1 | Page break |

### 6-2. Basic Instructions (confirmed in MAIN.csv + MELSEC manual)

#### Comparison Instructions

| Category | Mnemonic Prefix | Operands | Data Type |
|----------|----------------|----------|-----------|
| **Word (16-bit)** | `LD=`, `LD<>`, `LD>`, `LD<=`, `LD<`, `LD>=` | 2 | BIN 16-bit |
| | `AND=`, `AND<>`, `AND>`, `AND<=`, `AND<`, `AND>=` | 2 | |
| | `OR=`, `OR<>`, `OR>`, `OR<=`, `OR<`, `OR>=` | 2 | |
| **Double-word (32-bit)** | `LDD=`, `LDD<>`, `LDD>`, `LDD<=`, `LDD<`, `LDD>=` | 2 | BIN 32-bit |
| | `ANDD=`, `ANDD<>`, `ANDD>`, `ANDD<=`, `ANDD<`, `ANDD>=` | 2 | |
| | `ORD=`, `ORD<>`, `ORD>`, `ORD<=`, `ORD<`, `ORD>=` | 2 | |
| **Float (single)** | `LDE=`, `LDE<>`, `LDE>`, `LDE<=`, `LDE<`, `LDE>=` | 2 | 32-bit float |
| | `ANDE=`, `ANDE<>`, `ANDE>`, `ANDE<=`, `ANDE<`, `ANDE>=` | 2 | |
| | `ORE=`, `ORE<>`, `ORE>`, `ORE<=`, `ORE<`, `ORE>=` | 2 | |
| **Float (double)** | `LDED=`, `LDED<>`, `LDED>`, `LDED<=`, `LDED<`, `LDED>=` | 2 | 64-bit float |
| | `ANDED=`, `ANDED<>`, `ANDED>`, `ANDED<=`, `ANDED<`, `ANDED>=` | 2 | |
| | `ORED=`, `ORED<>`, `ORED>`, `ORED<=`, `ORED<`, `ORED>=` | 2 | |
| **String** | `LD$=`, `LD$<>`, `LD$>`, `LD$<=`, `LD$<`, `LD$>=` | 2 | String |
| | `AND$=`, `AND$<>`, `AND$>`, `AND$<=`, `AND$<`, `AND$>=` | 2 | |
| | `OR$=`, `OR$<>`, `OR$>`, `OR$<=`, `OR$<`, `OR$>=` | 2 | |

#### Transfer / Arithmetic / Conversion Instructions

| Category | Mnemonic | Operands | Description |
|----------|----------|----------|-------------|
| **Transfer** | `MOV` / `MOVP` | 2 | 16-bit data transfer |
| | `DMOV` / `DMOVP` | 2 | 32-bit data transfer |
| | `EMOV` / `EMOVP` | 2 | Floating-point data transfer |
| | `EDMOV` / `EDMOVP` | 2 | Double-precision float transfer |
| | `BMOV` / `BMOVP` | 2 | Block data transfer |
| | `FMOV` / `FMOVP` | 2 | Same data block transfer |
| | `XCH` / `XCHP` | 2 | 16-bit data exchange |
| | `DXCH` / `DXCHP` | 2 | 32-bit data exchange |
| | `SMOV` / `SMOVP` | 2 | Shift data transfer |
| | `CML` / `CMLP` | 2 | 16-bit complement transfer |
| | `DCML` / `DCMLP` | 2 | 32-bit complement transfer |
| **Arithmetic** | `+`, `+P` | 2 | 16-bit addition |
| | `D+`, `D+P` | 3 | 32-bit addition |
| | `-`, `-P` | 2 | 16-bit subtraction |
| | `D-`, `D-P` | 3 | 32-bit subtraction |
| | `*`, `*P` | 2 | 16-bit multiplication |
| | `D*`, `D*P` | 3 | 32-bit multiplication |
| | `/`, `/P` | 2 | 16-bit division |
| | `D/`, `D/P` | 3 | 32-bit division |
| | `INC` / `INCP` | 1 | 16-bit increment (+1) |
| | `DINC` / `DINCP` | 1 | 32-bit increment (+1) |
| | `DEC` / `DECP` | 1 | 16-bit decrement (-1) |
| | `DDEC` / `DDECP` | 1 | 32-bit decrement (-1) |
| | `NEG` / `NEGP` | 1 | 16-bit sign inversion |
| | `DNEG` / `DNEGP` | 1 | 32-bit sign inversion |
| | `ENEG` / `ENEGP` | 1 | Floating-point sign inversion |
| **Conversion** | `BIN` / `BINP` | 2 | BCD → BIN (16-bit) |
| | `DBIN` / `DBINP` | 2 | BCD → BIN (32-bit) |
| | `BCD` / `BCDP` | 2 | BIN → BCD (16-bit) |
| | `DBCD` / `DBCDP` | 2 | BIN → BCD (32-bit) |
| | `FLT` / `FLTP` | 2 | BIN → Float (single precision) |
| | `DFLT` / `DFLTP` | 2 | BIN → Float (double precision) |
| | `INT` / `INTP` | 2 | Float → BIN (16-bit) |
| | `DINT` / `DINTP` | 2 | Float → BIN (32-bit) |

#### Program Control Instructions

| Mnemonic | Operands | Description |
|----------|----------|-------------|
| `CJ` | 1 | Conditional jump |
| `SCJ` | 1 | Scan conditional jump |
| `JMP` | 1 | Unconditional jump |
| `GOEND` | 0 | Jump to END instruction |

### 6-3. Notation Rules

- All mnemonics are UPPERCASE.
- Comparison mnemonics are a single token: `LD=`, `LDD<=`, `ANDD<>`, etc. **No spaces** between the prefix and the comparison symbol.
- Double-word variants are prefixed with `D` (`DMOV`, `D+`, `D-`, `D*`, `D/`, `LDD=`, …).
- Pulse / falling-edge variants use the `P` / `F` suffix:
  - Rising edge: `LDP`, `ANDP`, `ORP`, `MOVP`, `INCP` — executes on OFF→ON transition.
  - Falling edge: `LDF`, `ANDF`, `ORF` — executes on ON→OFF transition.
  - Pulse NOT rising: `LDPI`, `ANDPI`, `ORPI` — same as rising edge, inverted logic.
  - Pulse NOT falling: `LDFI`, `ANDFI`, `ORFI` — same as falling edge, inverted logic.
- Floating-point comparison uses `E` prefix (single) or `E` + `D` (double): `LDE=`, `LDED=`.
- String comparison uses `$` suffix: `LD$=`, `AND$<>`.

> Verified against `MELSEC-Q/L Programming Manual (Common Instruction)`. Frequency counts are in `REF_DOCUMENT.md` → [Reference Data](#reference-data). Mnemonics not confirmed in MAIN.csv are marked in the reference data — prefer MAIN.csv-confirmed mnemonics for maximum GX Works2 compatibility.

---

## 7. Device / Operand Notation

### 7-1. Observed device prefixes

See `REF_DOCUMENT.md` → [Reference Data](#reference-data) for the full device prefix frequency table and additional device types common in MELSEC-Q IL exports.

### 7-2. Notation rules

- Device **prefixes** are UPPERCASE.
- `X` / `Y` indices are written in **UPPERCASE hexadecimal** with no `H` prefix (e.g. `X0BA`, not `X186` or `Xh0BA`).
- `M`, `D`, `T`, `L`, `SM`, `SD`, `C`, `R` indices are written in **decimal**.
- `W`, `B` indices are written in hexadecimal.
- Constant prefixes (`K`, `H`, `E`) are written without zero-padding; preserve the literal value exactly as it appears in the source ladder.
- Intelligent-module buffer notation `U<n>\G<addr>`: write the backslash literally; do not escape it. Do not insert spaces.

---

## 8. Step No. Rules

- Step No. values on Type A and Type B rows are **strictly increasing** through the file.
- Increments are **variable** because each instruction consumes a variable number of program steps depending on its operand count and width.
- Type C (continuation) rows have **no** step number; they extend the immediately preceding Type B row's step.
- A Type A label row carries the step number of the first instruction of the network it labels (the next Type B row may share or immediately follow that step number).

---

## 9. END Instruction

- The last instruction in the program MUST be `END`, written as a Type B row with no operand.

**Literal final line example:**
```
"4373<TAB>""""<TAB>""END""<TAB>""""<TAB>""""<TAB>""""<TAB>"""""
```

**Decoded:** `[4373, "", "END", "", "", "", ""]`

- No further records (no blank line, no trailing comment) may appear after the `END` row.
- Because END has zero operands, no Type C row follows it.

---

## 10. Field Content Constraints

- **Reserved columns** 5, 6, 7 (`Blank`, `PI Statement`, `Note`) are empty in every row of every file observed. A generator MUST still emit them as empty fields so each data record has 7 fields.
- **No TAB characters** may appear inside any logical field value (a TAB inside a field would be indistinguishable from the field delimiter — the format does not provide an escape for it).
- **Embedded double quotes** in a field value are escaped by doubling them (per the universal quoting model in §4). In practice, observed exports never include `"` inside any field value, so this case is theoretical for this format.

---

## 11. Rung Composition Rules

This section defines how a single ladder rung is represented in IL and what structural rules govern it.

### 11-1. Rung boundary identification

A new rung begins when **any contact-load instruction** (`LD`, `LDI`, `LDP`, `LDF`) appears in a Type B row after the previous rung's output has completed.

The following signal the end of the previous rung and the start of a new one:

| Signal | Effect |
|---|---|
| A Type B row with `LD` / `LDI` / `LDP` / `LDF` | **Starts a new rung.** |
| A Type A label row | **Marks a section boundary.** The next Type B row (which must be a load instruction) begins the first rung of the new section. |
| A Type B row with `OUT`, `SET`, `RST`, `PLS`, `MOV…`, `DMOV…`, `D+`, `D-`, `D*`, `D/`, `INCP`, `FLT` | Output / application of the current rung — does NOT start a new rung by itself. |

**Critical rule:** a Type A row never substitutes for a load instruction. After a Type A label, the next Type B row must be a load (`LD`/`LDI`/`LDP`/`LDF`) to open the next rung.

### 11-2. Rung internal structure (canonical order)

Each rung, in order, contains:

```
[1] Load                  — LD / LDI / LDP / LDF                       (exactly 1, always first)
[2] Series / parallel     — AND, ANI, ANDP, OR, ORI, ORP,              (0 or more, in any order
    conditions              AND=, OR=, ANDD=, ANDD<, ANDD<=, ANDD<>,    that matches the ladder)
                            ANDD>, ORD=, ORD<,
                            ANB, ORB                                    (block connectors)
[3] Stack push            — MPS                                         (0 or more, only when branching)
[4] Per-branch conditions — same as [2]                                 (0 or more, per branch)
[5] Output / application  — OUT, SET, RST, PLS, INV,                    (1 or more per branch)
                            MOV, MOVP, DMOV, DMOVP,
                            D+, D-, D*, D/, INCP, FLT
[6] Stack restore         — MRD (intermediate branch)                   (must match each MPS;
                            MPP (final branch)                           MRD optional)
[7] Repeat [4]–[6]        for additional branches                       (one MPP, zero+ MRDs per MPS)
```

**Rules:**
- Step [1] is mandatory exactly once per rung.
- `MPS` / `MPP` are **always paired** within the same rung.
- `MRD` is used for intermediate branches between an `MPS` and its closing `MPP`.
- Block connectors `ANB` (AND-block) and `ORB` (OR-block) appear inside step [2] to combine sub-ladders that were themselves built with load instructions internally. They are not rung boundaries — they consume the top two elements of the operand stack.
- `INV` inverts the current logical result; it is treated as a 0-operand modifier within the rung.
- A rung may legally have **multiple output / application instructions** in sequence under the same load result (no re-load needed).
- A second `LD` / `LDI` / `LDP` / `LDF` inside the same rung is forbidden — it always starts a new rung.

### 11-3. Rung composition patterns

**Pattern 1 — Simple load + single output**
```
LD   M1000
MOVP K0  D0          ← (Type B: MOVP K0  +  Type C: D0)
```

**Pattern 2 — Load + multiple comparisons selecting an output**
```
LD=  K1  D4          ← (Type B: LD= K1  +  Type C: D4)
OUT  L31
LD=  K2  D4
OUT  L32
LD=  K3  D4
OUT  L33
```

**Pattern 3 — Load + AND + OUT**
```
LD   L31
AND  X0BA
OUT  M731
```

**Pattern 4 — Load + parallel-branch with MPS / MRD / MPP**
```
LD   <cond>
MPS                       ← push
AND  <branch1 cond>
OUT  <branch1 out>
MRD                       ← intermediate restore
AND  <branch2 cond>
OUT  <branch2 out>
MPP                       ← final restore
OUT  <branch3 out>
```

**Pattern 5 — Double-word arithmetic with 3 operands**
```
LD   SM400
DMOV D780 D782            ← (Type B: DMOV D780  +  Type C: D782)
```

### 11-4. Rung-boundary decision table

| Current row | Action |
|---|---|
| Type A (label row) | Mark section boundary; next Type B row starts the first rung. |
| Type B with `LD` / `LDI` / `LDP` / `LDF` | Start a new rung. |
| Type B with anything else (AND…, OR…, MPS/MPP/MRD, ANB/ORB, OUT, MOV…, etc.) | Continuation of the current rung. |
| Type C | Continuation of the current instruction (never a rung boundary). |

### 11-5. Constraints summary

```
- Every rung starts with exactly one load instruction (LD / LDI / LDP / LDF).
- AND/OR (and their comparison/double-word variants) follow the load and precede outputs.
- ANB and ORB combine sub-blocks; they do not start a new rung.
- MPS and MPP are paired within the same rung; MRD only appears between them.
- Multiple outputs are allowed in one rung (sequential, no extra LD needed).
- A second LD/LDI/LDP/LDF inside the same rung is forbidden — it always starts a new rung.
- Type A label rows never contain instructions and never act as a rung start by themselves.
- END terminates the program; it has no load instruction in front of it and no rows after it.
```

---

## 12. Checklist for Generating or Modifying This Format

```
[ ] Encoding: UTF-16 LE with BOM (FF FE)
[ ] Line endings: CRLF (0D 00 0A 00 in UTF-16 LE)
[ ] NO blank lines anywhere in the file
[ ] File structure: Row 1 title -> Row 2 PLC info -> Row 3 column header -> Row 4+ data -> last row END
[ ] Row 1 is the bare title (or "?""title""" for partial exports); NOT a 7-field record
[ ] Row 2 has exactly 2 logical fields: "PLC Information:" + model
[ ] Rows 3..end have exactly 7 logical fields
[ ] Whole-record wrapping: each record (rows 2..end) begins with " and ends with "
[ ] Inner fields separated by TAB; every inner field value wraps its own pair of "..." EXCEPT the first inner field
[ ] Every embedded " inside a field value is doubled to ""
[ ] Reserved columns 5, 6, 7 are emitted as empty
[ ] Correct row type:
    - Step No. + non-empty Line Statement + all other fields empty  -> Type A
    - Step No. + Instruction + (optional) first operand              -> Type B
    - Step No., Line Statement, Instruction all empty + operand only -> Type C
[ ] Step No. strictly increasing across Type A and Type B rows; Type C has no step
[ ] Mnemonics UPPERCASE, no whitespace, comparison symbol concatenated (LD=, ANDD<=, ...)
[ ] Device prefixes UPPERCASE; X/Y indices uppercase hex; M/D/T/L/SM/SD indices decimal
[ ] Constants K (decimal), H (hex), E (float) preserved without zero-padding
[ ] U<n>\G<addr> backslash preserved literally
[ ] Rung composition:
    - Each rung starts with exactly one LD/LDI/LDP/LDF
    - MPS / MPP paired in the same rung; MRD only between them
    - ANB / ORB used as block connectors, not rung starts
    - No second LD/LDI/LDP/LDF inside an ongoing rung
    - Type A rows never substitute for a load
[ ] Last data row is END (zero operand), and no rows follow it
```

---

## 13. Parsing Notes (LLM-Specific)

1. **Decode the wrapping first, parse fields second.** Use the algorithm in §4-3. Do not feed the raw line into a stock CSV library configured for `delimiter=','` or even `delimiter='\t'` — neither handles the outer-wrap + doubled-inner-quote convention correctly out of the box.

2. **Empty Step No. ⇒ Type C.** If field 1 is empty after decoding, the row continues the previous instruction's operand list. It is never a new instruction.

3. **Non-empty Line Statement ⇒ Type A.** If field 2 is non-empty after decoding, the row is a label / section comment. Fields 3–7 are required to be empty and the row carries no executable semantics.

4. **Multi-operand instructions read from a Type B row plus N Type C rows.** Operand counts per mnemonic (from §6):
   - 0 operands: `END`, `FEND`, `INV`, `MPS`, `MPP`, `MRD`, `ANB`, `ORB`, `NOP`, `NOPLF`, `STOP`, `GOEND`
   - 1 operand:  `LD`, `LDI`, `LDP`, `LDF`, `LDPI`, `LDFI`, `AND`, `ANI`, `ANDP`, `ANDF`, `ANDPI`, `ANDFI`, `OR`, `ORI`, `ORP`, `ORF`, `ORPI`, `ORFI`, `OUT`, `SET`, `RST`, `PLS`, `PLF`, `FF`, `MC`, `MCR`, `INCP`, `INC`, `DEC`, `PAGE`, `CJ`, `SCJ`, `JMP`, `NEG`
   - 2 operands: `MOV`, `MOVP`, `DMOV`, `DMOVP`, `FLT`, `SFT`, `SFTP`, `SFR`, `SFL`, `DINC`, `DDEC`, `DNEG`, all comparison mnemonics (`LD=`, `LDD<=`, `ANDD<>`, `ORD=`, `LDE=`, `LDED=`, `LD$=`, …)
   - 3 operands: `D+`, `D-`, `D*`, `D/`

   Use this table to know how many Type C rows to consume after each Type B row. For mnemonics not listed here, see `REF_DOCUMENT.md` → [Reference Data](#reference-data).

5. **Row 1 is special.** Skip CSV decoding for row 1 — read it as raw UTF-16 LE text. Detect partial-export marker (`?` prefix) if present.

6. **Row 3 (column header) is not data.** It must be skipped during data processing but used to validate the column-count and column-order invariants.

7. **There are no blank lines to skip.** Any blank line encountered indicates a corrupted or hand-edited file.

8. **Non-ASCII content survives via UTF-16 LE.** Korean / Japanese / other Unicode characters in the title row, Line Statements, or future Note columns are preserved natively. Always decode with `encoding='utf-16'` (Python) / `Encoding Unicode` (PowerShell) — never UTF-8.

---

## 14. Official Manual Reference & List Mode Format

The CSV format defined in this specification corresponds to **List Mode** in the official Mitsubishi MELSEC-Q/L Programming Manual (`Notes/MELSEC_QL_Programming_Manual(Common_Instruction).pdf`, 1,096 pages).

### List Mode (IL) Column Mapping

The official manual displays instructions in List Mode with three columns:

```
[List Mode]
Step  Instruction  Device
0     LD           X0
1     AND          M0
2     OUT          Y30
```

This maps to our CSV columns:

| List Mode Column | CSV Field # | CSV Column Name |
|---|---|---|
| `Step` | 1 | `Step No.` |
| — | 2 | `Line Statement` (Type A only) |
| `Instruction` | 3 | `Instruction` |
| `Device` | 4 | `I/O(Device)` |
| — | 5 | `Blank` |
| — | 6 | `PI Statement` |
| — | 7 | `Note` |

### Extended Instruction Set

The MELSEC manual documents additional mnemonics not found in the MAIN.csv reference export. These include floating-point comparisons (`LDE=`, `ANDED<>`, …), string comparisons (`LD$=`, …), pulse-NOT variants (`LDPI`, `ANDFI`, …), shift instructions (`SFT`, `SFR`, `SFL`), master control (`MC`, `MCR`), and program control (`CJ`, `FEND`, `STOP`, …). See `REF_DOCUMENT.md` → [Reference Data](#reference-data) for the complete list.

When generating IL CSV files, prefer mnemonics confirmed in MAIN.csv for maximum compatibility. Use extended mnemonics only when the source ladder logic requires them.


---

## 15. Verified IL Coding Rules & Patterns (Project REF)

> These rules were derived from repeated import/program-check cycles during the REF project on Q03UDV.

### 15-1. Device Address Notation

| Device | Doc Notation | PLC Notation | Example |
|--------|:------------:|:------------:|---------|
| M | Hex (e.g. M12) | **Decimal** (M18) | M12 (0x12=18) -> M18 (dec) |
| L | Hex (e.g. L51) | **Decimal** (L81) | L51 (0x51=81) -> L81 (dec) |
| D | **Decimal** | **Decimal** | D160 stays D160 |
| T | **Decimal** | **Decimal** | T0 stays T0 |
| X | **Hex** | **Hex** | X0A0 stays X0A0 |
| Y | **Hex** | **Hex** | Y011 stays Y011 |
| K (constant) | **Decimal** | **Decimal** | K100 stays K100 |

**Rule**: M and L devices are documented in hex ranges (e.g. M30~M4F, L10~L1F). When writing to the CSV, convert each hex address to decimal. D, T, K devices are always decimal. X, Y devices are always hex.

### 15-2. Timer Instruction -- Use OUT not TMR

| Rejected | Accepted |
|----------|----------|
| TMR T0 K100 | OUT T0 K100 |
| Type B: "TMR" "T0" + Type C: "K100" | Type B: "OUT" "T0" + Type C: "K100" |

**Verified**: GX Works2 does not recognize TMR as a valid IL CSV mnemonic. Use OUT for all timer coil outputs with the preset on a Type C continuation row.

### 15-3. Conditional Jump -- Avoid CJ in IL CSV

| Rejected | Rejected | Accepted |
|----------|----------|----------|
| CJ L0SKP (label name) | CJ P0 (P pointer) | Remove CJ; use LD</LD> conditional MOV instead |

**Verified**: GX Works2 IL CSV does not accept label names, P pointers, or step numbers as CJ targets. Replace CJ with conditional execution. Or use LD= comparisons + ANB block combine for type branching.

### 15-4. Note Column -- Do Not Use in IL CSV

| Rejected | Accepted |
|----------|----------|
| Any non-empty Note field | All Note fields = empty string |

**Errors**: Type A rows get "Failed to read note and statement". Type C rows get "No instruction before note". Type B rows get unpredictable failures.

**Rule**: Note column must be empty. Device comments go in a separate comment CSV file.

### 15-5. Device Comment CSV Format

Verified format for GX Works2 global device comment import:

```
"AAAA"
"Device Name"   "Comment"
"X0A1"  "STOP PB L0"
"M18"   "GUN VAC step L0"
"D160"  "AD CH2 EU L0 (32)"
"T0"    "Gun vacuum timer"
```

- Line 1: "AAAA" (fixed header)
- Line 2: "Device Name" tab "Comment" (header)
- UTF-16 LE BOM, CRLF, TAB-delimited
- Device names match PLC decimal addresses (M/L converted)
- Comment length <= 32 half-width chars
- D register: note bit-width as (16) or (32)

### 15-6. Comparison Instruction Patterns

**Pattern A -- AND-type (single-rung, recommended)**:

```
"20" "" "LD"     "M18"  "" "" ""   ; M12(hex)
"21" "" "AND"    "T0"   "" "" ""
"22" "" "ANDD<=" "D160" "" "" ""   ; Type B
""   "" ""       "D22"  "" "" ""   ; Type C (operand 2)
"23" "" "SET"    "L16"  "" "" ""   ; L10(hex)
```

**Pattern B -- Load-type + ANB (for type branching)**:

```
"10" "" "LD"     "M21"  "" "" ""   ; M15(hex)
"11" "" "LD="    "D62"  "" "" ""   ; new stack entry
""   "" ""       "K1"   "" "" ""
"12" "" "ANB"    ""     "" "" ""   ; AND type check
"13" "" "LDD>="  "D124" "" "" ""   ; new stack entry
""   "" ""       "D10"  "" "" ""   ; Type C
"14" "" "ANB"    ""     "" "" ""   ; AND volume check
"15" "" "RST"    "M52"  "" "" ""   ; M34(hex)
```

Stack flow: LD -> [step] -> LD= -> [step, type] -> ANB -> [step AND type] -> LDD>= -> [step AND type, vol] -> ANB -> [step AND type AND vol].

### 15-7. Rung Size -- Avoid Ladder Too Large (C9322/C9521)

**Cause**: GX Works2 converts IL rungs to ladder. Single rung with > ~40 parallel outputs exceeds ladder conversion limit.

**Fix**: Insert LD M0 between groups of ~8 outputs:

```
"8"  "" "LD"  "M2"  "" "" ""   ; Rung 1
"9"  "" "SET" "L0"  "" "" ""
"10" "" "RST" "M16" "" "" ""
...(7 more)
"17" "" "LD"  "M2"  "" "" ""   ; Rung 2 (new)
"18" "" "RST" "M24" "" "" ""
...
```

Also applies to EMG/STOP handlers with many RST instructions.

### 15-8. Multi-Operand Instruction Counts (Verified)

| Mnemonic | Operands | CSV Format |
|----------|:--------:|------------|
| OUT Tn | 2 | B: OUT T0, C: D2 (preset) |
| MOV | 2 | B: MOV D270, C: D274 |
| DMOV | 2 | B: DMOV D160, C: D300 |
| BMOV | 3 | B + C + C |
| D+, D-, D*, D/ | 3 | B + C + C (S1 S2 D) |
| LD=, LD<, LD> | 2 | B + C |
| ANDD<=, ANDD>= | 2 | B + C |
| LDD>=, LDD> | 2 | B + C |
| ANB, ORB | 0 | B only (device must be empty) |
| PLS | 1 | B only |

### 15-9. Format Constraints Summary

| Item | Constraint | Verified |
|------|-----------|:--------:|
| BOM | UTF-16 LE (FF FE) | OK |
| Line ending | CRLF | OK |
| Delimiter | TAB | OK |
| Fields per row | Exactly 7 | OK |
| Encoding | UTF-16 LE (never UTF-8) | OK |
| File name | <= 8 chars (excl. .csv) | OK |
| Note field | Must be empty | OK |
| Timer | OUT Tn, not TMR | OK |
| CJ | Avoid (use conditional MOV) | OK |
| M/L address | Decimal in CSV | OK |
| Rung outputs | <= 8 per rung | OK |
| Comment file header | "AAAA" header | OK |
| Comment length | <= 32 half-width chars | OK |
