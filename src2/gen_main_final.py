# MAIN step machine ??ALL self-holding.
# SET/RST only allowed 1:1 for pulse flags.
# HMI buttons: momentary, used directly. PLS only for complement toggle.
# Stop/EMG/NG alarm: integrated into step self-holding (ANI or OR chain).
# Complex conditions: grouped into intermediate bits M312~M317 for readability.
#
# Step map:
#   L0: M16(init) → M17(wait) → M18(gunvac) → M19(unitvac) → M20(vacchec) → M21+M22(parallel, refrig) → M23(exhaust) → M24(complete)
#   L1: M32(init) → M33(wait) → M34(gunvac) → M35(unitvac) → M36(vacchec) → M37+M38(parallel, refrig) → M39(exhaust) → M40(complete)
st = 0; lines = []
def a(i,d): global st; lines.append(f'"{st}"\t""\t"{i}"\t"{d}"\t""\t""\t""'); st += 1
def ac(d): lines.append(f'""\t""\t""\t"{d}"\t""\t""\t""')
def al(t): global st; lines.append(f'"{st}"\t">> {t}"\t""\t""\t""\t""\t""'); st += 1
def hd(n):
    lines.append(f'"{n}"')
    lines.append('"PLC Information:"\t"QCPU (Q mode) Q03UDV"')
    lines.append('"Step No."\t"Line Statement"\t"Instruction"\t"I/O(Device)"\t"Blank"\t"PI Statement"\t"Note"')
def wr(p):
    c = "\r\n".join(lines) + "\r\n"
    with open(p, "wb") as f: f.write(b'\xff\xfe'); f.write(c.encode('utf-16-le'))

hd("REF_self_holding")

# ===== MODE CONTROL (complement toggle with PLS edge detect) =====
al("MODE CONTROL")
a("LD", "M1038"); a("PLS", "M600")
# SET/RST flip-flop (1:1, atomic) — prevents 1-scan M801+M802 overlap
a("LD", "M600"); a("AND", "M802"); a("SET", "M801"); a("RST", "M802")
a("LD", "M600"); a("AND", "M801"); a("SET", "M802"); a("RST", "M801")
# Direction flip self-holding
a("LD", "M1024"); a("OR", "M912"); a("ANI", "M1025"); a("OUT", "M912")
a("LD", "M1025"); a("OR", "M913"); a("ANI", "M1024"); a("OUT", "M913")
a("LD", "M1032"); a("OR", "M928"); a("ANI", "M1033"); a("OUT", "M928")
a("LD", "M1033"); a("OR", "M929"); a("ANI", "M1032"); a("OUT", "M929")
# M1026 complement toggle
a("LD", "M1026"); a("PLS", "M601")
a("LD", "M601"); a("ANI", "M916"); a("LD", "M916"); a("ANI", "M601"); a("ORB",""); a("OUT", "M916")

# ===== INTERLOCK CHECK (grouped) =====
al("INTERLOCK CHECK")
a("LD", "M881"); a("AND", "M882"); a("AND", "M883"); a("AND", "M884"); a("AND", "M885"); a("OUT", "M880")
a("LD", "M897"); a("AND", "M898"); a("AND", "M899"); a("AND", "M900"); a("AND", "M901"); a("OUT", "M896")

# ===== STOP/EMG LATCHES (self-holding) =====
al("STOP / EMG LATCH")
# M301: STOP latch L0. ON when M414 pressed, OFF when M16 init reached.
a("LD", "M1044"); a("OR", "M301"); a("ANI", "M16"); a("OUT", "M301")
# M317: STOP latch L1.
a("LD", "M1044"); a("OR", "M317"); a("ANI", "M32"); a("OUT", "M317")
# M330: EMG release permit. ON only when M303 restored AND reset pressed.
a("LD", "M303"); a("AND", "M1027"); a("OUT", "M330")
# M304: EMERGENCY latch. Manual reset required (IEC 60204-1).
a("LDI", "M303"); a("OR", "M304"); a("ANI", "M330"); a("OUT", "M304")

# M316: L0 interlock fail (self-holding). ON when any interlock opens during M18/M19.
# OFF when init M16 reached.
a("LD", "M18"); a("ANI", "M881")
a("LD", "M18"); a("ANI", "M882"); a("ORB","")
a("LD", "M18"); a("ANI", "M883"); a("ORB","")
a("LD", "M18"); a("ANI", "M884"); a("ORB","")
a("LD", "M18"); a("ANI", "M885"); a("ORB","")
a("LD", "M19"); a("ANI", "M881"); a("ORB","")
a("LD", "M19"); a("ANI", "M882"); a("ORB","")
a("LD", "M19"); a("ANI", "M883"); a("ORB","")
a("LD", "M19"); a("ANI", "M884"); a("ORB","")
a("LD", "M19"); a("ANI", "M885"); a("ORB","")
a("OR", "M316")
a("ANI", "M16")
a("OUT", "M316")
# M332: L1 interlock fail (self-holding). ON when any interlock opens during M34/M35.
# OFF when init M32 reached.
a("LD", "M34"); a("ANI", "M897")
a("LD", "M34"); a("ANI", "M898"); a("ORB","")
a("LD", "M34"); a("ANI", "M899"); a("ORB","")
a("LD", "M34"); a("ANI", "M900"); a("ORB","")
a("LD", "M34"); a("ANI", "M901"); a("ORB","")
a("LD", "M35"); a("ANI", "M897"); a("ORB","")
a("LD", "M35"); a("ANI", "M898"); a("ORB","")
a("LD", "M35"); a("ANI", "M899"); a("ORB","")
a("LD", "M35"); a("ANI", "M900"); a("ORB","")
a("LD", "M35"); a("ANI", "M901"); a("ORB","")
a("OR", "M332")
a("ANI", "M32")
a("OUT", "M332")

# ===== NG ALARM GROUP BITS (intermediate for readability) =====
al("NG ALARM GROUP")
l0_al_devs = ["M864","M865","M866","M867","M868","M869","M872","M873","M874","M875","M876"]
l1_al_devs = ["M864","M865","M866","M867","M868","M869","M872","M873","M874","M877","M878","M879"]
# M312: L0 NG alarm OR
a("LD", l0_al_devs[0])
for d in l0_al_devs[1:]: a("OR", d)
a("OUT", "M312")
# M328: L1 NG alarm OR
a("LD", l1_al_devs[0])
for d in l1_al_devs[1:]: a("OR", d)
a("OUT", "M328")

# ===== MANUAL FUNCTION ENTRY (direct HMI momentary + START) =====
# No intermediate READY flags. HMI buttons M1039-M1042 are function selects.
# Combined with START (M413 L0 / M415 L1) in step self-holding ORB blocks.

# ===== STEP MACHINE L0 (reverse order: releasing step before released step) =====
# Order: M24?�M23?�M21?�M22?�M20?�M19?�M18?�M17?�M16
# This ensures no one-scan overlap on step transitions.
al("STEP L0")

# M24 (complete): needs M23 AND T3 (exhaust timer)
a("LD", "M23"); a("AND", "T3")
a("OR", "M24")
a("ANI", "M16"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M24")

# Cycle complete pulse M824 (SET only here, 1:1 if RST'd elsewhere)
a("LD", "M23"); a("AND", "T3"); a("SET", "M824")
# Result code
a("LD", "M24"); a("MOV", "K1"); ac("D7012")

# M23 (exhaust): needs (M21 OR M22) AND M822 (exhaust flag)
a("LD", "M21"); a("OR", "M22"); a("AND", "M822")
a("OR", "M23")
a("ANI", "M24"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M23")

# M21 (refrig/main): M20+M820 OR M340(oil restart) OR function btn+start
a("LD", "M20"); a("AND", "M820")
a("OR", "M340")
a("LD", "M1042"); a("AND", "M1043"); a("ORB","")
a("OR", "M21")
a("ANI", "M23"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M21")

# M22 (parallel branch): same trigger as M21 + function btn+start
a("LD", "M20"); a("AND", "M820")
a("LD", "M1042"); a("AND", "M1043"); a("ORB","")
a("OR", "M22")
a("ANI", "M23"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M22")

# M20 (vacchec): needs M19 + M818 (unitvac OK) OR function btn+start
a("LD", "M19"); a("AND", "M818")
a("LD", "M1041"); a("AND", "M1043"); a("ORB","")
a("OR", "M20")
a("ANI", "M21"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M20")

# M19 (unitvac): needs M18 + M816 (gunvac OK) OR function btn+start
a("LD", "M18"); a("AND", "M816")
a("LD", "M1040"); a("AND", "M1043"); a("ORB","")
a("OR", "M19")
a("ANI", "M316"); a("ANI", "M20"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M19")

# M18 (gunvac): from M17 (auto) OR function btn+start (manual)
a("LD", "M17")
a("LD", "M1039"); a("AND", "M1043"); a("ORB","")
a("OR", "M18")
a("ANI", "M316"); a("ANI", "M19"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M18")

# M17 (wait): need M16 + start_conditions (L0, L50 interlock, M413, L1)
a("LD", "M16"); a("AND", "M800"); a("AND", "M880"); a("AND", "M1043"); a("AND", "M801")
a("OR", "M17")
a("ANI", "M18"); a("ANI", "M301"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M17")

# M16 (init)
a("LD", "M24"); a("OR", "M301"); a("OR", "M312"); a("OR", "M316"); a("OR", "M16")
a("ANI", "M17"); a("ANI", "M304")
for d in l0_al_devs: a("ANI", d)
a("OUT", "M16")

# ===== STEP MACHINE L1 (reverse order: releasing step before released step) =====
al("STEP L1")

# M40 (complete)
a("LD", "M39"); a("AND", "T3")
a("OR", "M40")
a("ANI", "M32"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M40")

# Cycle complete pulse M840
a("LD", "M39"); a("AND", "T3"); a("SET", "M840")
a("LD", "M40"); a("MOV", "K1"); ac("D8012")

# M39 (exhaust)
a("LD", "M37"); a("OR", "M38"); a("AND", "M838")
a("OR", "M39")
a("ANI", "M40"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M39")

# M37 (refrig L1): M36+M836 OR M356(oil restart) OR function btn+start
a("LD", "M36"); a("AND", "M836")
a("OR", "M356")
a("LD", "M1042"); a("AND", "M1045"); a("ORB","")
a("OR", "M37")
a("ANI", "M39"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M37")

# M38 (parallel L1): same trigger as M37 + function btn+start
a("LD", "M36"); a("AND", "M836")
a("LD", "M1042"); a("AND", "M1045"); a("ORB","")
a("OR", "M38")
a("ANI", "M39"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M38")

# M36 (vacchec L1): needs M35 + M834 (unitvac OK) OR function btn+start
a("LD", "M35"); a("AND", "M834")
a("LD", "M1041"); a("AND", "M1045"); a("ORB","")
a("OR", "M36")
a("ANI", "M37"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M36")

# M35 (unitvac L1): needs M34 + M832 (gunvac OK) OR function btn+start
a("LD", "M34"); a("AND", "M832")
a("LD", "M1040"); a("AND", "M1045"); a("ORB","")
a("OR", "M35")
a("ANI", "M332"); a("ANI", "M36"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M35")

# M34 (gunvac L1): from M33 (auto) OR function btn+start (manual)
a("LD", "M33")
a("LD", "M1039"); a("AND", "M1045"); a("ORB","")
a("OR", "M34")
a("ANI", "M332"); a("ANI", "M35"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M34")

# M33 (wait)
a("LD", "M32"); a("AND", "M800"); a("AND", "M896"); a("AND", "M1045"); a("AND", "M801")
a("OR", "M33")
a("ANI", "M34"); a("ANI", "M317"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M33")

# M32 (init): SET by M40(complete), M317(stop), M328(NG alarm), M332(interlock fail)
a("LD", "M40"); a("OR", "M317"); a("OR", "M328"); a("OR", "M332"); a("OR", "M32")
a("ANI", "M33"); a("ANI", "M304")
for d in l1_al_devs: a("ANI", d)
a("OUT", "M32")

# ===== NG ALARM RESULT CODES =====
al("NG RESULT CODE")
a("LD", "M817"); a("MOV", "K3"); ac("D7012"); a("MOV", "K3"); ac("D8012")
a("LD", "M819"); a("MOV", "K4"); ac("D7012"); a("MOV", "K4"); ac("D8012")
a("LD", "M821"); a("MOV", "K5"); ac("D7012"); a("MOV", "K5"); ac("D8012")
a("LD", "M823"); a("MOV", "K2"); ac("D7012"); a("MOV", "K2"); ac("D8012")

# ===== EXHAUST TIMER (shared T3 for both lanes) =====
al("EXHAUST TIMER")
a("LD", "M23"); a("OUT", "T3"); ac("D8")
a("LD", "M39"); a("OUT", "T3"); ac("D38")

# ===== LAMP CONTROL =====
al("LAMP CONTROL")
all_al_devs = ["M864","M865","M866","M867","M868","M869","M872","M873","M874","M875","M876","M877","M878","M879"]
# GREEN: any L0 step active AND no NG alarm
a("LD", "M16")
for s in ["M17","M18","M19","M20","M21","M22","M23","M24"]: a("OR", s)
for d in all_al_devs: a("ANI", d)
a("OUT", "M77")
# RED: any NG alarm
a("LD", all_al_devs[0])
for d in all_al_devs[1:]: a("OR", d)
a("OUT", "M78")
# YELLOW: init state + no interlock
a("LD", "M16"); a("ANI", "M880"); a("OUT", "M79")

# ===== HMI LAMP BITS =====
al("HMI LAMP")
a("LD", "M18"); a("OUT", "M530")
a("LD", "M19"); a("OUT", "M531")
a("LD", "M20"); a("OUT", "M532")
a("LD", "M21"); a("OR", "M22"); a("OUT", "M533")
a("LD", "M34"); a("OUT", "M546")
a("LD", "M35"); a("OUT", "M547")
a("LD", "M36"); a("OUT", "M548")
a("LD", "M37"); a("OR", "M38"); a("OUT", "M549")
# Running lamp L0
a("LD", "M18")
for s in ["M19","M20","M21","M22","M23","M24"]: a("OR", s)
a("OUT", "M540")
# Running lamp L1
a("LD", "M34")
for s in ["M35","M36","M37","M38","M39","M40"]: a("OR", s)
a("OUT", "M556")

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\MAIN.csv")
