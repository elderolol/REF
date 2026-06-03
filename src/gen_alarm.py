# ALARM LATCH — self-holding conversion
# L65-L79 use self-holding OUT (LD cond OR self ANI reset)
# L64 keeps SET/RST (also SET in gen_main_final.py EMERGENCY STOP)
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

R = "M750"  # alarm reset pulse

hd("alarm")
al("ALARM LATCH")
# L64: emergency stop — keep SET (also SET in gen_main_final.py EMERGENCY STOP)
a("LDI", "M771"); a("SET", "L64")

# L65: door open — self-holding
a("LDI", "M779"); a("OR", "L65"); a("ANI", R); a("OUT", "L65")

# L66: L17 OR L33 (vac mismatch)
a("LD", "L17"); a("OR", "L33"); a("OR", "L66"); a("ANI", R); a("OUT", "L66")

# L67: L19 OR L35
a("LD", "L19"); a("OR", "L35"); a("OR", "L67"); a("ANI", R); a("OUT", "L67")

# L68: L21 OR L37
a("LD", "L21"); a("OR", "L37"); a("OR", "L68"); a("ANI", R); a("OUT", "L68")

# L69: L23 OR L39
a("LD", "L23"); a("OR", "L39"); a("OR", "L69"); a("ANI", R); a("OUT", "L69")

# L70: always-on alarm (unconditional self-hold)
a("LD", "M0"); a("OR", "L70"); a("ANI", R); a("OUT", "L70")

# L71: always-on alarm (unconditional self-hold)
a("LD", "M0"); a("OR", "L71"); a("ANI", R); a("OUT", "L71")

# L72: M776 OR M792
a("LD", "M776"); a("OR", "M792"); a("OR", "L72"); a("ANI", R); a("OUT", "L72")

# L73: M777 OR M793
a("LD", "M777"); a("OR", "M793"); a("OR", "L73"); a("ANI", R); a("OUT", "L73")

# L74: D156 < -200 OR D156 > 800
a("LD<", "D156"); ac("K-200"); a("OR>", "D156"); ac("K800")
a("OR", "L74"); a("ANI", R); a("OUT", "L74")

# L78: always-on alarm
a("LD", "M0"); a("OR", "L78"); a("ANI", R); a("OUT", "L78")

# L79: M791
a("LD", "M791"); a("OR", "L79"); a("ANI", R); a("OUT", "L79")

# ===== BUZZER =====
al("BUZZER")
a("LD", "L64"); a("OR", "L65"); a("OR", "L66"); a("OR", "L67")
a("OR", "L68"); a("OR", "L69"); a("OR", "L70"); a("OR", "L71")
a("OR", "L72"); a("OR", "L73"); a("OR", "L74")
a("OR", "L76"); a("OR", "L77"); a("OR", "L78"); a("OR", "L79")
a("ANI", "M500"); a("OUT", "M76")

# Buzzer silence
a("LD", "M1028"); a("SET", "M500")
a("LD", "M1028"); a("RST", "M76")

# ===== ALARM RESET PULSE =====
al("ALARM RESET")
a("LD", "M1027"); a("PLS", R)
# L64 uses SET (also in MAIN EMERGENCY STOP), L76 SET by indexs PC DATA CHECK
a("LD", R); a("RST", "L64")
a("LD", R); a("RST", "L76")

a("END","")
wr("F:\\WorkSpace\\REF\\src\\alarm.csv")
