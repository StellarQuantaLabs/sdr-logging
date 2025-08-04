# sdr-logging


# SQL Anomaly Lab - SDR Logging & RF Tripwire

This tool is for monitoring and logging RF activity across multiple bands using an RTL-SDR dongle.  
It supports two modes:
- **Logger Mode**: Logs RF power levels, saves raw IQ captures and spectrograms when signals exceed a threshold.
- **Tripwire Mode** *(coming soon)*: Real-time detection and alerts for unusual or high-power RF activity.

## Features
- Scans multiple bands:
  - 30–88 MHz (VHF Low / SINCGARS Band)
  - 225–400 MHz (UHF Military Aviation & Satcom)
  - 800–900 MHz (High‑UHF / Tactical & Trunked)
  - 1.2–1.3 GHz (L‑Band Tactical / Surveillance / Experimental)
- Logs all detections to `scan_log.csv`
- Saves `.iq` and `.png` captures for strong signals
- **Audible alert** when a strong signal is detected

## Setup
1. Install Python 3.8+ and [RTL-SDR drivers](https://osmocom.org/projects/rtl-sdr/wiki/rtl-sdr).
2. Clone this repo:
   ```bash
   git clone https://github.com/StellarQuantaLabs/sdr-logging.git

## Background
### 1. 30–88 MHz (VHF Low / SINCGARS Band)
    Primary use:
    - SINCGARS (Single Channel Ground and Airborne Radio System): Standard U.S./NATO tactical comms for ground forces, vehicles, and some air assets.
    - Legacy military FM communications.

    Why it matters:
      - This is the bread‑and‑butter field comms band for ground troops — command, control, and battlefield coordination.
      - Also heavily used for training exercises and some low‑rate data links.

    EW significance:
      - Target for jamming and signal intercept in contested areas.
      - Often monitored by SIGINT units to detect troop movements or training.

### 2. 225–400 MHz (UHF Military Aviation & Satcom)
    Primary use:
    - Military air‑to‑air and air‑to‑ground comms.
    - UHF Satcom (legacy DoD satellites still use portions here).
    - Link‑16 gateways (some legacy interoperability).

    Why it matters:
      - Critical for fighter jets, bombers, and AWACS aircraft.
      - Combat search & rescue (CSAR) channels live here.
      - Used by airborne command posts and Navy assets.

    EW significance:
      - Often targeted for jamming or spoofing in conflict zones.
      - Can reveal aircraft activity when monitored (common SIGINT target).

### 3. 800–900 MHz (High‑UHF / Tactical & Trunked)
    Primary use:
    - Trunked radio systems for secure base operations.
    - Some encrypted tactical radios (special operations & law enforcement).
    - Telemetry and drone control links (esp. older UAV platforms).

    Why it matters:
      - Heavily used for secure on‑base communications.
      - Some encrypted drone control channels and telemetry pass through this range.

    EW significance:
      - Signal monitoring here can detect logistics and UAV ops.
      - Prime for denial‑of‑service (DoS) or link interference.

### 4. 1.2–1.3 GHz (L‑Band Tactical / Surveillance / Experimental)
    Primary use:
    - Surveillance radar (short‑range & experimental).
    - UAV and aircraft telemetry (esp. older Predator/Global Hawk channels).
    - DoD experimental comms (DARPA & test ranges).

    Why it matters:
      - Radar & targeting systems are active here.
      - ISR platforms (Intelligence, Surveillance, Reconnaissance) use these bands for data links.

    EW significance:
      - Radar jamming / spoofing and recon intercepts are key in this space.
      - Can reveal experimental tests or classified R&D systems operating in the area.
