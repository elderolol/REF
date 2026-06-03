# INDEXS ??Model selection + injection setpoint lookup
# Fixed: LDD>+ANB ??ANDD> (cleaner IL for GXW CSV import)
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

hd("REF_self_holding")

# ===== PC DATA CHECK =====
# D7000=1 (Line0), D8000=2 (Line1): validate data integrity
# Combined into single rung with ORB to eliminate double-coil
al("PC DATA CHECK")
a("LD", "M803"); a("AND>", "D7001"); ac("K0"); a("AND<>", "D7000"); ac("K1")
a("LD", "M803"); a("AND>", "D8001"); ac("K0"); a("AND<>", "D8000"); ac("K2")
a("ORB", ""); a("SET", "M876")

# ===== AUTO BARCODE =====
al("AUTO BARCODE")
a("LD>", "D7001"); ac("K0")
a("BMOV", "D6980"); ac("D7220"); ac("K20")
a("LD>", "D8001"); ac("K0")
a("BMOV", "D7980"); ac("D8220"); ac("K20")

# ===== BARCODE L1 (D7001 ??D60~D84) =====
al("BARCODE L1 (D60~D84)")
for k in range(1, 26):
    dev = f"D{59 + k}"
    a("LD", "M803"); a("AND>", "D7001"); ac("K0"); a("AND=", "D7001"); ac(dev)
    a("MOV", f"K{k}"); ac("D0")

# ===== BARCODE L2 (D8001 ??D88~D112) =====
al("BARCODE L2 (D88~D112)")
for k in range(1, 26):
    dev = f"D{87 + k}"
    a("LD", "M803"); a("AND>", "D8001"); ac("K0"); a("AND=", "D8001"); ac(dev)
    a("MOV", f"K{k}"); ac("D30")

# ===== MANUAL MODEL L0 (D0 ??D128 via D60~D84) =====
al("MANUAL MODEL L0")
for k in range(1, 26):
    dev = f"D{59 + k}"
    a("LDI", "M803"); a("AND>", "D0"); ac("K0"); a("AND<=", "D0"); ac("K25")
    a("AND=", "D0"); ac(f"K{k}")
    a("MOV", dev); ac("D128")

# ===== MANUAL MODEL L1 (D30 ??D404 via D88~D112) =====
al("MANUAL MODEL L1")
for k in range(1, 26):
    dev = f"D{87 + k}"
    a("LDI", "M803"); a("AND>", "D30"); ac("K0"); a("AND<=", "D30"); ac("K25")
    a("AND=", "D30"); ac(f"K{k}")
    a("MOV", dev); ac("D404")

# ===== BARCODE RESET =====
al("BARCODE RESET")
a("LD", "M824"); a("AND", "M16")
a("LD", "M840"); a("AND", "M32")
a("ORB", "")
a("OR", "M817"); a("OR", "M819"); a("OR", "M821"); a("OR", "M823"); a("OR", "M864")
a("MOV", "K0"); ac("D6890")
a("MOV", "K0"); ac("D7000")
a("MOV", "K0"); ac("D7001")
a("MOV", "K0"); ac("D8000")
a("MOV", "K0"); ac("D8001")

# ===== BARCODE MODEL CLEANUP =====
al("BARCODE MODEL CLEANUP")
a("LD", "M803")
a("LD", "M817"); a("OR", "M819"); a("OR", "M821"); a("OR", "M823")
a("OR", "M824"); a("OR", "M840"); a("OR", "M864")
a("ANB", "")
a("RST", "D0"); a("RST", "D30")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\indexs.csv")

