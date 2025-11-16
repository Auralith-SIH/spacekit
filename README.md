<p align="center">
  <img src="assets/spacekit-logo.png" width="180" alt="SpaceKit Logo">
</p>

<h1 align="center">SpaceKit 🚀</h1>

<p align="center">A lightweight, beginner-friendly Python toolkit for space-data analysis, astronomy calculations, and NASA/ISRO API integration.</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/github/stars/Auralith-SIH/spacekit?style=social" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/Maintained-Yes-green" />
</p>

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📚 API Reference](#-api-reference)
- [📡 Supported APIs](#-supported-apis)
- [📁 Project Structure](#-project-structure)
- [📖 Examples](#-examples)
- [📝 Configuration & API Keys](#-configuration--api-keys)
- [🤝 Contributing](#-contributing)
- [🗂 Changelog](#-changelog)
- [📊 Project Roadmap](#-project-roadmap)
- [🏗 Built With](#-built-with)
- [❓ FAQ](#-faq)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## ✨ Features

- 🛰️ **NASA API Integration** — APOD, Mars Rover, Space Weather  
- 🌌 **Astronomy Calculations** — RA/DEC to ALT/AZ, satellite passes  
- 📡 **Satellite Tracking** — ISS & other real-time predictions  
- 📊 **Data Processing Tools** — Clean, transform, visualize  
- 🎯 **Beginner Friendly** — Simple Python functions  
- 🇮🇳 **Indigenous Focus** — ISRO mission & telemetry utilities  
- 💡 **Modular, documented, open-source**

---

## 🚀 Quick Start

### **Installation**
```bash
pip install spacekit

Perfect! Here’s a **fully polished, GitHub-ready Markdown README** for your SpaceKit project. Everything is in **pure Markdown**, all Python code blocks are correct, tables render properly, and it looks professional. You can copy-paste this directly into your `README.md` file:

````markdown
# SpaceKit 🚀

A lightweight, beginner-friendly Python toolkit for space-data analysis, astronomy calculations, and NASA/ISRO API integration.

---

## 📌 Badges

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Auralith-SIH/spacekit?style=social)](https://github.com/Auralith-SIH/spacekit)
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![Maintained](https://img.shields.io/badge/Maintained-Yes-green)]()

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📚 API Reference](#-api-reference)
- [📡 Supported APIs](#-supported-apis)
- [📁 Project Structure](#-project-structure)
- [📖 Examples](#-examples)
- [📝 API Key Setup](#-api-key-setup)
- [🤝 Contributing](#-contributing)
- [📊 Roadmap](#-roadmap)
- [🏗 Built With](#-built-with)
- [❓ FAQ](#-faq)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## ✨ Features

- 🛰️ **NASA API Integration** — APOD, Mars Rover, Space Weather  
- 🌌 **Astronomy Calculations** — RA/DEC to ALT/AZ, satellite passes  
- 📡 **Satellite Tracking** — ISS & other real-time predictions  
- 📊 **Data Processing Tools** — Clean, transform, visualize  
- 🎯 **Beginner Friendly** — Simple Python functions  
- 🇮🇳 **Indigenous Focus** — ISRO mission & telemetry utilities  
- 💡 **Modular, documented, open-source**

---

## 🚀 Quick Start

### Installation
```bash
pip install spacekit
````

### Basic Usage

```python
import spacekit

# Space weather
weather = spacekit.get_space_weather()
print(f"Solar activity: {weather['solar_flares']}")

# ISS position
position = spacekit.satellite_position('ISS')
print("ISS Position:", position)

# NASA Astronomy Picture of the Day
apod = spacekit.get_apod()
print("Today's NASA APOD:", apod["title"])
```

---

## 📚 API Reference

### spacekit.nasa

```python
from spacekit import nasa

apod = nasa.get_apod()
mars_photos = nasa.get_mars_photos("curiosity", "2024-01-01")
space_weather = nasa.get_space_weather()
```

### spacekit.astronomy

```python
from spacekit import astronomy

coords = astronomy.radec_to_altaz(ra=83.82, dec=22.01, lat=28.61, lon=77.23)
passes = astronomy.get_satellite_passes("ISS", lat=28.61, lon=77.23)
```

### spacekit.isro

```python
from spacekit import isro

missions = isro.get_mission_data("Chandrayaan-3")
telemetry = isro.get_satellite_telemetry("INSAT-3DR")
```

---

## 📡 Supported APIs

| API Name            | Module                           | Status   | Description                         |
| ------------------- | -------------------------------- | -------- | ----------------------------------- |
| NASA APOD           | `nasa.get_apod()`                | ✔️ Ready | Astronomy Picture of the Day        |
| Mars Rover Photos   | `nasa.get_mars_photos()`         | ✔️ Ready | Curiosity/Opportunity/Spirit images |
| Space Weather       | `nasa.get_space_weather()`       | ✔️ Ready | Solar activity, solar wind, flares  |
| ISRO Mission DB     | `isro.get_mission_data()`        | 🚧 WIP   | Mission details & descriptions      |
| Satellite Telemetry | `isro.get_satellite_telemetry()` | 🚧 WIP   | INSAT, GSAT, NavIC telemetry        |
| ISS Tracking        | `astronomy.satellite_position()` | ✔️ Ready | Real-time ISS position              |

---

## 📁 Project Structure

```
spacekit/
│── spacekit/
│   ├── nasa.py
│   ├── astronomy.py
│   ├── isro.py
│   ├── utils.py
│   └── __init__.py
│── examples/
│── tests/
│── assets/
│── README.md
│── requirements.txt
│── setup.py
```

---

## 📖 Examples

### Space Weather Visualization

```python
import spacekit
import matplotlib.pyplot as plt

data = spacekit.nasa.get_space_weather()

plt.plot(data["solar_flux"])
plt.title("Solar Flux Activity")
plt.ylabel("Solar Flux Units")
plt.show()
```

### Real-Time ISS Tracker

```python
import spacekit
import time

while True:
    p = spacekit.astronomy.satellite_position("ISS")
    print(f"Lat: {p['latitude']:.2f}, Lon: {p['longitude']:.2f}")
    time.sleep(30)
```

---

## 📝 API Key Setup

**Option 1 — Environment Variable**

```bash
export NASA_API_KEY="your_key_here"
```

**Option 2 — In Python**

```python
spacekit.configure(api_key="your_key_here")
```

*If no key is set, SpaceKit uses NASA’s demo key.*

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch:

```bash
git checkout -b feature/amazing-feature
```

3. Commit changes:

```bash
git commit -m "Add amazing feature"
```

4. Push:

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

## 📊 Roadmap

* [x] NASA APOD API wrapper
* [x] Basic astronomy calculations
* [ ] ISRO mission & telemetry integration
* [ ] Real-time satellite tracking dashboard
* [ ] Space weather alert engine
* [ ] Mobile companion app
* [ ] Offline caching mode

---

## 🏗 Built With

* Python 3.8+
* Requests
* NumPy
* Pandas
* Matplotlib
* FastAPI (future)

---

## ❓ FAQ

**Do I need a NASA API key?**
Optional, the demo key is used by default.

**Does SpaceKit work offline?**
Astronomy calculations: ✔️
NASA/ISRO API calls: ❌ Internet required.

**Is it free?**
Yes — 100% open-source (MIT License).

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file.

---

## 📬 Contact

GitHub Issues: [https://github.com/Auralith-SIH/spacekit/issues](https://github.com/Auralith-SIH/spacekit/issues)

---

<p align="center"><b>⭐ If you find this project useful, please star the repository! ⭐</b></p>
<p align="center">Built with ❤️ by students passionate about space technology.</p>
```

---


