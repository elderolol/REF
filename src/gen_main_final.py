def M(h): return f"M{int(h,16)}"
def L(h): return f"L{int(h,16)}"
def l1(s): return f"{int(s,16)+0x10:X}"
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

hd("MAIN")
al("MODE CONTROL")
a("LD", M("40E")); a("PLS", M("600"))
a("LD", M("600")); a("AND", L("1")); a("SET", L("2")); a("RST", L("1"))
a("LD", M("600")); a("ANI", L("1")); a("SET", L("1")); a("RST", L("2"))
a("LD", M("400")); a("OR", L("70")); a("ANI", M("401")); a("OUT", L("70"))
a("LD", M("401")); a("OR", L("71")); a("ANI", M("400")); a("OUT", L("71"))
a("LD", M("408")); a("OR", L("72")); a("ANI", M("409")); a("OUT", L("72"))
a("LD", M("409")); a("OR", L("73")); a("ANI", M("408")); a("OUT", L("73"))
a("LD", M("402")); a("PLS", M("601")); a("LD", M("601")); a("AND", L("74")); a("RST", L("74"))
a("LD", M("601")); a("ANI", L("74")); a("SET", L("74"))

al("INTERLOCK CHECK")
a("LD", L("51")); a("AND", L("52")); a("AND", L("53")); a("AND", L("54")); a("AND", L("55")); a("OUT", L("50"))
a("LD", L("61")); a("AND", L("62")); a("AND", L("63")); a("AND", L("64")); a("AND", L("65")); a("OUT", L("60"))

l0_al = ["40","41","42","43","44","45","46","47","48","49","4A","4E"]
l1_al = ["40","41","42","43","44","45","46","47","48","49","4A","4F"]

# ===== READY + START for Manual Mode =====
al("READY SET L0")
a("LD", M("40F")); a("AND", L("2")); a("ANI", M("12")); a("SET", "M502")
a("LD", M("410")); a("AND", L("2")); a("ANI", M("13")); a("SET", "M503")
a("LD", M("411")); a("AND", L("2")); a("ANI", M("14")); a("SET", "M504")
a("LD", M("412")); a("AND", L("2")); a("ANI", M("15")); a("SET", "M505")

al("READY SET L1")
a("LD", M("40F")); a("AND", L("2")); a("ANI", M("22")); a("SET", "M506")
a("LD", M("410")); a("AND", L("2")); a("ANI", M("23")); a("SET", "M507")
a("LD", M("411")); a("AND", L("2")); a("ANI", M("24")); a("SET", "M508")
a("LD", M("412")); a("AND", L("2")); a("ANI", M("25")); a("SET", "M509")

al("START EXEC L0")
a("LD", M("413")); a("AND", "M502"); a("SET", M("12")); a("RST", "M502")
a("LD", M("413")); a("AND", "M503"); a("SET", M("13")); a("RST", "M503")
a("LD", M("413")); a("AND", "M504"); a("SET", M("14")); a("RST", "M504")
a("LD", M("413")); a("AND", "M505"); a("SET", M("15")); a("RST", "M505")

al("START EXEC L1")
a("LD", M("415")); a("AND", "M506"); a("SET", M("22")); a("RST", "M506")
a("LD", M("415")); a("AND", "M507"); a("SET", M("23")); a("RST", "M507")
a("LD", M("415")); a("AND", "M508"); a("SET", M("24")); a("RST", "M508")
a("LD", M("415")); a("AND", "M509"); a("SET", M("25")); a("RST", "M509")

# ===== SELF-HOLDING STEP MACHINE L0 =====
al("STEP L0")
# M16 (init): M24 cycle complete OR self-hold, release when M17 active
a("LD", M("18"))
a("OR", M("10"))
a("ANI", M("11"))
a("ANI", L("40"))
a("OUT", M("10"))

# M17: M16 AND start_conditions, release when M18 active
a("LD", M("10")); a("AND", L("0")); a("AND", L("50")); a("AND", M("413")); a("AND", L("1"))
for la in l0_al: a("ANI", L(la))
a("OR", M("11"))
a("ANI", M("12"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("11"))

# M18: M17 unconditional, release when M19 active
a("LD", M("11"))
a("OR", M("12"))
a("ANI", M("13"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("12"))

# M19: M18 AND L16, release when M20 active
a("LD", M("12")); a("AND", L("10"))
a("OR", M("13"))
a("ANI", M("14"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("13"))

# M20: M19 AND L18, release when M21 active
a("LD", M("13")); a("AND", L("12"))
a("OR", M("14"))
a("ANI", M("15"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("14"))

# M21: M20 AND L20, release when M23 active
a("LD", M("14")); a("AND", L("14"))
a("OR", M("15"))
a("ANI", M("17"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("15"))

# M22: parallel branch (same trigger as M21, release when M23 active)
a("LD", M("14")); a("AND", L("14"))
a("OR", M("16"))
a("ANI", M("17"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("16"))

# M23: M21 OR M22 AND L22, release when M24 active
a("LD", M("15")); a("OR", M("16")); a("AND", L("16"))
a("OR", M("17"))
a("ANI", M("18"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("17"))

# M24: M23 AND T3, release when M16 active (cycle complete)
a("LD", M("17")); a("AND", "T3")
a("OR", M("18"))
a("ANI", M("10"))
a("ANI", L("40"))
for la in l0_al: a("ANI", L(la))
a("OUT", M("18"))
# L24 cycle complete pulse
a("LD", M("17")); a("AND", "T3"); a("SET", L("18"))
# Result code K1: normal complete
a("LD", M("18")); a("MOV", "K1"); ac("D7012")

# ===== SELF-HOLDING STEP MACHINE L1 =====
al("STEP L1")
# M32 (init): M40 cycle complete OR self-hold, release when M33 active
a("LD", M("28"))
a("OR", M("20"))
a("ANI", M("21"))
a("ANI", L("40"))
a("OUT", M("20"))

# M33: M32 AND start_conditions, release when M34 active
a("LD", M("20")); a("AND", L("0")); a("AND", L("60")); a("AND", M("415")); a("AND", L("1"))
for la in l1_al: a("ANI", L(la))
a("OR", M("21"))
a("ANI", M("22"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("21"))

# M34: M33 unconditional, release when M35 active
a("LD", M("21"))
a("OR", M("22"))
a("ANI", M("23"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("22"))

# M35: M34 AND L32, release when M36 active
a("LD", M("22")); a("AND", L("20"))
a("OR", M("23"))
a("ANI", M("24"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("23"))

# M36: M35 AND L34, release when M37 active
a("LD", M("23")); a("AND", L("22"))
a("OR", M("24"))
a("ANI", M("25"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("24"))

# M37: M36 AND L36, release when M39 active
a("LD", M("24")); a("AND", L("24"))
a("OR", M("25"))
a("ANI", M("27"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("25"))

# M38: parallel branch (same trigger as M37, release when M39 active)
a("LD", M("24")); a("AND", L("24"))
a("OR", M("26"))
a("ANI", M("27"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("26"))

# M39: M37 OR M38 AND L38, release when M40 active
a("LD", M("25")); a("OR", M("26")); a("AND", L("26"))
a("OR", M("27"))
a("ANI", M("28"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("27"))

# M40: M39 AND T3, release when M32 active (cycle complete)
a("LD", M("27")); a("AND", "T3")
a("OR", M("28"))
a("ANI", M("20"))
a("ANI", L("40"))
for la in l1_al: a("ANI", L(la))
a("OUT", M("28"))
# L40 cycle complete pulse
a("LD", M("27")); a("AND", "T3"); a("SET", L("28"))
# Result code K1: normal complete
a("LD", M("28")); a("MOV", "K1"); ac("D8012")

# ===== NG ALARM STOP =====
# Self-holding: active steps turn off via alarm ANI in each step's self-hold rung
# Result codes: L17→K3 Gun vacuum NG, L19→K4 Unit vacuum NG, L21→K5 Vacuum check NG, L23→K2 Charging NG
al("NG ALARM STOP")
a("LD", L("11")); a("MOV", "K3"); ac("D7012"); a("MOV", "K3"); ac("D8012")
a("LD", L("13")); a("MOV", "K4"); ac("D7012"); a("MOV", "K4"); ac("D8012")
a("LD", L("15")); a("MOV", "K5"); ac("D7012"); a("MOV", "K5"); ac("D8012")
a("LD", L("17")); a("MOV", "K2"); ac("D7012"); a("MOV", "K2"); ac("D8012")
a("LD", L("11")); a("OR", L("13")); a("OR", L("15")); a("OR", L("17"))
for la in l0_al: a("OR", L(la))
a("SET", M("10"))
a("LD", L("11")); a("OR", L("13")); a("OR", L("15")); a("OR", L("17"))
for la in l1_al: a("OR", L(la))
a("SET", M("20"))

# ===== STOP =====
al("STOP")
all_sh = ["10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28"]
all_so = ["30","31","32","33","34","35","36","37","38","39","3A","3B","40","41","42","43","44","45","46","47","48","49","4A","4B","4C","4D","4E","4F","50"]
a("LD", M("414")); a("OR", M("301"))
for cs in range(0,len(all_sh),8):
    if cs>0: a("LD","M0")
    for s in all_sh[cs:cs+8]: a("RST",M(s))
for cs in range(0,len(all_so),8):
    a("LD","M0")
    for s in all_so[cs:cs+8]: a("RST",M(s))
a("LD","M0"); a("SET",M("10")); a("SET",M("20"))
a("MOV","K6 D7012"); a("MOV","K6 D8012")

# ===== EMERGENCY STOP =====
al("EMERGENCY STOP")
a("LDI",M("303")); a("SET",L("40"))
a("MOV","K6 D7012"); a("MOV","K6 D8012")
for cs in range(0,len(all_sh),8):
    if cs>0: a("LD","M0")
    for s in all_sh[cs:cs+8]: a("RST",M(s))
for cs in range(0,len(all_so),8):
    a("LD","M0")
    for s in all_so[cs:cs+8]: a("RST",M(s))

# ===== EXHAUST TIMER =====
al("EXHAUST TIMER")
a("LD",M("17")); a("OUT","T3"); ac("D8")
a("LD",M("27")); a("OUT","T3"); ac("D38")

# ===== LAMP CONTROL =====
al("LAMP CONTROL")
# GREEN
all_al = ["40","41","42","43","44","45","46","47","48","49","4A","4E","4F"]
a("LD",M("10"))
for s in ["11","12","13","14","15","16","17","18"]: a("OR",M(s))
for la in all_al: a("ANI",L(la))
a("OUT",M("4D"))
# RED
a("LD",L(all_al[0]))
for la in all_al[1:]: a("OR",L(la))
a("OUT",M("4E"))
# YELLOW
a("LD",M("10")); a("ANI",L("50")); a("OUT",M("4F"))

# ===== HMI LAMP BITS =====
al("HMI LAMP")
a("LD","M502"); a("OR",M("12")); a("OUT","M530")
a("LD","M503"); a("OR",M("13")); a("OUT","M531")
a("LD","M504"); a("OR",M("14")); a("OUT","M532")
a("LD","M505"); a("OR",M("15")); a("OR",M("16")); a("OUT","M533")
a("LD","M506"); a("OR",M("22")); a("OUT","M534")
a("LD","M507"); a("OR",M("23")); a("OUT","M535")
a("LD","M508"); a("OR",M("24")); a("OUT","M536")
a("LD","M509"); a("OR",M("25")); a("OR",M("26")); a("OUT","M537")
a("LD",M("12"))
for s in ["13","14","15","16","17","18"]: a("OR",M(s))
a("OUT","M540")
a("LD",M("22"))
for s in ["23","24","25","26","27","28"]: a("OR",M(s))
a("OUT","M541")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\MAIN.csv")
