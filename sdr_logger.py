import os, sys, ctypes, time, datetime, csv
import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Ensure DLLs load from script directory
dll_path = os.path.dirname(os.path.abspath(__file__))
os.add_dll_directory(dll_path)

# Output folder
OUTPUT_DIR = r"C:\Users\JENAU\sdr_scanner"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CSV log file
CSV_LOG = os.path.join(OUTPUT_DIR, "scan_log.csv")
if not os.path.exists(CSV_LOG):
    with open(CSV_LOG, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "frequency_MHz", "peak_power_dB"])

# SDR parameters
SAMPLE_RATE = 2.4e6
CAPTURE_DURATION = 5  # seconds per step
GAIN = 40  # manual gain (or 'auto')
POWER_THRESHOLD = -50  # dB threshold for saving IQ + PNG

# Define scan bands (start, end, step in Hz)
SCAN_BANDS = [
    (30e6, 88e6, 1e6),    # VHF Military
    (225e6, 400e6, 1e6),  # UHF Military
    (800e6, 900e6, 1e6),  # 800–900 MHz
    (1.2e9, 1.3e9, 1e6)   # 1.2–1.3 GHz
]

# Initialize SDR
sdr = RtlSdr()
sdr.sample_rate = SAMPLE_RATE
sdr.gain = GAIN

def capture_and_log(freq):
    sdr.center_freq = freq
    ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    samples = sdr.read_samples(int(SAMPLE_RATE * CAPTURE_DURATION))

    # Calculate peak power (approximate)
    power = 20 * np.log10(np.max(np.abs(samples)))

    # Always log to CSV
    with open(CSV_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, freq/1e6, round(power, 2)])

    # Only save IQ + PNG if above threshold
    if power >= POWER_THRESHOLD:
        iq_file = os.path.join(OUTPUT_DIR, f"{ts}_{freq/1e6:.3f}MHz.iq")
        samples.tofile(iq_file)

        plt.figure(figsize=(10, 4))
        plt.specgram(samples, NFFT=1024, Fs=SAMPLE_RATE, Fc=freq/1e6)
        plt.title(f"Spectrum at {freq/1e6:.3f} MHz")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.savefig(os.path.join(OUTPUT_DIR, f"{ts}_{freq/1e6:.3f}MHz.png"))
        plt.close()

# Continuous scanning loop
try:
    while True:
        for (start, end, step) in SCAN_BANDS:
            freq = start
            while freq <= end:
                print(f"[{datetime.datetime.utcnow()}] Capturing {freq/1e6:.3f} MHz")
                capture_and_log(freq)
                freq += step
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScanning stopped by user.")
    sdr.close()
