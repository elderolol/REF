# REF_COMMENT ??Device Comments (decimal addresses)
st = 0; lines = []
def a(i,d): global st; lines.append(f'"{st}"\t""\t"{i}"\t"{d}"\t""\t""\t""'); st += 1
def ac(d): lines.append(f'""\t""\t""\t"{d}"\t""\t""\t""')
def al(t): global st; lines.append(f'"{st}"\t">> {t}"\t""\t""\t""\t""\t""'); st += 1
def hd(n):
    lines.append(f'"{n}"'); lines.append('"PLC Information:"\t"QCPU (Q mode) Q03UDV"')
    lines.append('"Step No."\t"Line Statement"\t"Instruction"\t"I/O(Device)"\t"Blank"\t"PI Statement"\t"Note"')
def com(dev, c): lines.append(f'""\t""\t""\t"{dev}"\t""\t""\t"{c}"')
def wr(p):
    c = "\r\n".join(lines) + "\r\n"
    with open(p, "wb") as f: f.write(b'\xff\xfe'); f.write(c.encode('utf-16-le'))

hd("REF_self_holding")
al("DEVICE COMMENTS")

# Steps
com("M10","L1 IDLE"); com("M11","L1 PRECHECK"); com("M12","L1 GUN VAC"); com("M13","L1 UNIT VAC")
com("M14","L1 VAC CHECK"); com("M15","L1 REFRIG FAST"); com("M16","L1 REFRIG BASE")
com("M17","L1 EXHAUST"); com("M18","L1 COMPLETE")
com("M30","L2 IDLE"); com("M31","L2 PRECHECK"); com("M32","L2 GUN VAC"); com("M33","L2 UNIT VAC")
com("M34","L2 VAC CHECK"); com("M35","L2 REFRIG FAST"); com("M36","L2 REFRIG BASE")
com("M37","L2 EXHAUST"); com("M38","L2 COMPLETE")
com("M50","L3 OIL IDLE"); com("M51","L3 OIL FAST"); com("M52","L3 OIL BASE"); com("M53","L3 OIL COMPLETE")
# Solenoids
com("M60","VAC SOL A"); com("M61","STEM SOL A"); com("M62","FAST SOL A"); com("M63","BASE SOL A")
com("M64","EXHAUST SOL A"); com("M65","OIL FAST A"); com("M66","OIL BASE A")
com("M67","VAC PUMP"); com("M68","LINE VAC SOL"); com("M69","BUZZER")
com("M70","VAC SOL B"); com("M71","STEM SOL B"); com("M72","FAST SOL B"); com("M73","BASE SOL B")
com("M74","EXHAUST SOL B"); com("M75","OIL FAST B"); com("M76","OIL BASE B")
com("M77","GREEN"); com("M78","RED"); com("M79","YELLOW")
# Results L1
com("M100","L1 PRECHECK OK"); com("M101","L1 GUN VAC OK"); com("M102","L1 UNIT VAC OK")
com("M103","L1 VAC CHECK OK"); com("M104","L1 REFRIG FAST OK"); com("M105","L1 REFRIG BASE OK")
com("M106","L1 EXHAUST OK"); com("M107","L1 COMPLETE"); com("M108","L1 GUN VAC NG")
com("M109","L1 UNIT VAC/LEAK NG"); com("M110","L1 INJ NG"); com("M111","L1 VAC NG spare")
# Results L2
com("M116","L2 PRECHECK OK"); com("M117","L2 GUN VAC OK"); com("M118","L2 UNIT VAC OK")
com("M119","L2 VAC CHECK OK"); com("M120","L2 REFRIG FAST OK"); com("M121","L2 REFRIG BASE OK")
com("M122","L2 EXHAUST OK"); com("M123","L2 COMPLETE"); com("M124","L2 GUN VAC NG")
com("M125","L2 VAC/LEAK NG"); com("M126","L2 INJ NG"); com("M127","L2 VAC NG spare")
com("M145","OIL FAST OK"); com("M146","OIL BASE OK"); com("M147","OIL COMPLETE")
# Mode/Gun/Ready
com("M200","MANUAL"); com("M201","AUTO"); com("M210","GUN A"); com("M211","GUN B")
com("M220","GUN VAC READY"); com("M221","UNIT VAC READY"); com("M222","VAC CHECK READY")
com("M223","REFRIG INJ READY"); com("M224","OIL INJ READY")
# Alarms
com("M300","EMG"); com("M301","DOOR"); com("M302","BOMBE"); com("M303","PUMP")
com("M310","GUN VAC TO L1"); com("M311","UNIT VAC TO L1"); com("M312","VAC LEAK L1")
com("M313","INJ TO L1"); com("M314","INJ OVER L1"); com("M315","INJ UNDER L1")
com("M330","GUN VAC TO L2"); com("M331","UNIT VAC TO L2"); com("M332","VAC LEAK L2")
com("M333","INJ TO L2"); com("M334","INJ OVER L2"); com("M335","INJ UNDER L2")
com("M350","OIL TO"); com("M351","OIL OVER"); com("M352","OIL UNDER")
# Control
com("M450","L1 STOP"); com("M451","L2 STOP"); com("M452","EMG latch")
com("M460","WARMUP L1 PRECHECK"); com("M461","WARMUP L1 GUNVAC"); com("M462","WARMUP L1 UNITVAC")
com("M463","WARMUP VACCHECK (L1/L2)"); com("M464","WARMUP OIL");
com("M465","WARMUP L1 REFRIG"); com("M466","WARMUP L2 REFRIG")
com("M467","WARMUP L2 PRECHECK"); com("M468","WARMUP L2 GUNVAC"); com("M469","WARMUP L2 UNITVAC"); com("M470","SPC active L1"); com("M471","SPC active L2")
com("M490","STOPWATCH active")
com("M500","BUZZER MUTE"); com("M520","BARCODE"); com("M521","OIL+REFRIG EN")
com("M522","INTERLOCK EN")
# HMI
com("M400","HMI GUN A"); com("M401","HMI GUN B"); com("M402","HMI AUTO/MANUAL")
com("M403","HMI GUN VAC"); com("M404","HMI UNIT VAC"); com("M405","HMI VAC CHECK")
com("M406","HMI REFRIG INJ"); com("M407","HMI OIL INJ"); com("M408","HMI START")
com("M409","HMI STOP"); com("M410","HMI ALARM RESET"); com("M411","HMI BUZZER STOP")
com("M412","HMI VAC PUMP"); com("M413","HMI INTERLOCK EN"); com("M414","HMI COUNT RESET")
com("M415","HMI OIL+REFRIG EN")

# D registers - Parameters (32-bit ready, L1: D0-D31, L2: D32-D63)
com("D0","L1 model index (16)")         ; com("D2","L1 gun vac time (16)");
com("D4","L1 unit vac time (16)")       ; com("D6","L1 vac check time (16)");
com("D8","L1 exhaust time (16)")        ; com("D10","L1 refrig fast stop (32)");
com("D12","L1 refrig target (32)")       ; com("D14","L1 refrig tolerance (16)");
com("D16","L1 oil fast stop (32)")       ; com("D18","L1 oil target (32)");
com("D20","L1 oil tolerance (16)")       ; com("D22","L1 unit vac setting (16)");
com("D24","L1 vac check setting (16)")   ; com("D26","L1 pressure EU (16)");
com("D28","L1 temperature EU (16)")      ; com("D30","L1 vacuum EU (32)");

com("D32","L2 model index (16)")         ; com("D34","L2 gun vac time (16)");
com("D36","L2 unit vac time (16)")       ; com("D38","L2 vac check time (16)");
com("D40","L2 exhaust time (16)")        ; com("D42","L2 refrig fast stop (32)");
com("D44","L2 refrig target (32)")       ; com("D46","L2 refrig tolerance (16)");
com("D48","L2 oil fast stop (32)")       ; com("D50","L2 oil target (32)");
com("D52","L2 oil tolerance (16)")       ; com("D54","L2 unit vac setting (16)");
com("D56","L2 vac check setting (16)")   ; com("D58","L2 pressure EU (16)");
com("D60","L2 temperature EU (16)")      ; com("D62","L2 vacuum EU (32)");
com("D64","L3 temperature EU (16)");

com("D100","L1 display target (32)"); com("D102","L1 work: base refrig target (32)");
com("D104","L1 work: base oil target (32)"); com("D110","L2 display target (32)");
com("D112","L2 work: base refrig target (32)"); com("D114","L2 work: base oil target (32)");

com("D130","L1 cycle usage"); com("D150","L1 HSC count (32)"); com("D160","L2 cycle usage");
com("D170","L2 HSC count (32)"); com("D180","L3 oil HSC count (32)");

com("D200","L1 cum usage (32)"); com("D202","L1 cycle count"); com("D204","L1 cum inj (32)");
com("D206","L1 last use (32)"); com("D208","L1 last tgt (32)"); com("D210","Bombe setting (32)");
com("D220","L2 cum usage (32)"); com("D222","L2 cycle count"); com("D224","L2 cum inj (32)");
com("D226","L2 last use (32)"); com("D228","L2 last tgt (32)"); com("D230","L2 bombe set (32)")
com("D240","L1 injection count (16)"); com("D242","L2 injection count (16)")
com("D244","Stopwatch (0.1sec)");

com("D300","L1 model table (25x9)"); com("D550","L2 model table (25x9)");
com("D600","VAC CHECK work L1"); com("D602","VAC CHECK delta L1 (32)");
com("D610","VAC CHECK work L2"); com("D612","VAC CHECK delta L2 (32)");

com("D1000","L1 result code"); com("D1001","L1 step status"); com("D1002","Barcode mode");
com("D1003","Gun select"); com("D1004","L1 vacuum (32)"); com("D1006","L1 model#");
com("D1007","L1 target (32)"); com("D1009","L1 count (32)");
com("D1200","L2 result code"); com("D1201","L2 step status"); com("D1204","L2 vacuum (32)");
com("D1206","L2 model#"); com("D1207","L2 target (32)"); com("D1209","L2 count (32)");
com("D1401","L3 step status");
com("D6980","PC L1 barcode buffer (20w)"); com("D7000","PC L1 barcode status");
com("D7001","PC L1 barcode target"); com("D7020","L1 SPC log");
com("D7220","L1 barcode display (20w)");
com("D7980","PC L2 barcode buffer (20w)"); com("D8000","PC L2 barcode status");
com("D8001","PC L2 barcode target"); com("D8020","L2 SPC log");
com("D8220","L2 barcode display (20w)");

a("END","")
wr("C:\\WorkSpace\\REF\\src\\ref_comment.csv")
