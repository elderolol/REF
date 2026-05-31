# Graph Report - .  (2026-05-31)

## Corpus Check
- 16 files · ~56,119 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 515 nodes · 618 edges · 29 communities (22 shown, 7 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 146 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

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

## God Nodes (most connected - your core abstractions)
1. `REFRIGER_CHARGING_MACHINE_1LINE2GUN` - 34 edges
2. `2LINE2GUN_OIL Operation Screen (Unit 2)` - 33 edges
3. `Line 2 (라인2)` - 22 edges
4. `5-4. VACUUM CHECK` - 20 edges
5. `Line 1` - 19 edges
6. `Line 2` - 19 edges
7. `Line 1 (라인1)` - 18 edges
8. `운전 화면 (Operation Screen)` - 17 edges
9. `GX-Works2 Instruction List (IL) CSV Export — Strict Format Specification` - 15 edges
10. `GX Works2 IL CSV Format Specification` - 11 edges

## Surprising Connections (you probably didn't know these)
- `REFRIGER CHARGING MACHINE` --semantically_similar_to--> `REFRIGER CHARGING MACHINE — HMI Specification`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `방폭 Explosion-Proof Type` --semantically_similar_to--> `§7 Explosion-Proof Configuration`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `비방폭 Non-Explosion-Proof Type` --semantically_similar_to--> `Non-Explosion-Proof Configuration (비방폭)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Limit Sensor (좌/우, 방폭 전용)` --semantically_similar_to--> `Door Limit Sensor Subsystem (방폭 전용)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md
- `Door Open Alarm` --semantically_similar_to--> `Door Open Alarm (M-relay Latch)`  [INFERRED] [semantically similar]
  .opencode/memory/project.md → Notes/REFRIGER_CHARGING_MACHINE.md

## Hyperedges (group relationships)
- **Screen Navigation Hierarchy** — N04, N05, N06, N07, N08 [INFERRED]
- **Explosion-Proof Door Alarm Chain** — N16, N18, N19, N20, N07 [INFERRED]
- **PLC Parameter Communication Cycle** — N03, N05, N06, N23 [INFERRED]
- **1-Line 1-Gun Operation Screen Layout Structure** — recm_1line1gun_operation_screen, recm_hmi_top_control_bar, recm_hmi_injection_parameters, recm_hmi_sensor_readouts, recm_hmi_production_counter, recm_hmi_navigation_buttons, recm_hmi_bottom_action_bar, recm_operation_screen_colorscheme [EXTRACTED 1.00]
- **1-Line 1-Gun Machine Identity (R134a + Gun A + Single Line)** — recm_1line1gun_config, recm_refrigerant_r134a, recm_injection_gun_a, recm_line1_refrigerant_usage, recm_1line1gun_operation_screen [EXTRACTED 1.00]
- **1LINE2GUN_CONFIGURATION** — chunk03:machine:1line2gun, chunk03:line:line1, chunk03:param:injection_gun_a, chunk03:param:injection_gun_b, chunk03:gun_selection:gun_selector, chunk03:refrigerant:R134a [INFERRED]
- **OPERATION_SCREEN_LAYOUT** — chunk03:hmi:operation_screen, chunk03:ctrl:unit_pass, chunk03:ctrl:interlock_not_used, chunk03:ctrl:alarm_reset, chunk03:ctrl:buzzer_stop, chunk03:param:refrigerant_type, chunk03:param:line1_refrigerant_usage, chunk03:param:production_quantity, chunk03:param:injection_model, chunk03:param:injection_set_amount, chunk03:param:charging_pulse, chunk03:param:refrigerant_injection_amount, chunk03:param:injection_time, chunk03:param:vacuum_degree, chunk03:param:scan_information, chunk03:param:pressure, chunk03:param:temperature, chunk03:ctrl:barcode_use, chunk03:ctrl:production_reset, chunk03:ctrl:manual_mode, chunk03:ctrl:gun_exhaust, chunk03:ctrl:product_exhaust, chunk03:ctrl:vacuum_check, chunk03:ctrl:refrigerant_injection, chunk03:ctrl:start, chunk03:ctrl:stop, chunk03:ctrl:vacuum_pump [INFERRED]
- **CHARGING_PROCESS_CYCLE** — chunk03:ctrl:vacuum_check, chunk03:ctrl:vacuum_pump, chunk03:ctrl:refrigerant_injection, chunk03:ctrl:start, chunk03:ctrl:stop, chunk03:ctrl:gun_exhaust, chunk03:ctrl:product_exhaust, chunk03:ctrl:manual_mode, chunk03:param:vacuum_degree, chunk03:param:refrigerant_injection_amount, chunk03:param:injection_time [INFERRED]
- **he_2line2gun_layout** —  [INFERRED]
- **he_global_controls** —  [INFERRED]
- **he_line1_indicators** —  [INFERRED]
- **he_line2_indicators** —  [INFERRED]
- **he_system_monitoring** —  [INFERRED]
- **he_alarm_buzzer** —  [INFERRED]
- **HE_CONFIG_GROUP** —  [EXTRACTED 1.00]
- **HE_NAV_BAR** —  [EXTRACTED 1.00]
- **HE_MEASUREMENTS** —  [EXTRACTED 1.00]
- **HE_CONTROLS** —  [EXTRACTED 1.00]
- **HE_OIL_SECTION** —  [EXTRACTED 1.00]
- **HE_REFRIGERANT_SECTION** —  [EXTRACTED 1.00]
- **HE_2LINE2GUN_CONFIG** —  [EXTRACTED 1.00]
- **2LINE4GUN Machine Configuration** —  [INFERRED]
- **Operation Screen Interface** —  [INFERRED]
- **Line 1 Monitoring Parameters** —  [INFERRED]
- **Line 2 Monitoring and Control Parameters** —  [INFERRED]

## Communities (29 total, 7 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (50): 알람 리셋 (Alarm Reset) Left, 알람 리셋 (Alarm Reset) Right, 부저 정지 (Buzzer Stop) Left, 부저 정지 (Buzzer Stop) Right, 운전 화면 (Operation Screen), 인터락 미사용 (Interlock Not Used), Line 1, Line 1 바코드 사용 (Barcode Use) (+42 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (46): 2LINE2GUN_OIL Operation Screen (Unit 2), 자동스탭 (Auto Step), 차징시간 (Charging Time), 컨베어 인터록 (Conveyor Interlock), 컨베어 인터록 사용 (Conveyor Interlock Use), R32건 (R32 Gun), R410A건 (R410A Gun), 건 선택 (Gun Selection) (+38 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (43): 10. Field Content Constraints, 12. Checklist for Generating or Modifying This Format, 13. Parsing Notes (LLM-Specific), 14. Official Manual Reference & List Mode Format, 1. File Encoding and BOM, 2. Overall File Structure (order is fixed, NO blank rows), 3-1. Row 1 — Program Name (title) record, 3-2. Row 2 — PLC Information record (+35 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (36): ALARM_RESET, BARCODE_USE, BUZZER_STOP, GUN_EXHAUST, INTERLOCK_NOT_USED, MANUAL_MODE, PRODUCT_EXHAUST, PRODUCTION_RESET (+28 more)

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (35): Alarm Detection and Handling System, Analog Input Processing (AI Raw → EU Scaling), Barcode PC↔PLC Data Flow (Write Area → Working Area → Clear), System Configuration Parameters D228/D230/D232, Injection Volume Correction Logic (RefrigVol + Corr + HMI_Cal + Batch), CSV Module Responsibilities Map (idata, gmes, setting, gunvac, unitvac, vacchec, refinj, alarm, ad, 485, spc), A3 Design Report — PLC Standard Program, D (Data Register) Device Map (+27 more)

### Community 5 - "Community 5"
Cohesion: 0.10
Nodes (30): REFRIGER CHARGING MACHINE - 2LINE4GUN Configuration, 알람 리셋 (Alarm Reset) Button, 알람 화면 (Alarm Screen) Button, 부저 정지 (Buzzer Stop) Button, 주입건 A (Injection Gun A), 주입건 B (Injection Gun B), 주입량 설정화면 (Injection Amount Setting Screen) Button, 인터락 미사용 (Interlock Not Used) Button (+22 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (27): 주입건 C (Injection Gun C), 주입건 D (Injection Gun D), Line 2 바코드 사용 (Barcode Use) Button, Line 2 차징 펄스 (Charging Pulse), Line 2 건 배기 (Gun Exhaust) Button, Line 2 냉매 주입량 (Actual Refrigerant Injection Amount), Line 2 주입건 선택 (Injection Gun Selection), Line 2 주입 모델 (Injection Model) (+19 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (25): 0-1. 지원 구성, 0-1. 지원 구성 (Variations), 0-2. 구성 파라미터 (PLC D-Register), 0-3. Line / Gun 개념, 0-4. Gun Type, 0-5. Gun Index 공식, 0-5. Gun Index 공식, 0. 시스템 구성 (System Configuration) (+17 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (26): 5-1. Solenoid 동작 요약, 5-2. GUN VACUUM, 5-3. UNIT VACUUM, 5-4. VACUUM CHECK, 5. 진공 시퀀스 상세 (gunvac.csv / unitvac.csv), code:block10, code:block11, code:block12 (+18 more)

### Community 9 - "Community 9"
Cohesion: 0.14
Nodes (24): Alarm-Only Design — No Interlock, No Emergency Stop, Door Limit Sensor (좌/우, 방폭 전용), Door Open Alarm, 방폭 Explosion-Proof Type, 비방폭 Non-Explosion-Proof Type, REFRIGER CHARGING MACHINE, Alarm Screen, Design Choice: Alarm Without Emergency Stop or Interlock (+16 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (23): REFRIGER CHARGING MACHINE, LS IXP2-1200 HMI, Mitsubishi PLC, Operation Screen, Parameter Setting Screen, User Setting Screen, Alarm Screen, Screen Navigation Flow (+15 more)

### Community 11 - "Community 11"
Cohesion: 0.10
Nodes (20): Additional Device Types (not in MAIN.csv), code:block1 (REF/), code:block2 (FF FE  4D 00 43 00 5F 00 …      ← BOM, then "MC_..." in UTF-), Development Rules, Device Prefix Frequency (MAIN.csv), Directory Structure, External Reference, File Format (GX Works2 IL CSV) (+12 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (18): M (Internal Relay) Device Map, X (Digital Input) Device Map, Y (Digital Output) Device Map, Error/Alarm Handling System, Gun Coupler Sensor Interlock, HMI Button → PLC Internal Relay Mapping, Interlock System (per Line), Main Sequence Step Control (per Line) (+10 more)

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (15): 1-1. Display Items, 1-2. Labels, 1-3. Buttons, 1. Operation Screen, 2. Parameter Setting Screen, 3. User Setting Screen — Per Injection Gun, 4. Safety PLC Reset, 5. Vacuum Pump Operation (+7 more)

### Community 14 - "Community 14"
Cohesion: 0.13
Nodes (15): 3-1. M (Internal Relay) — Bit Device (0~), 3-2. D (Data Register) — Word Device (짝수 주소), 3-3. T (Timer) — 100ms 설정, 3-4. X (Digital Input) — Hex Address, 3-5. Y (Digital Output) — Hex Address, 3. 디바이스 맵 (Device Map), Analog (Line 0 / Line 1), Calculation Work (Line 0 / Line 1) (+7 more)

### Community 15 - "Community 15"
Cohesion: 0.15
Nodes (13): 11-1. Rung boundary identification, 11-2. Rung internal structure (canonical order), 11-3. Rung composition patterns, 11-4. Rung-boundary decision table, 11-5. Constraints summary, 11. Rung Composition Rules, code:block12 ([1] Load                  — LD / LDI / LDP / LDF            ), code:block13 (LD   M1000) (+5 more)

### Community 16 - "Community 16"
Cohesion: 0.18
Nodes (12): 1-Line 1-Gun Machine Configuration, Operation Screen - 1 Line 1 Gun Variant, HMI Bottom Action Bar (Manual Mode, Gun Exhaust, Product Exhaust, Vacuum Check, Refriger Injection, Start, Stop), Injection Parameters Display Group (Model, Set Amount, Charging Pulse, Vacuum Pump, Actual Amount, Injection Time), Navigation Buttons (Injection Amount Setting, Operation Setting, Alarm Screen), Production Quantity Counter with Reset, Real-Time Sensor Readouts Group (Vacuum Torr, Scan Info, Pressure kgf/cm², Temperature ℃), HMI Top Control Bar (Unit Pass, Interlock, Alarm Reset, Buzzer Stop, Navigation) (+4 more)

### Community 17 - "Community 17"
Cohesion: 0.23
Nodes (12): Device/Operand Notation Rules (X/Y hex, M/D decimal, constants K/H/E), Graphify Knowledge Graph Tool, GX Works2 IL CSV Format Specification, IL Instruction Mnemonics Catalog (46 distinct, Sequence + Basic), MAIN.csv Reference Export (3607 lines), MELSEC-Q/L Programming Manual (Common Instruction), REF Project Documentation, Row Type Classification (Type A=Label, B=Instruction, C=Continuation) (+4 more)

### Community 18 - "Community 18"
Cohesion: 0.25
Nodes (8): 5-1. Type A — Label / Line Statement row, 5-2. Type B — Instruction row (head of an instruction, with step number), 5-3. Type C — Continuation row (extra operands of the preceding instruction), 5. Three Types of Data Rows, code:block10 (Row B: [17, "", "LD=",  "K1", "", "", ""]), code:block7 ([90,   "<<<<< Q64RD Card Converting Setup Program >>>>>>>", ), code:block8 ([0,    "", "LD",   "M1000", "", "", ""]), code:block9 (Row B: [1,  "", "MOVP", "K0", "", "", ""])

### Community 19 - "Community 19"
Cohesion: 0.29
Nodes (7): Analog Input Processing (AD→EU Scaling), System Configuration Registers (D330-D339), D (Data Register) Device Map (Even-Address Rule), Line Independence Principle, Per-Line Parameter Register Layout (D0-D29 L0, D30-D59 L1), Line/Gun System Configuration (Supports 1L/1G ~ 2L/4G), Vacuum System Sharing Within Line

### Community 20 - "Community 20"
Cohesion: 0.43
Nodes (7): REFRIGER CHARGING MACHINE PLC Standard Program Design Report (A3), GX Works2 IL CSV Format Specification, REFRIGER_CHARGING_MACHINE.md HMI Specification, MELSEC Q/L Programming Manual (Common Instruction), PLC Program Structure Design Document, Mitsubishi QCPU Q03UDV (Q mode), REFRIGER CHARGING MACHINE System

### Community 21 - "Community 21"
Cohesion: 0.50
Nodes (5): FAST+NORMAL Simultaneous Open Injection, Gun Global Index Formula, Gun Selection-Based Injection Sequence Branching, Gun Type Definitions (Type 0-3), Gun Type per Gun Registers (D62/D76/D90/D104)

## Ambiguous Edges - Review These
- `Line 1 (라인1)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override
- `Line 2 (라인2)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override

## Knowledge Gaps
- **237 isolated node(s):** `graphify`, `1. File Encoding and BOM`, `code:block1 ([Row 1]   Program name (title)        ← see §3-1)`, `3-1. Row 1 — Program Name (title) record`, `code:block2 ("PLC Information:<TAB>""QCPU (Q mode) Q03UDV""")` (+232 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Line 1 (라인1)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **What is the exact relationship between `Line 2 (라인2)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **Why does `GX-Works2 Instruction List (IL) CSV Export — Strict Format Specification` connect `Community 2` to `Community 18`, `Community 15`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `REFRIGER CHARGING MACHINE — PLC Program Structure Design` connect `Community 7` to `Community 8`, `Community 14`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Why does `5. 진공 시퀀스 상세 (gunvac.csv / unitvac.csv)` connect `Community 8` to `Community 7`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `REFRIGER_CHARGING_MACHINE_1LINE2GUN` (e.g. with `UNIT_PASS` and `INTERLOCK_NOT_USED`) actually correct?**
  _`REFRIGER_CHARGING_MACHINE_1LINE2GUN` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `1. File Encoding and BOM`, `code:block1 ([Row 1]   Program name (title)        ← see §3-1)` to the rest of the system?**
  _245 weakly-connected nodes found - possible documentation gaps or missing edges._