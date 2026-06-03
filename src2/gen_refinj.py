# REFRIGERANT INJECTION -- all outputs self-holding, 1:1 SET/RST for pulse flags.
# Step bits M21-M24 owned by MAIN step machine (self-holding). No double-coil.
# M822 (L0 exhaust complete), M838 (L1 exhaust complete): self-holding.
# M320 (L0 timeout), M336 (L1 timeout): self-holding alarm triggers.
# M340 (L0 oil restart), M356 (L1 oil restart): self-holding request flags.
# M25/M26 (L0 oil sub-cycles), M41/M42 (L1 oil sub-cycles): self-holding.
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
a("LD", "M21"); a("OUT", "M52")
a("LD", "M21"); a("OUT", "M96")
a("LD", "M21"); a("OUT", "T4"); ac("K3000")

# ===== L0 REFRIG NORMAL =====
al("L0 REFRIG NORMAL")
a("LD", "M22"); a("OUT", "M53")
a("LD", "M22"); a("OUT", "T5"); ac("K3000")

# ===== L0 OIL FAST (M25 self-holding) =====
al("L0 OIL FAST")
# M25 self-holding: enters from M23, exits on complete/timeout
a("LD", "M23"); a("ANI", "T3"); a("ANI", "M822")
a("OR", "M25")
a("ANI", "M26"); a("ANI", "M340"); a("ANI", "M320")
a("ANI", "M301"); a("ANI", "M304")
a("OUT", "M25")
a("LD", "M25"); a("OUT", "M54")
# T6 shared timer: M25 (oil fast) OR M26 (oil normal)
a("LD", "M25"); a("OR", "M26"); a("OUT", "T6"); ac("K3000")

# ===== L0 OIL NORMAL (M26 self-holding) =====
al("L0 OIL NORMAL")
# M26 self-holding: enters when M25 AND gas_type1 AND oil_target
a("LD", "M25"); a("LD=", "D62"); ac("K1"); a("AND>=", "D124"); ac("D12"); a("ANB","")
a("OR", "M26")
a("ANI", "M340"); a("ANI", "M320"); a("ANI", "M301"); a("ANI", "M304")
a("OUT", "M26")
a("LD", "M26"); a("OUT", "M55")
# T6 handled by shared rung (M25 OR M26 OUT T6)

# ===== L0 EXHAUST =====
al("L0 EXHAUST")
# Outputs follow MAIN step bit M23
a("LD", "M23"); a("OUT", "M51")
# T3 exhaust timer handled by MAIN (EXHAUST TIMER section)

# ===== L1 REFRIG FAST =====
al("L1 REFRIG FAST")
a("LD", "M37"); a("OUT", "M68")
a("LD", "M37"); a("OUT", "M112")
a("LD", "M37"); a("OUT", "T13"); ac("K3000")

# ===== L1 REFRIG NORMAL =====
al("L1 REFRIG NORMAL")
a("LD", "M38"); a("OUT", "M69")
a("LD", "M38"); a("OUT", "T14"); ac("K3000")

# ===== L1 OIL FAST (M41 self-holding) =====
al("L1 OIL FAST")
a("LD", "M39"); a("ANI", "T12"); a("ANI", "M838")
a("OR", "M41")
a("ANI", "M42"); a("ANI", "M356"); a("ANI", "M336")
a("ANI", "M317"); a("ANI", "M304")
a("OUT", "M41")
a("LD", "M41"); a("OUT", "M70")
# T15 shared timer: M41 (oil fast) OR M42 (oil normal)
a("LD", "M41"); a("OR", "M42"); a("OUT", "T15"); ac("K3000")

# ===== L1 OIL NORMAL (M42 self-holding) =====
al("L1 OIL NORMAL")
a("LD", "M41")
a("LD", "M872"); a("LD=", "D90"); ac("K1"); a("ANB","")
a("LD", "M873"); a("LD=", "D104"); ac("K1"); a("ANB","")
a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D12")
a("OR", "M42")
a("ANI", "M356"); a("ANI", "M336"); a("ANI", "M317"); a("ANI", "M304")
a("OUT", "M42")
a("LD", "M42"); a("OUT", "M71")
# T15 handled by shared rung (M41 OR M42 OUT T15)

# ===== L1 EXHAUST =====
al("L1 EXHAUST")
a("LD", "M39"); a("OUT", "M67")
a("LD", "M39"); a("OUT", "T12"); ac("D38")

# ===== COMPLETION FLAG: M822 (L0 exhaust complete, self-holding) =====
al("COMPLETION L0 (M822)")
# M822 self-holding: OR of all completion conditions, consumed by MAIN M24
# M21 fast complete (gas1+target)
a("LD", "M21"); a("LD=", "D62"); ac("K1"); a("AND>=", "D124"); ac("D10"); a("ANB","")
# M21 skip exhaust (gas0+target)
a("LD", "M21"); a("LD=", "D62"); ac("K0"); a("AND>=", "D124"); ac("D64"); a("ANB",""); a("ORB","")
# M21 timeout
a("LD", "M21"); a("AND", "T4"); a("ORB","")
# M22 normal complete
a("LD", "M22"); a("AND>=", "D124"); ac("D64"); a("ORB","")
# M22 timeout
a("LD", "M22"); a("AND", "T5"); a("ORB","")
# M25 timeout
a("LD", "M25"); a("AND", "T6"); a("ORB","")
# M26 timeout
a("LD", "M26"); a("AND", "T6"); a("ORB","")
# M23 exhaust timer done
a("LD", "M23"); a("AND", "T3"); a("ORB","")
# Self-hold, release on M24
a("OR", "M822"); a("ANI", "M24"); a("OUT", "M822")

# ===== COMPLETION FLAG: M838 (L1 exhaust complete, self-holding) =====
al("COMPLETION L1 (M838)")
# M37 fast complete (gas1+target)
a("LD", "M37")
a("LD", "M872"); a("LD=", "D90"); ac("K1"); a("ANB","")
a("LD", "M873"); a("LD=", "D104"); ac("K1"); a("ANB","")
a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D10")
# M37 skip exhaust (gas0+target)
a("LD", "M37")
a("LD", "M872"); a("LD=", "D90"); ac("K0"); a("ANB","")
a("LD", "M873"); a("LD=", "D104"); ac("K0"); a("ANB","")
a("ORB",""); a("ANB","")
a("AND>=", "D400"); ac("D64"); a("ORB","")
# M37 timeout
a("LD", "M37"); a("AND", "T13"); a("ORB","")
# M38 normal complete
a("LD", "M38"); a("AND>=", "D400"); ac("D64"); a("ORB","")
# M38 timeout
a("LD", "M38"); a("AND", "T14"); a("ORB","")
# M41 timeout
a("LD", "M41"); a("AND", "T15"); a("ORB","")
# M42 timeout
a("LD", "M42"); a("AND", "T15"); a("ORB","")
# M39 exhaust timer done
a("LD", "M39"); a("AND", "T12"); a("ORB","")
# Self-hold, release on M40
a("OR", "M838"); a("ANI", "M40"); a("OUT", "M838")

# ===== ALARM TRIGGERS: M320 (L0 timeout), M336 (L1 timeout) self-holding =====
al("TIMEOUT ALARM TRIGGERS")
# M320 self-holding: any L0 timeout
a("LD", "M21"); a("AND", "T4")
a("LD", "M22"); a("AND", "T5"); a("ORB","")
a("LD", "M25"); a("AND", "T6"); a("ORB","")
a("LD", "M26"); a("AND", "T6"); a("ORB","")
a("OR", "M320"); a("ANI", "M1027"); a("OUT", "M320")

# M336 self-holding: any L1 timeout
a("LD", "M37"); a("AND", "T13")
a("LD", "M38"); a("AND", "T14"); a("ORB","")
a("LD", "M41"); a("AND", "T15"); a("ORB","")
a("LD", "M42"); a("AND", "T15"); a("ORB","")
a("OR", "M336"); a("ANI", "M1027"); a("OUT", "M336")

# ===== OIL RESTART FLAGS: M340 (L0), M356 (L1) self-holding =====
al("OIL RESTART FLAGS")
# M340: L0 oil target reached → restart refrig. ON when M25+M26 oil_done, OFF when M21 starts.
a("LD", "M25"); a("AND>=", "D124"); ac("D72")
a("LD", "M26"); a("AND>=", "D124"); ac("D72"); a("ORB","")
a("OR", "M340"); a("ANI", "M21"); a("OUT", "M340")

# M356: L1 oil target reached → restart refrig.
a("LD", "M41"); a("AND>=", "D400"); ac("D72")
a("LD", "M42"); a("AND>=", "D400"); ac("D72"); a("ORB","")
a("OR", "M356"); a("ANI", "M37"); a("OUT", "M356")

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\refinj.csv")
