import json
from pathlib import Path

# Chunk 1 result from agent
chunk1 = {"nodes":[{"id":"refriger_charging_machine","label":"REFRIGER CHARGING MACHINE","file_type":"document","source_file":"Notes/REFRIGER_CHARGING_MACHINE.md","source_location":null,"source_url":null,"captured_at":null,"author":null,"contributor":null},{"id":"mitsubishi_q03udv","label":"Mitsubishi Q03UDV PLC","file_type":"document","source_file":"Notes/DESIGN_REPORT_A3.html","source_location":null,"source_url":null,"captured_at":null,"author":null,"contributor":null},{"id":"gx_works2_il_csv_format","label":"GX Works2 IL CSV Format Specification","file_type":"document","source_file":"Notes/GX_WORKS2_IL_Spec.md","source_location":null,"source_url":null,"captured_at":null,"author":null,"contributor":null},{"id":"plc_program_structure","label":"PLC Program Structure Design","file_type":"document","source_file":"Notes/PLC_PROGRAM_STRUCTURE.md","source_location":null,"source_url":null,"captured_at":null,"author":null,"contributor":null}],"edges":[{"source":"plc_program_structure","target":"refriger_charging_machine","relation":"designs","confidence":"EXTRACTED","confidence_score":1.0,"source_file":"Notes/PLC_PROGRAM_STRUCTURE.md","source_location":null,"weight":1.0},{"source":"plc_program_structure","target":"hmi_specification","relation":"references","confidence":"EXTRACTED","confidence_score":1.0,"source_file":"Notes/PLC_PROGRAM_STRUCTURE.md","source_location":"§header","weight":1.0}],"hyperedges":[],"input_tokens":0,"output_tokens":0}

# Save chunk 1
Path('graphify-out/.graphify_chunk_01.json').write_text(json.dumps(chunk1, indent=2, ensure_ascii=False), encoding="utf-8")

# Chunk 2 - PDF extraction (minimal since PDF was empty)
chunk2 = {"nodes":[],"edges":[],"hyperedges":[],"input_tokens":0,"output_tokens":0}
Path('graphify-out/.graphify_chunk_02.json').write_text(json.dumps(chunk2, indent=2, ensure_ascii=False), encoding="utf-8")

print("Chunks saved")
