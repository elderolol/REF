# Graph Report - src2_md  (2026-06-03)

## Corpus Check
- 22 files · ~19,735 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 193 nodes · 171 edges · 22 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bee248bf`
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

## God Nodes (most connected - your core abstractions)
1. `Block Detail` - 16 edges
2. `Block Detail` - 13 edges
3. `Block Detail` - 9 edges
4. `meta` - 6 edges
5. `meta` - 6 edges
6. `meta` - 6 edges
7. `meta` - 6 edges
8. `meta` - 6 edges
9. `meta` - 6 edges
10. `meta` - 6 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (22 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.10
Nodes (19): Block 10: L1 EXHAUST (Step 84-87), Block 11: COMPLETION L0 (M822) (Step 89-118), Block 12: COMPLETION L1 (M838) (Step 120-161), Block 13: TIMEOUT ALARM TRIGGERS (Step 163-190), Block 14: OIL RESTART FLAGS (Step 192-207), Block 15: OIL NORMAL ENTRY (Step 209-226), Block 1: L0 REFRIG FAST (Step 1-6), Block 2: L0 REFRIG NORMAL (Step 8-11) (+11 more)

### Community 1 - "Community 1"
Cohesion: 0.12
Nodes (16): Block 10: EXHAUST TIMER (Step 556-559), Block 11: LAMP CONTROL (Step 561-600), Block 12: HMI LAMP (Step 602-643), Block 1: MODE CONTROL (Step 1-38), Block 2: INTERLOCK CHECK (Step 40-51), Block 3: STOP / EMG LATCH (Step 53-80), Block 4: NG ALARM GROUP (Step 82-107), Block 5: READY L0 (Step 109-142) (+8 more)

### Community 2 - "Community 2"
Cohesion: 0.15
Nodes (12): Block 1: SYSTEM FLAGS (Step 1-6), Block 2: INIT FIRST SCAN (Step 8-9), Block 3: INPUT MAPPING L0 (Step 98-129), Block 4: INPUT MAPPING L1 (Step 131-162), Block 5: OUTPUT MAPPING L0 (Step 164-189), Block 6: GLOBAL OUTPUTS (Step 191-198), Block 7: OUTPUT MAPPING L1 (Step 200-223), Block 8: CONFIG VALIDATION (Step 225-232) (+4 more)

### Community 3 - "Community 3"
Cohesion: 0.20
Nodes (9): Block 1: L0 CYCLE DONE (Step 1-12), Block 2: L1 CYCLE DONE (Step 14-25), Block 3: DISPLAY BOMBE (Step 27-30), Block 4: VAC SPC LOGGING (Step 32-53), Block 5: VAC SPC CLEAR (Step 55-58), Block Detail, Block List, Device Map (+1 more)

### Community 4 - "Community 4"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 6 - "Community 6"
Cohesion: 0.25
Nodes (7): Block 1: ALARM LATCH (Step 1-61), Block 2: BUZZER (Step 63-88), Block 3: ALARM RESET (Step 90-93), Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 7 - "Community 7"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 8 - "Community 8"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 9 - "Community 9"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 10 - "Community 10"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 11 - "Community 11"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 12 - "Community 12"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 13 - "Community 13"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 14 - "Community 14"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 15 - "Community 15"
Cohesion: 0.25
Nodes (7): blocks, meta, block_count, cpu, generated, source_file, total_steps

### Community 16 - "Community 16"
Cohesion: 0.29
Nodes (6): Block 1: GUN VACUUM (Line 0) (Step 1-35), Block 2: GUN VACUUM (Line 1) (Step 37-71), Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 17 - "Community 17"
Cohesion: 0.29
Nodes (6): Block 1: UNIT VACUUM (Line 0) (Step 1-42), Block 2: UNIT VACUUM (Line 1) (Step 44-85), Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 18 - "Community 18"
Cohesion: 0.29
Nodes (6): Block 1: VAC CHECK L0 (Step 1-21), Block 2: VAC CHECK L1 (Step 23-43), Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 19 - "Community 19"
Cohesion: 0.33
Nodes (5): Block 1: CONFIG SYNC (Step 1-4), Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 20 - "Community 20"
Cohesion: 0.40
Nodes (4): Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

### Community 21 - "Community 21"
Cohesion: 0.40
Nodes (4): Block Detail, Block List, Device Map, REF_self_holding -- IL Logic Map

## Knowledge Gaps
- **140 isolated node(s):** `source_file`, `cpu`, `total_steps`, `block_count`, `generated` (+135 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `source_file`, `cpu`, `total_steps` to the rest of the system?**
  _140 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._