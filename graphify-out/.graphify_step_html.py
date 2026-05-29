import json
from graphify.build import build_from_json
from graphify.export import to_html, save_manifest
from graphify.cache import save_semantic_cache
from pathlib import Path
from datetime import datetime, timezone

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text(encoding="utf-8"))
analysis   = json.loads(Path('graphify-out/.graphify_analysis.json').read_text(encoding="utf-8"))
labels_raw = json.loads(Path('graphify-out/.graphify_labels.json').read_text(encoding="utf-8"))
detect = json.loads(Path('graphify-out/.graphify_incremental.json').read_text(encoding="utf-8"))

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}
labels = {int(k): v for k, v in labels_raw.items()}

to_html(G, communities, 'graphify-out/graph.html', community_labels=labels or None)
print('graph.html written')

# Save cache
saved = save_semantic_cache(extraction.get('nodes', []), extraction.get('edges', []), extraction.get('hyperedges', []))
print(f'Cached {saved} files')

# Save manifest for --update
save_manifest(detect['files'])
print('Manifest saved')

# Update cost tracker
input_tok = extraction.get('input_tokens', 0)
output_tok = extraction.get('output_tokens', 0)
cost_path = Path('graphify-out/cost.json')
if cost_path.exists():
    cost = json.loads(cost_path.read_text(encoding="utf-8"))
else:
    cost = {'runs': [], 'total_input_tokens': 0, 'total_output_tokens': 0}
cost['runs'].append({
    'date': datetime.now(timezone.utc).isoformat(),
    'input_tokens': input_tok,
    'output_tokens': output_tok,
    'files': detect.get('total_files', 0),
})
cost['total_input_tokens'] += input_tok
cost['total_output_tokens'] += output_tok
cost_path.write_text(json.dumps(cost, indent=2, ensure_ascii=False), encoding="utf-8")
print(f'Tokens: {input_tok:,} in / {output_tok:,} out')
