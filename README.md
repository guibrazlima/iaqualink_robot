# iAqualink Robots Integration for Home Assistant (Enhanced Fork)

A comprehensive Home Assistant integration for **iAqualink robotic pool cleaners**, providing **full control**, **real-time monitoring**, **90+ sensors**, and **live telemetry** from the Zodiac WebSocket API.

> **This is an enhanced fork** of [galletn/iaqualink](https://github.com/galletn/iaqualink) with full API data exposure. The original integration only exposes ~20% of the available API data. This fork exposes **everything**.

## 🌟 What's New in v3.0.0 (Enhanced Fork)

### 70+ New Sensors — Full API Exposure

| Category | Sensors | Description |
|----------|---------|-------------|
| **Hardware (eboxData)** | 9 sensors | Control box, cleaner, power supply, sensor block, motor block serial numbers & part numbers, firmware versions |
| **Cycle Durations** | 6 sensors | Waterline, Quick, Smart, Deep, Custom, First Smart configured timers |
| **Weekly Schedule** | 21 sensors | 7 days × Enabled/Program/Time — see exactly when your robot is scheduled |
| **Telemetry: Voltages** | 3 sensors | Ebox, Robot, Sensor board voltages (V) |
| **Telemetry: Motor Currents** | 3 sensors | Pump, Track 1, Track 2 current draw (A) |
| **Telemetry: PWM** | 3 sensors | Pump, Track 1, Track 2 duty cycle (%) |
| **Telemetry: Environmental** | 2 sensors | Pressure (hPa), Live water temperature (°C) |
| **Telemetry: Gyroscope** | 3 sensors | X/Y/Z angular velocity (°/s) |
| **Telemetry: Accelerometer** | 3 sensors | X/Y/Z acceleration (m/s²) |
| **Telemetry: Magnetometer** | 3 sensors | X/Y/Z magnetic field (µT) |
| **Telemetry: Navigation** | 6 sensors | Angle rotation, cumulative angles, position, movement ID, last move length |
| **Telemetry: Counters** | 7 sensors | Loops, tilts, wall contacts, stairs, floor blockages, pattern/cycle ID |

### Real-time Telemetry via WebSocket

Telemetry sensors (voltages, currents, IMU, navigation, counters) update **in real-time** via WebSocket push while the robot is cleaning. Data is cached between cleaning cycles so you always see the last known values.

---

## 🚀 Installation

### Manual (Recommended for this fork)

1. Download/clone this repository
2. Copy `custom_components/iaqualink_robots/` to your Home Assistant `custom_components/` directory
3. Restart Home Assistant
4. Add the integration via Settings → Devices & Services → Add Integration → "iAqualink Robots"

### HACS (Custom Repository)

1. Open HACS → Integrations → Three dots menu → **Custom repositories**
2. Add: `https://github.com/guibrazlima/iaqualink_robot` — Category: **Integration**
3. Search for "iAqualink Robots (Enhanced)" and install
4. Restart Home Assistant

---

## ⚙️ Setup

1. **Settings** → **Devices & Services** → **Add Integration**
2. Search for **"iAqualink Robots"**
3. Enter your iAqualink/Zodiac credentials (same as the mobile app)
4. Select your robot from the detected devices

---

## 📱 Entities Overview

### Vacuum Entity
- Controls: Start/Stop, Return to base, Fan speed selection
- Status: Cleaning mode, Activity state
- Remote Control: Forward, Backward, Rotate Left/Right (VR/Vortrax only)

### Core Sensors (22 — from original integration)
- Serial Number, Device Type, Model
- Battery Level, Total Hours, Temperature
- Cycle info (Start time, Duration, Type, Time Remaining, Estimated End)
- Canister Level, Error State
- Fan Speed, Activity, Status
- Stepper adjustments (increment, base/adjusted duration)

### Hardware Sensors (9 — NEW)
- `Ebox Firmware` / `Robot Firmware`
- `Control Box Serial` / `Cleaner Serial` / `Power Supply Serial`
- `Sensor Block Serial` / `Motor Block Serial`
- `Control Box Part No.` / `Cleaner Part No.`

### Cycle Duration Sensors (6 — NEW)
- `Duration: Waterline` / `Duration: Quick` / `Duration: Smart`
- `Duration: Deep` / `Duration: Custom` / `Duration: First Smart`

### Weekly Schedule Sensors (21 — NEW)
For each day (Mon–Sun):
- `Schedule {Day} Enabled` — On/Off
- `Schedule {Day} Program` — Floor only / Wall only / SMART / Floor+Walls
- `Schedule {Day} Time` — HH:MM start time

### Real-time Telemetry Sensors (28 — NEW, VR/Vortrax only)

These update live via WebSocket while the robot is cleaning:

**Electrical:**
- `Voltage: Ebox` / `Voltage: Robot` / `Voltage: Sensor` (V)
- `Current: Pump` / `Current: Track 1` / `Current: Track 2` (A)
- `PWM: Pump` / `PWM: Track 1` / `PWM: Track 2` (%)

**Environmental:**
- `Pressure` (hPa)
- `Water Temperature (Live)` (°C)

**IMU (Inertial Measurement Unit):**
- `Gyroscope X/Y/Z` (°/s)
- `Accelerometer X/Y/Z` (m/s²)
- `Magnetometer X/Y/Z` (µT)

**Navigation:**
- `Angle Rotation` / `Cumulative Angle Rotation` / `Cumulative Compass Angle` (°)
- `Cleaner Position` / `Movement ID` / `Last Move Length` (m)

**Counters:**
- `Loop Count` / `Tilt Count` / `Wall Contact Count`
- `Stairs Count` / `Floor Blockage Count`
- `Pattern ID` / `Cycle ID`

### Buttons
- Remote Forward / Backward / Rotate Left / Right / Stop (VR/Vortrax only)

---

## 📋 Supported Models

### Fully Supported
- EX 4000 iQ
- **RA 6500 iQ** / RA 6570 iQ / RA 6900 iQ
- Polaris VRX iQ+
- CNX 30 iQ / CNX 40 iQ / CNX 50 iQ / CNX 4090 iQ
- OV 5490 iQ / RF 5600 iQ
- OA 6400 IQ
- P965 iQ / 9650iQ
- VortraX TRX 8500 iQ
- Polaris Freedom Cordless (Cyclobat)
- CycloNext models
- Vortrax models

### Telemetry Availability
| Robot Type | Core Sensors | Hardware | Schedule | Durations | Live Telemetry |
|-----------|:---:|:---:|:---:|:---:|:---:|
| VR (RA 6500, etc.) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Vortrax | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cyclobat | ✅ | ❌ | ❌ | ❌ | ❌ |
| CycloNext | ✅ | ❌ | ❌ | ❌ | ❌ |
| i2d_robot | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## 🌍 Multi-Language Support

* 🇺🇸 English (Default)
* 🇫🇷 Français
* 🇪🇸 Español
* 🇩🇪 Deutsch
* 🇳🇱 Nederlands
* 🇵🇹 Português
* 🇨🇿 Čeština
* 🇮🇹 Italiano
* 🇸🇰 Slovenčina

---

## 🔧 Troubleshooting

**Robot shows unavailable** → Check connection in iAqualink mobile app first.

**Telemetry sensors show "Unknown"** → These only populate when the robot is actively cleaning. Start a cleaning cycle and they'll update in real-time.

**Schedule sensors show "Unknown"** → The robot may not have a schedule configured, or it's a model that doesn't support schedules.

Enable debug logging:
```yaml
logger:
  logs:
    custom_components.iaqualinkRobots: debug
```

---

## 🤝 Credits

- Original integration by [@galletn](https://github.com/galletn)
- Enhanced fork with full API exposure by [@guibrazlima](https://github.com/guibrazlima)
- Based on reverse-engineered Zodiac/iAqualink WebSocket API
