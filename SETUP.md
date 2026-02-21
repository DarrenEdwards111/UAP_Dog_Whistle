# Raspberry Pi Setup Guide

Quick setup guide for running the Hydrogen Line Beacon (HLB) and electromechanical signal system on a Raspberry Pi.

## Hardware Requirements

### Minimum (Mechanical Channel Only)
- Raspberry Pi 4/5 (recommended)
- PCM5102A I2S DAC board
- TPA3116D2 Class D amplifier
- Dayton Audio BST-1 bass shaker
- Ground coupling plate + spike
- 12V power supply for amplifier
- Speaker wire (14 AWG)

### Full System (RF + Mechanical)
- Everything above, plus:
- HackRF One SDR transceiver
- USB cable for HackRF
- Antenna (discone for wideband, or specific for target frequency)
- SMA cables and adapters
- Optional: RTL-SDR v4 for monitoring
- Optional: USB magnetometer

## Software Installation

### System Dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv git libportaudio2
```

### HackRF Tools (if using RF channel)

```bash
sudo apt-get install -y hackrf libhackrf-dev
```

### Python Environment

```bash
cd ~
git clone https://github.com/DarrenEdwards111/SHARD.git
cd SHARD

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install hydrogen-line-beacon package
cd hydrogen-line-beacon
pip install -e .

# Or install dependencies manually:
pip install numpy scipy
```

## Hardware Setup

### I2S DAC (PCM5102A) Pinout

Connect to Raspberry Pi GPIO:

| PCM5102A Pin | Pi GPIO | Physical Pin |
|--------------|---------|--------------|
| VIN | 3.3V | Pin 1 |
| GND | GND | Pin 6 |
| BCK | GPIO 18 | Pin 12 |
| LRCK | GPIO 19 | Pin 35 |
| DIN | GPIO 21 | Pin 40 |

### Enable I2S Audio

Edit `/boot/config.txt`:

```bash
sudo nano /boot/config.txt
```

Add this line:

```
dtoverlay=hifiberry-dac
```

Reboot:

```bash
sudo reboot
```

### Amplifier Connection

```
PCM5102A line out → TPA3116D2 audio input
TPA3116D2 output → Bass shaker terminals
TPA3116D2 power → 12V DC supply
```

### Ground Coupling

1. Bolt bass shaker to centre of ground plate (aluminium disc, 400mm diameter, 6mm thick)
2. Weld or bolt ground spike (steel rod, 300mm) to underside of plate
3. Drive spike into soil at installation site
4. Ensure good mechanical coupling — tighten all bolts

## Quick Start

### Mechanical Channel Only

```bash
cd ~/SHARD/hydrogen-line-beacon
source ../venv/bin/activate

# 10-minute test
hlb --duration 600

# 1-hour full programme
hlb --duration 3600 --programme full

# Generate WAV file for inspection
hlb --generate schumann_test.wav
aplay schumann_test.wav
```

### RF + Mechanical (Requires HackRF)

```bash
# ISM band (433 MHz, legal, no licence)
hlb --rf --freq 433 --duration 600

# Hydrogen line (1.42 GHz, requires amateur radio licence)
hlb --rf --freq hydrogen --duration 3600
```

### Check Hardware Status

```bash
hlb --check
```

This will verify:
- I2S DAC availability
- HackRF connection (if connected)
- Audio output devices

## Testing Individual Components

### Test I2S DAC

```bash
speaker-test -t sine -f 440 -c 2
```

You should hear a 440 Hz tone. If the bass shaker is connected, it won't produce audible sound, but you should feel vibration above ~20 Hz.

### Test HackRF

```bash
hackrf_info
```

Should display device serial number and firmware version.

### Generate Test Signals

```bash
# Pure 7.83 Hz Schumann fundamental
hlb --generate schumann_7.83.wav --programme fundamental

# Pulsed programme (all harmonics with prime pulse timing)
hlb --generate schumann_pulsed.wav --programme pulsed

# Combined (all 5 harmonics simultaneously)
hlb --generate schumann_combined.wav --programme combined
```

## Signal Layers

The mechanical channel generates ground-coupled vibrations at Schumann resonance frequencies:

1. **7.83 Hz** — Fundamental Schumann resonance
2. **14.3 Hz** — 2nd harmonic
3. **20.8 Hz** — 3rd harmonic
4. **27.3 Hz** — 4th harmonic
5. **33.8 Hz** — 5th harmonic

The RF channel (when enabled) transmits these same frequencies as amplitude modulation over a carrier:
- **433 MHz** — ISM band (legal, no licence)
- **868 MHz** — European ISM band (legal, no licence)
- **1.42 GHz** — Hydrogen line (requires amateur radio licence)

## Auto-Start on Boot (Optional)

To run the beacon automatically on boot, create a systemd service:

```bash
sudo nano /etc/systemd/system/hlb.service
```

```ini
[Unit]
Description=Hydrogen Line Beacon
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/SHARD/hydrogen-line-beacon
ExecStart=/home/pi/SHARD/venv/bin/hlb --duration 0 --programme pulsed
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable hlb.service
sudo systemctl start hlb.service
```

Check status:

```bash
sudo systemctl status hlb.service
```

## Bluetooth Speaker (Alternative to Ground Coupling)

If you want to test with a regular Bluetooth speaker instead of ground coupling:

```bash
bluetoothctl
scan on
# Wait for your speaker to appear, note the MAC address
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
exit
```

Then play generated WAV files:

```bash
aplay schumann_test.wav
```

**Note:** Regular speakers cannot reproduce frequencies below ~20 Hz. You'll only hear the higher Schumann harmonics (20.8, 27.3, 33.8 Hz). Ground coupling is required for the fundamental (7.83 Hz) and 2nd harmonic (14.3 Hz).

## Legal Compliance (UK)

### RF Transmission
- **433 MHz ISM:** Licence-free, max 10 mW ERP
- **868 MHz ISM:** Licence-free, max 500 mW ERP (25 mW for some sub-bands)
- **1.42 GHz:** Requires Foundation, Intermediate, or Full amateur radio licence

Before transmitting, verify you're compliant with Ofcom regulations. Get a Foundation licence if you want to experiment with the hydrogen line.

### Mechanical Channel
No restrictions. It's just physical vibration — no different from playing music through a subwoofer.

## Troubleshooting

### No audio output
- Check I2S is enabled in `/boot/config.txt`
- Verify DAC connections (GPIO 18, 19, 21)
- Run `aplay -l` to list audio devices
- Test with `speaker-test`

### HackRF not detected
- Check USB connection
- Run `hackrf_info` to test
- Install `hackrf` tools: `sudo apt-get install hackrf`

### Amplifier not powering on
- Verify 12V power supply is connected
- Check fuse on amplifier board
- Test with multimeter

### No vibration from bass shaker
- Check speaker wire connections (amplifier → shaker)
- Verify amplifier volume is turned up
- Test shaker with known audio source (phone, laptop)
- Ensure shaker is rated for low frequencies (Dayton BST-1 is 10–80 Hz)

## Further Resources

- [Hydrogen Line Beacon README](hydrogen-line-beacon/README.md)
- [Electromechanical System README](electromechanical/README.md)
- [Build Guide PDF](hydrogen-line-beacon/build-guide.pdf)
- [Theory Document](electromechanical/THEORY.md)

## Safety

- **RF exposure:** Keep antennas at least 2m from people during transmission
- **Infrasound:** Prolonged high-amplitude infrasound can cause discomfort. Keep levels moderate (<80 dB)
- **Electrical:** Use proper fuses and circuit protection
- **Mechanical:** Ensure all bolts/fasteners are tight before operation

---

For questions or issues, see the main [README.md](README.md) or consult the theory documentation in each subdirectory.
