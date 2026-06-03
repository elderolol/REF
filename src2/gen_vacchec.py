# VAC CHECK — result flags only, no double-coil with alarm.csv.
# M820(OK)/M821(NG)/M836(OK)/M837(NG): result flags checked by MAIN + alarm.csv.
# Alarm latches M868/M878 handled entirely by alarm.csv (self-holding).
# M868 triggered by M821/M837 → alarm.csv self-holds.
# M878 (interlock alarm) removed from here — alarm.csv self-holds it.
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

# M821: NG result (M775 interlock OR D304 leak > D24)
a("LD", "M20"); a("AND", "M775")
a("LD", "M20"); a("AND>", "D304"); ac("D24"); a("ORB",""); a("OUT", "M821")
# M821 RST when step exits (let MAIN step machine transition consume it)
a("LD", "M21"); a("RST", "M821")

# OK: timer expired AND vacuum stable, NOT interlock
a("LD", "M20"); a("ANI", "M775"); a("AND", "T2"); a("AND<=", "D304"); ac("K5"); a("OUT", "M820")
a("LD", "M21"); a("RST", "M820")

al("VAC CHECK L1")
a("LD", "M36"); a("DMOV", "D172"); ac("D306")
a("LD", "M36"); a("OUT", "T11"); ac("D36")
a("LD", "M36"); a("D-", "D306"); ac("D172"); ac("D308")

# Interlock OR leak → NG
a("LD", "M36"); a("AND", "M791")
a("LD", "M36"); a("AND>", "D308"); ac("D52"); a("ORB",""); a("OUT", "M837")
a("LD", "M37"); a("RST", "M837")

# OK
a("LD", "M36"); a("ANI", "M791"); a("AND", "T11"); a("AND<=", "D308"); ac("K5"); a("OUT", "M836")
a("LD", "M37"); a("RST", "M836")

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\vacchec.csv")
