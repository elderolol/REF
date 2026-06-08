# IDATA — I/O Mapping, System Flags, Physical X↔M Mirror, M↔Y Mapping
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

al("SYSTEM FLAGS")
a("LD","SM400"); a("OUT","M0")
a("LD","SM401"); a("OUT","M1")
a("LD","SM402"); a("OUT","M2")
# M3: 1-second clock
a("LD","SM412"); a("OUT","M3")

al("INPUT MAPPING (X → M)")
# X0A0-X0AF (16 inputs) → M768-M783
a("LD","X0A0"); a("OUT","M768")
a("LD","X0A1"); a("OUT","M769")
a("LD","X0A2"); a("OUT","M770")   # EMG N/C
a("LD","X0A3"); a("OUT","M771")   # Door
a("LD","X0A4"); a("OUT","M772")   # Pump fault
a("LD","X0A5"); a("OUT","M773")   # Gun coupler L1
a("LD","X0A6"); a("OUT","M774")
a("LD","X0A7"); a("OUT","M775")
a("LD","X0A8"); a("OUT","M776")
a("LD","X0A9"); a("OUT","M777")
a("LD","X0AA"); a("OUT","M778")
a("LD","X0AB"); a("OUT","M779")
a("LD","X0AC"); a("OUT","M780")   # Interlock L1-1
a("LD","X0AD"); a("OUT","M781")   # Interlock L1-2
a("LD","X0AE"); a("OUT","M782")   # Interlock L1-3
a("LD","X0AF"); a("OUT","M783")   # Interlock L1-4
# X0B0-X0B5 → M784-M795
a("LD","X0B0"); a("OUT","M784")   # Gun coupler L2
a("LD","X0B1"); a("OUT","M785")
a("LD","X0B2"); a("OUT","M786")
a("LD","X0B3"); a("OUT","M787")
a("LD","X0B4"); a("OUT","M788")
a("LD","X0B5"); a("OUT","M789")
a("LD","X0B6"); a("OUT","M790")
a("LD","X0B7"); a("OUT","M791")   # Interlock L2-1
a("LD","X0B8"); a("OUT","M792")   # Interlock L2-2
a("LD","X0B9"); a("OUT","M793")   # Interlock L2-3
a("LD","X0BA"); a("OUT","M794")   # Interlock L2-4
a("LD","X0BB"); a("OUT","M795")   # Interlock L2-5

al("INTERLOCK WIRING")
# L1 interlock: M81-M85 assigned from X mirrors
a("LD","M780"); a("OUT","M81")
a("LD","M781"); a("OUT","M82")
a("LD","M782"); a("OUT","M83")
a("LD","M783"); a("OUT","M84")
a("LD","M0");  a("OUT","M85")   # spare (always ON)
# L2 interlock: M91-M95
a("LD","M791"); a("OUT","M91")
a("LD","M792"); a("OUT","M92")
a("LD","M793"); a("OUT","M93")
a("LD","M794"); a("OUT","M94")
a("LD","M0");  a("OUT","M95")   # spare

al("OUTPUT MAPPING (M → Y)")
# L1 solenoids → physical outputs
a("LD","M60"); a("OUT","Y020")   # VAC SOL L1
a("LD","M61"); a("OUT","Y021")   # STEM SOL L1
a("LD","M62"); a("OUT","Y022")   # FAST SOL L1
a("LD","M63"); a("OUT","Y023")   # BASE SOL L1
a("LD","M64"); a("OUT","Y024")   # EXHAUST SOL L1
# L2 solenoids
a("LD","M70"); a("OUT","Y030")   # VAC SOL L2
a("LD","M71"); a("OUT","Y031")   # STEM SOL L2
a("LD","M72"); a("OUT","Y032")   # FAST SOL L2
a("LD","M73"); a("OUT","Y033")   # BASE SOL L2
a("LD","M74"); a("OUT","Y034")   # EXHAUST SOL L2
# L3 oil solenoids GUN A
a("LD","M65"); a("OUT","Y025")   # OIL FAST SOL GUN A
a("LD","M66"); a("OUT","Y026")   # OIL BASE SOL GUN A
# L3 oil solenoids GUN B
a("LD","M75"); a("OUT","Y028")   # OIL FAST SOL GUN B
a("LD","M76"); a("OUT","Y029")   # OIL BASE SOL GUN B
# Global outputs
a("LD","M69"); a("OUT","Y040")   # BUZZER
a("LD","M77"); a("OUT","Y041")   # GREEN lamp
a("LD","M78"); a("OUT","Y042")   # RED lamp
a("LD","M79"); a("OUT","Y043")   # YELLOW lamp
a("LD","M67"); a("OUT","Y044")   # VAC PUMP
a("LD","M96"); a("OUT","Y045")   # HYDRO PUMP
a("LD","M97"); a("OUT","Y046")   # OIL LINE SOL
a("LD","M98"); a("OUT","Y047")   # HEATER RELAY (OFF=Gun A, ON=Gun B)
a("LD","M68"); a("OUT","Y027")   # LINE VAC SOL (shared, N/O)

al("HMI BUTTON BUFFER")
# HMI buttons → momentary M bits (direct X→M mapping for button area)
# M400-M411 assigned to HMI fixed button addresses
a("LD","M400"); a("OUT","M400")   # GUN A
a("LD","M401"); a("OUT","M401")   # GUN B
a("LD","M402"); a("OUT","M402")   # AUTO/MANUAL
a("LD","M403"); a("OUT","M403")   # GUN VAC
a("LD","M404"); a("OUT","M404")   # UNIT VAC
a("LD","M405"); a("OUT","M405")   # VAC CHECK
a("LD","M406"); a("OUT","M406")   # OIL INJ
a("LD","M407"); a("OUT","M407")   # REFRIG INJ
a("LD","M408"); a("OUT","M408")   # START
a("LD","M409"); a("OUT","M409")   # STOP
a("LD","M410"); a("OUT","M410")   # ALARM RESET
a("LD","M411"); a("OUT","M411")   # BUZZER STOP
a("LD","M412"); a("OUT","M412")   # VAC PUMP ON/OFF
a("LD","M413"); a("OUT","M413")   # INTERLOCK USE/NOT USE
a("LD","M414"); a("OUT","M414")   # L1 INJECTION COUNT RESET
a("LD","M415"); a("OUT","M415")   # OIL+REFRIG ENABLE
a("LD","M416"); a("OUT","M416")   # L2 INJECTION COUNT RESET
a("LD","M417"); a("OUT","M417")   # L1 USAGE RESET
a("LD","M418"); a("OUT","M418")   # L2 USAGE RESET
a("LD","M419"); a("OUT","M419")   # HYDRO PUMP

a("END","")
wr("C:/WorkSpace/2L2GOIL/src\\idata.csv")
