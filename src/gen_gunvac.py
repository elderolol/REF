# GUN VACUUM ??self-holding OUT conversion
# Results: M816/M832 OUT (single condition), M817/M833 SET (multi-condition), M866 OUT (alarm.csv self-holds)
# Solenoids M49/M65: OUT (step tracking) + RST (immediate off)
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
al("GUN VACUUM (Line 0)")
a("LD", "M18"); a("OUT", "T0"); ac("D2")
# vac_complete flag for M49 tracking
a("LD", "T0"); a("AND<=", "D160"); ac("D22"); a("OUT", "M100")
# M49 solenoid: OUT follows step state minus completion
a("LD", "M18"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M100"); a("OUT", "M49")
# Interlock fail ??restart init
a("LD", "M18"); a("ANI", "M881"); a("SET", "M16"); a("RST", "M18"); a("RST", "M49")
# Vac switch mismatch ??M817 NG result (persistent, let alarm.csv capture)
a("LD", "M18"); a("LD", "M914"); a("ANI", "M772"); a("LD", "M915"); a("ANI", "M773"); a("ORB",""); a("ANB",""); a("SET", "M817")
# Vac complete ??M816 OK result (one-shot, MAIN captures)
a("LD", "M18"); a("AND", "T0"); a("AND<=", "D160"); ac("D22"); a("OUT", "M816")
a("LD", "M18"); a("AND", "T0"); a("AND<=", "D160"); ac("D22"); a("RST", "M18"); a("RST", "M49")
# Timeout
a("LD", "M18"); a("AND", "T0"); a("AND>", "D160"); ac("D22"); a("OUT", "T7"); ac("K100")
a("LD", "T7"); a("SET", "M817"); a("OUT", "M866"); a("SET", "M76"); a("RST", "M18"); a("RST", "M49")

al("GUN VACUUM (Line 1)")
a("LD", "M34"); a("OUT", "T8"); ac("D32")
a("LD", "T8"); a("AND<=", "D172"); ac("D50"); a("OUT", "M101")
a("LD", "M34"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M101"); a("OUT", "M65")
a("LD", "M34"); a("ANI", "M897"); a("SET", "M32"); a("RST", "M34"); a("RST", "M65")
a("LD", "M34"); a("LD", "M914"); a("ANI", "M788"); a("LD", "M915"); a("ANI", "M789"); a("ORB",""); a("ANB",""); a("SET", "M833")
a("LD", "M34"); a("AND", "T8"); a("AND<=", "D172"); ac("D50"); a("OUT", "M832")
a("LD", "M34"); a("AND", "T8"); a("AND<=", "D172"); ac("D50"); a("RST", "M34"); a("RST", "M65")
a("LD", "M34"); a("AND", "T8"); a("AND>", "D172"); ac("D50"); a("OUT", "T17"); ac("K100")
a("LD", "T17"); a("SET", "M833"); a("OUT", "M866"); a("SET", "M76"); a("RST", "M34"); a("RST", "M65")
a("END","")
wr("F:\\WorkSpace\\REF\\src\\gunvac.csv")

