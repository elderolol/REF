# REFRIGERANT INJECTION ??self-holding OUT conversion
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

# ===== L0 REFRIG FAST =====
al("L0 REFRIG FAST")
# M52 timer coil = M21 step active + RST on completion
a("LD", "M21"); a("OUT", "M52")
# M96 solenoid = M21 step active + RST on completion  
a("LD", "M21"); a("OUT", "M96")
a("LD", "M21"); a("OUT", "T4"); ac("K3000")
# D62=1 (gas type 1) AND target reached ??refrig normal
a("LD", "M21"); a("LD=", "D62"); ac("K1"); a("AND>=", "D124"); ac("D10"); a("ANB",""); a("RST", "M52"); a("SET", "M22")
# D62=0 (gas type 0) AND target reached ??exhaust (skip refrig normal)
a("LD", "M21"); a("LD=", "D62"); ac("K0"); a("AND>=", "D124"); ac("D64"); a("ANB",""); a("RST", "M52"); a("RST", "M96"); a("SET", "M23")
# T4 timeout ??exhaust + alarm
a("LD", "M21"); a("AND", "T4"); a("RST", "M52"); a("RST", "M96"); a("SET", "M23"); a("SET", "M869")

# ===== L0 REFRIG NORMAL =====
al("L0 REFRIG NORMAL")
a("LD", "M22"); a("OUT", "M53")
a("LD", "M22"); a("OUT", "T5"); ac("K3000")
a("LD", "M22"); a("AND>=", "D124"); ac("D64"); a("RST", "M53"); a("RST", "M96"); a("SET", "M23")
a("LD", "M22"); a("AND", "T5"); a("RST", "M53"); a("RST", "M96"); a("SET", "M23"); a("SET", "M869")

# ===== L0 OIL FAST =====
al("L0 OIL FAST")
a("LD", "M25"); a("OUT", "M54")
a("LD", "M25"); a("OUT", "T6"); ac("K3000")
# D62=1 AND target reached ??oil normal
a("LD", "M25"); a("LD=", "D62"); ac("K1"); a("AND>=", "D124"); ac("D12"); a("ANB",""); a("RST", "M54"); a("SET", "M26")
# D124 >= D72 (oil target) ??repeat refrig fast
a("LD", "M25"); a("AND>=", "D124"); ac("D72"); a("RST", "M54"); a("SET", "M21")
# T6 timeout ??exhaust + alarm
a("LD", "M25"); a("AND", "T6"); a("RST", "M54"); a("SET", "M23"); a("SET", "M869")

# ===== L0 OIL NORMAL =====
al("L0 OIL NORMAL")
a("LD", "M26"); a("OUT", "M55")
a("LD", "M26"); a("OUT", "T6"); ac("K3000")
a("LD", "M26"); a("AND>=", "D124"); ac("D72"); a("RST", "M55"); a("SET", "M21")
a("LD", "M26"); a("AND", "T6"); a("RST", "M55"); a("SET", "M23"); a("SET", "M869")

# ===== L0 EXHAUST =====
al("L0 EXHAUST")
a("LD", "M23"); a("OUT", "M51")
a("LD", "M23"); a("OUT", "T3"); ac("D8")
a("LD", "M23"); a("AND", "T3"); a("RST", "M51"); a("SET", "M822"); a("RST", "M23")

# ===== L1 REFRIG FAST =====
al("L1 REFRIG FAST")
a("LD", "M37"); a("OUT", "M68")
a("LD", "M37"); a("OUT", "M98")
a("LD", "M37"); a("OUT", "T13"); ac("K3000")
# M872/M873 gas type check for L1
a("LD", "M37"); a("LD", "M872"); a("LD=", "D90"); ac("K1"); a("ANB",""); a("LD", "M873"); a("LD=", "D104"); ac("K1"); a("ANB",""); a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D10"); a("RST", "M68"); a("SET", "M38")
# Gas type 0
a("LD", "M37"); a("LD", "M872"); a("LD=", "D90"); ac("K0"); a("ANB",""); a("LD", "M873"); a("LD=", "D104"); ac("K0"); a("ANB",""); a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D64"); a("RST", "M68"); a("RST", "M98"); a("SET", "M39")
# Timeout
a("LD", "M37"); a("AND", "T13"); a("RST", "M68"); a("RST", "M98"); a("SET", "M39"); a("SET", "M869")

# ===== L1 REFRIG NORMAL =====
al("L1 REFRIG NORMAL")
a("LD", "M38"); a("OUT", "M69")
a("LD", "M38"); a("OUT", "T14"); ac("K3000")
a("LD", "M38"); a("AND>=", "D400"); ac("D64"); a("RST", "M69"); a("RST", "M98"); a("SET", "M39")
a("LD", "M38"); a("AND", "T14"); a("RST", "M69"); a("RST", "M98"); a("SET", "M39"); a("SET", "M869")

# ===== L1 OIL FAST =====
al("L1 OIL FAST")
a("LD", "M41"); a("OUT", "M70")
a("LD", "M41"); a("OUT", "T15"); ac("K3000")
a("LD", "M41"); a("LD", "M872"); a("LD=", "D90"); ac("K1"); a("ANB",""); a("LD", "M873"); a("LD=", "D104"); ac("K1"); a("ANB",""); a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D12"); a("RST", "M70"); a("SET", "M42")
a("LD", "M41"); a("AND>=", "D400"); ac("D72"); a("RST", "M70"); a("SET", "M37")
a("LD", "M41"); a("AND", "T15"); a("RST", "M70"); a("SET", "M39"); a("SET", "M869")

# ===== L1 OIL NORMAL =====
al("L1 OIL NORMAL")
a("LD", "M42"); a("OUT", "M71")
a("LD", "M42"); a("OUT", "T15"); ac("K3000")
a("LD", "M42"); a("AND>=", "D400"); ac("D72"); a("RST", "M71"); a("SET", "M37")
a("LD", "M42"); a("AND", "T15"); a("RST", "M71"); a("SET", "M39"); a("SET", "M869")

# ===== L1 EXHAUST =====
al("L1 EXHAUST")
a("LD", "M39"); a("OUT", "M67")
a("LD", "M39"); a("OUT", "T12"); ac("D38")
a("LD", "M39"); a("AND", "T12"); a("RST", "M67"); a("SET", "M838"); a("RST", "M39")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\refinj.csv")

