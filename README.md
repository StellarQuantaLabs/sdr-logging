# sdr-logging


# SQL Anomaly Lab
**Purpose:**  
This project continuously monitors and correlates multiple environmental and operational data streams to detect and visualize anomalous activity.  

**Data Sources:**  
- **SDR (Software Defined Radio):** Wideband IQ captures + FFT snapshots  
- **FlightRadar24 API:** Aircraft position data, including blocked call signs  
- **NOAA & NASA APIs:** Geomagnetic (Kp index), solar wind, and flare data  
- **Local Weather:** METAR and NWS data  
- **Starlink Outage Reports:** Public outage reporting APIs

**Features:**  
- Continuous SDR recording with timestamped IQ data  
- Automated data pulls (hourly) from APIs  
- Correlation engine to align SDR anomalies with flights, outages, and solar/weather events  
- Grafana dashboard for live visualization  
- Alerts on thresholds (e.g., SDR spike + low geomagnetic activity + unlogged aircraft)
