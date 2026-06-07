# REFRIG INJECTION — H+L solenoid only (no gas type branching)
# L1: M15(FAST)→M16(BASE)→EXHAUST  L2: M35(FAST)→M36(BASE)→EXHAUST
# Results: L1=M100-M111 (PRECHECK OK~VAC NG), L2=M116-M127
# M104=REFRIG FAST OK, M105=REFRIG BASE OK, M106=EXHAUST OK
# M110=INJ NG L1, M120=REFRIG FAST OK L2, M121=REFRIG BASE OK L2, M122=EXHAUST OK L2, M126=INJ NG L2
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

al("L1 REFRIG FAST")
a("LD","M15"); a("OUT","M62"); a("OUT","M63")
a("LD","M15"); a("OUT","T4"); ac("K3000")
a("LD","M15"); a("LDD>=","D150"); ac("D10")
a("RST","M62"); a("SET","M104"); a("SET","M16")    # FAST done, goto BASE
a("LD","M15"); a("AND","T4")
a("RST","M62"); a("RST","M63"); a("SET","M313"); a("SET","M110"); a("SET","M17"); a("RST","M15")

al("L1 REFRIG BASE")
a("LD","M16"); a("OUT","M63")
a("LD","M16"); a("OUT","T5"); ac("K3000")
a("LD","M16"); a("LDD>=","D150"); ac("D12")
a("RST","M63"); a("SET","M105"); a("SET","M17")    # BASE OK, goto EXHAUST
a("LD","M16"); a("AND","T5")
a("RST","M63"); a("SET","M313"); a("SET","M110"); a("SET","M17"); a("RST","M16")
a("LD","M16"); a("LDD>","D150"); ac("D14"); a("SET","M314")  # amount NG (over)
a("LD","M17"); a("LDD<","D150"); ac("D12"); a("SET","M314")  # amount NG (under)

al("L1 EXHAUST")
a("LD","M17"); a("OUT","M64")
a("LD","M17"); a("OUT","T6"); ac("D8")
a("LD","M17"); a("AND","T6"); a("RST","M64"); a("SET","M106")

al("L2 REFRIG FAST")
a("LD","M35"); a("OUT","M72"); a("OUT","M73")
a("LD","M35"); a("OUT","T10"); ac("K3000")
a("LD","M35"); a("LDD>=","D170"); ac("D42")
a("RST","M72"); a("SET","M120"); a("SET","M36")
a("LD","M35"); a("AND","T10")
a("RST","M72"); a("RST","M73"); a("SET","M333"); a("SET","M126"); a("SET","M37"); a("RST","M35")

al("L2 REFRIG BASE")
a("LD","M36"); a("OUT","M73")
a("LD","M36"); a("OUT","T11"); ac("K3000")
a("LD","M36"); a("LDD>=","D170"); ac("D44")
a("RST","M73"); a("SET","M121"); a("SET","M37")
a("LD","M36"); a("AND","T11")
a("RST","M73"); a("SET","M333"); a("SET","M126"); a("SET","M37"); a("RST","M36")
a("LD","M36"); a("LDD>","D170"); ac("D46"); a("SET","M334")
a("LD","M37"); a("LDD<","D170"); ac("D44"); a("SET","M334")

al("L2 EXHAUST")
a("LD","M37"); a("OUT","M74")
a("LD","M37"); a("OUT","T12"); ac("D40")
a("LD","M37"); a("AND","T12"); a("RST","M74"); a("SET","M122")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\refinj.csv")
