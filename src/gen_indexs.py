# INDEXS — Barcode copy + Model lookup (barcode/manual)
# PC writes barcode → D6980-D6999(L1)/D7980-D7999(L2)
# PLC copies to D7220-D7239/D8220-D8239 for HMI display
# Model lookup uses D7000-D7001/D8000-D8001 (validated barcode target)
# Tables: L1 D300-D524, L2 D550-D774 (25x9)
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

al("BARCODE COPY L1")
# New barcode from PC (D6980-D6999) → copy to HMI display (D7220-D7239)
a("LD>","D6980"); ac("K0")
a("BMOV","D6980"); ac("D7220"); ac("K20")

al("BARCODE COPY L2")
a("LD>","D7980"); ac("K0")
a("BMOV","D7980"); ac("D8220"); ac("K20")

al("L1 MODEL LOOKUP")
# Barcode mode: D7001 = validated barcode target → find matching model row
for k in range(1, 26):
    base = 300 + (k-1) * 9
    a("LD","M520"); a("LDD>=","D7000"); ac("K1"); a("ANDD=","D7001"); ac(f"D{base+1}")
    a("MOV",f"K{k}"); ac("D0")
# Both modes: D0==model# → load target + apply correction
for k in range(1, 26):
    base = 300 + (k-1) * 9
    a("LD","M0"); a("AND=","D0"); ac(f"K{k}")
    a("DMOV",f"D{base+1}"); ac("D102")
    a("D+",f"D{base+3}"); ac("D102"); ac("D12")
    a("DMOV",f"D{base+5}"); ac("D104")
    a("D+",f"D{base+7}"); ac("D104"); ac("D18")

al("L2 MODEL LOOKUP")
for k in range(1, 26):
    base = 550 + (k-1) * 9
    a("LD","M520"); a("LDD>=","D8000"); ac("K1"); a("ANDD=","D8001"); ac(f"D{base+1}")
    a("MOV",f"K{k}"); ac("D32")
for k in range(1, 26):
    base = 550 + (k-1) * 9
    a("LD","M0"); a("AND=","D32"); ac(f"K{k}")
    a("DMOV",f"D{base+1}"); ac("D112")
    a("D+",f"D{base+3}"); ac("D112"); ac("D44")
    a("DMOV",f"D{base+5}"); ac("D114")
    a("D+",f"D{base+7}"); ac("D114"); ac("D50")

al("BARCODE CLEAR")
# Cycle complete/NG → clear PC barcode buffer (barcode mode only)
a("LD","M107"); a("OR","M123")
a("OR","M108"); a("OR","M109")
a("OR","M124"); a("OR","M125")
a("OR","M300")
a("FMOV","K0"); ac("D6980"); ac("K20")
a("FMOV","K0"); ac("D7980"); ac("K20")
a("MOV","K0"); ac("D7000"); a("MOV","K0"); ac("D7001")
a("MOV","K0"); ac("D8000"); a("MOV","K0"); ac("D8001")
# Reset model# on barcode mode + NG/complete
a("LD","M520")
a("LD","M107"); a("OR","M123")
a("OR","M108"); a("OR","M109"); a("OR","M124"); a("OR","M125")
a("OR","M300")
a("ANB",""); a("RST","D0"); a("RST","D32")

al("DISPLAY CORRECTION")
a("LD","M0"); a("DMOV","D12"); ac("D100")
for k in range(1,26):
    base = 300 + (k-1)*9
    a("LD","M0"); a("AND=","D0"); ac(f"K{k}")
    a("D+",f"D{base+4}"); ac("D100"); ac("D100")
a("LD","M0"); a("DMOV","D44"); ac("D110")
for k in range(1,26):
    base = 550 + (k-1)*9
    a("LD","M0"); a("AND=","D32"); ac(f"K{k}")
    a("D+",f"D{base+4}"); ac("D110"); ac("D110")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\indexs.csv")
