<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenEdwards111/SHARD/main/shard-logo.jpg" alt="SHARD" width="400" />
</p>

# SHARD
## Schumann Hydrogen Active RF Discovery

[![PyPI version](https://badge.fury.io/py/shard-rf.svg)](https://badge.fury.io/py/shard-rf)
[![Python](https://img.shields.io/pypi/pyversions/shard-rf.svg)](https://pypi.org/project/shard-rf/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Downloads](https://pepy.tech/badge/shard-rf)](https://pepy.tech/project/shard-rf)

A collection of experimental signal processing and RF transmission tools focused on Earth's electromagnetic environment, particularly Schumann resonances and the hydrogen line.

## Why Active Discovery? The Problem with Passive Listening

For over 60 years, the Search for Extraterrestrial Intelligence (SETI) has relied on **passive observation** — pointing antennas at the sky and waiting for a signal. Despite scanning billions of frequencies across thousands of stars, this approach has produced no confirmed detections. The fundamental limitation isn't technological — it's epistemological.

### The Silence Problem

Passive listening can never distinguish between three possibilities:
1. **Nothing is there** — no signals exist in the observed band
2. **Wrong place/time/frequency** — signals exist but we're not looking where they are
3. **Below detection threshold** — signals exist but are too weak to separate from noise

After decades of silence, SETI cannot tell you which of these is true. Absence of evidence is not evidence of absence — and passive observation provides no mechanism to resolve this ambiguity.

### The Active Alternative

SHARD takes a fundamentally different approach: **active probing with sequential hypothesis testing**.

| | Passive (SETI) | Active (SHARD) |
|---|---|---|
| **Method** | Listen and wait | Probe, listen, adapt |
| **Signal** | Hope to receive | Transmit structured probes |
| **Analysis** | Threshold detection | Sequential likelihood ratio |
| **Adaptation** | None — fixed observation plan | KL-optimal probe selection |
| **Conclusion from silence** | Nothing (ambiguous) | Confirmed null (H₀ accepted) |
| **Statistical guarantee** | None | Controlled Type I/II error (α, β) |
| **Speed** | Unlimited observation time | Up to 45× faster decision |
| **Falsifiability** | Cannot falsify "something is there" | Can reject H₁ with known confidence |

### How It Works

Instead of passively monitoring, SHARD:

1. **Transmits a structured probe** — hydrogen line pulses, Schumann-modulated signals, mathematical sequences
2. **Listens for a response** — measures power spectral density, cross-correlation, anomalies
3. **Computes a log-likelihood ratio** — how likely is this response under "adaptive responder" vs "background noise"?
4. **Updates a sequential test (Wald SPRT)** — accumulates evidence across probes
5. **Selects the next optimal probe** — KL-divergence maximisation ensures each probe is maximally informative
6. **Decides when evidence is sufficient** — either "adaptive response detected" (reject H₀) or "confirmed null" (accept H₀), both with mathematically guaranteed error rates

The key insight: **if something adaptive is out there, probing forces it to either respond (detectable) or not respond (also informative).** Either way, you learn something. Passive listening only learns from positive detections — which may never come.

### Scientific Rigour

SHARD doesn't claim to detect aliens. It provides a **statistically rigorous framework** for answering a specific question: "Is there an adaptive response to structured RF probes in this environment?" The answer is either yes (with confidence 1−α) or no (with confidence 1−β). No ambiguity, no hand-waving.

This same framework applies equally to ionospheric research, radar development, and any domain where you need to detect weak adaptive signals in noise.

---

## Projects

### 🌍 Electromechanical Signal System

Dual-channel signal transmission combining RF and mechanical transduction for studying atmospheric electromagnetic phenomena.

**Location:** `electromechanical/`

A Raspberry Pi-based platform that:
- Broadcasts RF signals at configurable frequencies (including Schumann resonance harmonics)
- Couples low-frequency vibrations into the ground via bass shakers
- Explores the relationship between electromagnetic and seismic signal propagation

**Physics basis:**
- Schumann resonances (7.83 Hz fundamental, harmonics at 14.3, 20.8, 27.3, 33.8 Hz)
- Ground-coupled seismic transduction as an alternative to airborne acoustic transmission
- RF amplitude modulation with ELF patterns

See [electromechanical/README.md](https://github.com/DarrenEdwards111/SHARD/blob/main/electromechanical/README.md) and [electromechanical/THEORY.md](https://github.com/DarrenEdwards111/SHARD/blob/main/electromechanical/THEORY.md)

### 📡 Hydrogen Line Beacon

1420.405 MHz hydrogen line RF beacon with Schumann resonance modulation.

**Location:** `hydrogen-line-beacon/`

A dual-channel system transmitting on the universal hydrogen emission frequency:
- RF channel at 1.42 GHz (21 cm hydrogen line)
- Mechanical channel with ground-coupled Schumann frequencies
- Prime-number pulse timing for temporal structure
- Call-and-response monitoring protocol

**Features:**
- Python API and CLI (`hlb` command)
- Multiple transmission programmes (pulsed, combined, scan, chirp)
- Anomaly detection and EM monitoring
- Legal ISM band options (433/868 MHz) for testing

See [hydrogen-line-beacon/README.md](https://github.com/DarrenEdwards111/SHARD/blob/main/hydrogen-line-beacon/README.md), [hydrogen-line-beacon/BUILD-GUIDE.md](https://github.com/DarrenEdwards111/SHARD/blob/main/hydrogen-line-beacon/BUILD-GUIDE.md), and [hydrogen-line-beacon/FOL-ARRAY.md](https://github.com/DarrenEdwards111/SHARD/blob/main/hydrogen-line-beacon/FOL-ARRAY.md)

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenEdwards111/SHARD/main/apd-logo.jpg" alt="Active Protocol Discovery" width="500" />
</p>

### 🔬 Active Discovery (APD Integration)

**NEW:** Sequential hypothesis testing for RF anomaly detection.

**Location:** `active-discovery/`

An experimental module that combines the Hydrogen Line Beacon with **Active Protocol Discovery (APD)** — a statistical framework for detecting adaptive responses to structured RF probes.

Instead of passively broadcasting a beacon, the Active Discovery system:
- **Adaptively selects** optimal probe signals (KL-divergence maximization)
- **Transmits** structured probes via HackRF One
- **Listens** for responses via RTL-SDR
- **Analyzes** responses for statistical anomalies
- **Decides** using Wald Sequential Probability Ratio Test (SPRT)

**Probe types:**
- Hydrogen line pulses (1420 MHz)
- Schumann-modulated carriers (7.83 Hz AM)
- Frequency sweeps
- Mathematical sequences (prime numbers, Fibonacci, golden ratio)
- Silence (control)

**Use cases:**
- RF anomaly detection with statistical rigor
- Active SETI experiments
- Ionospheric probing
- Adaptive radar waveform development

**Scientific basis:** Sequential hypothesis testing (Wald SPRT) applied to radio-frequency anomaly detection. The system can detect weak adaptive responses orders of magnitude faster than passive approaches, with controlled Type I/II error rates (typically α=0.01, β=0.01).

**Legal:** Requires amateur radio license for 1420 MHz. Can use ISM bands (433/868 MHz) without license.

See [active-discovery/README.md](https://github.com/DarrenEdwards111/SHARD/blob/main/active-discovery/README.md) for full documentation, hardware requirements, and usage examples.

## Physical Phenomena

### Schumann Resonances

The Schumann resonances are global electromagnetic resonances in the Earth-ionosphere cavity, excited by lightning discharges. The fundamental mode is 7.83 Hz, with harmonics approximately:

| Mode | Frequency (Hz) | Description |
|------|----------------|-------------|
| 1 | 7.83 | Fundamental |
| 2 | 14.3 | 2nd harmonic |
| 3 | 20.8 | 3rd harmonic |
| 4 | 27.3 | 4th harmonic |
| 5 | 33.8 | 5th harmonic |

These are actual atmospheric electromagnetic waves, not pseudoscience. They can be measured with sensitive magnetometers and VLF receivers.

### Hydrogen Line (21 cm)

The hydrogen line at 1420.405 MHz is the electromagnetic radiation spectral line emitted by neutral hydrogen atoms due to the hyperfine transition of the ground state. It's used in radio astronomy for mapping galactic hydrogen distribution and was included on the Pioneer plaque and Voyager Golden Record as a universal physical constant.

## Hardware Components

### RF Transmission
- HackRF One (1 MHz – 6 GHz SDR transceiver)
- RTL-SDR v4 (monitoring receiver)
- Antennas (discone, Yagi, helical for 1.42 GHz)
- RF amplifiers (optional, for increased range)

### Mechanical Transduction
- Raspberry Pi 5
- PCM5102A I2S DAC
- TPA3116D2 Class D amplifier
- Dayton Audio bass shakers (BST-1, TT25-8)
- Ground coupling plate + spike

### Monitoring
- USB magnetometers
- Pi camera modules
- Environmental sensors

## Legal Considerations (UK)

### RF Transmission
- **ISM bands (433 MHz, 868 MHz, 2.4 GHz):** Licence-free at low power (≤25 mW for 433, ≤500 mW for 868)
- **Amateur radio bands:** Require Foundation/Intermediate/Full amateur radio licence
- **1.42 GHz hydrogen line:** Requires amateur radio licence
- **Everything else:** Illegal to transmit without specific Ofcom authorisation

**Recommendation:** Start with 433 MHz ISM (legal, no licence required) or obtain a Foundation amateur radio licence (approximately £50, one-day course).

### Mechanical Channel
No restrictions — it's physical vibration. Safe levels are well below thresholds for human discomfort.

## Research Applications

- Studying Schumann resonance propagation characteristics
- Ground-coupled vs. airborne signal transmission efficiency
- RF modulation techniques with ELF patterns
- Seismic transduction for infrasound research
- Amateur radio experimentation on the hydrogen line
- Antenna design and testing for specific frequencies

## References & Further Reading

See PDFs in `electromechanical/` and `hydrogen-line-beacon/` directories for technical documentation, build guides, and theoretical background.

## Licence

MIT — Mikoshi Ltd, 2026

---

**Note:** This is experimental RF and signal processing work. Always comply with local radio regulations, maintain safe RF exposure distances, and respect the electromagnetic spectrum.
