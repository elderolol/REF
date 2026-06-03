# Communication
- ALWAYS respond in English ONLY, regardless of the language the user writes in.
- Never switch to Korean or any other language, even if asked.
- Be concise.

## Work Mode
- Work sequentially, one task at a time.
- Never dispatch subagents, background tasks, or parallel work under any circumstances.
- All work must be done directly in the main session without delegation.
- Exception: graphify skill tool calls are allowed.

## Project Conventions
- `src/` — IL Logic CSV source files only.
- `src_md/` — converted MD + JSON files from src/ CSV only.
- `src2/` — same structure as src/, newly built version.
- `src2_md/` — converted MD + JSON files from src2/ CSV.
- Reference/docs content uses `.md` or `.txt` extensions only. Never put documentation text in source code files.
- GX Works2 IL coding rules: see `Notes/GX_WORKS2_IL_Spec.md` in project root.
- PLC program structure and logic architecture: see `Notes/REF_DOCUMENT.md`

## graphify
This project has a knowledge graph at src_md/graphify-out/ with god nodes, community structure, and cross-file relationships.
When the user types `/graphify`, invoke the `skill` tool with `skill: "graphify"` before doing anything else.
Rules:
- For codebase questions, first run `graphify query "<question>"` when src_md/graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If src_md/graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read src_md/graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying MD/JSON in src_md/, run `graphify update src_md` to keep the graph current (AST-only, no API cost).

## CSV → MD/JSON Conversion
- When any CSV in src/ or src2/ changes, re-generate only the changed file's MD + JSON in src_md/ or src2_md/.
- Conversion rule: re-generate if src/filename.csv mtime > src_md/filename.md mtime.
- Skip files: `ref_comment.csv`
- Skip folders: `src/set_reset/`
- Always run `graphify update src_md` (or `graphify update src2_md`) after conversion.
- Generated CSVs: MAIN.csv from `gen_main_final.py`, alarm.csv from `gen_alarm.py`, vacchec.csv from `gen_vacchec.py`, gunvac.csv from `gen_gunvac.py`, unitvac.csv from `gen_unitvac.py`, refinj.csv from `gen_refinj.py`, indexs.csv from `gen_indexs.py`, spc.csv from `gen_spc.py`, gmes.csv from `gen_gmes.py`. Run all gen*.py before convert_to_md.py.