# SPC ??Cycle done accumulation + VAC SPC logging
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

# ===== L0 CYCLE DONE =====
al("L0 CYCLE DONE")
a("LD", "M824"); a("D+", "D280"); ac("D130"); ac("D280")
a("LD", "M824"); a("D+", "D282"); ac("K1"); ac("D282")
a("LD", "M824"); a("D+", "D284"); ac("D124"); ac("D284")
a("LD", "M824"); a("DMOV", "D130"); ac("D286")
a("LD", "M824"); a("DMOV", "D128"); ac("D288")

# ===== L1 CYCLE DONE =====
al("L1 CYCLE DONE")
a("LD", "M840"); a("D+", "D290"); ac("D406"); ac("D290")
a("LD", "M840"); a("D+", "D292"); ac("K1"); ac("D292")
a("LD", "M840"); a("D+", "D294"); ac("D400"); ac("D294")
a("LD", "M840"); a("DMOV", "D406"); ac("D296")
a("LD", "M840"); a("DMOV", "D128"); ac("D298")

# ===== DISPLAY BOMBE =====
al("DISPLAY BOMBE")
a("LD", "M0"); a("MOV", "D282"); ac("D88")
a("LDD>=", "D280"); ac("D14"); a("SET", "M875")

# ===== VAC SPC LOGGING =====
al("VAC SPC LOGGING")
a("LD", "M18"); a("OR", "M19"); a("OR", "M20"); a("OUTH", "T18"); ac("K8")
a("LD", "M34"); a("OR", "M35"); a("OR", "M36"); a("OUTH", "T19"); ac("K8")
a("LD", "T18"); a("BMOV", "D7020"); ac("D7022"); ac("K198")
a("LD", "T18")
a("LD", "M18"); a("OR", "M19"); a("OR", "M20"); a("ANB", "")
a("DMOV", "D160"); ac("D7020")
a("LD", "T19")
a("LD", "M34"); a("OR", "M35"); a("OR", "M36"); a("ANB", "")
a("DMOV", "D172"); ac("D8020")

# ===== VAC SPC CLEAR =====
al("VAC SPC CLEAR")
a("LD", "M17"); a("OR", "M33")
a("FMOV", "K0"); ac("D7020"); ac("K200")
a("FMOV", "K0"); ac("D8020"); ac("K200")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\spc.csv")

