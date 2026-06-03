# GUN VACUUM -- self-holding for solenoids, 1:1 SET/RST for result flags.
# Step bits M18/M34 owned by MAIN. No SET/RST on MAIN bits.
# M76 buzzer handled by alarm.csv (no double-coil).
# M816(OK L0), M817(NG L0), M832(OK L1), M833(NG L1): 1:1 SET/RST.
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
a("LD", "T0"); a("AND<=", "D160"); ac("D22"); a("OUT", "M100")
# M49 solenoid: follows M18 (gunvac) OR M19 (unitvac), OFF on completion
a("LD", "M18"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M100"); a("ANI", "M816"); a("ANI", "M817")
a("LD", "M19"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M102"); a("ANI", "M818"); a("ANI", "M819")
a("ORB","")
a("OUT", "M49")

# M817: NG result (self-holding with all trigger conditions)
a("LD", "M18"); a("LD", "M928"); a("ANI", "M772"); a("LD", "M929"); a("ANI", "M773"); a("ORB",""); a("ANB","")
a("LD", "T7"); a("ORB","")
a("OR", "M817"); a("ANI", "M19"); a("OUT", "M817")

# M816: OK result (1:1: SET here, RST on M19/M16)
a("LD", "M18"); a("AND", "T0"); a("AND<=", "D160"); ac("D22"); a("SET", "M816")
a("LD", "M19"); a("OR", "M16"); a("RST", "M816")

# Timeout timer T7: gunvac L0 OR unitvac L0 timeout
a("LD", "M18"); a("AND", "T0"); a("AND>", "D160"); ac("D22")
a("LD", "M19"); a("AND", "T1"); a("AND>", "D160"); ac("D22")
a("ORB","")
a("OUT", "T7"); ac("K100")

al("GUN VACUUM (Line 1)")
a("LD", "M34"); a("OUT", "T8"); ac("D32")
a("LD", "T8"); a("AND<=", "D172"); ac("D50"); a("OUT", "M116")
a("LD", "M34"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M116"); a("ANI", "M832"); a("ANI", "M833")
a("LD", "M35"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M118"); a("ANI", "M834"); a("ANI", "M835")
a("ORB","")
a("OUT", "M65")

# M833: NG result L1 (self-holding)
a("LD", "M34"); a("LD", "M928"); a("ANI", "M788"); a("LD", "M929"); a("ANI", "M789"); a("ORB",""); a("ANB","")
a("LD", "T17"); a("ORB","")
a("OR", "M833"); a("ANI", "M35"); a("OUT", "M833")

# M832: OK result L1 (1:1)
a("LD", "M34"); a("AND", "T8"); a("AND<=", "D172"); ac("D50"); a("SET", "M832")
a("LD", "M35"); a("OR", "M32"); a("RST", "M832")

# Timeout timer T17: gunvac L1 OR unitvac L1 timeout
a("LD", "M34"); a("AND", "T8"); a("AND>", "D172"); ac("D50")
a("LD", "M35"); a("AND", "T9"); a("AND>", "D172"); ac("D50")
a("ORB","")
a("OUT", "T17"); ac("K100")

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\gunvac.csv")
