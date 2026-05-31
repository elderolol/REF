# REFRIGER CHARGING MACHINE — Function Spec: setting.csv

> **Module**: `setting.csv`  
> **Execution**: Always ON  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

HMI의 Parameter Setting 화면 및 User Setting 화면과 PLC D 레지스터 간의 데이터 동기화를 담당.
setting.csv를 통해 모든 시스템 설정값이 관리되며, 이 값들을 변경함으로써 장비 구성을 전환함.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| D0~D28 | Line 0 Parameter Settings (HMI 입력 수신) |
| D30~D56 | Line 1 Parameter Settings (HMI 입력 수신) |
| D60~D115 | User Settings — 4 Gun × 14 words (HMI 입력 수신) |
| D6980~D6999 | Barcode PC Write — Line 1 (40 Text) |
| D7220~D7239 | Barcode Working Area — Line 1 |
| D7980~D7999 | Barcode PC Write — Line 2 (40 Text) |
| D8220~D8239 | Barcode Working Area — Line 2 |
| D7000 / D8000 | Gas Type (PC Write) |
| D7001 / D8001 | Target Amount (PC Write) |
| M400~M416 | HMI Button Buffer (Momentary) |
| D270~D276 | System Configuration |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| D0~D28 | Line 0 Parameter — PLC에 기록, HMI에 표시 |
| D30~D56 | Line 1 Parameter |
| D60~D115 | User Settings — Gun별 저장 |
| D116~D148 | Operation Display (HMI Read용 Mirror) |
| L3 | Barcode Use Flag (→ D276 Oil Mode와 연동) |

---

## 4. Parameters 관리

### 4-1. System Configuration (D270~D276)

> **setting.csv의 핵심 역할**: 아래 값만 바꾸면 모든 장비 구성 커버.

| Addr | Width | 항목 | Range | Default | Description |
|:----:|:-----:|------|:-----:|:-------:|-------------|
| **D270** | 16 | Line Count | 1~2 | 2 | 운전 라인 수. 1이면 Line 1 로직 Skip |
| **D272** | 16 | Gun Per Line | 1~2 | 2 | 라인당 건 수. 1이면 Gun B 로직 Skip |
| **D274** | 16 | Total Gun | 1~4 | — | PLC 연산 (D270×D272), Read-Only |
| **D276** | 16 | Oil Mode | 0~1 | 0 | 0=REF Only, 1=REF+OIL |

> D270/D272 변경 시 PLC STOP 후 다운로드. D276는 운전 중 변경 가능.

### 4-2. Parameter Settings — Line 0 (D0~D29)

| Addr | Width | 항목 | Unit | Range | HMI 표시 |
|:----:|:-----:|------|:----:|:-----:|:--------:|
| **D0** | 16 | L0 Model Number | — | 0~9999 | Injection Model |
| **D2** | 16 | Gun Vacuum Time | 0.1 sec | 0~6000 | Gun Vacuum Time |
| **D4** | 16 | Unit Vacuum Time | 0.1 sec | 0~6000 | Unit Vacuum Time |
| **D6** | 16 | Vacuum Check Time | 0.1 sec | 0~6000 | Vacuum Check Time |
| **D8** | 16 | Gas Exhaust Time | 0.1 sec | 0~6000 | Gas Exhaust Time |
| **D10** | 16 | Refrig High-Speed Inj Stop | g | 0~30000 | Refrig H-Speed Stop |
| **D12** | 16 | Oil High-Speed Inj Stop | g | 0~30000 | Oil H-Speed Stop (D276=1) |
| **D14** | **32** | Refriger Bombe Alarm Setting | Kg | 0~999999 | Bombe Alarm Setting |
| **D16** | **32** | Refriger Gas Used Amount | Kg | 0~999999 | Bombe Used Amount |
| **D18** | 16 | Pressure High Limit | kgf/㎠ | 0~500 | Pressure High Limit |
| **D20** | 16 | Pressure Low Limit | kgf/㎠ | 0~500 | Pressure Low Limit |
| **D22** | **32** | Unit Vacuum Setting Value | Torr | 0~76000 | Unit Vacuum Setting |
| **D24** | **32** | Vacuum Check Setting Value | Torr | 0~76000 | Vacuum Check Setting |
| **D26** | 16 | Refrig Injection Tolerance | ±g | 0~500 | Refrig Tolerance |
| **D28** | 16 | Oil Injection Tolerance | ±g | 0~500 | Oil Tolerance (D276=1) |

### 4-3. Parameter Settings — Line 1 (D30~D59)

> D270=1 (1 Line 모드) 시 이 영역 사용 안 함.

| Addr | Width | 항목 | Unit | Addr | Width | 항목 |
|:----:|:-----:|------|:----:|:----:|:-----:|------|
| **D30** | 16 | L1 Model Number | — | **D46** | 16 | Pressure High Limit |
| **D32** | 16 | Gun Vacuum Time | 0.1 sec | **D48** | 16 | Pressure Low Limit |
| **D34** | 16 | Unit Vacuum Time | 0.1 sec | **D50** | **32** | Unit Vacuum Setting |
| **D36** | 16 | Vacuum Check Time | 0.1 sec | **D52** | **32** | Vacuum Check Setting |
| **D38** | 16 | Gas Exhaust Time | 0.1 sec | **D54** | 16 | Refrig Tolerance |
| **D40** | 16 | Refrig H-Speed Stop | g | **D56** | 16 | Oil Tolerance |
| **D42** | 16 | Oil H-Speed Stop | g | **D58~D59** | — | 예비 |

---

## 5. User Settings — Gun별 (D60~D115)

> Gun Global Index 공식: `GlobalIndex = Line × D272 + GunLocal`  
> Base Address = `D60 + (GlobalIndex × 14)`

| Global Gun | Line | Gun | Base | Type | Refrig Vol(32) | Corr | HMI Cal | Batch | Oil Vol(32) |
|:----------:|:----:|:---:|:----:|:----:|:--------------:|:----:|:-------:|:-----:|:-----------:|
| 0 (G0) | 0 | 0 | D60 | D62 | D64~D65 | D66 | D68 | D70 | D72~D73 |
| 1 (G1) | 0 | 1 | D74 | D76 | D78~D79 | D80 | D82 | D84 | D86~D87 |
| 2 (G2) | 1 | 0 | D88 | D90 | D92~D93 | D94 | D96 | D98 | D100~D101 |
| 3 (G3) | 1 | 1 | D102 | D104 | D106~D107 | D108 | D110 | D112 | D114~D115 |

### 각 필드 설명

| Offset | Width | 항목 | Description |
|:------:|:-----:|------|-------------|
| +0 | 16 | Model# | Preset Model Number (HMI 표시용) |
| +1 | 16 | Gun Type | **0**=1-Sol(Base), **1**=H+L(Fast+Normal) |
| +2~+3 | **32** | Refrig Injection Volume | 냉매 주입 목표량 (g) |
| +4 | 16 | Correction Value | 실측 보정값 |
| +5 | 16 | HMI Display Calibration | HMI 표시 보정 |
| +6 | 16 | Batch Correction | 냉매별 일괄 보정 |
| +7~+8 | **32** | Oil Injection Volume | 오일 주입 목표량 (g), D276=1 전용 |

---

## 6. Barcode Model Lookup Logic

### 6-1. Barcode = Not Used (수동 모드)

```
사용자가 MODEL 버튼(M40B)을 누름 → HMI 숫자 입력창 표시
    → Model#(Index) 입력
    → D60~D115 Table에서 해당 Index Injection Amount 검색
    → Injection Setting Amount(D128)에 로드
    → MODEL button에 Model# 표시 (D0/D30)
```

### 6-2. Barcode = Used (PC 연동 모드)

```
PC가 GMES Injection Amount Address(D180/D230)에 기록
    → 485.csv에서 수신 → Working Area(D200/D250)로 복사
    → setting.csv가 D60~D115 Table과 비교 → 일치하는 Amount 검색
    → 매칭된 Index → Model# (D0/D30)에 할당
    → 해당 Injection Amount → Injection Setting Amount(D128)에 설정
```

---

## 7. Range Check

| 항목 | Check | Action |
|------|:-----:|--------|
| D270 (Line Count) | 1~2 | 범위 외 → 강제 2 |
| D272 (Gun/Line) | 1~2 | 범위 외 → 강제 2 |
| D276 (Oil Mode) | 0~1 | 범위 외 → 강제 0 |
| 각 Time 값 | 0~6000 | 범위 외 → 강제 0 |
| 각 Tolerance | 0~500 | 범위 외 → 강제 0 |

---

## 8. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `DMOV` | D register 간 32-bit 데이터 전송 (Injection Volume 등) |
| `MOV` | 16-bit 데이터 전송 (Time, Tolerance 등) |
| `LD=` | HMI 입력값과 현재값 비교 (Range Check) |
| `CMP` | 범위 비교 (D270, D272 Validation) |
