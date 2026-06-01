# REFRIGER CHARGING MACHINE — Function Spec: vacchec.csv

> **Module**: `vacchec.csv`  
> **Execution**: Step 진입 시 (M14=L0, M24=L1)  
> **PLC**: Mitsubishi Q03UDV  

---

## 1. Purpose

진공 체크 (Vacuum Check / Leak Test) 공정 수행. 모든 진공 솔레노이드를 OFF한 상태에서
진공도를 감시하여 리크(Leak) 여부를 판정. 일정 시간 동안 진공도 유지 시 Pass,
진공도가 떨어지면 Leak NG.

---

## 2. Inputs

| Device | Description |
|:------:|-------------|
| M14 | Step: VAC CHECK (Line 0) |
| M24 | Step: VAC CHECK (Line 1) |
| D6 | Vacuum Check Time Setting (Line 0, 0.1 sec) |
| D36 | Vacuum Check Time Setting (Line 1, 0.1 sec) |
| D24 | Vacuum Check Setting Value (32-bit Torr, Line 0) |
| D52 | Vacuum Check Setting Value (32-bit Torr, Line 1) |
| D160~D161 | Current Vacuum EU (32-bit Torr, Line 0) |
| D172~D173 | Current Vacuum EU (32-bit Torr, Line 1) |
| M307 | Door Sensor L0 (방폭 전용) |
| M317 | Door Sensor L1 (방폭 전용) |

---

## 3. Outputs

| Device | Description |
|:------:|-------------|
| T2 | Vacuum Check Timer (100ms base) |
| L14 | VacCheck Done (Leak OK, Line 0) |
| L24 | VacCheck Done (Leak OK, Line 1) |
| L15 | VacCheck NG (Leak Detected, Line 0) |
| L25 | VacCheck NG (Leak Detected, Line 1) |
| L44 | Vacuum Leak Alarm |
| Scratch D | P_start 저장 (진공 시작값) |

---

## 4. Sequence Logic (Line 0 기준)

```
M14 (Step Entry) ─── Rising Edge
    │
    ├── 모든 진공 SOL OFF 확인 (M31, M32가 OFF 상태여야 함)
    │
    ├── 현재 진공도(D160) 확인
    │   ├── D160 ≤ D24 (진공도 충분) → Continue
    │   └── D160 > D24 (진공 부족) → 대기, 진공도가 D24 이하로 떨어질 때까지
    │
    ├── P_start = D160 기록 (Scratch D에 저장)
    ├── T2 RST, T2 Start
    │
    ▼
[VAC CHECK 진행 중 — 모든 SOL OFF, 진공도 모니터링]
    │
    ├── STOP 감지 → 즉시 RST, IDLE
    ├── EMG → 즉시 All Stop
    │
    ├── 정상 완료 조건:
    │   T2 ≥ D6 AND |D160 - P_start| ≤ Tolerance
    │   → SET L14 (Done), RST M14
    │
    ├── 리크 검출 조건:
    │   |D160 - P_start| > D24 (진공 Check Setting 초과)
    │   → SET L15 (NG), SET L44 (Vac Leak Alarm)
    │
    └── 방폭(Door) 리크:
        M307=OPEN → 즉시 L15, SET L4E (Door Alarm)
```

---

## 5. ΔP (차압) 계산

```
ΔP = |Current_Vacuum - P_start|

ΔP ≤ Tolerance (고정값, 예: 5 Torr) → Sealed OK
ΔP > D24 (Vacuum Check Setting) → Leak Detected
```

---

## 6. Step Transition

| From | To | Condition |
|:----:|:--:|:---------:|
| UNIT VAC (M13) | VAC CHECK (M14) | UnitVac Done → gmes SET M14 |
| VAC CHECK (M14) | [OIL/REFRIG] | L14 Done → gmes가 D276 확인 후 다음 Step |
| VAC CHECK (M14) | IDLE (M10) | L15 NG → Alarm + IDLE |

---

## 7. Error Conditions

| Error | Detection | Action |
|-------|:---------:|--------|
| Vacuum Leak | |D160 - P_start| > D24 | SET L15, L44 |
| Vacuum Insufficient | D160 > D24 at entry | 대기, Timeout → NG |
| Door Open (방폭) | M307=OPEN | SET L4E, L15 |
| Check Timeout | T2 ≥ D6+5s (Done 미도달) | SET L15 |

---

## 8. IL Mnemonics

| Mnemonic | Usage |
|:--------:|-------|
| `LD` | Step entry |
| `AND` | Door sensor / Safety check |
| `MOV` | P_start 저장 |
| `DMOV` | 32-bit vacuum read |
| `D-` | ΔP = Current - P_start |
| `LDD<=` | ΔP ≤ Tolerance? |
| `SET` | Done/NG |
| `RST` | Step off |
