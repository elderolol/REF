# AD — Analog EU scaling (raw → engineering units)
# D100 = Pressure L1, D102 = Temperature L1, D104-D105 = Vacuum L1 (32-bit)
# D110 = Pressure L2, D112 = Temperature L2, D114-D115 = Vacuum L2
# D120 = Temperature L3
# Actual EU destinations (for step logic): D44-D45(L1 press), D46-D47(L1 temp), D48-D49(L1 vac)
# D54-D55(L2 press), D56-D57(L2 temp), D58-D59(L2 vac), D60-D61(L3 temp)
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

al("ANALOG RAW TO EU")
# L1 Pressure: raw D100 → scaled → D44
a("LD","M0"); a("MOV","D100"); ac("D26")
# L1 Temperature: raw D102 → scaled → D46
a("LD","M0"); a("MOV","D102"); ac("D28")
# L1 Vacuum: raw D104-D105 → scaled → D48-D49
a("LD","M0"); a("DMOV","D104"); ac("D30")
# L2 Pressure
a("LD","M0"); a("MOV","D110"); ac("D58")
# L2 Temperature
a("LD","M0"); a("MOV","D112"); ac("D60")
# L2 Vacuum
a("LD","M0"); a("DMOV","D114"); ac("D62")
# L3 Temperature
a("LD","M0"); a("MOV","D120"); ac("D60")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\ad.csv")
