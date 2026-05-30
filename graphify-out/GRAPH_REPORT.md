# Graph Report - .  (2026-05-29)

## Corpus Check
- 16 files · ~52,777 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 343 nodes · 450 edges · 21 communities (15 shown, 6 thin omitted)
- Extraction: 67% EXTRACTED · 32% INFERRED · 0% AMBIGUOUS · INFERRED: 146 edges (avg confidence: 0.88)
- Token cost: 51,159 input · 4,844 output

## Community Hubs (Navigation)
- [[_COMMUNITY_HMI Dashboard Operations|HMI Dashboard Operations]]
- [[_COMMUNITY_PLC Control Parameters (1LINE2GUN)|PLC Control Parameters (1LINE2GUN)]]
- [[_COMMUNITY_System Architecture & Safety Design|System Architecture & Safety Design]]
- [[_COMMUNITY_2LINE2GUN Line 1 Parameters|2LINE2GUN Line 1 Parameters]]
- [[_COMMUNITY_2LINE4GUN Line 1 HMI|2LINE4GUN Line 1 HMI]]
- [[_COMMUNITY_2LINE4GUN Line 2 HMI|2LINE4GUN Line 2 HMI]]
- [[_COMMUNITY_Door Safety & Alarm System|Door Safety & Alarm System]]
- [[_COMMUNITY_PLC Network Instructions|PLC Network Instructions]]
- [[_COMMUNITY_Control System Architecture|Control System Architecture]]
- [[_COMMUNITY_2LINE2GUN Line 2 Parameters|2LINE2GUN Line 2 Parameters]]
- [[_COMMUNITY_1LINE1GUN HMI Configuration|1LINE1GUN HMI Configuration]]
- [[_COMMUNITY_Documentation & Format Specifications|Documentation & Format Specifications]]
- [[_COMMUNITY_System Configuration Registers|System Configuration Registers]]
- [[_COMMUNITY_Core Project Documentation|Core Project Documentation]]
- [[_COMMUNITY_Gun Type Selection Logic|Gun Type Selection Logic]]
- [[_COMMUNITY_OpenCode Package Dependencies|OpenCode Package Dependencies]]
- [[_COMMUNITY_POU Module & CSV Data Flow|POU Module & CSV Data Flow]]
- [[_COMMUNITY_SPC Statistics & End Conditions|SPC Statistics & End Conditions]]
- [[_COMMUNITY_OpenCode Project Config|OpenCode Project Config]]
- [[_COMMUNITY_OpenCode Project Memory|OpenCode Project Memory]]
- [[_COMMUNITY_Device Map T-Timer|Device Map T-Timer]]

## God Nodes (most connected - your core abstractions)
1. `REFRIGER_CHARGING_MACHINE_1LINE2GUN` - 34 edges
2. `2LINE2GUN_OIL Operation Screen (Unit 2)` - 33 edges
3. `Line 2 (라인2)` - 22 edges
4. `Line 1` - 19 edges
5. `Line 2` - 19 edges
6. `Line 1 (라인1)` - 18 edges
7. `운전 화면 (Operation Screen)` - 17 edges
8. `GX Works2 IL CSV Format Specification` - 11 edges
9. `REFRIGER CHARGING MACHINE — HMI Specification` - 11 edges
10. `PLC Program Structure Design` - 10 edges

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

## Communities (21 total, 6 thin omitted)

### Community 0 - "HMI Dashboard Operations"
Cohesion: 0.06
Nodes (46): 2LINE2GUN_OIL Operation Screen (Unit 2), 자동스탭 (Auto Step), 차징시간 (Charging Time), 컨베어 인터록 (Conveyor Interlock), 컨베어 인터록 사용 (Conveyor Interlock Use), R32건 (R32 Gun), R410A건 (R410A Gun), 건 선택 (Gun Selection) (+38 more)

### Community 1 - "PLC Control Parameters (1LINE2GUN)"
Cohesion: 0.08
Nodes (36): ALARM_RESET, BARCODE_USE, BUZZER_STOP, GUN_EXHAUST, INTERLOCK_NOT_USED, MANUAL_MODE, PRODUCT_EXHAUST, PRODUCTION_RESET (+28 more)

### Community 2 - "System Architecture & Safety Design"
Cohesion: 0.07
Nodes (35): Alarm Detection and Handling System, Analog Input Processing (AI Raw → EU Scaling), Barcode PC↔PLC Data Flow (Write Area → Working Area → Clear), System Configuration Parameters D228/D230/D232, Injection Volume Correction Logic (RefrigVol + Corr + HMI_Cal + Batch), CSV Module Responsibilities Map (idata, gmes, setting, gunvac, unitvac, vacchec, refinj, alarm, ad, 485, spc), A3 Design Report — PLC Standard Program, D (Data Register) Device Map (+27 more)

### Community 3 - "2LINE2GUN Line 1 Parameters"
Cohesion: 0.09
Nodes (33): 알람 리셋 (Alarm Reset) Left, 알람 리셋 (Alarm Reset) Right, 부저 정지 (Buzzer Stop) Left, 부저 정지 (Buzzer Stop) Right, 운전 화면 (Operation Screen), 인터락 미사용 (Interlock Not Used), Line 1, Line 1 바코드 사용 (Barcode Use) (+25 more)

### Community 4 - "2LINE4GUN Line 1 HMI"
Cohesion: 0.1
Nodes (30): REFRIGER CHARGING MACHINE - 2LINE4GUN Configuration, 알람 리셋 (Alarm Reset) Button, 알람 화면 (Alarm Screen) Button, 부저 정지 (Buzzer Stop) Button, 주입건 A (Injection Gun A), 주입건 B (Injection Gun B), 주입량 설정화면 (Injection Amount Setting Screen) Button, 인터락 미사용 (Interlock Not Used) Button (+22 more)

### Community 5 - "2LINE4GUN Line 2 HMI"
Cohesion: 0.11
Nodes (27): 주입건 C (Injection Gun C), 주입건 D (Injection Gun D), Line 2 바코드 사용 (Barcode Use) Button, Line 2 차징 펄스 (Charging Pulse), Line 2 건 배기 (Gun Exhaust) Button, Line 2 냉매 주입량 (Actual Refrigerant Injection Amount), Line 2 주입건 선택 (Injection Gun Selection), Line 2 주입 모델 (Injection Model) (+19 more)

### Community 6 - "Door Safety & Alarm System"
Cohesion: 0.14
Nodes (24): Alarm-Only Design — No Interlock, No Emergency Stop, Door Limit Sensor (좌/우, 방폭 전용), Door Open Alarm, 방폭 Explosion-Proof Type, 비방폭 Non-Explosion-Proof Type, REFRIGER CHARGING MACHINE, Alarm Screen, Design Choice: Alarm Without Emergency Stop or Interlock (+16 more)

### Community 7 - "PLC Network Instructions"
Cohesion: 0.12
Nodes (23): REFRIGER CHARGING MACHINE, LS IXP2-1200 HMI, Mitsubishi PLC, Operation Screen, Parameter Setting Screen, User Setting Screen, Alarm Screen, Screen Navigation Flow (+15 more)

### Community 8 - "Control System Architecture"
Cohesion: 0.12
Nodes (18): M (Internal Relay) Device Map, X (Digital Input) Device Map, Y (Digital Output) Device Map, Error/Alarm Handling System, Gun Coupler Sensor Interlock, HMI Button → PLC Internal Relay Mapping, Interlock System (per Line), Main Sequence Step Control (per Line) (+10 more)

### Community 9 - "2LINE2GUN Line 2 Parameters"
Cohesion: 0.17
Nodes (17): Line 2, Line 2 바코드 사용 (Barcode Use), Line 2 차징 펄스 (Charging Pulse), 주입건 B (Injection Gun B), Line 2 주입 모델 (Injection Model), Line 2 주입 설정량 (Injection Set Amount), Line 2 주입 시간 (Injection Time), Line 2 압력 (Pressure) (+9 more)

### Community 10 - "1LINE1GUN HMI Configuration"
Cohesion: 0.18
Nodes (12): 1-Line 1-Gun Machine Configuration, Operation Screen - 1 Line 1 Gun Variant, HMI Bottom Action Bar (Manual Mode, Gun Exhaust, Product Exhaust, Vacuum Check, Refriger Injection, Start, Stop), Injection Parameters Display Group (Model, Set Amount, Charging Pulse, Vacuum Pump, Actual Amount, Injection Time), Navigation Buttons (Injection Amount Setting, Operation Setting, Alarm Screen), Production Quantity Counter with Reset, Real-Time Sensor Readouts Group (Vacuum Torr, Scan Info, Pressure kgf/cm², Temperature ℃), HMI Top Control Bar (Unit Pass, Interlock, Alarm Reset, Buzzer Stop, Navigation) (+4 more)

### Community 11 - "Documentation & Format Specifications"
Cohesion: 0.23
Nodes (12): Device/Operand Notation Rules (X/Y hex, M/D decimal, constants K/H/E), Graphify Knowledge Graph Tool, GX Works2 IL CSV Format Specification, IL Instruction Mnemonics Catalog (46 distinct, Sequence + Basic), MAIN.csv Reference Export (3607 lines), MELSEC-Q/L Programming Manual (Common Instruction), REF Project Documentation, Row Type Classification (Type A=Label, B=Instruction, C=Continuation) (+4 more)

### Community 12 - "System Configuration Registers"
Cohesion: 0.29
Nodes (7): Analog Input Processing (AD→EU Scaling), System Configuration Registers (D330-D339), D (Data Register) Device Map (Even-Address Rule), Line Independence Principle, Per-Line Parameter Register Layout (D0-D29 L0, D30-D59 L1), Line/Gun System Configuration (Supports 1L/1G ~ 2L/4G), Vacuum System Sharing Within Line

### Community 13 - "Core Project Documentation"
Cohesion: 0.43
Nodes (7): REFRIGER CHARGING MACHINE PLC Standard Program Design Report (A3), GX Works2 IL CSV Format Specification, REFRIGER_CHARGING_MACHINE.md HMI Specification, MELSEC Q/L Programming Manual (Common Instruction), PLC Program Structure Design Document, Mitsubishi QCPU Q03UDV (Q mode), REFRIGER CHARGING MACHINE System

### Community 14 - "Gun Type Selection Logic"
Cohesion: 0.5
Nodes (5): FAST+NORMAL Simultaneous Open Injection, Gun Global Index Formula, Gun Selection-Based Injection Sequence Branching, Gun Type Definitions (Type 0-3), Gun Type per Gun Registers (D62/D76/D90/D104)

## Ambiguous Edges - Review These
- `Line 1 (라인1)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override
- `Line 2 (라인2)` → `인터락 미사용 (Interlock Not Used) Button`  [AMBIGUOUS]
   · relation: safety_override

## Knowledge Gaps
- **123 isolated node(s):** `MELSEC-Q/L Programming Manual (Common Instruction)`, `MC_26074 Reference Project`, `M (Internal Relay) Device Map`, `D (Data Register) Device Map`, `Analog Input Processing (AI Raw → EU Scaling)` (+118 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Line 1 (라인1)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **What is the exact relationship between `Line 2 (라인2)` and `인터락 미사용 (Interlock Not Used) Button`?**
  _Edge tagged AMBIGUOUS (relation: safety_override) - confidence is low._
- **Why does `Line 2 (라인2)` connect `2LINE4GUN Line 2 HMI` to `2LINE4GUN Line 1 HMI`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Why does `Line 1 (라인1)` connect `2LINE4GUN Line 1 HMI` to `2LINE4GUN Line 2 HMI`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `REFRIGER_CHARGING_MACHINE_1LINE2GUN` (e.g. with `UNIT_PASS` and `INTERLOCK_NOT_USED`) actually correct?**
  _`REFRIGER_CHARGING_MACHINE_1LINE2GUN` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `MELSEC-Q/L Programming Manual (Common Instruction)`, `MC_26074 Reference Project`, `Line Independence Design Principle` to the rest of the system?**
  _131 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `HMI Dashboard Operations` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._