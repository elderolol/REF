# CSV (GX Works IL) -> MD + JSON converter
import csv, io, json, os, re
from datetime import date

def convert_csv_to_md_json(csv_path, md_path, json_path):
    with open(csv_path, 'rb') as f:
        raw = f.read().decode('utf-16-le')
    reader = csv.reader(io.StringIO(raw), delimiter='\t')
    rows = list(reader)

    if len(rows) < 3:
        return

    src_name = rows[0][0].strip('\ufeff').strip('"').lstrip('?') if rows[0] else os.path.basename(csv_path)
    cpu = rows[1][1].strip() if len(rows) > 1 and len(rows[1]) > 1 else "Q03UDV"

    # Parse instructions
    instructions = []
    current_step = None
    section_name = "HEADER"
    sections = {}  # name -> [(step, inst, dev)]

    for row in rows[3:]:
        if len(row) < 4:
            continue
        step_str = row[0].strip().strip('"')
        label = row[1].strip().strip('"') if len(row) > 1 else ''
        inst = row[2].strip().strip('"') if len(row) > 2 else ''
        dev = row[3].strip().strip('"') if len(row) > 3 else ''
        note = row[6].strip().strip('"') if len(row) > 6 else ''

        if label.startswith('>> '):
            section_name = label[3:]
            if section_name not in sections:
                sections[section_name] = []
            continue

        if inst == 'END':
            break

        if step_str.isdigit():
            current_step = int(step_str)

        if inst:
            sections.setdefault(section_name, []).append((current_step, inst, dev))

    # Build blocks
    blocks = []
    for name, insts in sections.items():
        if not insts:
            continue
        steps = [s for s, i, d in insts if s is not None]
        step_start = min(steps) if steps else 0
        step_end = max(steps) if steps else 0
        conditions = [(i, d) for s, i, d in insts if i in ('LD', 'LDI')]
        actions = [(i, d) for s, i, d in insts if i not in ('LD', 'LDI')]
        blocks.append({
            'name': name,
            'step_start': step_start,
            'step_end': step_end,
            'conditions': conditions,
            'actions': actions,
        })

    total_steps = max([b['step_end'] for b in blocks]) if blocks else 0
    today = date.today().isoformat()

    # Build device map
    dev_set = {}
    dev_rst = {}
    dev_out = {}
    dev_read = {}
    for b in blocks:
        for inst, dev in b['conditions'] + b['actions']:
            if not dev:
                continue
            if inst == 'SET':
                dev_set[dev] = dev_set.get(dev, 0) + 1
            elif inst == 'RST':
                dev_rst[dev] = dev_rst.get(dev, 0) + 1
            elif inst == 'OUT':
                dev_out[dev] = dev_out.get(dev, 0) + 1
            else:
                dev_read[dev] = dev_read.get(dev, 0) + 1
    all_devs = sorted(set(list(dev_set.keys()) + list(dev_rst.keys()) + list(dev_out.keys()) + list(dev_read.keys())))

    # ===== Generate MD =====
    md_lines = []
    md_lines.append('---')
    md_lines.append(f'# {src_name} -- IL Logic Map')
    md_lines.append(f'**CPU:** {cpu}')
    md_lines.append(f'**Total Steps:** {total_steps}')
    md_lines.append(f'**Blocks:** {len(blocks)}')
    md_lines.append(f'**Generated:** {today}')
    md_lines.append('---')
    md_lines.append('')
    md_lines.append('## Block List')
    md_lines.append('| # | Name | Steps | Condition Device | Action Count |')
    md_lines.append('|---|------|-------|-----------------|--------------|')
    for i, b in enumerate(blocks):
        cond_devs = ', '.join([f'{i} {d}' for i, d in b['conditions'][:3]])
        if len(b['conditions']) > 3:
            cond_devs += f' ... (+{len(b["conditions"])-3})'
        md_lines.append(f'| {i+1} | {b["name"]} | {b["step_start"]}\u2013{b["step_end"]} | {cond_devs} | {len(b["actions"])} |')
    md_lines.append('')
    md_lines.append('## Block Detail')
    md_lines.append('')
    for i, b in enumerate(blocks):
        md_lines.append(f'### Block {i+1}: {b["name"]} (Step {b["step_start"]}-{b["step_end"]})')
        md_lines.append('')
        md_lines.append('**Trigger Condition:**')
        for inst, dev in b['conditions']:
            md_lines.append(f'- {inst} {dev}')
        md_lines.append('')
        md_lines.append('**Actions:**')
        for inst, dev in b['actions']:
            md_lines.append(f'- {inst} {dev}')
        md_lines.append('')

    # Device map
    md_lines.append('## Device Map')
    md_lines.append('| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |')
    md_lines.append('|--------|------|-----------|-----------|-----------|------------|')
    for dev in all_devs:
        dtype = 'M' if dev.startswith('M') else 'L' if dev.startswith('L') else 'D' if dev.startswith('D') else 'T' if dev.startswith('T') else 'K' if dev.startswith('K') else 'X' if dev.startswith('X') else 'Y' if dev.startswith('Y') else '?'
        s = str(dev_set.get(dev, ''))
        r = str(dev_rst.get(dev, ''))
        o = str(dev_out.get(dev, ''))
        rd = str(dev_read.get(dev, ''))
        md_lines.append(f'| {dev} | {dtype} | {s} | {r} | {o} | {rd} |')

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines) + '\n')

    # ===== Generate JSON =====
    json_data = {
        'meta': {
            'source_file': os.path.basename(csv_path),
            'cpu': cpu,
            'total_steps': total_steps,
            'block_count': len(blocks),
            'generated': today,
        },
        'blocks': [{
            'id': i+1,
            'name': b['name'],
            'step_start': b['step_start'],
            'step_end': b['step_end'],
            'conditions': [{'instruction': i, 'device': d} for i, d in b['conditions']],
            'actions': [{'instruction': i, 'device': d} for i, d in b['actions']],
        } for i, b in enumerate(blocks)],
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    src_dir = 'F:/WorkSpace/REF/src2'
    dst_dir = 'F:/WorkSpace/REF/src2_md'
    skip_files = {'ref_comment.csv'}
    skip_dirs = {'set_reset'}

    for fname in os.listdir(src_dir):
        if not fname.endswith('.csv'):
            continue
        if fname in skip_files:
            continue
        fpath = os.path.join(src_dir, fname)
        if os.path.isdir(fpath):
            continue

        basename = fname[:-4]
        md_path = os.path.join(dst_dir, f'{basename}.md')
        json_path = os.path.join(dst_dir, f'{basename}.json')

        print(f'Converting: {fname} -> {basename}.md + {basename}.json')
        convert_csv_to_md_json(fpath, md_path, json_path)
    print('Done.')
