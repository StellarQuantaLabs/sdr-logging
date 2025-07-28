# sdr-logging


# SQL Anomaly Lab - SDR Logging & RF Tripwire

This tool is for monitoring and logging RF activity across multiple bands using an RTL-SDR dongle.  
It supports two modes:
- **Logger Mode**: Logs RF power levels, saves raw IQ captures and spectrograms when signals exceed a threshold.
- **Tripwire Mode** *(coming soon)*: Real-time detection and alerts for unusual or high-power RF activity.

## Features
- Scans multiple bands:
  - 30–88 MHz (VHF Military)
  - 225–400 MHz (UHF Military)
  - 800–900 MHz
  - 1.2–1.3 GHz
- Logs all detections to `scan_log.csv`
- Saves `.iq` and `.png` captures for strong signals
- **Audible alert** when a strong signal is detected

## Setup
1. Install Python 3.8+ and [RTL-SDR drivers](https://osmocom.org/projects/rtl-sdr/wiki/rtl-sdr).
2. Clone this repo:
   ```bash
   git clone https://github.com/StellarQuantaLabs/sdr-logging.git

