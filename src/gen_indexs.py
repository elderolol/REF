# INDEXS — Model selection + injection setpoint lookup
# Extracted from gmes.csv: GAS TYPE MAP, BARCODE match, MANUAL MODEL
st = 0; lines = []
def a(i,d): global st; lines.append(f'"{st}"\t""\t"{i}"\t"{d}"\t""\t""\t""'); st += 1
def ac(d): lines.append(f'""\t""\t""\t"{d}"\t""\t""\t""')
def al(t): global st; lines.append(f'"{st}"\t">> {t}"\t""\t""\t""\t""\t""'); st += 1
def hd(n):
    lines.append(f'"{n}"'); lines.append('"PLC Information:"\t"QCPU (Q mode) Q03UDV"')
    lines.append('"Step No."\t"Line Statement"\t"Instruction"\t"I/O(Device)"\t"Blank"\t"PI Statement"\t"Note"')
def wr(p):
    c = "\r\n".join(lines) + "\r\n"
    with open(p, "wb") as f: f.write(b'\xff\xfe'); f.write(c.encode('utf-16-le'))

hd("indexs")

# ===== PC DATA CHECK =====
# D7000=1 (Line1), D8000=2 (Line2): validate data integrity
al("PC DATA CHECK")
a("LD", "L3"); a("LDD>", "D7001"); ac("K0")
a("LD<>", "D7000"); ac("K1")
a("ANB", ""); a("SET", "L76")
a("LD", "L3"); a("LDD>", "D8001"); ac("K0")
a("LD<>", "D8000"); ac("K2")
a("ANB", ""); a("SET", "L76")

# ===== AUTO BARCODE =====
al("AUTO BARCODE")
a("LDD>", "D7001"); ac("K0")
a("BMOV", "D6980"); ac("D7220"); ac("K20")
a("LDD>", "D8001"); ac("K0")
a("BMOV", "D7980"); ac("D8220"); ac("K20")

# ===== BARCODE L1 (D7001 → D60~D84) =====
al("BARCODE L1 (D60~D84)")
for k in range(1, 26):
    dev = f"D{59 + k}"  # D60..D84
    a("LD", "L3")
    a("LDD>", "D7001"); ac("K0")
    a("ANB", "")
    a("LDD=", "D7001"); ac(dev)
    a("ANB", "")
    a("MOV", f"K{k}"); ac("D0")

# ===== BARCODE L2 (D8001 → D88~D112) =====
al("BARCODE L2 (D88~D112)")
for k in range(1, 26):
    dev = f"D{87 + k}"  # D88..D112
    a("LD", "L3")
    a("LDD>", "D8001"); ac("K0")
    a("ANB", "")
    a("LDD=", "D8001"); ac(dev)
    a("ANB", "")
    a("MOV", f"K{k}"); ac("D30")

# ===== MANUAL MODEL L0 (D0 → D128 via D60~D84) =====
al("MANUAL MODEL L0")
for k in range(1, 26):
    dev = f"D{59 + k}"  # D60..D84
    a("LDI", "L3")
    a("AND>", "D0"); ac("K0")
    a("AND<=", "D0"); ac("K25")
    a("LD=", "D0"); ac(f"K{k}")
    a("ANB", "")
    a("MOV", dev); ac("D128")

# ===== MANUAL MODEL L1 (D30 → D404 via D88~D112) =====
al("MANUAL MODEL L1")
for k in range(1, 26):
    dev = f"D{87 + k}"  # D88..D112
    a("LDI", "L3")
    a("AND>", "D30"); ac("K0")
    a("AND<=", "D30"); ac("K25")
    a("LD=", "D30"); ac(f"K{k}")
    a("ANB", "")
    a("MOV", dev); ac("D404")

# ===== BARCODE RESET =====
# Clear PC barcode area on NG STOP or (cycle done + idle)
# Allows detecting new PC data: 0 → non-zero transition
al("BARCODE RESET")
a("LD", "L24"); a("AND", "M16")
a("LD", "L40"); a("AND", "M32")
a("ORB", "")
a("OR", "L17"); a("OR", "L19"); a("OR", "L21"); a("OR", "L23"); a("OR", "L64")
a("MOV", "K0"); ac("D6890")
a("MOV", "K0"); ac("D7000")
a("MOV", "K0"); ac("D7001")
a("MOV", "K0"); ac("D8000")
a("MOV", "K0"); ac("D8001")

# ===== BARCODE MODEL CLEANUP =====
al("BARCODE MODEL CLEANUP")
a("LD", "L3")
a("LD", "L17"); a("OR", "L19"); a("OR", "L21"); a("OR", "L23")
a("OR", "L24"); a("OR", "L40"); a("OR", "L64")
a("ANB", "")
a("RST", "D0"); a("RST", "D30")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\indexs.csv")
