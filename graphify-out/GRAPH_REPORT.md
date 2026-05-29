# Graph Report - .  (2026-05-28)

## Corpus Check
- Corpus is ~17,468 words - fits in a single context window. You may not need a graph.

## Summary
- 47 nodes · 58 edges · 9 communities
- Extraction: 17% EXTRACTED · 83% INFERRED · 0% AMBIGUOUS · INFERRED: 48 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Injection Configuration & Control|Injection Configuration & Control]]
- [[_COMMUNITY_Safety & Alarm System|Safety & Alarm System]]
- [[_COMMUNITY_Module Architecture & Communication|Module Architecture & Communication]]
- [[_COMMUNITY_IL CSV Format Specification|IL CSV Format Specification]]
- [[_COMMUNITY_PLC Program Architecture|PLC Program Architecture]]
- [[_COMMUNITY_Project Overview|Project Overview]]
- [[_COMMUNITY_HMI Interface|HMI Interface]]
- [[_COMMUNITY_Project Reference & Tools|Project Reference & Tools]]
- [[_COMMUNITY_IL Instruction Rules|IL Instruction Rules]]

## God Nodes (most connected - your core abstractions)
1. `GX Works2 IL CSV Format Specification` - 11 edges
2. `PLC Program Structure Design` - 10 edges
3. `11-Module POU (Program Organization Unit) Structure` - 9 edges
4. `REFRIGER CHARGING MACHINE` - 5 edges
5. `Alarm Detection and Handling System` - 5 edges
6. `HMI Specification for Refriger Charging Machine` - 4 edges
7. `Injection Control Sequence (Type 0/1/2 branching)` - 4 edges
8. `REF Project Documentation` - 3 edges
9. `A3 Design Report — PLC Standard Program` - 3 edges
10. `Gun Type Classification (0=1-Sol, 1=Refrig H+L, 2=Oil+Refrig H+L)` - 3 edges

## Surprising Connections (you probably didn't know these)
- `A3 Design Report — PLC Standard Program` --semantically_similar_to--> `PLC Program Structure Design`  [INFERRED] [semantically similar]
  Notes/DESIGN_REPORT_A3.html → Notes/PLC_PROGRAM_STRUCTURE.md
- `Graphify Knowledge Graph Tool` --conceptually_related_to--> `REF Project Documentation`  [INFERRED]
  AGENTS.md → Notes/REF_DOCUMENT.md
- `CSV Module Responsibilities Map (idata, gmes, setting, gunvac, unitvac, vacchec, refinj, alarm, ad, 485, spc)` --semantically_similar_to--> `11-Module POU (Program Organization Unit) Structure`  [INFERRED] [semantically similar]
  Notes/DESIGN_REPORT_A3.html → Notes/PLC_PROGRAM_STRUCTURE.md
- `MC_26074 Reference Project` --conceptually_related_to--> `REFRIGER CHARGING MACHINE`  [INFERRED]
  Notes/REF_DOCUMENT.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `GX Works2 IL CSV Format Specification` --references--> `MAIN.csv Reference Export (3607 lines)`  [EXTRACTED]
  Notes/GX_WORKS2_IL_Spec.md → Notes/REF_DOCUMENT.md

## Hyperedges (group relationships)
- **Core Safety-and-Control Pattern (Step Sequence + Alarms + Interlocks)** — step_sequence_control, alarm_system, interlock_design [INFERRED 0.75]
- **IL CSV Format Specification Foundation (Quoting + Encoding + Row Types + Rung Rules)** — universal_quoting_model, utf16_le_encoding_rule, row_type_classification, rung_composition_rules [INFERRED 0.75]
- **POU Module → CSV → IL Format Implementation Chain** — pou_module_structure, gx_works2_il_csv_format, plc_program_structure [INFERRED 0.75]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Injection Configuration & Control"
Cohesion: 0.22
Nodes (9): System Configuration Parameters D228/D230/D232, Injection Volume Correction Logic (RefrigVol + Corr + HMI_Cal + Batch), Gun Global Index Formula (Line×GunPerLine+GunLocal), Gun Type Classification (0=1-Sol, 1=Refrig H+L, 2=Oil+Refrig H+L), Injection Control Sequence (Type 0/1/2 branching), Line Independence Design Principle, Pulse-to-Injection-Volume Conversion, Single Program for All Configurations (1L/1G ~ 2L/4G) (+1 more)

### Community 1 - "Safety & Alarm System"
Cohesion: 0.29
Nodes (8): Alarm Detection and Handling System, Emergency Stop Logic (M90 latch, ALL OUT OFF), Global Alarm Actions (EMG Stop, Safety PLC Fault → ALL OUT OFF, Latch), Interlock Design (per-Line safety conditions), Per-Line Alarm Instances (M110~M118 L0, M120~M128 L1), Refrigerant Bombe Low Alarm (D14~D15 ≥ D12~D13), Safety PLC Integration Interface, SPC Statistics Module (Cumulative Usage, Count, Pulse)

### Community 2 - "Module Architecture & Communication"
Cohesion: 0.33
Nodes (6): Analog Input Processing (AI Raw → EU Scaling), Barcode PC↔PLC Data Flow (Write Area → Working Area → Clear), CSV Module Responsibilities Map (idata, gmes, setting, gunvac, unitvac, vacchec, refinj, alarm, ad, 485, spc), PC Write → Working Copy → Cycle Complete → 0 Clear Handshake Protocol, 11-Module POU (Program Organization Unit) Structure, Vacuum Control Sequence (Gun Vac, Unit Vac, Vac Check/Leak Test)

### Community 3 - "IL CSV Format Specification"
Cohesion: 0.4
Nodes (6): Device/Operand Notation Rules (X/Y hex, M/D decimal, constants K/H/E), GX Works2 IL CSV Format Specification, MELSEC-Q/L Programming Manual (Common Instruction), Universal Quoting Model (3-layer escaping convention), UTF-16 LE Encoding with BOM Constraint, Wrapped-TSV Quoting Model (Outer wrapping + doubled inner quotes)

### Community 4 - "PLC Program Architecture"
Cohesion: 0.4
Nodes (5): D (Data Register) Device Map, M (Internal Relay) Device Map, Physical I/O Estimate (DI×32, DO×32, AI×6ch, HSC×2, RS-485), PLC Program Structure Design, System Signal Flow (HMI↔PLC↔Field I/O, PC↔PLC Barcode)

### Community 5 - "Project Overview"
Cohesion: 0.67
Nodes (4): A3 Design Report — PLC Standard Program, MC_26074 Reference Project, Mitsubishi Q03UDV PLC, REFRIGER CHARGING MACHINE

### Community 6 - "HMI Interface"
Cohesion: 0.67
Nodes (3): HMI Button → PLC M-Register Mapping (23 buttons), HMI Screen Navigation Flow (Operation→User Setting / Parameter / Alarm), HMI Specification for Refriger Charging Machine

### Community 7 - "Project Reference & Tools"
Cohesion: 0.67
Nodes (3): Graphify Knowledge Graph Tool, MAIN.csv Reference Export (3607 lines), REF Project Documentation

### Community 8 - "IL Instruction Rules"
Cohesion: 0.67
Nodes (3): IL Instruction Mnemonics Catalog (46 distinct, Sequence + Basic), Row Type Classification (Type A=Label, B=Instruction, C=Continuation), Ladder Rung Composition Rules (LD→AND/OR→OUT, MPS/MPP pairing)

## Knowledge Gaps
- **16 isolated node(s):** `MELSEC-Q/L Programming Manual (Common Instruction)`, `MC_26074 Reference Project`, `M (Internal Relay) Device Map`, `D (Data Register) Device Map`, `Analog Input Processing (AI Raw → EU Scaling)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PLC Program Structure Design` connect `PLC Program Architecture` to `Injection Configuration & Control`, `Module Architecture & Communication`, `IL CSV Format Specification`, `Project Overview`, `HMI Interface`?**
  _High betweenness centrality (0.689) - this node is a cross-community bridge._
- **Why does `11-Module POU (Program Organization Unit) Structure` connect `Module Architecture & Communication` to `Injection Configuration & Control`, `Safety & Alarm System`, `PLC Program Architecture`?**
  _High betweenness centrality (0.611) - this node is a cross-community bridge._
- **Why does `GX Works2 IL CSV Format Specification` connect `IL CSV Format Specification` to `IL Instruction Rules`, `PLC Program Architecture`, `Project Reference & Tools`?**
  _High betweenness centrality (0.419) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `GX Works2 IL CSV Format Specification` (e.g. with `Wrapped-TSV Quoting Model (Outer wrapping + doubled inner quotes)` and `Universal Quoting Model (3-layer escaping convention)`) actually correct?**
  _`GX Works2 IL CSV Format Specification` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `PLC Program Structure Design` (e.g. with `11-Module POU (Program Organization Unit) Structure` and `Step Sequence Control (IDLE→PRECHECK→GUN VAC→UNIT VAC→VAC CHECK→INJECTION→GAS EXHAUST→COMPLETE)`) actually correct?**
  _`PLC Program Structure Design` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `11-Module POU (Program Organization Unit) Structure` (e.g. with `PLC Program Structure Design` and `Alarm Detection and Handling System`) actually correct?**
  _`11-Module POU (Program Organization Unit) Structure` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `REFRIGER CHARGING MACHINE` (e.g. with `A3 Design Report — PLC Standard Program` and `MC_26074 Reference Project`) actually correct?**
  _`REFRIGER CHARGING MACHINE` has 2 INFERRED edges - model-reasoned connections that need verification._