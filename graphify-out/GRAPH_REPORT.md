# Graph Report - F:/WorkSpace/REF  (2026-06-01)

## Corpus Check
- 0 files · ~30,754 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 507 nodes · 707 edges · 28 communities (21 shown, 7 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 146 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Machine Button IO|Machine Button I/O]]
- [[_COMMUNITY_Serial Comm & Alarms|Serial Comm & Alarms]]
- [[_COMMUNITY_Program Steps N01-N22|Program Steps N01-N22]]
- [[_COMMUNITY_Register Configuration|Register Configuration]]
- [[_COMMUNITY_HMI Step Control|HMI Step Control]]
- [[_COMMUNITY_Program Steps N02-N09|Program Steps N02-N09]]
- [[_COMMUNITY_System Architecture|System Architecture]]
- [[_COMMUNITY_CSV Data Structure|CSV Data Structure]]
- [[_COMMUNITY_IO Mapping & Control|I/O Mapping & Control]]
- [[_COMMUNITY_Sensor & Alarm Design|Sensor & Alarm Design]]
- [[_COMMUNITY_Instruction Patterns|Instruction Patterns]]
- [[_COMMUNITY_Documentation Reference|Documentation Reference]]
- [[_COMMUNITY_BOM & Format Rules|BOM & Format Rules]]
- [[_COMMUNITY_HMI Screen Layout|HMI Screen Layout]]
- [[_COMMUNITY_Manual Notation Guide|Manual Notation Guide]]
- [[_COMMUNITY_Algorithm Rules|Algorithm Rules]]
- [[_COMMUNITY_Row Format Rules|Row Format Rules]]
- [[_COMMUNITY_Record Field Format|Record Field Format]]
- [[_COMMUNITY_Register Definitions|Register Definitions]]
- [[_COMMUNITY_Mapping Format|Mapping Format]]
- [[_COMMUNITY_Instruction Manual|Instruction Manual]]
- [[_COMMUNITY_Project Communication|Project Communication]]
- [[_COMMUNITY_Plugin Dependencies|Plugin Dependencies]]
- [[_COMMUNITY_Flow Structure|Flow Structure]]
- [[_COMMUNITY_Condition Statistics|Condition Statistics]]
- [[_COMMUNITY_Project Plugin|Project Plugin]]
- [[_COMMUNITY_Project Config|Project Config]]
- [[_COMMUNITY_Timer Logic|Timer Logic]]

## God Nodes (most connected - your core abstractions)
1. `REFRIGER CHARGING MACHINE` - 45 edges
2. `2LINE2GUN_OIL Operation Screen (Unit 2)` - 33 edges
3. `Line 2 (라인2)` - 22 edges
4. `gmes.csv — Main Sequence Controller` - 21 edges
5. `REFRIGER_CHARGING_MACHINE.md HMI Specification` - 20 edges
6. `Line 1` - 19 edges
7. `Line 2` - 19 edges
8. `운전 화면 (Operation Screen)` - 17 edges
9. `Line 1 (라인1)` - 17 edges
10. `GX-Works2 Instruction List (IL) CSV Export — Strict Format Specification` - 15 edges

## Surprising Connections (you probably didn't know these)
- `REFRIGER CHARGING MACHINE` --semantically_similar_to--> `REFRIGER_CHARGING_MACHINE.md HMI Specification`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/PLC_PROGRAM_STRUCTURE.md
- `방폭 Explosion-Proof Type` --semantically_similar_to--> `§7 Explosion-Proof Configuration`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `비방폭 Non-Explosion-Proof Type` --semantically_similar_to--> `Non-Explosion-Proof Configuration (비방폭)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Limit Sensor (좌/우, 방폭 전용)` --semantically_similar_to--> `Door Limit Sensor Subsystem (방폭 전용)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Open Alarm` --semantically_similar_to--> `Door Open Alarm (M-relay Latch)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md

## Communities (28 total, 7 thin omitted)

### Community 0 - "Machine Button I/O"
Cohesion: 0.05
Nodes (74): REFRIGER CHARGING MACHINE - 2LINE4GUN Configuration, 알람 화면 (Alarm Screen) Button, 부저 정지 (Buzzer Stop) Button, 주입건 A (Injection Gun A), 주입건 C (Injection Gun C), 주입건 D (Injection Gun D), 주입량 설정화면 (Injection Amount Setting Screen) Button, 인터락 미사용 (Interlock Not Used) Button (+66 more)

### Community 1 - "Serial Comm & Alarms"
Cohesion: 0.06
Nodes (63): 485.csv — RS-485 Sensor Communication, RS-485 Sensor Polling (Modbus RTU, CRC Validation), Shared EU Output Space (D152/D156/D160/D164/D168/D172), ad.csv — Analog I/O Scaling, Analog Scaling (Raw 0~4000 → EU, 1st Order Filter), alarm.csv — Alarm Management, Alarm Latch System (L40~L4E — 15 Alarm Types), Buzzer and Lamp Control (M4C/M4D/M4E/M4F → Y30~Y33) (+55 more)

### Community 2 - "Program Steps N01-N22"
Cohesion: 0.05
Nodes (57): REFRIGER CHARGING MACHINE, Explosion-Proof Enclosure Type, Non-Explosion-Proof Enclosure Type, Left Door Limit Sensor, Right Door Limit Sensor, DOOR OPEN Alarm, Door Alarm Non-Latching Behavior, No Emergency Stop on Door Open (+49 more)

### Community 3 - "Register Configuration"
Cohesion: 0.04
Nodes (47): 0-1. 지원 구성, 0-1. 지원 구성 (Variations), 0-2. 구성 파라미터 (PLC D-Register), 0-3. Line / Gun 개념, 0-4. Gun Type, 0-5. Gun Index 공식, 0. 시스템 구성 (System Configuration), 1-1. HMI Button → PLC 내부 릴레이 (M, 푸시=ON) (+39 more)

### Community 4 - "HMI Step Control"
Cohesion: 0.06
Nodes (44): 2LINE2GUN_OIL Operation Screen (Unit 2), 자동스탭 (Auto Step), 차징시간 (Charging Time), 컨베어 인터록 사용 (Conveyor Interlock Use), R32건 (R32 Gun), R410A건 (R410A Gun), 건 선택 (Gun Selection), 모델 선택 (Model Selection) (+36 more)

### Community 5 - "Program Steps N02-N09"
Cohesion: 0.09
Nodes (34): LS IXP2-1200 HMI, Mitsubishi PLC, Operation Screen, Parameter Setting Screen, User Setting Screen, Alarm Screen, Screen Navigation Flow, Momentary Button Rule (+26 more)

### Community 6 - "System Architecture"
Cohesion: 0.08
Nodes (28): Alarm Detection and Handling System, Analog Input Processing (AI Raw → EU Scaling), Barcode PC↔PLC Data Flow (Write Area → Working Area → Clear), System Configuration Registers (D330-D339), D (Data Register) Device Map (Even-Address Rule), Line Independence Principle, Per-Line Parameter Register Layout (D0-D29 L0, D30-D59 L1), Line/Gun System Configuration (Supports 1L/1G ~ 2L/4G) (+20 more)

### Community 7 - "CSV Data Structure"
Cohesion: 0.10
Nodes (20): Additional Device Types (not in MAIN.csv), code:block1 (REF/), code:block2 (FF FE  4D 00 43 00 5F 00 …      ← BOM, then "MC_..." in UTF-), Development Rules, Device Prefix Frequency (MAIN.csv), Directory Structure, External Reference, File Format (GX Works2 IL CSV) (+12 more)

### Community 8 - "I/O Mapping & Control"
Cohesion: 0.12
Nodes (18): X (Digital Input) Device Map, Y (Digital Output) Device Map, Error/Alarm Handling System, Gun Coupler Sensor Interlock, HMI Button → PLC Internal Relay Mapping, Interlock System (per Line), Main Sequence Step Control (per Line), Main Sequence Flow Diagram (A3 Visual) (+10 more)

### Community 9 - "Sensor & Alarm Design"
Cohesion: 0.21
Nodes (14): Alarm-Only Design — No Interlock, No Emergency Stop, Door Limit Sensor (좌/우, 방폭 전용), Door Open Alarm, 방폭 Explosion-Proof Type, 비방폭 Non-Explosion-Proof Type, REFRIGER CHARGING MACHINE, Design Choice: Alarm Without Emergency Stop or Interlock, Door Limit Sensor Subsystem (방폭 전용) (+6 more)

### Community 10 - "Instruction Patterns"
Cohesion: 0.15
Nodes (13): 11-1. Rung boundary identification, 11-2. Rung internal structure (canonical order), 11-3. Rung composition patterns, 11-4. Rung-boundary decision table, 11-5. Constraints summary, 11. Rung Composition Rules, code:block12 ([1] Load                  — LD / LDI / LDP / LDF            ), code:block13 (LD   M1000) (+5 more)

### Community 11 - "Documentation Reference"
Cohesion: 0.23
Nodes (12): Device/Operand Notation Rules (X/Y hex, M/D decimal, constants K/H/E), Graphify Knowledge Graph Tool, GX Works2 IL CSV Format Specification, IL Instruction Mnemonics Catalog (46 distinct, Sequence + Basic), MAIN.csv Reference Export (3607 lines), MELSEC-Q/L Programming Manual (Common Instruction), REF Project Documentation, Row Type Classification (Type A=Label, B=Instruction, C=Continuation) (+4 more)

### Community 12 - "BOM & Format Rules"
Cohesion: 0.17
Nodes (11): 10. Field Content Constraints, 12. Checklist for Generating or Modifying This Format, 13. Parsing Notes (LLM-Specific), 1. File Encoding and BOM, 2. Overall File Structure (order is fixed, NO blank rows), 8. Step No. Rules, 9. END Instruction, code:block1 ([Row 1]   Program name (title)        ← see §3-1) (+3 more)

### Community 13 - "HMI Screen Layout"
Cohesion: 0.20
Nodes (11): 1-Line 1-Gun Machine Configuration, Operation Screen - 1 Line 1 Gun Variant, HMI Bottom Action Bar (Manual Mode, Gun Exhaust, Product Exhaust, Vacuum Check, Refriger Injection, Start, Stop), Injection Parameters Display Group (Model, Set Amount, Charging Pulse, Vacuum Pump, Actual Amount, Injection Time), Navigation Buttons (Injection Amount Setting, Operation Setting, Alarm Screen), Production Quantity Counter with Reset, Real-Time Sensor Readouts Group (Vacuum Torr, Scan Info, Pressure kgf/cm², Temperature ℃), HMI Top Control Bar (Unit Pass, Interlock, Alarm Reset, Buzzer Stop, Navigation) (+3 more)

### Community 14 - "Manual Notation Guide"
Cohesion: 0.22
Nodes (9): 6-1. Sequence Instructions (confirmed in MAIN.csv + MELSEC manual), 6-3. Notation Rules, 6. Instruction Mnemonics, 7-1. Observed device prefixes, 7. Device / Operand Notation, Association Instructions, Contact Instructions (Load / AND / OR), Output Instructions (+1 more)

### Community 15 - "Algorithm Rules"
Cohesion: 0.25
Nodes (8): 4-1. Rule, 4-2. Worked example — Type B row `LD M1000` at step 0, 4-3. Parsing algorithm (recommended), 4-4. Generating (encoding) algorithm, 4. Universal Quoting Model (the most error-prone part), code:block4 ("0<TAB>""""<TAB>""LD""<TAB>""M1000""<TAB>""""<TAB>""""<TAB>"), code:python (def decode_record(raw: str) -> list[str]:), code:python (def encode_record(fields: list[str]) -> str:)

### Community 16 - "Row Format Rules"
Cohesion: 0.25
Nodes (8): 5-1. Type A — Label / Line Statement row, 5-2. Type B — Instruction row (head of an instruction, with step number), 5-3. Type C — Continuation row (extra operands of the preceding instruction), 5. Three Types of Data Rows, code:block10 (Row B: [17, "", "LD=",  "K1", "", "", ""]), code:block7 ([90,   "<<<<< Q64RD Card Converting Setup Program >>>>>>>", ), code:block8 ([0,    "", "LD",   "M1000", "", "", ""]), code:block9 (Row B: [1,  "", "MOVP", "K0", "", "", ""])

### Community 17 - "Record Field Format"
Cohesion: 0.33
Nodes (6): 3-1. Row 1 — Program Name (title) record, 3-2. Row 2 — PLC Information record, 3-3. Row 3 — Column header record (exactly 7 fields), 3. Detailed Rules for Each Row, code:block2 ("PLC Information:<TAB>""QCPU (Q mode) Q03UDV"""), code:block3 ("Step No.<TAB>""Line Statement""<TAB>""Instruction""<TAB>""I)

### Community 18 - "Register Definitions"
Cohesion: 0.50
Nodes (5): FAST+NORMAL Simultaneous Open Injection, Gun Global Index Formula, Gun Selection-Based Injection Sequence Branching, Gun Type Definitions (Type 0-3), Gun Type per Gun Registers (D62/D76/D90/D104)

### Community 19 - "Mapping Format"
Cohesion: 0.50
Nodes (4): 14. Official Manual Reference & List Mode Format, code:block20 ([List Mode]), Extended Instruction Set, List Mode (IL) Column Mapping

### Community 20 - "Instruction Manual"
Cohesion: 0.50
Nodes (4): 6-2. Basic Instructions (confirmed in MAIN.csv + MELSEC manual), Comparison Instructions, Program Control Instructions, Transfer / Arithmetic / Conversion Instructions

## Ambiguous Edges - Review These
- `Line 1 (라인1)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override
- `Line 2 (라인2)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override

## Knowledge Gaps
- **197 isolated node(s):** `graphify`, `1. File Encoding and BOM`, `code:block1 ([Row 1]   Program name (title)        ← see §3-1)`, `3-1. Row 1 — Program Name (title) record`, `code:block2 ("PLC Information:<TAB>""QCPU (Q mode) Q03UDV""")` (+192 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Line 1 (라인1)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **What is the exact relationship between `Line 2 (라인2)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **Why does `PLC Program Structure Design` connect `Program Steps N01-N22` to `I/O Mapping & Control`, `Documentation Reference`, `Program Steps N02-N09`, `System Architecture`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `REFRIGER CHARGING MACHINE` connect `Program Steps N01-N22` to `Program Steps N02-N09`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `REFRIGER_CHARGING_MACHINE.md HMI Specification` connect `Program Steps N02-N09` to `Sensor & Alarm Design`, `Program Steps N01-N22`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `REFRIGER CHARGING MACHINE` (e.g. with `A3 Design Report — PLC Standard Program` and `MC_26074 Reference Project`) actually correct?**
  _`REFRIGER CHARGING MACHINE` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `1. File Encoding and BOM`, `code:block1 ([Row 1]   Program name (title)        ← see §3-1)` to the rest of the system?**
  _204 weakly-connected nodes found - possible documentation gaps or missing edges._