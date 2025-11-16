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

- 🛰️ **NASA API Integration** — Astronomy Picture of the Day (APOD) with demo fallback
- 🌌 **Space Weather Simulation** — Solar activity and space weather data
- 📡 **Satellite Tracking** — ISS position and tracking utilities
- 🎯 **Beginner Friendly** — Simple Python functions with clear documentation
- 💡 **Modular & Open Source** — Easy to extend and contribute to

---

## 🚀 Quick Start

### Installation
```bash
pip install spacekit

### Basic Usage
```python
import spacekit

# Get NASA Astronomy Picture of the Day (with demo fallback)
apod = spacekit.get_apod_safe()
print("Title:", apod['title'])

# Get space weather data
weather = spacekit.get_space_weather()
print("Solar flares:", weather['solar_flares'])

# Track ISS position
iss = spacekit.satellite_position('ISS')
print("ISS Latitude:", iss['latitude'])
```

---

## 📚 API Reference

### Core Functions

#### `get_apod(api_key="DEMO_KEY")`
Get NASA Astronomy Picture of the Day.

```python
from spacekit import get_apod

# With demo key (rate limited)
result = get_apod()

# With your NASA API key
result = get_apod(api_key="your_nasa_api_key")
```

#### `get_apod_safe()`
Safe version that provides demo data if NASA API fails.

```python
from spacekit import get_apod_safe

# Always returns data, even if API fails
result = get_apod_safe()
print(result['title'])  # Always works
```

#### `get_space_weather()`
Get simulated space weather data.

```python
from spacekit import get_space_weather

weather = get_space_weather()
print(weather['solar_flares'])  # "low", "medium", "high"
```

#### `satellite_position(satellite_name)`
Get satellite position data.

```python
from spacekit import satellite_position

iss = satellite_position('ISS')
print(f"Lat: {iss['latitude']}, Lon: {iss['longitude']}")
```

---

## 📡 Supported APIs

| Feature       |         Module         |    Status   |        Description          |
|---------------|------------------------|-------------|-----------------------------|
| NASA APOD     | `get_apod()`           | ✅ Working | Astronomy Picture of the Day |
| Safe APOD     | `get_apod_safe()`      | ✅ Working | Demo data fallback           |
| Space Weather | `get_space_weather()`  | ✅ Working | Simulated space weather      |
| ISS Tracking  | `satellite_position()` | ✅ Working | Satellite position data      |

---

## 📁 Project Structure
```
spacekit/
├── spacekit/
│   ├── __init__.py          # Package exports
│   ├── nasa.py              # NASA API integration
│   └── astronomy.py         # Astronomy utilities
├── requirements.txt         # Dependencies
├── setup.py                # Package configuration
└── README.md               # This file
```

---

## 📖 Examples

### Complete Demo Script
```python
from spacekit import get_apod_safe, get_space_weather, satellite_position

print("🚀 SpaceKit Demo")
print("NASA APOD:", get_apod_safe()['title'])
print("Space Weather:", get_space_weather()['solar_flares'])
print("ISS Position:", satellite_position('ISS')['latitude'])
```

### Real-time ISS Tracker
```python
import time
from spacekit import satellite_position

while True:
    iss = satellite_position('ISS')
    print(f"ISS: Lat {iss['latitude']}°, Lon {iss['longitude']}°")
    time.sleep(10)
```

---
## 📝 Configuration & API Keys

### NASA API Key
For full NASA API access, get a free key at [api.nasa.gov](https://api.nasa.gov):

```python
from spacekit import get_apod

# Use your NASA API key for full access
result = get_apod(api_key="YOUR_NASA_API_KEY")
```

**Without an API key**, SpaceKit uses NASA's demo key which has rate limits.

---
## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

---
## 🗂 Changelog

### v0.1.0
- Initial release with NASA APOD integration
- Space weather simulation
- Satellite tracking utilities
- Safe fallback mechanisms

---
## 📊 Project Roadmap

- [x] NASA APOD API integration
- [x] Space weather simulation
- [x] Satellite tracking utilities
- [ ] Real NASA API key support
- [ ] More astronomy calculations
- [ ] ISRO data integration
- [ ] Data visualization tools

---
## 🏗 Built With

- **Python 3.8+** - Core programming language
- **Requests** - HTTP library for API calls
- **Setuptools** - Package distribution

---
## ❓ FAQ

**Do I need a NASA API key?**
- Optional. SpaceKit works with the demo key, but for full access get a free key from api.nasa.gov.

**Does it work offline?**
- Basic functions work, but NASA API features require internet.

**Is this free to use?**
- Yes! 100% open-source under MIT License.

**How accurate is the satellite tracking?**
- Currently provides simulated data - real tracking is planned for future versions.

---
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## 📬 Contact

- **GitHub Issues**: [AuralithLabs/spacekit/issues](https://github.com/AuralithLabs/spacekit/issues)
- **Auralith Labs** - Student-led SpaceTech initiative
---

<p align="center"><b>⭐ If you find this project useful, please star the repository! ⭐</b></p>
<p align="center">Built with ❤️ by students passionate about space technology.</p>
```
