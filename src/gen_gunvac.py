# GUN VACUUM ? L1: M12, L2: M32
# Results: L1 M101(OK), M108(NG)  L2 M117(OK), M124(NG)
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

al("GUN VAC L1")
a("LD","M12"); a("OUT","M60"); a("OUT","T1"); ac("D2")
a("LD","M12"); a("AND","T1")
a("OUT","M101")    # Gun vac OK, timer only (no vacuum check)
# NG timeout: timer done + grace ¡æ NG
a("LD","M12"); a("AND","T1")
a("OUT","T15"); ac("K100")
a("LD","T15"); a("SET","M108"); a("SET","M310"); a("RST","M12"); a("RST","M60")
a("LD","M12"); a("ANI","M80"); a("SET","M108"); a("SET","M310"); a("RST","M12"); a("RST","M60")

al("GUN VAC L2")
a("LD","M32"); a("OUT","M70"); a("OUT","T7"); ac("D34")
a("LD","M32"); a("AND","T7")
a("OUT","M117")    # L2 Gun vac OK, timer only
# L2 NG timeout
a("LD","M32"); a("AND","T7")
a("OUT","T16"); ac("K100")
a("LD","T16"); a("SET","M124"); a("SET","M330"); a("RST","M32"); a("RST","M70")
a("LD","M32"); a("ANI","M90"); a("SET","M124"); a("SET","M330"); a("RST","M32"); a("RST","M70")

a("END","")
wr("C:\\WorkSpace\\REF\\src\\gunvac.csv")
