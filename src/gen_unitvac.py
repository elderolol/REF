# UNIT VACUUM ??self-holding OUT conversion
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
al("UNIT VACUUM (Line 0)")
a("LD", "M19"); a("OUT", "T1"); ac("D4")
a("LD", "T1"); a("AND<=", "D160"); ac("D22"); a("OUT", "M102")
# M50 solenoid + M49 (gun vac solenoid also maintained during unit vac)
a("LD", "M19"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M102"); a("OUT", "M50")
a("LD", "M19"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M102"); a("OUT", "M49")
# Interlock fail
a("LD", "M19"); a("ANI", "M881"); a("SET", "M16"); a("RST", "M19"); a("RST", "M49"); a("RST", "M50")
# Vac switch mismatch
a("LD", "M19"); a("LD", "M914"); a("ANI", "M772"); a("LD", "M915"); a("ANI", "M773"); a("ORB",""); a("ANB",""); a("SET", "M819")
# Vac complete
a("LD", "M19"); a("AND", "T1"); a("AND<=", "D160"); ac("D22"); a("OUT", "M818")
a("LD", "M19"); a("AND", "T1"); a("AND<=", "D160"); ac("D22"); a("RST", "M19"); a("RST", "M49"); a("RST", "M50")
# Timeout
a("LD", "M19"); a("AND", "T1"); a("AND>", "D160"); ac("D22"); a("OUT", "T7"); ac("K100")
a("LD", "T7"); a("SET", "M819"); a("OUT", "M867"); a("SET", "M76"); a("RST", "M19"); a("RST", "M49"); a("RST", "M50")

al("UNIT VACUUM (Line 1)")
a("LD", "M35"); a("OUT", "T9"); ac("D34")
a("LD", "T9"); a("AND<=", "D172"); ac("D50"); a("OUT", "M103")
a("LD", "M35"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M103"); a("OUT", "M66")
a("LD", "M35"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M103"); a("OUT", "M65")
a("LD", "M35"); a("ANI", "M897"); a("SET", "M32"); a("RST", "M35"); a("RST", "M65"); a("RST", "M66")
a("LD", "M35"); a("LD", "M914"); a("ANI", "M788"); a("LD", "M915"); a("ANI", "M789"); a("ORB",""); a("ANB",""); a("SET", "M835")
a("LD", "M35"); a("AND", "T9"); a("AND<=", "D172"); ac("D50"); a("OUT", "M834")
a("LD", "M35"); a("AND", "T9"); a("AND<=", "D172"); ac("D50"); a("RST", "M35"); a("RST", "M65"); a("RST", "M66")
a("LD", "M35"); a("AND", "T9"); a("AND>", "D172"); ac("D50"); a("OUT", "T17"); ac("K100")
a("LD", "T17"); a("SET", "M835"); a("OUT", "M867"); a("SET", "M76"); a("RST", "M35"); a("RST", "M65"); a("RST", "M66")
a("END","")
wr("F:\\WorkSpace\\REF\\src\\unitvac.csv")

