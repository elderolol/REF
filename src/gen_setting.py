# SETTING — Config sync, line count, operating mode, HMI parameters
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

al("CONFIG SYNC")
# Always-on sync for critical settings
a("LD","M0"); a("MOV","D2"); ac("D2")     # L1 gun vac time
a("LD","M0"); a("MOV","D4"); ac("D4")     # L1 unit vac time
a("LD","M0"); a("MOV","D6"); ac("D6")     # L1 vac check time
a("LD","M0"); a("MOV","D8"); ac("D8")     # L1 exhaust time
a("LD","M0"); a("MOV","D22"); ac("D22")   # L2 gun vac time
a("LD","M0"); a("MOV","D24"); ac("D24")   # L2 unit vac time
a("LD","M0"); a("MOV","D26"); ac("D26")   # L2 vac check time
a("LD","M0"); a("MOV","D28"); ac("D28")   # L2 exhaust time

a("END","")
wr("F:\\WorkSpace\\REF\\src\\setting.csv")
