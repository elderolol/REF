# ALARM LATCH — all self-holding OUT
# M76 buzzer: self-holding, one central rung (no double-coil)
# M500 silence: self-holding latch
# HMI bits M1027/M1028: momentary, used directly

st = 0; lines = []
def a(i,d): global st; lines.append(f'"{st}"\t""\t"{i}"\t"{d}"\t""\t""\t""'); st += 1
def ac(d): lines.append(f'""\t""\t""\t"{d}"\t""\t""\t""')
def al(t): global st; lines.append(f'"{st}"\t">> {t}"\t""\t""\t""\t""\t""'); st += 1
def hd(n):
    lines.append(f'"{n}"')
    lines.append('"PLC Information:"\t"QCPU (Q mode) Q03UDV"')
    lines.append('"Step No."\t"Line Statement"\t"Instruction"\t"I/O(Device)"\t"Blank"\t"PI Statement"\t"Note"')
def wr(p):
    c = "\r\n".join(lines) + "\r\n"
    with open(p, "wb") as f: f.write(b'\xff\xfe'); f.write(c.encode('utf-16-le'))

R = "M1027"   # alarm reset (HMI momentary)
SILENCE = "M1028"  # buzzer silence (HMI momentary)

hd("REF_self_holding")

# ===== ALARM LATCHES (self-holding) =====
al("ALARM LATCH")

# M864: emergency stop → door interlock
a("LDI", "M771"); a("OR", "M864"); a("ANI", R); a("OUT", "M864")

# M865: door open
a("LDI", "M779"); a("OR", "M865"); a("ANI", R); a("OUT", "M865")

# M866: vac mismatch L0 (M817 from gunvac)
a("LD", "M817"); a("OR", "M833"); a("OR", "M866"); a("ANI", R); a("OUT", "M866")

# M867: vac mismatch unit L0 (M819 from unitvac)
a("LD", "M819"); a("OR", "M835"); a("OR", "M867"); a("ANI", R); a("OUT", "M867")

# M868: vac leak L0 (M821 from vacchec)
a("LD", "M821"); a("OR", "M837"); a("OR", "M868"); a("ANI", R); a("OUT", "M868")

# M869: vac leak alarm (M823/M839 from vacchec + M320/M336 timeout from refinj)
a("LD", "M823"); a("OR", "M839"); a("OR", "M320"); a("OR", "M336")
a("OR", "M869"); a("ANI", R); a("OUT", "M869")

# M870-M871: reserved

# M872: gas check L1A
a("LD", "M776"); a("OR", "M792"); a("OR", "M872"); a("ANI", R); a("OUT", "M872")

# M873: gas check L1B
a("LD", "M777"); a("OR", "M793"); a("OR", "M873"); a("ANI", R); a("OUT", "M873")

# M874: temperature out of range (D156 < -200 OR D156 > 800)
a("LD<", "D156"); ac("K-200")
a("OR>", "D156"); ac("K800")
a("OR", "M874"); a("ANI", R); a("OUT", "M874")

# M875: L0 bombe alarm (SET in spc.csv, 1:1)
# M876: L0 PC data error (SET in indexs.csv, 1:1)
# M877: L1 PC data error (SET in indexs.csv, 1:1)
# M878: L1 bombe alarm (SET in spc.csv, 1:1)

# M879: L1 interlock fail
a("LD", "M791"); a("OR", "M879"); a("ANI", R); a("OUT", "M879")

# ===== BUZZER (self-holding) =====
al("BUZZER")
# M500: buzzer silence latch. ON when silence pressed, OFF on alarm reset.
a("LD", SILENCE); a("OR", "M500"); a("ANI", R); a("OUT", "M500")

# M76 buzzer: ON when any alarm AND not silenced. OFF on silence button.
a("LD", "M864"); a("OR", "M865"); a("OR", "M866"); a("OR", "M867")
a("OR", "M868"); a("OR", "M869"); a("OR", "M872"); a("OR", "M873"); a("OR", "M874")
a("OR", "M875"); a("OR", "M876"); a("OR", "M877"); a("OR", "M878"); a("OR", "M879")
a("ANI", "M500")
a("OR", "M76")
a("ANI", SILENCE)
a("OUT", "M76")

# ===== ALARM RESET ACTIONS =====
al("ALARM RESET")
a("LD", R); a("RST", "M875")  # L0 bombe
a("LD", R); a("RST", "M876")  # L0 PC data error
a("LD", R); a("RST", "M877")  # L1 PC data error
a("LD", R); a("RST", "M878")  # L1 bombe

a("END","")
wr("F:\\WorkSpace\\REF\\src2\\alarm.csv")
