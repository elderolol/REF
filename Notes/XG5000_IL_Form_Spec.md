# XG5000 IL Export — Strict Format Specification

> **Non-compliance = import failure or abnormal PLC behavior.**

---

## 1. File Encoding

- UTF-16 LE with BOM (`\xFF\xFE`)
- File extension: `.il`
- Line ending: CR+LF (`\r\n`)
- Tab (`\t`) separates mnemonic from operands
- No file-level headers, no step numbers, no column headers

**Wide-character display artifact:** When viewed as raw bytes, UTF-16 LE text appears spaced (`L O A D`, `M 0 0 0 4 2`). This is normal. Write content as plain UTF-16 LE — do NOT insert spaces between characters.

---

## 2. File Structure

```
[optional]  CMT lines
[repeated]  Instruction / CMT / OUTCMT lines
[last]      END
```

No header rows. No step numbers. No blank rows required.

---

## 3. Line Types

| Type | Format | Purpose |
|------|--------|---------|
| Instruction | `MNEMONIC\t<op1>\t<op2>...` | Executable IL instruction |
| CMT | `CMT\t<text>` | Section/rung label (non-executing) |
| OUTCMT | `OUTCMT\t<text>` | Output annotation (non-executing) |
| END | `END` | Program terminator — last line, no operands |

- All operands for one instruction are on the **same line** (no continuation rows)
- Multiple consecutive CMT lines allowed
- Multiple consecutive OUTCMT lines belong to the same preceding output

---

## 4. Instruction Set

All mnemonics UPPERCASE.

### Load (rung starters)
| Mnemonic | Operands | Operand order |
|----------|----------|---------------|
| `LOAD` | `<device>` | |
| `LOAD NOT` | `<device>` | |
| `LOADP` | `<device>` | rising-edge |
| `LOADN` | `<device>` | falling-edge |
| `LOAD=` | `<val>\t<device>` | constant first |
| `LOAD<` | `<val>\t<device>` | constant first |
| `LOAD>=` | `<device>\t<val>` | device first ⚠️ |

### AND Conditions
| Mnemonic | Operands |
|----------|----------|
| `AND` | `<device>` |
| `AND NOT` | `<device>` |
| `ANDP` | `<device>` rising-edge |
| `ANDN` | `<device>` falling-edge |
| `AND=` | `<val>\t<device>` constant first |
| `AND<` | `<val>\t<device>` constant first |
| `AND<=` | `<device>\t<val>` device first ⚠️ |
| `AND LOAD` | none — merges sub-stack into main |

### OR Conditions
| Mnemonic | Operands |
|----------|----------|
| `OR` | `<device>` |
| `OR NOT` | `<device>` keyword form |
| `ORP` | `<device>` rising-edge |
| `ORN` | `<device>` falling-edge / NC contact |
| `OR LOAD` | none — merges sub-stack into main |

### Stack (branch)
| Mnemonic | Operands | GX-Works2 equiv |
|----------|----------|-----------------|
| `MPUSH` | none | `MPS` |
| `MLOAD` | none | `MRD` |
| `MPOP` | none | `MPP` |

### Output
| Mnemonic | Operands |
|----------|----------|
| `OUT` | `<device>` |
| `OUTN` | `<device>` negated |
| `OUTP` | `<device>` pulse |
| `SET` | `<device>` |
| `RST` | `<device>` |

### Transfer
| Mnemonic | Operands |
|----------|----------|
| `MOV` / `MOVP` | `<src>\t<dst>` |
| `DMOV` / `DMOVP` | `<src>\t<dst>` 32-bit |
| `GMOV` / `GMOVP` | `<src>\t<dst>\t<count>` block |

### Timer / Counter
| Mnemonic | Operands |
|----------|----------|
| `TON` | `<timer>\t<preset>` |
| `TOFF` | `<timer>\t<preset>` |
| `CTU` | `<counter>\t<preset>` |

### Arithmetic / Block
| Mnemonic | Operands |
|----------|----------|
| `ADD` / `DIV` / `DSUB` | `<src1>\t<src2>\t<dst>` |
| `INCP` | `<device>` |
| `WSFLP` / `MINP` / `MAXP` | `<src>\t<dst>\t<count>` |

### Misc
| Mnemonic | Operands |
|----------|----------|
| `NOT` | none — inverts accumulator |

---

## 5. Device Notation

| Prefix | Type | Format | Example |
|--------|------|--------|---------|
| `M` | Internal relay | 5 hex digits, zero-padded | `M00042` `M0050B` |
| `D` | Data register | 5 decimal digits, zero-padded | `D17002` `D00018` |
| `T` | Timer | 4 decimal digits, zero-padded | `T0803` |
| `C` | Counter | 4 decimal digits, zero-padded | `C0000` |
| `F` | Special flag | 5 decimal digits | `F00000` `F00099` |
| `P` | Special pulse relay | 5 decimal digits | `P00998` |
| `U` | Module I/O | `U<slot>.<ch>.<bit>` | `U02.00.F` `U03.01.2` |

**Special flags:**
- `F00000` — Always-ON (≡ GX-Works2 `SM400`)
- `F00099` — Always-ON every scan
- `F00091` — 1-scan pulse

**Constants:**
- Decimal: plain integer, no prefix (`2`, `10`, `300`)
- Hex: lowercase `h` prefix, 8 digits (`h00000041`) — NOT `0x`

**Bit-addressed register:** `D<nnnnn>.<bit>` (e.g. `D02500.1`)

**U module operand spacing:** Operands are normally tab-separated.
Some observed instructions use a space within U-module operands (e.g. `DMOV\tU02.02 D00030`).
Both are accepted by XG5000. Prefer tab for new code.

---

## 6. Comparison Operand Order ⚠️

This asymmetry is critical and must be preserved exactly:

| Mnemonic | Order | Example |
|----------|-------|---------|
| `LOAD=` `LOAD<` | constant first | `LOAD=\t0\tD00080` |
| `AND=` `AND<` | constant first | `AND=\t0\tD00404` |
| `LOAD>=` | device first | `LOAD>=\tD01402\t10` |
| `AND<=` | device first | `AND<=\tD00148\tD00204` |

---

## 7. Rung Rules

### Rung boundary
A new rung starts with any Load instruction:
`LOAD` `LOAD NOT` `LOADP` `LOADN` `LOAD=` `LOAD<` `LOAD>=`

**Exception:** A secondary `LOAD`/`LOADP`/`LOADN` inside a rung is part of a sub-stack expression if followed by `AND LOAD` or `OR LOAD`. It does NOT start a new rung.

`CMT` lines mark section boundaries but do not start rungs.

### Rung internal structure
```
[1] Load                  LOAD / LOAD NOT / LOADP / LOADN / LOAD= / LOAD< / LOAD>=
[2] AND/OR conditions     AND / AND NOT / ANDP / ANDN / AND= / AND< / AND<=
                          OR / OR NOT / ORP / ORN / NOT
[3] MPUSH                 (optional — branch start)
[4] Branch conditions     AND / AND NOT / AND= ...
[5] Output(s)             OUT / OUTN / OUTP / MOV / TON / SET / RST ...
[6] MLOAD                 (optional — intermediate branch reload)
[7] MPOP                  (matches MPUSH)
[8] Final branch output   after MPOP
```

### Stack rules
- `MPUSH` and `MPOP` MUST be matched pairs within the same rung
- `MLOAD` only appears between `MPUSH` and `MPOP`
- Multiple sequential (non-nested) `MPUSH`/`MPOP` pairs allowed
- `MPUSH` / `MLOAD` / `MPOP` take NO operands

### Sub-stack (AND LOAD / OR LOAD)
```
LOAD    <main>
LOADN   <sub A>       ← sub-stack load (NOT a new rung)
ORN     <sub B>
AND LOAD              ← merges sub-result into main
<output>
```

### NOT instruction
`NOT` inverts the accumulator. No operand. Appears between conditions or before output.

### Rung completeness
- Every rung MUST start with a Load instruction
- Every rung MUST end with an output instruction (OUT / MOV / TON / SET / RST etc.)
- MPUSH and MPOP must be paired
- NOT must be followed by an output or MPUSH

---

## 8. Observed Patterns

```
# Pattern 1 — Simple
LOAD    F00000
GMOV    D16980  D17220  20

# Pattern 2 — Inverted AND chain
LOAD NOT  M00042
AND NOT   M0050B
NOT
MOV       2  D17002

# Pattern 3 — MPUSH branch
LOAD NOT  M00048
MPUSH
AND=      D17001  D00900
MOV       1  D00080
MLOAD
AND=      D17001  D00902
MOV       2  D00080
MPOP
AND=      D17001  D00938
MOV       10  D00080

# Pattern 4 — Sub-stack AND LOAD
LOAD NOT  M01011
LOADN     M00040
ORN       M00070
AND LOAD
MOV       1  D17012

# Pattern 5 — Comparison load
LOAD=     0  D00080
DMOVP     0  D00018

LOAD>=    D01402  10
TON       T0402   30

# Pattern 6 — Hex constant
LOAD    M00053
DMOV    h00000041  D06102

# Pattern 7 — Bit-addressed output
LOAD    T0402
AND NOT T0403
OUT     D02500.1

# Pattern 8 — U module
LOAD    U03.00.F
MPUSH
AND     U03.01.0
MOV     U03.02 D02610
MPOP
```

---

## 9. Checklist

```
[ ] UTF-16 LE with BOM (\xFF\xFE), CR+LF line endings, .il extension
[ ] No file headers, no step numbers, no column headers
[ ] All operands on the same line as the mnemonic (no continuation rows)
[ ] Mnemonic and operands tab-separated
[ ] All mnemonics UPPERCASE
[ ] Multi-word mnemonics use space: LOAD NOT / AND NOT / AND LOAD / OR LOAD / OR NOT
[ ] Pulse/edge suffixes appended directly: LOADP LOADN ANDP ANDN ORP ORN OUTN OUTP DMOVP MOVP GMOVP INCP MINP MAXP
[ ] Comparison operand order:
    LOAD= LOAD< AND= AND<  →  constant first: \t<val>\t<device>
    LOAD>= AND<=           →  device first:   \t<device>\t<val>
[ ] M: 5 hex digits | D: 5 decimal | T: 4 decimal | C: 4 decimal | F: 5 decimal
[ ] U device: U<slot>.<channel>.<bit>
[ ] Hex constants: lowercase h prefix (h00000041), not 0x
[ ] Bit-addressed: D<nnnnn>.<bit>
[ ] Decimal constants: plain integer, no prefix
[ ] Rung starts with LOAD / LOAD NOT / LOADP / LOADN / LOAD= / LOAD< / LOAD>=
[ ] Secondary LOAD inside AND LOAD / OR LOAD is NOT a new rung
[ ] MPUSH and MPOP always paired within the same rung
[ ] MLOAD only between MPUSH and MPOP
[ ] MPUSH / MLOAD / MPOP have no operands
[ ] NOT has no operand
[ ] SET RST INCP: 1 operand | CTU TON TOFF: 2 operands | ADD DIV DSUB WSFLP MINP MAXP: 3 operands
[ ] Every rung starts with a Load instruction
[ ] Every rung ends with an output instruction
[ ] MPUSH/MPOP paired; NOT followed by output or MPUSH
[ ] END is the last line — no operands, nothing after it
```