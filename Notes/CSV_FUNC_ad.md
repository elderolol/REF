# REFRIGER CHARGING MACHINE — Function Spec: ad.csv

> **Module**: `ad.csv`  
> **Execution**: Always ON  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

**아날로그 I/O 전용** (0~10V, 4~20mA 등).  
아날로그 입력 채널의 Raw 값(0~4000)을 Engineering Unit(EU) 값으로 변환(Scaling).

> **RS-485 통신 센서** (진공 센서, 압력 센서, 온도 센서 등)는 `485.csv` 에서 처리.  
> `ad.csv`는 순수 아날로그 신호 입출력만 담당.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| D150 | L0 CH0 AD Raw (0~4000) — 예: Pressure |
| D154 | L0 CH1 AD Raw (0~4000) — 예: Temperature |
| D158 | L0 CH2 AD Raw (0~4000) — 예: Vacuum |
| D162 | L1 CH0 AD Raw (0~4000, D270≥2) |
| D166 | L1 CH1 AD Raw (0~4000) |
| D170 | L1 CH2 AD Raw (0~4000) |
| HSC | Flow Meter Pulse (고속카운터, 별도 채널) |

> 실제 CH 할당은 하드웨어 구성에 따름. 위는 예시.
> RS-485 센서 데이터는 `485.csv`에서 수신하므로 `ad.csv`에서는 제외.

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| D152 | L0 CH0 EU 변환값 |
| D156 | L0 CH1 EU 변환값 |
| D160~D161 | L0 CH2 EU 변환값 (32-bit) |
| D164 | L1 CH0 EU 변환값 |
| D168 | L1 CH1 EU 변환값 |
| D172~D173 | L1 CH2 EU 변환값 (32-bit) |
| D138~D148 | Operation Display Mirror (HMI 표시용) |
| D124 | Charging Pulse (Display) |

---

## 4. Scaling Logic

### 4-1. CH0 Scaling (예: Pressure)

```
EU = Raw × (MaxRange - MinRange) / 4000 + MinRange

L0: D152 = D150 × Scale / 4000 + Offset
L1: D164 = D162 × Scale / 4000 + Offset
```

> Scale/Offset은 센서 사양에 따라 HMI 파라미터에서 설정 가능.

### 4-2. CH1 Scaling (예: Temperature)

```
EU = Raw × 100.0 / 4000 - 20.0
(0.1℃ 단위, -20.0~80.0℃)

L0: D156 = D154 × 1000 / 4000 - 200
L1: D168 = D166 × 1000 / 4000 - 200
```

### 4-3. CH2 Scaling (예: Vacuum)

```
EU = Raw × 760.0 / 4000
(Torr, 0~760 Torr 범위, 32-bit)

L0: D160~D161 = D158 × 76000 / 4000
L1: D172~D173 = D170 × 76000 / 4000
```

### 4-4. Display Mirror

매 스캔마다 Operation Display 영역으로 EU 값 복사:

```
D138 ← D160~D161  // L0 Current Vacuum (Display)
D140 ← D156         // L0 Temperature (Display)
D142 ← D152         // L0 Pressure (Display)
D144 ← D172~D173  // L1 Current Vacuum (Display)
D146 ← D168         // L1 Temperature (Display)
D148 ← D164         // L1 Pressure (Display)
```

---

## 5. Filtering

1차 지연 필터 또는 이동평균 적용하여 노이즈 제거:

```
Filtered = α × CurrentRaw + (1 - α) × PreviousFiltered
α = 0.2 (필터 계수, 튜닝 가능)
```

---

## 6. 센서 Type 선택 아키텍처 (미래 확장)

> **현재**: ad.csv와 485.csv는 독립적으로 동작. 각 센서의 HW Type에 따라 선택.
> **미래**: 동일 센서가 Analog/RS-485 양쪽으로 존재 시, `setting.csv`에서 Type 선택.

```
[Dxxx Sensor Type Select]
    ├── = 0 → ad.csv 출력 사용 (Analog)
    └── = 1 → 485.csv 출력 사용 (RS-485)
```

| 항목 | Select D Addr | Options |
|------|:------------:|:--------:|
| L0 Vacuum Sensor Type | TBD | 0=Analog, 1=RS-485 |
| L0 Pressure Sensor Type | TBD | 0=Analog, 1=RS-485 |
| L0 Temperature Sensor Type | TBD | 0=Analog, 1=RS-485 |
| L1 Vacuum Sensor Type | TBD | 0=Analog, 1=RS-485 |
| ... | TBD | |

> 두 모듈은 동일한 D152/D156/D160/D164/D168/D172 출력 영역을 공유.
> Type Select에 따라 실제 값을 기록하는 쪽이 결정됨.

---

## 7. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Raw 값 읽기 |
| `MOV` | 16-bit 데이터 전송 |
| `DMOV` | 32-bit 데이터 전송 (Vacuum) |
| `D*` | 곱셈 (Scaling) |
| `D/` | 나눗셈 (Scaling) |
| `D+` | 덧셈 (Offset) |
| `D-` | 뺄셈 (Offset) |
