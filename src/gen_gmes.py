# GMES ? PC communication + SPC logging (merged)
# L1 results: M100-M111, L2 results: M116-M127
# SPC: L1 D7020-D7219, L2 D8020-D8219
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

al("L1 CYCLE DONE SPC")
a("LD","M107")
a("D+","D300"); ac("D130"); ac("D300")
a("LD","M107"); a("D+","D202"); ac("K1"); ac("D202")
a("LD","M107"); a("D+","D204"); ac("D150"); ac("D204")
a("LD","M107"); a("DMOV","D130"); ac("D206")
a("LD","M107"); a("DMOV","D12"); ac("D208")
a("LDD>=","D300"); ac("D210"); a("SET","M302")
# Total injection counter (per line)
a("LD","M107"); a("D+","D240"); ac("K1"); ac("D240")
a("LD","M123"); a("D+","D242"); ac("K1"); ac("D242")

al("L2 CYCLE DONE SPC")
a("LD","M123")
a("D+","D220"); ac("D160"); ac("D220")
a("LD","M123"); a("D+","D222"); ac("K1"); ac("D222")
a("LD","M123"); a("D+","D224"); ac("D170"); ac("D224")
a("LD","M123"); a("DMOV","D160"); ac("D226")
a("LD","M123"); a("DMOV","D44"); ac("D228")
a("LDD>=","D220"); ac("D230"); a("SET","M302")

al("VAC SPC LOGGING")
a("LD","M12"); a("AND","M201"); a("SET","M470")
a("LD","M470"); a("OUTH","T18"); ac("K8")
a("LD","M14"); a("PLS","M480")
a("LD","M480"); a("SET","M481"); a("OUT","T20"); ac("K14")
a("LD","M481"); a("AND","T20"); a("RST","M470"); a("RST","M481")
a("LD","M450"); a("RST","M470"); a("RST","M481")
a("LD","M452"); a("RST","M470"); a("RST","M481")
a("LD","T18"); a("BMOV","D7020"); ac("D7022"); ac("K198")
a("LD","T18"); a("DMOV","D30"); ac("D7020")

a("LD","M32"); a("AND","M201"); a("SET","M471")
a("LD","M471"); a("OUTH","T19"); ac("K8")
a("LD","M34"); a("PLS","M482")
a("LD","M482"); a("SET","M483"); a("OUT","T21"); ac("K14")
a("LD","M483"); a("AND","T21"); a("RST","M471"); a("RST","M483")
a("LD","M451"); a("RST","M471"); a("RST","M483")
a("LD","M452"); a("RST","M471"); a("RST","M483")
a("LD","T19"); a("BMOV","D8020"); ac("D8022"); ac("K198")
a("LD","T19"); a("DMOV","D62"); ac("D8020")

al("VAC SPC CLEAR")
a("LD","M11"); a("FMOV","K0"); ac("D7020"); ac("K200")
a("LD","M31"); a("FMOV","K0"); ac("D8020"); ac("K200")

al("PC COMM STATUS")
a("LD","M10"); a("MOV","K0"); ac("D1001")
a("LD","M11"); a("MOV","K1"); ac("D1001")
a("LD","M12"); a("MOV","K2"); ac("D1001")
a("LD","M13"); a("MOV","K3"); ac("D1001")
a("LD","M14"); a("MOV","K4"); ac("D1001")
a("LD","M15"); a("OR","M16"); a("MOV","K5"); ac("D1001")
a("LD","M17"); a("MOV","K6"); ac("D1001")
a("LD","M18"); a("MOV","K7"); ac("D1001")
a("LD","M30"); a("MOV","K0"); ac("D1201")
a("LD","M31"); a("MOV","K1"); ac("D1201")
a("LD","M32"); a("MOV","K2"); ac("D1201")
a("LD","M33"); a("MOV","K3"); ac("D1201")
a("LD","M34"); a("MOV","K4"); ac("D1201")
a("LD","M35"); a("OR","M36"); a("MOV","K5"); ac("D1201")
a("LD","M37"); a("MOV","K6"); ac("D1201")
a("LD","M38"); a("MOV","K7"); ac("D1201")
a("LD","M50"); a("MOV","K0"); ac("D1401")
a("LD","M51"); a("MOV","K1"); ac("D1401")
a("LD","M52"); a("MOV","K2"); ac("D1401")
a("LD","M53"); a("MOV","K3"); ac("D1401")

a("LD","M520"); a("MOV","K1"); ac("D1002")
a("LDI","M520"); a("MOV","K2"); ac("D1002")
a("LD","M210"); a("MOV","K1"); ac("D1003")
a("LD","M211"); a("MOV","K2"); ac("D1003")
a("LD","M0"); a("DMOV","D30"); ac("D1004")
a("LD","M0"); a("DMOV","D62"); ac("D1204")
a("LD","M0"); a("MOV","D0"); ac("D1006")
a("LD","M0"); a("MOV","D32"); ac("D1206")   # L2 model#
a("LD","M0"); a("DMOV","D12"); ac("D1007")
a("LD","M0"); a("DMOV","D44"); ac("D1207")
a("LD","M0"); a("DMOV","D150"); ac("D1009")
a("LD","M0"); a("DMOV","D170"); ac("D1209")

al("INJECTION COUNT RESET")
a("LD","M414"); a("MOV","K0"); ac("D240")    # L1 count reset
a("LD","M416"); a("MOV","K0"); ac("D242")    # L2 count reset

al("REFRIGERANT USAGE RESET")
a("LD","M417"); a("DMOV","K0"); ac("D200")   # L1 usage reset
a("LD","M418"); a("DMOV","K0"); ac("D220")   # L2 usage reset

a("END","")
wr("C:\\WorkSpace\\REF\\src\\gmes.csv")
