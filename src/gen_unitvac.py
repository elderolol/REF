# UNIT VACUUM ? L1: M13, L2: M33
# Results: L1 M102(OK), M109(NG)  L2 M118(OK), M125(NG)
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

al("UNIT VAC L1")
a("LD","M13"); a("OUT","M60"); a("OUT","M61"); a("OUT","T2"); ac("D4")
a("LD","M13"); a("AND","T2"); a("LDD<=","D30"); ac("D22")
a("OUT","M102")    # Unit vac OK, step released by warmup chain
a("LD","M13"); a("AND","T2"); a("LDD>","D30"); ac("D22")
a("OUT","T15"); ac("K100")
a("LD","T15"); a("SET","M109"); a("SET","M311"); a("RST","M13"); a("RST","M60"); a("RST","M61")
a("LD","M13"); a("ANI","M80"); a("SET","M109"); a("SET","M311"); a("RST","M13"); a("RST","M60"); a("RST","M61")

al("UNIT VAC L2")
a("LD","M33"); a("OUT","M70"); a("OUT","M71"); a("OUT","T8"); ac("D36")
a("LD","M33"); a("AND","T8"); a("LDD<=","D62"); ac("D54")
a("OUT","M118")    # L2 Unit vac OK, step released by warmup chain
a("LD","M33"); a("AND","T8"); a("LDD>","D62"); ac("D54")
a("OUT","T16"); ac("K100")
a("LD","T16"); a("SET","M125"); a("SET","M331"); a("RST","M33"); a("RST","M70"); a("RST","M71")
a("LD","M33"); a("ANI","M90"); a("SET","M125"); a("SET","M331"); a("RST","M33"); a("RST","M70"); a("RST","M71")

a("END","")
wr("C:\\WorkSpace\\REF\\src\\unitvac.csv")
