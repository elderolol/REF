# ALARM — Per-line + L3 oil alarms, buzzer (M69), lamp colors
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

R = "M410"
hd("REF_self_holding")

al("SHARED ALARMS")
a("LDI","M770"); a("OR","M300"); a("ANI",R); a("OUT","M300")
a("LDI","M771"); a("AND","M522"); a("OR","M301"); a("ANI",R); a("OUT","M301")
a("LDD>=","D300"); ac("D210"); a("OR","M302"); a("ANI",R); a("OUT","M302")
a("LDI","M772"); a("OR","M303"); a("ANI",R); a("OUT","M303")

al("L1 ALARMS")
a("LD","M12"); a("AND","T1"); a("OR","M310"); a("ANI",R); a("OUT","M310")
a("LD","M13"); a("AND","T2"); a("OR","M311"); a("ANI",R); a("OUT","M311")
a("LD","M109"); a("OR","M312"); a("ANI",R); a("OUT","M312")
a("LD","M110"); a("OR","M313"); a("ANI",R); a("OUT","M313")
a("LD","M314"); a("OR","M314"); a("ANI",R); a("OUT","M314")    # L1 amount NG
a("LDD>=","D26"); ac("D28"); a("OR","M316"); a("ANI",R); a("OUT","M316")
a("LDD<=","D26"); ac("D30"); a("OR","M317"); a("ANI",R); a("OUT","M317")
a("LDD<","D28"); ac("K-200"); a("OR>","D28"); a("LDD>","D28"); ac("K800"); a("ORB","")
a("OR","M318"); a("ANI",R); a("OUT","M318")
a("LD","M11"); a("AND=","D0"); ac("K0"); a("OR","M319"); a("ANI",R); a("OUT","M319")
a("LD","M11"); a("LDD=","D12"); ac("K0"); a("OR","M320"); a("ANI",R); a("OUT","M320")

al("L2 ALARMS")
a("LD","M32"); a("AND","T7"); a("OR","M330"); a("ANI",R); a("OUT","M330")
a("LD","M33"); a("AND","T8"); a("OR","M331"); a("ANI",R); a("OUT","M331")
a("LD","M125"); a("OR","M332"); a("ANI",R); a("OUT","M332")
a("LD","M126"); a("OR","M333"); a("ANI",R); a("OUT","M333")
a("LD","M334"); a("OR","M334"); a("ANI",R); a("OUT","M334")    # L2 amount NG
a("LDD>=","D58"); ac("D60"); a("OR","M336"); a("ANI",R); a("OUT","M336")
a("LDD<=","D58"); ac("D62"); a("OR","M337"); a("ANI",R); a("OUT","M337")
a("LDD<","D60"); ac("K-200"); a("OR>","D60"); a("LDD>","D60"); ac("K800"); a("ORB","")
a("OR","M338"); a("ANI",R); a("OUT","M338")
a("LD","M31"); a("AND=","D32"); ac("K0"); a("OR","M339"); a("ANI",R); a("OUT","M339")
a("LD","M31"); a("LDD=","D44"); ac("K0"); a("OR","M340"); a("ANI",R); a("OUT","M340")

al("L3 OIL ALARMS")
a("LD","M51"); a("AND","T13"); a("OR","M350"); a("ANI",R); a("OUT","M350")
a("LD","M351"); a("OR","M351"); a("ANI",R); a("OUT","M351")    # oil amount NG

al("BUZZER")
a("LD","M300")
for b in ["301","302","303","310","311","312","313","314","316","317","318","319","320",
          "330","331","332","333","334","336","337","338","339","340","350","351"]:
    a("OR",("M"+b))
a("ANI","M500"); a("OUT","M69")     # M69 = BUZZER
a("LD","M411"); a("SET","M500")
a("LD","M411"); a("RST","M69")

al("ALARM RESET")
a("LD",R); a("RST","M500")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\alarm.csv")
