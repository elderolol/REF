# XGK/XGB PLC — IL Instruction Reference for LLM Coding
> Source: XGK/XGB Instructions & Programming Manual V2.9 (LS Electric, 2020)  
> Target CPU: XGK-CPUE (Standard type)  
> Purpose: Machine-readable reference for LLM-assisted PLC code generation

---

## 1. Naming Conventions

### 1.1 Data Size Prefix/Suffix
| Symbol | Meaning | Example |
|--------|---------|---------|
| *(none)* | 16-bit WORD | `MOV`, `ADD` |
| `D` prefix | 32-bit DWORD (Double Word) | `DMOV`, `DADD` |
| `R` prefix | 32-bit Short Real (float) | `RMOV`, `RADD` |
| `L` prefix | 64-bit Long Real (double) | `LMOV`, `LADD` |
| `$` prefix | String | `$MOV`, `$ADD` |
| `G` prefix | Group (N words) | `GMOV`, `GADD` |
| `4` suffix | Nibble (4-bit) | `MOV4`, `BCD4` |
| `8` suffix | Byte (8-bit) | `MOV8`, `BCD8` |
| `3` suffix | 3-operand | `LOAD3`, `AND3` |

### 1.2 Execution Type Suffix
| Symbol | Meaning |
|--------|---------|
| *(none)* | Level-triggered (executes every scan while ON) |
| `P` suffix | Pulse (executes once on rising edge OFF→ON) |
| `N` suffix | Negative pulse (executes once on falling edge ON→OFF) |

> **Rule:** `MOVP` = MOV executed once on rising edge. `DADDP` = 32-bit ADD on rising edge.

### 1.3 Operand Symbols
| Symbol | Role |
|--------|------|
| `S` | Source — value not changed after operation |
| `D` | Destination — value written after operation |
| `S1`, `S2` | Two source operands |
| `N`, `n` | Count / number to process |
| `St`, `En` | Start, End (used in shift instructions) |
| `Sb`, `Db` | Source/Destination with Bit position specified |
| `Z` | Control word (format defined per instruction) |
| `T`, `t` | Timer area and preset value |
| `C`, `c` | Counter area and preset value |

---

## 2. Device (Memory) Area Reference

| Area | Symbol | Description | Bit Access | Word Access |
|------|--------|-------------|-----------|-------------|
| Input relay | `P` | Physical I/O inputs | `P0000` ~ | `P0000` ~ |
| Output relay | `P` | Physical I/O outputs | `P0040` ~ | `P0040` ~ |
| Auxiliary relay | `M` | Internal coils | `M0000` ~ | `M0000` ~ |
| Keep relay | `K` | Retentive coils | `K0000` ~ | `K0000` ~ |
| Link relay | `L` | Network link area | `L0000` ~ | `L0000` ~ |
| Timer | `T` | Timer contact/coil | `T000` ~ `T2047` | — |
| Counter | `C` | Counter contact/coil | `C000` ~ `C2047` | — |
| Step relay | `S` | SFC step control | `S00.00` ~ | — |
| Data register | `D` | General data memory | — | `D0000` ~ `D32767` |
| Special relay | `F` | System flags (read-only) | `F0000` ~ | — |
| File register | `R` | Extended data | — | `R0000` ~ `R32767` |
| Index register | `Z` | Index/offset register | — | `Z0` ~ `Z7` |
| Constant (Decimal) | `K` | Literal decimal | — | e.g. `K100` |
| Constant (Hex) | `H` | Literal hex | — | e.g. `H00FF` |

> **Index modifier:** `P00001[Z1]` — if Z1=8, resolves to `P00009`

---

## 3. Basic Instructions

### 3.1 Contact Instructions
| Mnemonic | Steps | Description |
|----------|-------|-------------|
| `LOAD` | 1 | Load NO (Normally Open) contact — start of rung |
| `LOAD NOT` | 1 | Load NC (Normally Closed) contact |
| `AND` | 1 | Series connect NO contact |
| `AND NOT` | 1 | Series connect NC contact |
| `OR` | 1 | Parallel connect NO contact |
| `OR NOT` | 1 | Parallel connect NC contact |
| `LOADP` | 2 | Load, triggers on rising edge (OFF→ON) |
| `LOADN` | 2 | Load, triggers on falling edge (ON→OFF) |
| `LOADP NOT` | 2 | Load NC, rising edge |
| `LOADN NOT` | 2 | Load NC, falling edge |
| `ANDP` | 2 | Series, rising edge |
| `ANDN` | 2 | Series, falling edge |
| `ANDP NOT` | 2 | Series NC, rising edge |
| `ANDN NOT` | 2 | Series NC, falling edge |
| `ORP` | 2 | Parallel, rising edge |
| `ORN` | 2 | Parallel, falling edge |
| `ORP NOT` | 2 | Parallel NC, rising edge |
| `ORN NOT` | 2 | Parallel NC, falling edge |
| `R_EDGE` | 1.5 | Positive edge detection |
| `F_EDGE` | 1.5 | Negative edge detection |

### 3.2 Union (Block Connection) Instructions
| Mnemonic | Steps | Description |
|----------|-------|-------------|
| `AND LOAD` | 1 | Connect two blocks in series |
| `OR LOAD` | 1 | Connect two blocks in parallel |
| `MPUSH` | 1 | Push current result to stack (branch point save) |
| `MLOAD` | 1 | Load previous branch point result |
| `MPOP` | 1 | Pop previous branch point result |

### 3.3 Reversion
| Mnemonic | Steps | Description |
|----------|-------|-------------|
| `NOT` | 1 | Invert current accumulator result |

### 3.4 Master Control
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `MCS` | `n` | 1 | Master Control Set (n: 0~7, nesting level) |
| `MCSCLR` | `n` | 1 | Master Control Clear |

### 3.5 Output Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `OUT` | `D` | 1 | Output coil (follows rung condition) |
| `OUT NOT` | `D` | 1 | Inverted output coil |
| `OUTP` | `D` | 2 | Output one scan on rising edge |
| `OUTN` | `D` | 2 | Output one scan on falling edge |
| `SET` | `D` | 1 | Latch coil ON (retentive) |
| `RST` | `D` | 1 | Latch coil OFF |
| `FF` | `D` | 1 | Flip-flop: toggle output on rising edge |

### 3.6 Step Control (SFC)
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `SET S` | `Sxx.xx` | 1 | Sequence control (activate step) |
| `OUT S` | `Sxx.xx` | 1 | Last-input preferred output |

### 3.7 End / NOP
| Mnemonic | Steps | Description |
|----------|-------|-------------|
| `END` | 1 | End of program |
| `NOP` | 1 | No operation (used in mnemonic/IL mode) |

---

## 4. Timer Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `TON` | `T n` | 2 | On-Delay timer — T contact ON after n×10ms |
| `TOFF` | `T n` | 2 | Off-Delay timer — T contact OFF after n×10ms |
| `TMR` | `T n` | 2 | Accumulative On-Delay (cumulative) |
| `TMON` | `T n` | 2 | Monostable (one-shot) timer |
| `TRTG` | `T n` | 2 | Retrigger timer — resets on re-trigger |

> `T`: timer area address (T000~T2047), `n`: preset value (×10ms resolution default)

---

## 5. Counter Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `CTU` | `C c` | 2 | Count-Up counter |
| `CTD` | `C c` | 2 | Count-Down counter |
| `CTUD` | `C U D c` | 4 | Up/Down counter (U=up pulse input, D=down pulse input) |
| `CTR` | `C c` | 2 | Ring counter (wraps at preset) |

> `C`: counter address, `c`: preset count value, `U/D`: up/down pulse contacts

---

## 6. Data Transfer Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `MOV` | `S D` | 2 | Copy 16-bit S → D |
| `MOVP` | `S D` | 3 | Copy 16-bit, rising edge |
| `DMOV` | `S D` | 2 | Copy 32-bit (S+1,S) → (D+1,D) |
| `DMOVP` | `S D` | 3 | Copy 32-bit, rising edge |
| `RMOV` | `S D` | 2 | Copy Short Real (32-bit float) |
| `RMOVP` | `S D` | 3 | Copy Short Real, rising edge |
| `LMOV` | `S D` | 2 | Copy Long Real (64-bit double) |
| `LMOVP` | `S D` | 3 | Copy Long Real, rising edge |
| `MOV4` | `Sb Db` | 3 | Copy 4-bit nibble |
| `MOV8` | `Sb Db` | 3 | Copy 8-bit byte |
| `CMOV` | `S D` | 2 | Copy 1's complement of S → D |
| `DCMOV` | `S D` | 2 | Copy 1's complement, 32-bit |
| `GMOV` | `S D N` | 4 | Copy N words from S → D |
| `GMOVP` | `S D N` | 5 | Copy N words, rising edge |
| `FMOV` | `S D N` | 4 | Fill N words in D with value S |
| `FMOVP` | `S D N` | 5 | Fill N words, rising edge |
| `BMOV` | `S D Z` | 4 | Copy specified bits (Z=control word) |
| `$MOV` | `S D` | 2 | Copy string from S → D |
| `$MOVP` | `S D` | 3 | Copy string, rising edge |

---

## 7. Code Conversion Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `BCD` | `S D` | 2 | BIN → BCD (16-bit) |
| `DBCD` | `S D` | 2 | BIN → BCD (32-bit) |
| `BIN` | `S D` | 2 | BCD → BIN (16-bit) |
| `DBIN` | `S D` | 2 | BCD → BIN (32-bit) |
| `BCD4` | `Sb Db` | 3 | BIN(0~9) → 4-bit BCD |
| `BCD8` | `Sb Db` | 3 | BIN(0~99) → 8-bit BCD |
| `BIN4` | `Sb Db` | 3 | 4-bit BCD → BIN |
| `BIN8` | `Sb Db` | 3 | 8-bit BCD → BIN |
| `GBCD` | `S D N` | 4 | Group BIN→BCD (N words) |
| `GBIN` | `S D N` | 4 | Group BCD→BIN (N words) |
| `WTODW` | `S D` | 4 | WORD → DWORD (zero-extend) |
| `DWTOW` | `S D` | 4 | DWORD → WORD (lower 16-bit) |

---

## 8. Data Type Conversion Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `I2R` | `S D` | 2 | INT(16) → Short Real |
| `I2L` | `S D` | 2 | INT(16) → Long Real |
| `D2R` | `S D` | 2 | DINT(32) → Short Real |
| `D2L` | `S D` | 2 | DINT(32) → Long Real |
| `R2I` | `S D` | 2 | Short Real → INT(16) |
| `R2D` | `S D` | 2 | Short Real → DINT(32) |
| `L2I` | `S D` | 2 | Long Real → INT(16) |
| `L2D` | `S D` | 2 | Long Real → DINT(32) |
| `R2L` | `S D` | 2 | Short Real → Long Real |
| `L2R` | `S D` | 2 | Long Real → Short Real |
| `U2R` | `S D` | 2 | UINT(16) → Short Real |
| `U2L` | `S D` | 2 | UINT(16) → Long Real |
| `UD2R` | `S D` | 2 | UDINT(32) → Short Real |
| `UD2L` | `S D` | 2 | UDINT(32) → Long Real |
| `R2U` | `S D` | 2 | Short Real → UINT(16) |
| `R2UD` | `S D` | 2 | Short Real → UDINT(32) |
| `L2U` | `S D` | 2 | Long Real → UINT(16) |
| `L2UD` | `S D` | 2 | Long Real → UDINT(32) |

> All above have `P` variants (e.g. `I2RP`) for rising-edge execution.

---

## 9. Comparison Instructions

### 9.1 Output Comparison (result → special relay flags)
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `CMP` | `S1 S2` | 2 | Compare S1 vs S2 (16-bit unsigned) → sets F (flag) |
| `DCMP` | `S1 S2` | 2 | Compare 32-bit unsigned |
| `CMP4` | `S1 S2` | 3 | Compare 4-bit (nibble) |
| `CMP8` | `S1 S2` | 3 | Compare 8-bit (byte) |
| `TCMP` | `S1 S2 D` | 4 | Table compare 16 words; result bits in D~D+15 |
| `DTCMP` | `S1 S2 D` | 4 | Table compare 16 double-words |

### 9.2 Input Comparison (used directly in rung as contact)
| Mnemonic | Operands | Description |
|----------|----------|-------------|
| `LOAD= S1 S2` | S1, S2 | True if S1 == S2 (signed 16-bit) |
| `LOAD<> S1 S2` | S1, S2 | True if S1 != S2 |
| `LOAD> S1 S2` | S1, S2 | True if S1 > S2 |
| `LOAD>= S1 S2` | S1, S2 | True if S1 >= S2 |
| `LOAD< S1 S2` | S1, S2 | True if S1 < S2 |
| `LOAD<= S1 S2` | S1, S2 | True if S1 <= S2 |
| `LOADD= S1 S2` | S1, S2 | 32-bit signed equal |
| `LOADR= S1 S2` | S1, S2 | Short Real equal |
| `LOADL= S1 S2` | S1, S2 | Long Real equal |
| `LOAD$ = S1 S2` | S1, S2 | String equal |

> Also available: `AND=`, `OR=` variants and unsigned versions `ULOAD`, `UAND`, `UOR`.

---

## 10. Increment / Decrement Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `INC` | `D` | 1 | D = D + 1 (16-bit signed) |
| `INCP` | `D` | 2 | D = D + 1, rising edge |
| `DINC` | `D` | 1 | D = D + 1 (32-bit) |
| `DINCP` | `D` | 2 | 32-bit INC, rising edge |
| `DEC` | `D` | 1 | D = D - 1 (16-bit signed) |
| `DECP` | `D` | 2 | D = D - 1, rising edge |
| `DDEC` | `D` | 1 | D = D - 1 (32-bit) |
| `DDECP` | `D` | 2 | 32-bit DEC, rising edge |
| `INCU` | `D` | 1 | D = D + 1 (16-bit unsigned) |
| `DECU` | `D` | 1 | D = D - 1 (16-bit unsigned) |

---

## 11. BIN Arithmetic Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `ADD` | `S1 S2 D` | 4 | D = S1 + S2 (16-bit signed) |
| `DADD` | `S1 S2 D` | 4 | D = S1 + S2 (32-bit signed) |
| `SUB` | `S1 S2 D` | 4 | D = S1 - S2 (16-bit signed) |
| `DSUB` | `S1 S2 D` | 4 | D = S1 - S2 (32-bit signed) |
| `MUL` | `S1 S2 D` | 4 | D+1,D = S1 × S2 (16-bit → 32-bit) |
| `DMUL` | `S1 S2 D` | 4 | D+3~D = S1 × S2 (32×32 → 64-bit) |
| `DIV` | `S1 S2 D` | 4 | D=quotient, D+1=remainder (16-bit) |
| `DDIV` | `S1 S2 D` | 4 | 32-bit division |
| `ADDU` | `S1 S2 D` | 4 | Unsigned ADD (16-bit) |
| `SUBU` | `S1 S2 D` | 4 | Unsigned SUB (16-bit) |
| `MULU` | `S1 S2 D` | 4 | Unsigned MUL |
| `DIVU` | `S1 S2 D` | 4 | Unsigned DIV |
| `RADD` | `S1 S2 D` | 4 | Short Real addition |
| `RSUB` | `S1 S2 D` | 4 | Short Real subtraction |
| `RMUL` | `S1 S2 D` | 4 | Short Real multiplication |
| `RDIV` | `S1 S2 D` | 4 | Short Real division |
| `LADD` | `S1 S2 D` | 4 | Long Real addition |
| `LSUB` | `S1 S2 D` | 4 | Long Real subtraction |
| `LMUL` | `S1 S2 D` | 4 | Long Real multiplication |
| `LDIV` | `S1 S2 D` | 4 | Long Real division |
| `$ADD` | `S1 S2 D` | 4 | String concatenation |
| `GADD` | `S1 S2 D N` | 4 | Group ADD (N words) |
| `GSUB` | `S1 S2 D N` | 4 | Group SUB (N words) |

> All have `P` variants for rising-edge execution.

---

## 12. BCD Arithmetic Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `ADDB` | `S1 S2 D` | 4 | BCD ADD (16-bit) |
| `DADDB` | `S1 S2 D` | 4 | BCD ADD (32-bit) |
| `SUBB` | `S1 S2 D` | 4 | BCD SUB (16-bit) |
| `DSUBB` | `S1 S2 D` | 4 | BCD SUB (32-bit) |
| `MULB` | `S1 S2 D` | 4 | BCD MUL |
| `DMULB` | `S1 S2 D` | 4 | BCD MUL (32-bit) |
| `DIVB` | `S1 S2 D` | 4 | BCD DIV |
| `DDIVB` | `S1 S2 D` | 4 | BCD DIV (32-bit) |

---

## 13. Logic Operation Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `WAND` | `S1 S2 D` | 4 | Bitwise AND (16-bit) |
| `DWAND` | `S1 S2 D` | 4 | Bitwise AND (32-bit) |
| `WOR` | `S1 S2 D` | 4 | Bitwise OR (16-bit) |
| `DWOR` | `S1 S2 D` | 4 | Bitwise OR (32-bit) |
| `WXOR` | `S1 S2 D` | 4 | Bitwise XOR (16-bit) |
| `DWXOR` | `S1 S2 D` | 4 | Bitwise XOR (32-bit) |
| `WXNR` | `S1 S2 D` | 4 | Bitwise XNOR (16-bit) |
| `DWXNR` | `S1 S2 D` | 4 | Bitwise XNOR (32-bit) |

---

## 14. Rotation Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `ROL` | `D n` | 2 | Rotate left n bits (16-bit, with carry) |
| `DROL` | `D n` | 2 | Rotate left (32-bit) |
| `ROR` | `D n` | 2 | Rotate right n bits (16-bit) |
| `DROR` | `D n` | 2 | Rotate right (32-bit) |
| `RCL` | `D n` | 2 | Rotate left through carry |
| `DRCL` | `D n` | 2 | Rotate left through carry (32-bit) |
| `RCR` | `D n` | 2 | Rotate right through carry |
| `DRCR` | `D n` | 2 | Rotate right through carry (32-bit) |

---

## 15. Move / Shift Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `BSFL` | `D n` | 2 | Bit shift left n bits (16-bit) |
| `DBSFL` | `D n` | 2 | Bit shift left (32-bit) |
| `BSFR` | `D n` | 2 | Bit shift right n bits |
| `DBSFR` | `D n` | 2 | Bit shift right (32-bit) |
| `WSFL` | `D1 D2 N` | 3 | Word shift left N words (D1~D2) |
| `WSFR` | `D1 D2 N` | 3 | Word shift right N words |
| `WSFT` | `St En` | 2 | Word shift (St to En, left) |
| `SR` | `Db I D N` | 2 | N-bit shift along direction I |
| `BRR` | `S D n1 n2` | 5 | Byte rotate right n2 times, n1 bytes |
| `BRL` | `S D n1 n2` | 5 | Byte rotate left n2 times, n1 bytes |

---

## 16. Exchange Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `XCHG` | `D1 D2` | 2 | Exchange D1 ↔ D2 (16-bit) |
| `DXCHG` | `D1 D2` | 2 | Exchange (32-bit) |
| `GXCHG` | `D1 D2 N` | 4 | Exchange N words |
| `SWAP` | `D` | 2 | Swap upper/lower byte of D |
| `GSWAP` | `D N` | 2 | Swap bytes of N words from D |
| `SWAP2` | `S D` | 2 | Swap bytes of S, save to D |

---

## 17. Branch / Program Flow Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `JMP` | `label` | 1 | Unconditional jump to label |
| `CALL` | `label` | 1 | Subroutine call |
| `RET` | — | 1 | Return from subroutine |
| `FOR` | `N` | 2 | Loop start (repeat N times) |
| `NEXT` | — | 1 | Loop end |
| `BREAK` | — | 1 | Exit FOR loop |

---

## 18. System / Flag Instructions
| Mnemonic | Operands | Steps | Description |
|----------|----------|-------|-------------|
| `WDT` | — | 1 | Watchdog timer reset |
| `STOP` | — | 1 | Stop PLC operation |
| `CLC` | — | 1 | Clear carry flag |
| `SEC` | — | 1 | Set carry flag |
| `EI` | — | 1 | Enable interrupt |
| `DI` | — | 1 | Disable interrupt |
| `IRET` | — | 1 | Return from interrupt |

---

## 19. IL (Mnemonic) Program Format

XGK IL is Ladder-equivalent mnemonic code. Each line = one instruction step.

### 19.1 General Structure
```
[Step No.]  INSTRUCTION  [Operand1]  [Operand2]  [Operand3]
```

### 19.2 Example: Simple Output
```
; Turn on M0000 when P0000 is ON and P0001 is OFF
0    LOAD    P0000
1    AND NOT P0001
2    OUT     M0000
3    END
```

### 19.3 Example: Timer
```
; TON: T000 turns on 5 seconds (500 × 10ms) after P0000 rises
0    LOAD    P0000
1    TON     T000  K500
3    LOAD    T000
4    OUT     M0010
5    END
```

### 19.4 Example: Counter
```
; Count 10 pulses of P0001, reset with P0002, output to M0020
0    LOAD    P0001
1    CTU     C000  K10
3    LOAD    P0002
4    RST     C000
5    LOAD    C000
6    OUT     M0020
7    END
```

### 19.5 Example: Arithmetic
```
; D0000 = D0010 + D0020 (16-bit, on rising edge of M0000)
0    LOADP   M0000
1    ADD     D0010  D0020  D0000
4    END
```

### 19.6 Example: Data Move with Comparison
```
; If D0100 > K100, copy D0100 to D0200
0    LOAD>   D0100  K100
1    MOVP    D0100  D0200
3    END
```

### 19.7 Example: FOR Loop
```
; Fill D0000~D0009 with K0
0    LOADP   M0001
1    FOR     K10
3    MOV     K0   D0000
5    NEXT
6    END
```

---

## 20. Special Relay (F) — Common Flags

| Address | Description |
|---------|-------------|
| `F0000` | Always ON (1-scan ON at RUN start) |
| `F0001` | Always OFF |
| `F0002` | 0.1s clock pulse |
| `F0003` | 0.2s clock pulse |
| `F0004` | 1s clock pulse |
| `F0005` | 2s clock pulse |
| `F0006` | 10s clock pulse |
| `F0010` | Carry flag (CY) |
| `F0011` | Zero flag (ZF) — set when result = 0 |
| `F0012` | Overflow flag |
| `F0013` | Sign flag (negative result) |
| `F0050` | WDT error flag |
| `F0060` | I/O error flag |

---

## 21. LLM Coding Guidelines

When generating XGK IL code, follow these rules:

1. **Always end program with `END`.**
2. **Use `LOADP`/`OUTP` for one-shot actions** (not `LOAD`/`OUT` which repeat every scan).
3. **Timer preset unit is 10ms by default.** K500 = 5 seconds.
4. **Counter reset must use `RST Cxxx`** before reuse.
5. **32-bit operations use consecutive registers:** `D0010` means words `D0010` and `D0011`.
6. **MUL result is double width:** `MUL D0 D1 D2` → result in `D3,D2` (32-bit).
7. **DIV result:** quotient in `D`, remainder in `D+1`.
8. **`SET`/`RST` are retentive** — they hold state across scans and power cycles (with battery).
9. **Index register Z0~Z7** can offset any device address: `D0000[Z0]`.
10. **Pulse suffix `P`** is preferred in production code for all data-write instructions to prevent unintended repeated writes.

---

*Generated from XGK/XGB Instructions & Programming Manual V2.9 (LS Electric, December 2020)*
