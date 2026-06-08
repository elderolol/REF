# MAIN — Step Machine, Mode, Gun Select, Ready, Interlock, Stop/EMG, Lamps
# L1=M10~M18, L2=M30~M38, L3=M50~M53 (shared oil)
# Auto: PRECHECK→GUNVAC→UNITVAC→VACCHECK→[OIL→]REFRIG→EXHAUST→COMPLETE→IDLE
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

# === SYSTEM FLAGS ===
al("SYSTEM FLAGS")
a("LD","SM400"); a("OUT","M0")
a("LD","SM401"); a("OUT","M1")
a("LD","SM402"); a("OUT","M2")

# === POWER-ON DEFAULTS ===
al("POWER-ON DEFAULTS")
a("LD","M2"); a("SET","M200"); a("RST","M201")   # MANUAL
a("LD","M2"); a("SET","M210"); a("RST","M211")   # GUN A
a("LD","M2"); a("SET","M520")                     # Barcode used
a("LD","M2"); a("SET","M521")                     # Oil+Refrig enabled
a("LD","M2"); a("SET","M522")                     # Interlock used
a("LD","M2"); a("SET","M10"); a("SET","M30"); a("SET","M50")   # IDLE init

# === MODE CONTROL (IDLE only) ===
al("MODE CONTROL")
a("LD","M402"); a("PLS","M600")
a("LD","M600"); a("AND","M200"); a("AND","M10"); a("SET","M201"); a("RST","M200")
a("LD","M600"); a("AND","M201"); a("AND","M10"); a("SET","M200"); a("RST","M201")

# === GUN SELECT (IDLE only) ===
al("GUN SELECT")
a("LD","M400"); a("PLS","M601")
a("LD","M601"); a("AND","M10"); a("AND","M30"); a("SET","M210"); a("RST","M211")
a("LD","M401"); a("PLS","M602")
a("LD","M602"); a("AND","M10"); a("AND","M30"); a("SET","M211"); a("RST","M210")

# === OIL+REFRIG ENABLE TOGGLE ===
al("OIL+REFRIG ENABLE")
a("LD","M415"); a("PLS","M621")
a("LD","M621"); a("ANI","M521"); a("SET","M521")
a("LD","M621"); a("AND","M521"); a("RST","M521")

# === INTERLOCK USE/NOT USE TOGGLE ===
al("INTERLOCK ENABLE")
a("LD","M413"); a("PLS","M622")
a("LD","M622"); a("ANI","M522"); a("SET","M522")
a("LD","M622"); a("AND","M522"); a("RST","M522")

# === READY SET (Manual Mode, toggle) ===
al("READY SET")
a("LD","M403"); a("PLS","M603")
a("LD","M603"); a("AND","M200"); a("ANI","M220"); a("SET","M220")
a("LD","M603"); a("AND","M200"); a("AND","M220"); a("RST","M220")
a("LD","M404"); a("PLS","M604")
a("LD","M604"); a("AND","M200"); a("ANI","M221"); a("SET","M221")
a("LD","M604"); a("AND","M200"); a("AND","M221"); a("RST","M221")
a("LD","M405"); a("PLS","M605")
a("LD","M605"); a("AND","M200"); a("ANI","M222"); a("SET","M222")
a("LD","M605"); a("AND","M200"); a("AND","M222"); a("RST","M222")
a("LD","M406"); a("PLS","M606")
a("LD","M606"); a("AND","M200"); a("ANI","M520"); a("ANI","M223"); a("SET","M223")  # REFRIG INJ
a("LD","M606"); a("AND","M200"); a("AND","M223"); a("RST","M223")
a("LD","M407"); a("PLS","M607")
a("LD","M607"); a("AND","M200"); a("ANI","M520"); a("ANI","M224"); a("SET","M224")  # OIL INJ
a("LD","M607"); a("AND","M200"); a("AND","M224"); a("RST","M224")

# === MANUAL START with WARMUP T0 ===
al("MANUAL START ENTRY")
a("LD","M408"); a("AND","M220"); a("PLS","M610")
a("LD","M408"); a("AND","M221"); a("PLS","M611")
a("LD","M408"); a("AND","M222"); a("PLS","M612")
a("LD","M408"); a("AND","M223"); a("PLS","M613")
a("LD","M408"); a("AND","M224"); a("PLS","M614")
a("LD","M610"); a("OR","M611"); a("OR","M612"); a("OR","M613"); a("OR","M614")
a("SET","M453")
a("LD","M453"); a("OUT","T0"); ac("K5")
# GUN VAC
a("LD","M610"); a("AND","T0"); a("AND","M210"); a("RST","M220"); a("SET","M12"); a("RST","M453")
a("LD","M610"); a("AND","T0"); a("AND","M211"); a("RST","M220"); a("SET","M32"); a("RST","M453")
# UNIT VAC
a("LD","M611"); a("AND","T0"); a("AND","M210"); a("RST","M221"); a("SET","M13"); a("RST","M453")
a("LD","M611"); a("AND","T0"); a("AND","M211"); a("RST","M221"); a("SET","M33"); a("RST","M453")
# VAC CHECK
a("LD","M612"); a("AND","T0"); a("AND","M210"); a("RST","M222"); a("SET","M14"); a("RST","M453")
a("LD","M612"); a("AND","T0"); a("AND","M211"); a("RST","M222"); a("SET","M34"); a("RST","M453")
# REFRIG INJ (M15→M16 for L1, M35→M36 for L2)
a("LD","M613"); a("AND","T0"); a("AND","M210"); a("RST","M223"); a("SET","M15"); a("RST","M453")
a("LD","M613"); a("AND","T0"); a("AND","M211"); a("RST","M223"); a("SET","M35"); a("RST","M453")
# OIL INJ (L3 chain, only if M521 enabled)
a("LD","M614"); a("AND","T0"); a("AND","M521"); a("ANI","M304"); a("RST","M224"); a("SET","M51"); a("RST","M453")

# === AUTO START → PRECHECK ===
al("AUTO START")
a("LD","M408"); a("AND","M201"); a("AND","M210"); a("AND","M10"); a("PLS","M615")
a("LD","M408"); a("AND","M201"); a("AND","M211"); a("AND","M30"); a("PLS","M616")
a("LD","M615"); a("SET","M453")
a("LD","M616"); a("SET","M453")
a("LD","M615"); a("AND","T0"); a("SET","M11"); a("RST","M453")
a("LD","M616"); a("AND","T0"); a("SET","M31"); a("RST","M453")
# Stopwatch start: auto cycle begin
a("LD","M615"); a("OR","M616"); a("SET","M490"); a("MOV","K0"); ac("D244")

# === AUTO CHAIN WARMUP ===
al("AUTO CHAIN WARMUP")
# PRECHECK done → GUN VAC (auto mode only)
a("LD","M11"); a("AND","M100"); a("AND","M201"); a("SET","M460")
a("LD","M460"); a("OUT","T0"); ac("K5")
a("LD","M460"); a("AND","T0"); a("SET","M12"); a("RST","M11"); a("RST","M460")
a("LD","M31"); a("AND","M116"); a("AND","M201"); a("SET","M467")
a("LD","M467"); a("OUT","T0"); ac("K5")
a("LD","M467"); a("AND","T0"); a("SET","M32"); a("RST","M31"); a("RST","M467")
# GUN VAC done → UNIT VAC (auto mode only)
a("LD","M12"); a("AND","M101"); a("AND","M201"); a("SET","M461")
a("LD","M461"); a("OUT","T0"); ac("K5")
a("LD","M461"); a("AND","T0"); a("SET","M13"); a("RST","M12"); a("RST","M461")
a("LD","M32"); a("AND","M117"); a("AND","M201"); a("SET","M468")
a("LD","M468"); a("OUT","T0"); ac("K5")
a("LD","M468"); a("AND","T0"); a("SET","M33"); a("RST","M32"); a("RST","M468")
# UNIT VAC done → VAC CHECK (auto mode only)
a("LD","M13"); a("AND","M102"); a("AND","M201"); a("SET","M462")
a("LD","M462"); a("OUT","T0"); ac("K5")
a("LD","M462"); a("AND","T0"); a("SET","M14"); a("RST","M13"); a("RST","M462")
a("LD","M33"); a("AND","M118"); a("AND","M201"); a("SET","M469")
a("LD","M469"); a("OUT","T0"); ac("K5")
a("LD","M469"); a("AND","T0"); a("SET","M34"); a("RST","M33"); a("RST","M469")
# VAC CHECK done → OIL or REFRIG (auto only)
a("LD","M14"); a("AND","M103"); a("AND","M201")
a("LD","M34"); a("AND","M119"); a("AND","M201")
a("ORB","")
a("SET","M463")
a("LD","M463"); a("OUT","T0"); ac("K5")
a("LD","M463"); a("AND","T0"); a("AND","M210"); a("AND","M521"); a("LDD>=","D18"); ac("K1")
a("ANI","M304"); a("SET","M51"); a("RST","M14"); a("RST","M463")
a("LD","M463"); a("AND","T0"); a("AND","M211"); a("AND","M521"); a("LDD>=","D50"); ac("K1")
a("ANI","M304"); a("SET","M51"); a("RST","M34"); a("RST","M463")
a("LD","M463"); a("AND","T0"); a("AND","M210"); a("LDD>=","D18"); ac("K1"); a("ANI","M0")
a("SET","M15"); a("RST","M14"); a("RST","M463")
a("LD","M463"); a("AND","T0"); a("AND","M211"); a("LDD>=","D50"); ac("K1"); a("ANI","M0")
a("SET","M35"); a("RST","M34"); a("RST","M463")
a("LD","M463"); a("AND","T0"); a("AND","M210"); a("ANI","M521"); a("SET","M15"); a("RST","M14"); a("RST","M463")
a("LD","M463"); a("AND","T0"); a("AND","M211"); a("ANI","M521"); a("SET","M35"); a("RST","M34"); a("RST","M463")
# OIL COMPLETE → REFRIG (auto only)
a("LD","M53"); a("AND","M201"); a("AND","M521"); a("SET","M464")
a("LD","M464"); a("OUT","T0"); ac("K5")
a("LD","M464"); a("AND","T0"); a("AND","M210"); a("SET","M15"); a("RST","M53"); a("RST","M464")
a("LD","M464"); a("AND","T0"); a("AND","M211"); a("SET","M35"); a("RST","M53"); a("RST","M464")
# REFRIG BASE done → EXHAUST
a("LD","M16"); a("AND","M105"); a("AND","M201"); a("SET","M465")
a("LD","M465"); a("OUT","T0"); ac("K5")
a("LD","M465"); a("AND","T0"); a("SET","M17"); a("RST","M16"); a("RST","M465")
a("LD","M36"); a("AND","M121"); a("AND","M201"); a("SET","M466")
a("LD","M466"); a("OUT","T0"); ac("K5")
a("LD","M466"); a("AND","T0"); a("SET","M37"); a("RST","M36"); a("RST","M466")

# ==========================================
# STEP MACHINE L1 (M10~M18)
# ==========================================
l1_al = ["300","301","302","303","310","311","312","313","314","316","317","318","319","320"]
l2_al = ["300","301","302","303","330","331","332","333","334","336","337","338","339","340"]

al("STEP L1")
a("LD","M17"); a("AND","M106")
a("OR","M18"); a("ANI","M10"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M18")
a("LD","M17"); a("AND","M106"); a("SET","M107")
a("LD","M18"); a("MOV","K1"); ac("D1000")

a("LD","M17"); a("OR","M17"); a("ANI","M18"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M17")
a("LD","M16"); a("OR","M16"); a("ANI","M17"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M16")
a("LD","M15"); a("OR","M15"); a("ANI","M16"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M15")
a("LD","M14"); a("OR","M14"); a("ANI","M15"); a("ANI","M51"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M14")
a("LD","M13"); a("OR","M13"); a("ANI","M14"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M13")
a("LD","M12"); a("OR","M12"); a("ANI","M13"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M12")
a("LD","M11"); a("OR","M11"); a("ANI","M12"); a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M11")
# PRECHECK OK: interlock OK, model>0, target>0
a("LD","M11"); a("AND","M80"); a("LD>","D0"); ac("K0"); a("ANB","")
a("LDD>=","D12"); ac("K1"); a("ANB",""); a("OUT","M100")

a("LD","M18"); a("OR","M10")
a("ANI","M11"); a("ANI","M12"); a("ANI","M13"); a("ANI","M14"); a("ANI","M15"); a("ANI","M16")
a("ANI","M450")
for la in l1_al: a("ANI",("M"+la))
a("OUT","M10")
a("LD","M10"); a("MOV","K0"); ac("D0")

# ==========================================
# STEP MACHINE L2 (M30~M38)
# ==========================================
al("STEP L2")
a("LD","M37"); a("AND","M122")
a("OR","M38"); a("ANI","M30"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M38")
a("LD","M37"); a("AND","M122"); a("SET","M123")
a("LD","M38"); a("MOV","K1"); ac("D1200")

a("LD","M37"); a("OR","M37"); a("ANI","M38"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M37")
a("LD","M36"); a("OR","M36"); a("ANI","M37"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M36")
a("LD","M35"); a("OR","M35"); a("ANI","M36"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M35")
a("LD","M34"); a("OR","M34"); a("ANI","M35"); a("ANI","M51"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M34")
a("LD","M33"); a("OR","M33"); a("ANI","M34"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M33")
a("LD","M32"); a("OR","M32"); a("ANI","M33"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M32")
a("LD","M31"); a("OR","M31"); a("ANI","M32"); a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M31")
a("LD","M31"); a("AND","M90"); a("LD>","D32"); ac("K0"); a("ANB","")
a("LDD>=","D44"); ac("K1"); a("ANB",""); a("OUT","M116")

a("LD","M38"); a("OR","M30")
a("ANI","M31"); a("ANI","M32"); a("ANI","M33"); a("ANI","M34"); a("ANI","M35"); a("ANI","M36")
a("ANI","M451")
for la in l2_al: a("ANI",("M"+la))
a("OUT","M30")
a("LD","M30"); a("MOV","K0"); ac("D32")    # reset L2 model# on IDLE

# ==========================================
# STEP MACHINE L3 (M50~M53) — Oil
# ==========================================
l3_al = ["300","301","302","303","304","350","351"]
al("STEP L3")
a("LD","M52"); a("AND","M146")            # M146 = OIL BASE OK
a("OR","M53"); a("ANI","M50"); a("ANI","M450"); a("ANI","M451")
for la in l3_al: a("ANI",("M"+la))
a("OUT","M53")
a("LD","M52"); a("AND","M146"); a("SET","M147")   # OIL COMPLETE

a("LD","M51"); a("AND","M145")            # M145 = OIL FAST OK
a("OR","M52"); a("ANI","M53"); a("ANI","M450"); a("ANI","M451")
for la in l3_al: a("ANI",("M"+la))
a("OUT","M52")

a("LD","M51"); a("OUT","M51")

a("LD","M53"); a("OR","M50")
a("ANI","M51"); a("ANI","M450"); a("ANI","M451")
for la in l3_al: a("ANI",("M"+la))
a("OUT","M50")

# === INTERLOCK CHECK ===
al("INTERLOCK CHECK")
a("LD","M81"); a("AND","M82"); a("AND","M83"); a("AND","M84"); a("AND","M85"); a("OUT","M80")
a("LD","M91"); a("AND","M92"); a("AND","M93"); a("AND","M94"); a("AND","M95"); a("OUT","M90")

# === NG ALARM STOP ===
al("NG ALARM STOP")
a("LD","M108"); a("OR","M109"); a("OR","M111") ; a("LD","M310"); a("OR","M311"); a("OR","M312")
a("ORB",""); a("SET","M450")
a("LD","M124"); a("OR","M125"); a("OR","M127") ; a("LD","M330"); a("OR","M331"); a("OR","M332")
a("ORB",""); a("SET","M451")
a("LD","M450"); a("RST","M12"); a("RST","M13"); a("RST","M14"); a("RST","M15"); a("RST","M16"); a("SET","M17")
a("LD","M451"); a("RST","M32"); a("RST","M33"); a("RST","M34"); a("RST","M35"); a("RST","M36"); a("SET","M37")
a("LD","M450"); a("OR","M451")
a("RST","M51"); a("RST","M52"); a("SET","M53")
a("RST","M65"); a("RST","M66"); a("RST","M75"); a("RST","M76")
a("RST","M96"); a("RST","M97")

# === STOP ===
al("STOP")
a("LD","M409"); a("AND","M210"); a("SET","M450")
a("LD","M409"); a("AND","M211"); a("SET","M451")
a("LD","M10"); a("RST","M450")
a("LD","M30"); a("RST","M451")
a("LD","M450"); a("MOV","K6"); ac("D1000")
a("LD","M451"); a("MOV","K6"); ac("D1200")

# === EMERGENCY STOP ===
al("EMERGENCY STOP")
a("LDI","M770"); a("OR","M452"); a("ANI","M410"); a("OUT","M452")
all_steps = ["10","11","12","13","14","15","16","17","18","30","31","32","33","34","35","36","37","38","50","51","52","53"]
a("LD","M452")
for i,s in enumerate(all_steps):
    if i>0 and i%8==0: a("LD","M452")
    a("RST",("M"+s))
all_sols = ["60","61","62","63","64","65","66","68","69","70","71","72","73","74","75","76","96","97"]
a("LD","M452")
for i,s in enumerate(all_sols):
    if i>0 and i%8==0: a("LD","M452")
    a("RST",("M"+s))
a("LD","M452"); a("MOV","K6"); ac("D1000")
a("LD","M452"); a("MOV","K6"); ac("D1200")

# === LAMP CONTROL ===
al("LAMP CONTROL")
a("LD","M12"); a("OR","M13"); a("OR","M14"); a("OR","M15"); a("OR","M16"); a("OR","M17")
a("LD","M32"); a("OR","M33"); a("OR","M34"); a("OR","M35"); a("OR","M36"); a("OR","M37")
a("ORB",""); a("LD","M51"); a("OR","M52"); a("ORB","")
all_al_l = l1_al + l2_al + l3_al
for la in all_al_l: a("ANI",("M"+la))
a("OUT","M77")
a("LD","M300")
for b in ["301","302","303","304","310","311","312","313","314","316","317","318","319","320","330","331","332","333","334","336","337","338","339","340","350","351"]:
    a("OR",("M"+b))
a("OUT","M78")
a("LD","M10"); a("LD","M30"); a("ORB",""); a("ANI","M80"); a("ANI","M90"); a("OUT","M79")

# === STOPWATCH (0.1sec, auto cycle only) ===
al("STOPWATCH")
# Active: auto cycle start → IDLE
a("LD","M490"); a("ANI","T22"); a("OUT","T22"); ac("K1")    # 100ms self-reset
a("LD","T22"); a("D+","D244"); ac("K1"); ac("D244")         # +0.1 sec
# Stop on IDLE
a("LD","M10"); a("OR","M30"); a("RST","M490")
# Also stop on cycle complete/NG
a("LD","M450"); a("OR","M451"); a("RST","M490")
a("LD","M452"); a("RST","M490")

# === VACUUM PUMP ===
al("VACUUM PUMP")
a("LD","M412"); a("PLS","M620")
a("LD","M620"); a("ANI","M67"); a("SET","M67")
a("LD","M620"); a("AND","M67"); a("RST","M67")

# === HYDRO PUMP ===
al("HYDRO PUMP")
a("LD","M419"); a("PLS","M623")
a("LD","M623"); a("ANI","M96"); a("SET","M96"); a("SET","M97")
a("LD","M623"); a("AND","M96"); a("RST","M96"); a("RST","M97")
# Auto SET during oil steps (if pump not tripped)
a("LD","M51"); a("ANI","M304"); a("SET","M96"); a("SET","M97")
a("LD","M52"); a("ANI","M304"); a("SET","M96"); a("SET","M97")

# === HEATER RELAY ===
al("HEATER RELAY")
# Power-on default: Gun A -> relay OFF
a("LD","M2"); a("RST","M98")
# Gun A selected -> relay OFF (Gun A heated)
a("LD","M210"); a("RST","M98")
# Gun B selected -> relay ON (Gun B heated)
a("LD","M211"); a("SET","M98")

a("END","")
wr("C:/WorkSpace/2L2GOIL/src\\MAIN.csv")
