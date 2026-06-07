# VAC CHECK — L1: M14, L2: M34. VAC+STEM SOL ON + LINE VAC SOL(M68) ON
# Results: L1 M103(OK), M109(NG/leak)  L2 M119(OK), M125(NG/leak)
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

al("VAC CHECK L1")
a("LD","M14"); a("OUT","M60"); a("OUT","M61"); a("OUT","M68")
a("LD","M14"); a("DMOV","D30"); ac("D600"); a("OUT","T3"); ac("D6")
a("LD","M14"); a("D-","D600"); ac("D30"); ac("D602")
a("LD","M14"); a("AND","T3"); a("LDD<=","D602"); ac("D24")
a("OUT","M103")    # Vac check OK, step released by warmup chain
a("RST","M60"); a("RST","M61"); a("RST","M68")
a("LD","M14"); a("AND","T3"); a("LDD>","D602"); ac("D24")
a("SET","M109"); a("SET","M312"); a("RST","M14"); a("RST","M60"); a("RST","M61"); a("RST","M68")

al("VAC CHECK L2")
a("LD","M34"); a("OUT","M70"); a("OUT","M71"); a("OUT","M68")
a("LD","M34"); a("DMOV","D62"); ac("D610"); a("OUT","T9"); ac("D38")
a("LD","M34"); a("D-","D610"); ac("D62"); ac("D612")
a("LD","M34"); a("AND","T9"); a("LDD<=","D612"); ac("D56")
a("OUT","M119")    # L2 Vac check OK, step released by warmup chain
a("RST","M70"); a("RST","M71"); a("RST","M68")
a("LD","M34"); a("AND","T9"); a("LDD>","D612"); ac("D56")
a("SET","M125"); a("SET","M332"); a("RST","M34"); a("RST","M70"); a("RST","M71"); a("RST","M68")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\vacchec.csv")
