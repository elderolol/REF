# VAC CHECK ??self-holding OUT conversion
# Result latches use OUT (MAIN's self-holding captures one-shot)
# Alarm triggers use OUT (alarm.csv self-holds)
# No explicit step RST needed ??MAIN's step self-holding handles release
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
al("VAC CHECK L0")

# Save initial vacuum, start timer
a("LD", "M20"); a("DMOV", "D160"); ac("D300")
a("LD", "M20"); a("OUT", "T2"); ac("D6")
# Delta = initial - current
a("LD", "M20"); a("D-", "D300"); ac("D160"); ac("D304")

# Interlock: M775 ON at entry ??NG (immediate, no timer wait)
# M878: alarm condition (alarm.csv self-holds: LD M0 OR M878 ANI M750)
a("LD", "M20"); a("AND", "M775"); a("OUT", "M878")
# M821: NG result (M775 OR leak) ??ORB for two conditions
a("LD", "M20"); a("AND", "M775")
a("LD", "M20"); a("AND>", "D304"); ac("D24"); a("ORB",""); a("OUT", "M821")
# M868: alarm trigger only on leak (not on interlock)
a("LD", "M20"); a("AND>", "D304"); ac("D24"); a("OUT", "M868")

# OK: timer expired AND vacuum stable, NOT interlock
a("LD", "M20"); a("ANI", "M775"); a("AND", "T2"); a("AND<=", "D304"); ac("K5"); a("OUT", "M820")

al("VAC CHECK L1")
a("LD", "M36"); a("DMOV", "D172"); ac("D306")
a("LD", "M36"); a("OUT", "T11"); ac("D36")
a("LD", "M36"); a("D-", "D306"); ac("D172"); ac("D308")

# Interlock
a("LD", "M36"); a("AND", "M791"); a("OUT", "M879")
a("LD", "M36"); a("AND", "M791")
a("LD", "M36"); a("AND>", "D308"); ac("D52"); a("ORB",""); a("OUT", "M837")
# M868 also for L1 leak
a("LD", "M36"); a("AND>", "D308"); ac("D52"); a("OUT", "M868")

# OK
a("LD", "M36"); a("ANI", "M791"); a("AND", "T11"); a("AND<=", "D308"); ac("K5"); a("OUT", "M836")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\vacchec.csv")

