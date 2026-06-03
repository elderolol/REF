# UNIT VACUUM -- self-holding for solenoids, 1:1 SET/RST for result flags.
# Step bits M19/M35 owned by MAIN. No SET/RST on MAIN bits.
# M818(OK L0), M819(NG L0), M834(OK L1), M835(NG L1): 1:1 or self-holding.
# M867 alarm latch handled by alarm.csv (self-holding based on M819/M835).
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
# M49/M65 solenoids, T7/T17 timers now consolidated in gen_gunvac.py for both steps

# M50 solenoid: unitvac only (L0)
a("LD", "M19"); a("ANI", "M881"); a("ANI", "T7"); a("ANI", "M102"); a("ANI", "M818"); a("ANI", "M819"); a("OUT", "M50")

# M818: OK result (1:1)
a("LD", "M19"); a("AND", "T1"); a("AND<=", "D160"); ac("D22"); a("SET", "M818")
a("LD", "M20"); a("OR", "M16"); a("RST", "M818")

# Timeout handled by gen_gunvac.py (shared T7/T17)

al("UNIT VACUUM (Line 1)")
a("LD", "M35"); a("OUT", "T9"); ac("D34")
a("LD", "T9"); a("AND<=", "D172"); ac("D50"); a("OUT", "M118")
# M66 solenoid: unitvac only (L1)
a("LD", "M35"); a("ANI", "M897"); a("ANI", "T17"); a("ANI", "M118"); a("ANI", "M834"); a("ANI", "M835"); a("OUT", "M66")

# M835: NG result L1 (self-holding)
a("LD", "M35"); a("LD", "M928"); a("ANI", "M788"); a("LD", "M929"); a("ANI", "M789"); a("ORB",""); a("ANB","")
a("LD", "T17"); a("ORB","")
a("OR", "M835"); a("ANI", "M36"); a("OUT", "M835")

# M834: OK result L1 (1:1)
a("LD", "M35"); a("AND", "T9"); a("AND<=", "D172"); ac("D50"); a("SET", "M834")
a("LD", "M36"); a("OR", "M32"); a("RST", "M834")

# T17 timeout handled by gen_gunvac.py (shared)

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\unitvac.csv")
