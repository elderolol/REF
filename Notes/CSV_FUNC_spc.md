# REFRIGER CHARGING MACHINE — Function Spec: spc.csv

> **Module**: `spc.csv`  
> **Execution**: Cycle Complete 시 Trigger  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

- 라인별 누계 데이터 관리 (냉매 총 사용량, 주입 횟수, 펄스 누계)
- 최근 실주입량 / 설정량 기록 (라인별)
- 봄베 알람 조건 감시

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| L18 | Cycle Done (Line 0) — Rising Edge |
| L28 | Cycle Done (Line 1) — Rising Edge |
| M60~M63 | Injection Active (각 Gun) |
| D130 | Actual Injection Volume (Refrig, 32-bit, g) |
| D128 | Injection Setting Amount (Refrig, 32-bit, g) |
| D134 | Actual Oil Injection Volume (32-bit, g) |
| D124 | Charging Pulse |
| D14 | Bombe Alarm Setting (32-bit, Kg) |
| D16 | Bombe Used Amount (32-bit, Kg) |

---

## 3. Outputs

| Device | Width | Description |
|:------:|:----:|-------------|
| D280~D281 | **32-bit** | L0 Refrigerant Total Usage (Kg) |
| D282~D283 | **32-bit** | L0 Total Injection Count |
| D284~D285 | **32-bit** | L0 Total Pulse Count |
| D286~D287 | **32-bit** | L0 Last Actual Injection Volume (g) |
| D288~D289 | **32-bit** | L0 Last Setting Injection Volume (g) |
| D290~D291 | **32-bit** | L1 Refrigerant Total Usage (Kg) |
| D292~D293 | **32-bit** | L1 Total Injection Count |
| D294~D295 | **32-bit** | L1 Total Pulse Count |
| D296~D297 | **32-bit** | L1 Last Actual Injection Volume (g) |
| D298~D299 | **32-bit** | L1 Last Setting Injection Volume (g) |
| D88 | 16-bit | Number of Injections (HMI Display) |
| L4B | — | Refriger Bombe Low Alarm Flag |

---

## 4. Logic

### 4-1. L0 Total Usage Accumulation

```
L18 (L0 Cycle Done) Rising Edge
    │
    ├── D280~D281 (L0 Total Usage) += D130 (Actual Inj Volume)
    ├── D282~D283 (L0 Total Count) += 1
    ├── D284~D285 (L0 Total Pulse) += D124
    ├── D286~D287 = D130 (L0 Last Actual Volume)
    └── D288~D289 = D128 (L0 Last Setting Volume)
```

### 4-2. L1 Total Usage Accumulation

```
L28 (L1 Cycle Done) Rising Edge
    │
    ├── D290~D291 (L1 Total Usage) += D130 (Actual Inj Volume)
    ├── D292~D293 (L1 Total Count) += 1
    ├── D294~D295 (L1 Total Pulse) += D124
    ├── D296~D297 = D130 (L1 Last Actual Volume)
    └── D298~D299 = D128 (L1 Last Setting Volume)
```

### 4-3. Display Mirror

```
D88 (Number of Injections) = D282~D283 (하위 16-bit)
```

### 4-4. Bombe Alarm Check

```
// 매 Update 시 Bombe 사용량 확인 (L0 + L1 합)
LDD>= D280~D281 + D290~D291    // Total Usage ≥ Bombe Setting?
        D14                     // Bombe Alarm Setting
    → SET L4B (Refriger Bombe Low Alarm)
```

---

## 5. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Cycle Done read |
| `D+` | 32-bit Accumulation (Usage, Count, Pulse) |
| `DMOV` | 32-bit Data Move (Last Volume) |
| `LDD>=` | 32-bit Compare (Bombe Alarm) |
| `SET` | Bombe Low Alarm |
