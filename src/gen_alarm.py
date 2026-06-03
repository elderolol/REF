# ALARM LATCH ??self-holding conversion
# M865-M879 use self-holding OUT (LD cond OR self ANI reset)
# M864 keeps SET/RST (also SET in gen_main_final.py EMERGENCY STOP)
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

R = "M1027"  # alarm reset (HMI momentary button, no PLS needed)

hd("REF_self_holding")
al("ALARM LATCH")
# M864: emergency stop ??self-holding (MAIN no longer SETs it directly)
a("LDI", "M771"); a("OR", "M864"); a("ANI", R); a("OUT", "M864")

# M865: door open ??self-holding
a("LDI", "M779"); a("OR", "M865"); a("ANI", R); a("OUT", "M865")

# M866: M817 OR M833 (vac mismatch)
a("LD", "M817"); a("OR", "M833"); a("OR", "M866"); a("ANI", R); a("OUT", "M866")

# M867: M819 OR M835
a("LD", "M819"); a("OR", "M835"); a("OR", "M867"); a("ANI", R); a("OUT", "M867")

# M868: M821 OR M837
a("LD", "M821"); a("OR", "M837"); a("OR", "M868"); a("ANI", R); a("OUT", "M868")

# M869: M823 OR M839
a("LD", "M823"); a("OR", "M839"); a("OR", "M869"); a("ANI", R); a("OUT", "M869")

# M870: always-on alarm (unconditional self-hold)
a("LD", "M0"); a("OR", "M870"); a("ANI", R); a("OUT", "M870")

# M871: always-on alarm (unconditional self-hold)
a("LD", "M0"); a("OR", "M871"); a("ANI", R); a("OUT", "M871")

# M872: M776 OR M792
a("LD", "M776"); a("OR", "M792"); a("OR", "M872"); a("ANI", R); a("OUT", "M872")

# M873: M777 OR M793
a("LD", "M777"); a("OR", "M793"); a("OR", "M873"); a("ANI", R); a("OUT", "M873")

# M874: D156 < -200 OR D156 > 800
a("LD<", "D156"); ac("K-200"); a("OR>", "D156"); ac("K800")
a("OR", "M874"); a("ANI", R); a("OUT", "M874")

# M878: always-on alarm
a("LD", "M0"); a("OR", "M878"); a("ANI", R); a("OUT", "M878")

# M879: M791
a("LD", "M791"); a("OR", "M879"); a("ANI", R); a("OUT", "M879")

# ===== BUZZER =====
al("BUZZER")
a("LD", "M864"); a("OR", "M865"); a("OR", "M866"); a("OR", "M867")
a("OR", "M868"); a("OR", "M869"); a("OR", "M870"); a("OR", "M871")
a("OR", "M872"); a("OR", "M873"); a("OR", "M874")
a("OR", "M876"); a("OR", "M877"); a("OR", "M878"); a("OR", "M879")
a("ANI", "M500"); a("OUT", "M76")

# Buzzer silence
a("LD", "M1028"); a("SET", "M500")
a("LD", "M1028"); a("RST", "M76")

# ===== ALARM RESET =====
# M1027 is HMI momentary button — direct use, no PLS needed
al("ALARM RESET")
# M876 SET by indexs PC DATA CHECK
a("LD", R); a("RST", "M876")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\alarm.csv")

