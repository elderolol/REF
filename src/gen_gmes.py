# GMES — PC communication + result code
# Model/injection → indexs.csv, VAC SPC → spc.csv
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

hd("gmes")

# ===== PC COMM L1 =====
al("PC COMM L1")
# D7002/D7003: D7001 non-zero → update continuously
a("LD>", "D7001"); ac("K0")
a("MOV", "D7000"); ac("D7002")
a("MOV", "D7001"); ac("D7003")
# D7004~D7006: capture when REFRIG injection ends (M23 exhaust start)
a("LD", "M23"); a("DMOV", "D130"); ac("D7004")
a("LD", "M23"); a("MOV", "D142"); ac("D7005")
a("LD", "M23"); a("MOV", "D142"); ac("D7006")
a("LD", "M0"); a("MOV", "D7007"); ac("D7007")
a("LD", "M0"); a("MOV", "D140"); ac("D7008")
a("LD", "M0"); a("DMOV", "D160"); ac("D7010")
a("LD", "M0"); a("DMOV", "D22"); ac("D7013")
a("LD", "M0"); a("MOV", "K1"); ac("D7017")
a("LD", "M0"); a("MOV", "K0"); ac("D7018")
a("LD", "L3"); a("MOV", "K1"); ac("D7009")
a("LDI", "L3"); a("MOV", "K2"); ac("D7009")
a("LD", "M16"); a("MOV", "K0"); ac("D7016")
a("LDI", "M16"); a("MOV", "K1"); ac("D7016")
a("LD", "M18"); a("MOV", "K1"); ac("D7015")
a("LD", "M19"); a("MOV", "K2"); ac("D7015")
a("LD", "M20"); a("MOV", "K3"); ac("D7015")
a("LD", "M21"); a("OR", "M22"); a("MOV", "K4"); ac("D7015")
a("LD", "M16"); a("MOV", "K0"); ac("D7015")

# ===== PC COMM L2 =====
al("PC COMM L2")
# D8002/D8003: D8001 non-zero → update continuously
a("LD>", "D8001"); ac("K0")
a("MOV", "D8000"); ac("D8002")
a("MOV", "D8001"); ac("D8003")
# D8004~D8006: capture when REFRIG injection ends (M39 exhaust start)
a("LD", "M39"); a("DMOV", "D406"); ac("D8004")
a("LD", "M39"); a("MOV", "D148"); ac("D8005")
a("LD", "M39"); a("MOV", "D148"); ac("D8006")
a("LD", "M0"); a("MOV", "D8007"); ac("D8007")
a("LD", "M0"); a("MOV", "D146"); ac("D8008")
a("LD", "M0"); a("DMOV", "D172"); ac("D8010")
a("LD", "M0"); a("DMOV", "D50"); ac("D8013")
a("LD", "M0"); a("MOV", "K2"); ac("D8017")
a("LD", "M0"); a("MOV", "K0"); ac("D8018")
a("LD", "L3"); a("MOV", "K1"); ac("D8009")
a("LDI", "L3"); a("MOV", "K2"); ac("D8009")
a("LD", "M32"); a("MOV", "K0"); ac("D8016")
a("LDI", "M32"); a("MOV", "K1"); ac("D8016")
a("LD", "M34"); a("MOV", "K1"); ac("D8015")
a("LD", "M35"); a("MOV", "K2"); ac("D8015")
a("LD", "M36"); a("MOV", "K3"); ac("D8015")
a("LD", "M37"); a("OR", "M38"); a("MOV", "K4"); ac("D8015")
a("LD", "M32"); a("MOV", "K0"); ac("D8015")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\gmes.csv")
