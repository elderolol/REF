HARDWARE OR HMI BUTTON IS ON only when pressed.

OPERATION SCREEN  
	DISPLAY

- Refrigerant usage(32BIT) 12345.6 Kg  
- Number of injections(16BIT) 12345  
- Injection model(16BIT) 123  
- CHARGING PULSE(32BIT) 123456  
- Injection time(16BIT) 123.4 sec  
- Injection setting amount(32BIT) 12345 g  
- Actual injection volume(32BIT) 12345 g  
- SCAN injection volume(16BIT) 12345 g  
- Current vacuum level(32BIT) 123.456 Torr  
- TEMPERATURE(16bit) 12.3 ℃   
- PRESSURE(16bit) 12.3 kgf/㎠  
    
  LABEL  
- “OPERATION SCREEN”  
- “REFRIGER TYPE”  
- REFRIGER TYPE  
- “EACH LINE REFRIGER USED AMOUT”  
- “GUN SELECT”  
- “INJECTION TIME”  
- “Number of injections”   
- “INJECTION MODEL”  
- “INJECTION SETTING AMOUNT”  
- “CHARGING PULS”  
- “VACUUM PUMP”  
- “REAL INJECTION AMOUNT”  
- “INJECTION TIME”  
- “VACUUM(Torr)”  
- “SCAN INFO”  
- “PRESSURE”  
- “TEMPERETURE”


BUTTON

- UNIT PASS  
- INTERLOCK USE/NOT USE  
- ALARM RESET  
- BUZZER STOP  
- USER SETTING SCREEN  
- PARAMETER SETTING SCREEN  
- ALARM SCREEN  
- EATCH GUN SELECT  
- NUMBER OF INJECTIONS RESET  
- MODEL SELECT  
- VACUUM PUMP ON/OFF  
- BARCODE USE/NOT USE  
- MANUAL/AUTO  
- GUN VACUUM  
- UNIT VACUUM  
- VACUUM CHECK  
- REFRIGER INJECTION  
- START  
- STOP

PARAMETER SETTING SCREEN  
(All items are read from the PLC, and recorded in the PLC upon input)

- GUN VACUUM TIME 12.3 sec(16bit)  
- UINT VACUUM TIME 12.3 sec(16bit)  
- VACUUM CHECK TIME 12.3 sec(16bit)  
- REFRIGER GAS EXHAUST TIME 12.3 sec(16bit)  
- REFRIGER GAS high-speed injection stop section setting 1234 g(16bit)  
- REFRIGER USED BOMBE ALARM SETTING 123456.7 Kg(32bit)  
- REFRIGER GAS USED AMOUNT 123456.7 Kg(32bit)  
- REFRIGER GAS PRESSURE HIGH LIMIT \-12.3 kgf/㎠(16bit)  
-                                                  LOW LIMIT \-12.3 kgf/㎠(16bit)  
- UNIT VACUUM SETTING VALUE \-123.456 Torr(32bit)  
- VACUUM CHECK SETTING VALUE \-123.456 Torr(32bit)  
- Injection tolerance ± 12.3 g

USER SETING SCREEN \- EATCH INJECTION GUN  
(All items are read from the PLC, and recorded in the PLC upon input)

- INJECTION AMOUNT MODEL NUMBER(16bit)  
- INJECTION AMOUNT VOLUME(32bit)  
- Value that corrects the actual measurement(16bit)  
- HMI display calibration value(16bit)  
- Batch correction amount by refrigerant gas(16bit)

REFRIGER CHARGING MACHINE

POWER ON

SAFTY PLC RESET  
HARD RESET \- RESET PUSH BUTTON  
SOFT RESET \- HMI ANY RESET BUTTON

VACUUM PUMP BUTTON ON for each line  
