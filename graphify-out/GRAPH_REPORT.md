# Graph Report - REF  (2026-06-02)

## Corpus Check
- 20 files · ~32,333 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 822 nodes · 1017 edges · 44 communities (38 shown, 6 thin omitted)
- Extraction: 85% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 146 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9bb13e19`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]

## God Nodes (most connected - your core abstractions)
1. `REFRIGER CHARGING MACHINE` - 45 edges
2. `2LINE2GUN_OIL Operation Screen (Unit 2)` - 33 edges
3. `Line 2 (라인2)` - 22 edges
4. `gmes.csv — Main Sequence Controller` - 21 edges
5. `REFRIGER_CHARGING_MACHINE.md HMI Specification` - 20 edges
6. `Line 1` - 19 edges
7. `Line 2` - 19 edges
8. `3. D Device — Data Register` - 17 edges
9. `운전 화면 (Operation Screen)` - 17 edges
10. `Line 1 (라인1)` - 17 edges

## Surprising Connections (you probably didn't know these)
- `REFRIGER_CHARGING_MACHINE.md HMI Specification` --semantically_similar_to--> `REFRIGER CHARGING MACHINE`  [INFERRED] [semantically similar]
  Notes/PLC_PROGRAM_STRUCTURE.md → .opencode/memory/project.md
- `방폭 Explosion-Proof Type` --semantically_similar_to--> `§7 Explosion-Proof Configuration`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `비방폭 Non-Explosion-Proof Type` --semantically_similar_to--> `Non-Explosion-Proof Configuration (비방폭)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Limit Sensor (좌/우, 방폭 전용)` --semantically_similar_to--> `Door Limit Sensor Subsystem (방폭 전용)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Open Alarm` --semantically_similar_to--> `Door Open Alarm (M-relay Latch)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md

## Communities (44 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (74): REFRIGER CHARGING MACHINE - 2LINE4GUN Configuration, 알람 화면 (Alarm Screen) Button, 부저 정지 (Buzzer Stop) Button, 주입건 A (Injection Gun A), 주입건 C (Injection Gun C), 주입건 D (Injection Gun D), 주입량 설정화면 (Injection Amount Setting Screen) Button, 인터락 미사용 (Interlock Not Used) Button (+66 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (63): 485.csv — RS-485 Sensor Communication, RS-485 Sensor Polling (Modbus RTU, CRC Validation), Shared EU Output Space (D152/D156/D160/D164/D168/D172), ad.csv — Analog I/O Scaling, Analog Scaling (Raw 0~4000 → EU, 1st Order Filter), alarm.csv — Alarm Management, Alarm Latch System (L40~L4E — 15 Alarm Types), Buzzer and Lamp Control (M4C/M4D/M4E/M4F → Y30~Y33) (+55 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (57): REFRIGER CHARGING MACHINE, Explosion-Proof Enclosure Type, Non-Explosion-Proof Enclosure Type, Left Door Limit Sensor, Right Door Limit Sensor, DOOR OPEN Alarm, Door Alarm Non-Latching Behavior, No Emergency Stop on Door Open (+49 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (40): 0-1. 지원 구성, 0-1. 지원 구성 (Variations), 0-2. 구성 파라미터 (PLC D-Register), 0-3. Line / Gun 개념, 0-4. Gun Type, 0-5. Gun Index 공식, 0. 시스템 구성 (System Configuration), 10-2. 봄베 알람 (+32 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (44): 2LINE2GUN_OIL Operation Screen (Unit 2), 자동스탭 (Auto Step), 차징시간 (Charging Time), 컨베어 인터록 사용 (Conveyor Interlock Use), R32건 (R32 Gun), R410A건 (R410A Gun), 건 선택 (Gun Selection), 모델 선택 (Model Selection) (+36 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (49): LS IXP2-1200 HMI, Mitsubishi PLC, Operation Screen, Parameter Setting Screen, User Setting Screen, Alarm Screen, Screen Navigation Flow, Momentary Button Rule (+41 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (28): Alarm Detection and Handling System, Analog Input Processing (AI Raw → EU Scaling), Barcode PC↔PLC Data Flow (Write Area → Working Area → Clear), System Configuration Registers (D330-D339), D (Data Register) Device Map (Even-Address Rule), Line Independence Principle, Per-Line Parameter Register Layout (D0-D29 L0, D30-D59 L1), Line/Gun System Configuration (Supports 1L/1G ~ 2L/4G) (+20 more)

### Community 7 - "Community 7"
Cohesion: 0.10
Nodes (20): Additional Device Types (not in MAIN.csv), code:block1 (REF/), code:block2 (FF FE  4D 00 43 00 5F 00 …      ← BOM, then "MC_..." in UTF-), Development Rules, Device Prefix Frequency (MAIN.csv), Directory Structure, External Reference, File Format (GX Works2 IL CSV) (+12 more)

### Community 8 - "Community 8"
Cohesion: 0.12
Nodes (18): X (Digital Input) Device Map, Y (Digital Output) Device Map, Error/Alarm Handling System, Gun Coupler Sensor Interlock, HMI Button → PLC Internal Relay Mapping, Interlock System (per Line), Main Sequence Step Control (per Line), Main Sequence Flow Diagram (A3 Visual) (+10 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (39): 1. L Device — Latch Bit (정전 유지), 2-1. System Flags (M0~M9), 2-2. Step State — Line 0 (M10~M19), 2-3. Step State — Line 1 (M20~M29), 2-4. Solenoid Coil Images (M30~M6F), 2-5. Physical Input Mirrors (M300~M31F), 2-6. HMI Button Buffer (M400~M41F), 2-7. Communication Flags (M500~M50F) (+31 more)

### Community 10 - "Community 10"
Cohesion: 0.29
Nodes (7): 11-1. Rung boundary identification, 11-2. Rung internal structure (canonical order), 11-4. Rung-boundary decision table, 11-5. Constraints summary, 11. Rung Composition Rules, code:block12 ([1] Load                  — LD / LDI / LDP / LDF            ), code:block18 (- Every rung starts with exactly one load instruction (LD / )

### Community 11 - "Community 11"
Cohesion: 0.23
Nodes (12): Device/Operand Notation Rules (X/Y hex, M/D decimal, constants K/H/E), Graphify Knowledge Graph Tool, GX Works2 IL CSV Format Specification, IL Instruction Mnemonics Catalog (46 distinct, Sequence + Basic), MAIN.csv Reference Export (3607 lines), MELSEC-Q/L Programming Manual (Common Instruction), REF Project Documentation, Row Type Classification (Type A=Label, B=Instruction, C=Continuation) (+4 more)

### Community 12 - "Community 12"
Cohesion: 0.17
Nodes (11): 10. Field Content Constraints, 12. Checklist for Generating or Modifying This Format, 13. Parsing Notes (LLM-Specific), 1. File Encoding and BOM, 2. Overall File Structure (order is fixed, NO blank rows), 8. Step No. Rules, 9. END Instruction, code:block1 ([Row 1]   Program name (title)        ← see §3-1) (+3 more)

### Community 13 - "Community 13"
Cohesion: 0.20
Nodes (11): 1-Line 1-Gun Machine Configuration, Operation Screen - 1 Line 1 Gun Variant, HMI Bottom Action Bar (Manual Mode, Gun Exhaust, Product Exhaust, Vacuum Check, Refriger Injection, Start, Stop), Injection Parameters Display Group (Model, Set Amount, Charging Pulse, Vacuum Pump, Actual Amount, Injection Time), Navigation Buttons (Injection Amount Setting, Operation Setting, Alarm Screen), Production Quantity Counter with Reset, Real-Time Sensor Readouts Group (Vacuum Torr, Scan Info, Pressure kgf/cm², Temperature ℃), HMI Top Control Bar (Unit Pass, Interlock, Alarm Reset, Buzzer Stop, Navigation) (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.25
Nodes (8): 4-1. Rule, 4-2. Worked example — Type B row `LD M1000` at step 0, 4-3. Parsing algorithm (recommended), 4-4. Generating (encoding) algorithm, 4. Universal Quoting Model (the most error-prone part), code:block4 ("0<TAB>""""<TAB>""LD""<TAB>""M1000""<TAB>""""<TAB>""""<TAB>"), code:python (def decode_record(raw: str) -> list[str]:), code:python (def encode_record(fields: list[str]) -> str:)

### Community 15 - "Community 15"
Cohesion: 0.18
Nodes (11): 6-1. Sequence Instructions (confirmed in MAIN.csv + MELSEC manual), 6-2. Basic Instructions (confirmed in MAIN.csv + MELSEC manual), 6-3. Notation Rules, 6. Instruction Mnemonics, Association Instructions, Comparison Instructions, Contact Instructions (Load / AND / OR), Output Instructions (+3 more)

### Community 16 - "Community 16"
Cohesion: 0.25
Nodes (8): 5-1. Type A — Label / Line Statement row, 5-2. Type B — Instruction row (head of an instruction, with step number), 5-3. Type C — Continuation row (extra operands of the preceding instruction), 5. Three Types of Data Rows, code:block10 (Row B: [17, "", "LD=",  "K1", "", "", ""]), code:block7 ([90,   "<<<<< Q64RD Card Converting Setup Program >>>>>>>", ), code:block8 ([0,    "", "LD",   "M1000", "", "", ""]), code:block9 (Row B: [1,  "", "MOVP", "K0", "", "", ""])

### Community 17 - "Community 17"
Cohesion: 0.33
Nodes (6): 3-1. Row 1 — Program Name (title) record, 3-2. Row 2 — PLC Information record, 3-3. Row 3 — Column header record (exactly 7 fields), 3. Detailed Rules for Each Row, code:block2 ("PLC Information:<TAB>""QCPU (Q mode) Q03UDV"""), code:block3 ("Step No.<TAB>""Line Statement""<TAB>""Instruction""<TAB>""I)

### Community 18 - "Community 18"
Cohesion: 0.50
Nodes (5): FAST+NORMAL Simultaneous Open Injection, Gun Global Index Formula, Gun Selection-Based Injection Sequence Branching, Gun Type Definitions (Type 0-3), Gun Type per Gun Registers (D62/D76/D90/D104)

### Community 19 - "Community 19"
Cohesion: 0.05
Nodes (36): 1. Purpose, 2. Inputs, 3. Outputs, 4-1. Manual / Auto Toggle (M40E), 4-2. Line Select (M400 / M401), 4-3. Gun Select (M408 / M409), 4-4. PC Barcode Data 수신, 4. Mode Management (+28 more)

### Community 20 - "Community 20"
Cohesion: 0.50
Nodes (4): 14. Official Manual Reference & List Mode Format, code:block20 ([List Mode]), Extended Instruction Set, List Mode (IL) Column Mapping

### Community 21 - "Community 21"
Cohesion: 0.40
Nodes (4): Communication, graphify, Project Conventions, Work Mode

### Community 28 - "Community 28"
Cohesion: 0.07
Nodes (26): Alarm Page Navigation by D Register, Alarm Per-Line Separation Plan, ALARM RESET (per-line), Bombe — configurable (depends on D330), Buzzer (M4C → Y30) — single, shared, code:block1 (L40 OR L41 OR L42 OR L43 OR L44 OR L45 OR L46 OR L47), Current (direct execute), Current Problem (+18 more)

### Community 29 - "Community 29"
Cohesion: 0.08
Nodes (23): 10. IL Mnemonics, 1. Purpose, 2. Inputs, 3. Outputs, 4-1. Type 0 (1-Sol Base) + D276=0 (REF Only), 4-2. Type 0 (1-Sol Base) + D276=1 (REF+OIL), 4-3. Type 1 (H+L Fast+Normal) + D276=0 (REF Only), 4-4. Type 1 (H+L) + D276=1 (REF+OIL) (+15 more)

### Community 30 - "Community 30"
Cohesion: 0.09
Nodes (23): 3-1. M (Internal Relay) — Bit Device (0~), 3-1. 핵심 할당 원칙, 3-2. D (Data Register) — Word Device (짝수 주소), 3-2. L Device 요약 (정전유지 Bit), 3-3. M Device 요약 (Volatile Bit), 3-3. T (Timer) — 100ms 설정, 3-4. D Device 요약 (Data Register), 3-4. X (Digital Input) — Hex Address (+15 more)

### Community 31 - "Community 31"
Cohesion: 0.09
Nodes (21): 1-1. Gun Type (솔레노이드 구조), 1-2. Oil Mode (주입 모드), 1-3. 방폭 Type (Enclosure), 1-4. 냉매 Type, 1-5. HMI Screen Type, 1-6. Reset Type, 1-7. 공정 Step Type (시퀀스), 1. 장비 Type 일람 (+13 more)

### Community 32 - "Community 32"
Cohesion: 0.11
Nodes (18): 1. Purpose, 2. Inputs, 3. Outputs, 4-1. CH0 Scaling (예: Pressure), 4-2. CH1 Scaling (예: Temperature), 4-3. CH2 Scaling (예: Vacuum), 4-4. Display Mirror, 4. Scaling Logic (+10 more)

### Community 33 - "Community 33"
Cohesion: 0.11
Nodes (17): 1. Purpose, 2. Inputs, 3. Outputs, 4-1. System Configuration (D270~D276), 4-2. Parameter Settings — Line 0 (D0~D29), 4-3. Parameter Settings — Line 1 (D30~D59), 4. Parameters 관리, 5. User Settings — Gun별 (D60~D115) (+9 more)

### Community 34 - "Community 34"
Cohesion: 0.12
Nodes (16): 10. IL Mnemonics, 1. Purpose, 2. Inputs, 3. Outputs, 4. Alarm Detection & Latch Logic, 5. Buzzer Control, 6. Lamp Control, 7. Alarm Reset Logic (+8 more)

### Community 35 - "Community 35"
Cohesion: 0.12
Nodes (16): 1. Purpose, 2. Inputs, 3. Outputs, 4. Initialization Logic (First Scan Only), 5-1. X → M Mapping (Input Scan), 5-2. M → Y Mapping (Output Scan), 5-3. System Flags, 5. Main Scan Logic (Always ON, SM400) (+8 more)

### Community 36 - "Community 36"
Cohesion: 0.13
Nodes (14): 1. Purpose, 2. Inputs, 3. Outputs, 4-1. L0 Total Usage Accumulation, 4-2. L1 Total Usage Accumulation, 4-3. Display Mirror, 4-4. Bombe Alarm Check, 4. Logic (+6 more)

### Community 37 - "Community 37"
Cohesion: 0.15
Nodes (12): 1. Purpose, 2. 대상 센서, 3. Inputs, 4. Outputs, 5. Data Flow, 6. Communication Protocol, 7. 센서 Type 선택 아키텍처 (미래 확장), 8. Error Conditions (+4 more)

### Community 38 - "Community 38"
Cohesion: 0.15
Nodes (12): 1. input.csv — Physical Input Mapping, 2. output.csv — Physical Output Mapping, 3. HMI Button Mapping (M → HMI), 4. Analog Input Mapping (AI → D), 5. 변경 시 영향 범위, code:block1 (// input.csv 에 정의된 대로 매 scanning 마다 X → M 복사), code:block2 (// output.csv 에 정의된 대로 매 scanning 마다 M → Y 복사), Coding Pattern (Ladder) (+4 more)

### Community 39 - "Community 39"
Cohesion: 0.17
Nodes (11): 1. Purpose, 2. Inputs, 3. Outputs, 4. Sequence Logic (Line 0 기준), 5. ΔP (차압) 계산, 6. Step Transition, 7. Error Conditions, 8. IL Mnemonics (+3 more)

### Community 40 - "Community 40"
Cohesion: 0.20
Nodes (9): 1. Purpose, 2. Inputs, 3. Outputs, 4. Sequence Logic (Line 0 기준, Line 1은 +10 offset), 5. Step Transition, 6. Error Conditions, 7. IL Mnemonics, code:block1 (M12 (Step Entry) ─── Rising Edge) (+1 more)

### Community 41 - "Community 41"
Cohesion: 0.20
Nodes (9): 1. Purpose, 2. Inputs, 3. Outputs, 4. Sequence Logic (Line 0 기준), 5. Step Transition, 6. Error Conditions, 7. IL Mnemonics, code:block1 (M13 (Step Entry) ─── Rising Edge) (+1 more)

### Community 42 - "Community 42"
Cohesion: 0.33
Nodes (6): 11-3. Rung composition patterns, code:block13 (LD   M1000), code:block14 (LD=  K1  D4          ← (Type B: LD= K1  +  Type C: D4)), code:block15 (LD   L31), code:block16 (LD   <cond>), code:block17 (LD   SM400)

### Community 43 - "Community 43"
Cohesion: 0.67
Nodes (3): 7-1. Observed device prefixes, 7-2. Notation rules, 7. Device / Operand Notation

## Ambiguous Edges - Review These
- `Line 1 (라인1)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override
- `Line 2 (라인2)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override

## Knowledge Gaps
- **389 isolated node(s):** `Work Mode`, `Project Conventions`, `graphify`, `Terminology`, `Current Problem` (+384 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Line 1 (라인1)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **What is the exact relationship between `Line 2 (라인2)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **Why does `PLC Program Structure Design` connect `Community 2` to `Community 8`, `Community 11`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `REFRIGER CHARGING MACHINE` connect `Community 2` to `Community 5`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `REFRIGER_CHARGING_MACHINE.md HMI Specification` connect `Community 5` to `Community 2`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `REFRIGER CHARGING MACHINE` (e.g. with `A3 Design Report — PLC Standard Program` and `MC_26074 Reference Project`) actually correct?**
  _`REFRIGER CHARGING MACHINE` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Work Mode`, `Project Conventions`, `graphify` to the rest of the system?**
  _396 weakly-connected nodes found - possible documentation gaps or missing edges._