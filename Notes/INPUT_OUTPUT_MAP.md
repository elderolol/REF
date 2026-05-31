# Input/Output Map — Physical I/O ↔ Internal Logic Mapping

> **목적**: 물리적 X/Y 주소 변경 시 `input.csv` / `output.csv`만 수정하면 프로그램 본체 수정 불필요  
> **원칙**: Ladder Logic은 **절대로 X/Y를 직접 참조하지 않음**. 항상 M을 통해 간접 참조.

---

## 1. input.csv — Physical Input Mapping

실제 입력 디바이스(X)를 내부 릴레이(M)에 매핑.

### Format

| X_Addr | M_Addr | Signal Name | Line | Description |
|:------:|:------:|-------------|:----:|-------------|
| `X00` | `M300` | START_PB_L0 | L0 | Line 0 Start Push Button (NO) |
| `X01` | `M301` | STOP_PB_L0 | L0 | Line 0 Stop Push Button (NC) |
| `X02` | `M302` | SAFETY_RESET | L0 | Safety PLC Reset Request |
| `X03` | `M303` | EMG_STOP | L0 | Emergency Stop (NC) |
| `X04` | `M304` | GUN_COUPLER_L0_G0 | L0 | Line 0 Gun A Coupler Sensor |
| `X05` | `M305` | GUN_COUPLER_L0_G1 | L0 | Line 0 Gun B Coupler Sensor |
| `X06` | `M306` | VAC_PUMP_FB_L0 | L0 | Line 0 Vacuum Pump Run FB |
| `X07` | `M307` | DOOR_SENSOR_L0 | L0 | Line 0 Door Limit (방폭 전용) |
| `X08` | `M308` | PRESSURE_SW_H_L0 | L0 | Line 0 Pressure High Switch |
| `X09` | `M309` | PRESSURE_SW_L_L0 | L0 | Line 0 Pressure Low Switch |
| `X0A` | `M30A` | REFRIG_SUPPLY_OK_L0 | L0 | Line 0 Refrigerant Supply OK |
| `X0B` | `M30B` | SAFETY_PLC_HEALTHY | L0 | Safety PLC Healthy Signal |
| `X0C~X0F` | `M30C~M30F` | SPARE_DI_L0 | L0 | 예비 DI |

| X_Addr | M_Addr | Signal Name | Line | Description |
|:------:|:------:|-------------|:----:|-------------|
| `X10` | `M310` | START_PB_L1 | L1 | Line 1 Start Push Button |
| `X11` | `M311` | STOP_PB_L1 | L1 | Line 1 Stop Push Button |
| `X12` | `M312` | SPARE_L1 | L1 | 예비 |
| `X13` | `M313` | EMG_STOP_L1 | L1 | Line 1 Emergency Stop |
| `X14` | `M314` | GUN_COUPLER_L1_G0 | L1 | Line 1 Gun A Coupler Sensor |
| `X15` | `M315` | GUN_COUPLER_L1_G1 | L1 | Line 1 Gun B Coupler Sensor |
| `X16` | `M316` | VAC_PUMP_FB_L1 | L1 | Line 1 Vacuum Pump Run FB |
| `X17` | `M317` | DOOR_SENSOR_L1 | L1 | Line 1 Door Limit (방폭 전용) |
| `X18` | `M318` | PRESSURE_SW_H_L1 | L1 | Line 1 Pressure High Switch |
| `X19` | `M319` | PRESSURE_SW_L_L1 | L1 | Line 1 Pressure Low Switch |
| `X1A` | `M31A` | REFRIG_SUPPLY_OK_L1 | L1 | Line 1 Refrigerant Supply OK |
| `X1B~X1F` | `M31B~M31F` | SPARE_DI_L1 | L1 | 예비 DI |

### Coding Pattern (Ladder)

```
// input.csv 에 정의된 대로 매 scanning 마다 X → M 복사
// idata.csv 에서 처리
LD  X00    // START_PB_L0
OUT M300

LD  X01    // STOP_PB_L0
OUT M301
// ... (이하 동일)
```

> **변경 방법**: X 주소가 바뀌면 `input.csv`의 X_Addr만 수정.  
> 프로그램 내 `M300~M31F` 참조는 그대로 유지.

---

## 2. output.csv — Physical Output Mapping

내부 릴레이(M)를 실제 출력 디바이스(Y)에 매핑.

### Format

| M_Addr | Y_Addr | Signal Name | Line | Description |
|:------:|:------:|-------------|:----:|-------------|
| `M350` | `Y10` | VAC_PUMP_RUN_L0 | L0 | Line 0 Vacuum Pump Run |
| `M351` | `Y11` | LINE_VAC_SOL_L0 | L0 | Line 0 Line Vacuum Solenoid |
| `M352` | `Y12` | LINE_STEM_SOL_L0 | L0 | Line 0 Line Stem Solenoid |
| `M353` | `Y13` | REFRIG_BASE_SOL_L0_G0 | L0 | Line 0 Gun A Refrig Base/Fast Sol |
| `M354` | `Y14` | REFRIG_NORMAL_SOL_L0_G0 | L0 | Line 0 Gun A Refrig Normal Sol |
| `M355` | `Y15` | OIL_BASE_SOL_L0_G0 | L0 | Line 0 Gun A Oil Base/Fast Sol |
| `M356` | `Y16` | OIL_NORMAL_SOL_L0_G0 | L0 | Line 0 Gun A Oil Normal Sol |
| `M357` | `Y17` | REFRIG_BASE_SOL_L0_G1 | L0 | Line 0 Gun B Refrig Base/Fast Sol |
| `M358` | `Y18` | REFRIG_NORMAL_SOL_L0_G1 | L0 | Line 0 Gun B Refrig Normal Sol |
| `M359` | `Y19` | OIL_BASE_SOL_L0_G1 | L0 | Line 0 Gun B Oil Base/Fast Sol |
| `M35A` | `Y1A` | OIL_NORMAL_SOL_L0_G1 | L0 | Line 0 Gun B Oil Normal Sol |
| `M35B` | `Y1B` | EXHAUST_SOL_L0 | L0 | Line 0 Exhaust Solenoid |
| `M35C` | `Y1C` | SAFETY_RESET_ACK | L0 | Safety PLC Reset Acknowledge |
| `M35D~M35F` | `Y1D~Y1F` | SPARE_DO_L0 | L0 | 예비 DO |

| M_Addr | Y_Addr | Signal Name | Line | Description |
|:------:|:------:|-------------|:----:|-------------|
| `M360` | `Y20` | VAC_PUMP_RUN_L1 | L1 | Line 1 Vacuum Pump Run |
| `M361` | `Y21` | LINE_VAC_SOL_L1 | L1 | Line 1 Line Vacuum Solenoid |
| `M362` | `Y22` | LINE_STEM_SOL_L1 | L1 | Line 1 Line Stem Solenoid |
| `M363` | `Y23` | REFRIG_BASE_SOL_L1_G0 | L1 | Line 1 Gun A Refrig Base/Fast Sol |
| `M364` | `Y24` | REFRIG_NORMAL_SOL_L1_G0 | L1 | Line 1 Gun A Refrig Normal Sol |
| `M365` | `Y25` | OIL_BASE_SOL_L1_G0 | L1 | Line 1 Gun A Oil Base/Fast Sol |
| `M366` | `Y26` | OIL_NORMAL_SOL_L1_G0 | L1 | Line 1 Gun A Oil Normal Sol |
| `M367` | `Y27` | REFRIG_BASE_SOL_L1_G1 | L1 | Line 1 Gun B Refrig Base/Fast Sol |
| `M368` | `Y28` | REFRIG_NORMAL_SOL_L1_G1 | L1 | Line 1 Gun B Refrig Normal Sol |
| `M369` | `Y29` | OIL_BASE_SOL_L1_G1 | L1 | Line 1 Gun B Oil Base/Fast Sol |
| `M36A` | `Y2A` | OIL_NORMAL_SOL_L1_G1 | L1 | Line 1 Gun B Oil Normal Sol |
| `M36B` | `Y2B` | EXHAUST_SOL_L1 | L1 | Line 1 Exhaust Solenoid |
| `M36C~M36F` | `Y2C~Y2F` | SPARE_DO_L1 | L1 | 예비 DO |

| M_Addr | Y_Addr | Signal Name | Line | Description |
|:------:|:------:|-------------|:----:|-------------|
| `M370` | `Y30` | BUZZER | G | 부저 출력 |
| `M371` | `Y31` | LAMP_GREEN | G | 운전 중 램프 (Green) |
| `M372` | `Y32` | LAMP_RED | G | 알람 램프 (Red) |
| `M373` | `Y33` | LAMP_YELLOW | G | 경고 램프 (Yellow) |
| `M374~M37F` | `Y34~Y3F` | SPARE_DO_G | G | 예비 DO (Global) |

### Coding Pattern (Ladder)

```
// output.csv 에 정의된 대로 매 scanning 마다 M → Y 복사
// idata.csv 에서 처리 (input 매핑과 동일 POU)
LD  M350    // VAC_PUMP_RUN_L0
OUT Y10

LD  M351    // LINE_VAC_SOL_L0
OUT Y11
// ... (이하 동일)
```

> **변경 방법**: Y 주소가 바뀌면 `output.csv`의 Y_Addr만 수정.  
> 프로그램 내 `M350~M37F` 참조는 그대로 유지.

---

## 3. HMI Button Mapping (M → HMI)

HMI 버튼 → PLC M bit 매핑. HMI는 푸시 시 ON, 떼면 OFF (Momentary).  
PLC가 상태를 기억해야 하는 경우 (ALT 동작) M bit를 PLC 내부에서 Self-Hold 또는 Toggle 처리.

| M_Addr | HMI Button | Action Type | Description |
|:------:|------------|:-----------:|-------------|
| `M400` | LINE 0 SELECT | SELF-HOLD | Line 0 선택 |
| `M401` | LINE 1 SELECT | SELF-HOLD | Line 1 선택 |
| `M402` | INTERLOCK USE/NOT USE | TOGGLE | 인터락 토글 |
| `M403` | ALARM RESET | ONESHOT | 알람 리셋 |
| `M404` | BUZZER STOP | ONESHOT | 부저 정지 |
| `M405` | USER SETTING SCREEN | ONESHOT | 화면 이동 |
| `M406` | PARAMETER SETTING SCREEN | ONESHOT | 화면 이동 |
| `M407` | ALARM SCREEN | ONESHOT | 화면 이동 |
| `M408` | GUN SELECT A | SELF-HOLD | Gun A 선택 |
| `M409` | GUN SELECT B | SELF-HOLD | Gun B 선택 |
| `M40A` | NUMBER OF INJECTIONS RESET | ONESHOT | 주입 횟수 리셋 |
| `M40B` | MODEL SELECT | ONESHOT | 모델 선택 |
| `M40C` | VACUUM PUMP ON/OFF | TOGGLE | 진공 펌프 ON/OFF |
| `M40D` | BARCODE USE/NOT USE | TOGGLE | 바코드 토글 |
| `M40E` | MANUAL/AUTO | TOGGLE | 모드 전환 |
| `M40F` | GUN VACUUM (Manual) | ONESHOT | 건 진공 수동 시작 |
| `M410` | UNIT VACUUM (Manual) | ONESHOT | 유닛 진공 수동 시작 |
| `M411` | VACUUM CHECK (Manual) | ONESHOT | 진공 체크 수동 시작 |
| `M412` | REFRIG INJECTION (Manual) | ONESHOT | 냉매 주입 수동 시작 |
| `M413` | START (Line 0) | ONESHOT | Line 0 Auto Start |
| `M414` | STOP (Line 0) | ONESHOT | Line 0 Stop |
| `M415` | START (Line 1) | ONESHOT | Line 1 Auto Start |
| `M416` | STOP (Line 1) | ONESHOT | Line 1 Stop |
| `M417~M41F` | — | — | 예비 HMI 버튼 |

> **Action Type 설명**:
> - **ONESHOT**: HMI가 1 scan만 ON → PLC가 rising edge 감지 후 내부 처리
> - **SELF-HOLD**: HMI가 ON을 유지 → PLC가 Self-Hold 회로로 상태 유지
> - **TOGGLE**: HMI 누를 때마다 PLC 내부 상태 반전
> - **HMI 버튼 자체는 전부 Momentary** (누를 때만 ON). 상태 기억/토글은 PLC에서 처리.

---

## 4. Analog Input Mapping (AI → D)

| Channel | Line | Raw Addr | EU Addr | Signal | Range |
|:-------:|:----:|:--------:|:-------:|--------|-------|
| CH0 | L0 | `D120` | `D122` | Pressure | D14~D16 설정 (kgf/㎠) |
| CH1 | L0 | `D124` | `D126` | Temperature | -20.0~80.0℃ |
| CH2 | L0 | `D128` | `D130~D131` | Vacuum | 0~760 Torr |
| CH0 | L1 | `D132` | `D134` | Pressure | (D228≥2) |
| CH1 | L1 | `D136` | `D138` | Temperature | (D228≥2) |
| CH2 | L1 | `D140` | `D142~D143` | Vacuum | (D228≥2) |

> **ad.csv** 에서 처리: Raw → EU 변환 후 D 레지스터 갱신.
> HSC (Flow Meter Pulse)는 별도 고속 카운터 채널 사용.

---

## 5. 변경 시 영향 범위

| 변경 사항 | 수정 파일 | 프로그램 본체 영향 |
|-----------|:---------:|:------------------:|
| X 주소 변경 | `input.csv` | **없음** (M 참조 그대로) |
| Y 주소 변경 | `output.csv` | **없음** (M 참조 그대로) |
| I/O 증설 (DI/DO 추가) | `input.csv` + `output.csv` | 해당 M 사용하는 로직만 영향 |
| HMI 버튼 추가 | HMI 설정 + 매핑 테이블 | 해당 M 사용 로직 추가 필요 |
| 센서  → 다른 X | `input.csv` | **없음** |
| 솔레노이드 → 다른 Y | `output.csv` | **없음** |
