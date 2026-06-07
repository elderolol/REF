# OIL INJECTION — Per-GUN H+L solenoids
# GUN A: M65(OIL FAST), M66(OIL BASE)  GUN B: M75(OIL FAST), M76(OIL BASE)
# Results: M145(FAST OK), M146(BASE OK), M147(COMPLETE)
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

al("OIL FAST")
a("LD","M51"); a("AND","M210"); a("OUT","M65"); a("OUT","M66")
a("LD","M51"); a("AND","M211"); a("OUT","M75"); a("OUT","M76")
a("LD","M51"); a("OUT","T13"); ac("K3000")
# Count >= fast_stop
a("LD","M51")
a("LD","M210"); a("LDD>=","D180"); ac("D16")
a("LD","M211"); a("LDD>=","D180"); ac("D48")
a("ORB",""); a("ANB","")
a("AND","M210"); a("RST","M65"); a("SET","M145"); a("SET","M52")
a("LD","M51")
a("LD","M210"); a("LDD>=","D180"); ac("D16")
a("LD","M211"); a("LDD>=","D180"); ac("D48")
a("ORB",""); a("ANB","")
a("AND","M211"); a("RST","M75"); a("SET","M145"); a("SET","M52")
# Timeout
a("LD","M51"); a("AND","T13")
a("AND","M210"); a("RST","M65"); a("RST","M66"); a("SET","M350"); a("SET","M145"); a("SET","M53"); a("RST","M51")
a("LD","M51"); a("AND","T13")
a("AND","M211"); a("RST","M75"); a("RST","M76"); a("SET","M350"); a("SET","M145"); a("SET","M53"); a("RST","M51")

al("OIL BASE")
a("LD","M52"); a("AND","M210"); a("OUT","M66")
a("LD","M52"); a("AND","M211"); a("OUT","M76")
a("LD","M52"); a("OUT","T14"); ac("K3000")
# Count >= target
a("LD","M52")
a("LD","M210"); a("LDD>=","D180"); ac("D18")
a("LD","M211"); a("LDD>=","D180"); ac("D50")
a("ORB",""); a("ANB","")
a("AND","M210"); a("RST","M66"); a("SET","M146"); a("SET","M53")
a("LD","M52")
a("LD","M210"); a("LDD>=","D180"); ac("D18")
a("LD","M211"); a("LDD>=","D180"); ac("D50")
a("ORB",""); a("ANB","")
a("AND","M211"); a("RST","M76"); a("SET","M146"); a("SET","M53")
# Timeout
a("LD","M52"); a("AND","T14")
a("AND","M210"); a("RST","M66"); a("SET","M350"); a("SET","M146"); a("SET","M53"); a("RST","M52")
a("LD","M52"); a("AND","T14")
a("AND","M211"); a("RST","M76"); a("SET","M350"); a("SET","M146"); a("SET","M53"); a("RST","M52")
# Tolerance
a("LD","M52")
a("LD","M210"); a("LDD>","D180"); ac("D20")
a("LD","M211"); a("LDD>","D180"); ac("D52")
a("ORB",""); a("SET","M351")    # oil amount NG (over)
a("LD","M53"); a("AND","M210"); a("LDD<","D180"); ac("D18"); a("SET","M351")  # oil amount NG (under)
a("LD","M53"); a("AND","M211"); a("LDD<","D180"); ac("D50"); a("SET","M351")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\oilinj.csv")
