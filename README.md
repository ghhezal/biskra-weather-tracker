# 🌤️ Biskra Weather Tracker

A lightweight Python script that pulls the past 7 days of real weather data for Biskra, Algeria from the [Open-Meteo](https://open-meteo.com/) free API, processes it with pandas, and produces a temperature trend chart and a CSV export — no API key required.

---

## 📸 Output Preview

Running the script generates two files inside `data/`:

| File | Description |
|---|---|
| `weather_chart.png` | Line chart of max, min, and average temperatures |
| `biskra_weather.csv` | Raw daily temperature records |

---

## ✨ Features

- Fetches live daily max/min temperature data (no API key needed)
- Computes daily average as the midpoint between the high and low
- Plots a clean 7-day temperature trend with color-coded lines
- Exports both the chart (PNG) and the data (CSV) automatically
- Creates the `data/` output folder if it doesn't exist yet

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `requests` | HTTP calls to the Open-Meteo API |
| `pandas` | Data loading and transformation |
| `matplotlib` | Chart generation |
| `datetime` | Dynamic date range calculation |

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/biskra-weather-tracker.git
cd biskra-weather-tracker
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python weather_tracker.py
```

**Expected output in the terminal:**
```
Average temperature: 28.4°C
Files saved in 'data' folder
```

The `data/` folder will contain your chart and CSV after the first run.

---

## 📁 Project Structure

```
biskra-weather-tracker/
├── weather_tracker.py   # Main script
├── requirements.txt     # Python dependencies
├── .gitignore           # Files excluded from version control
├── data/
│   └── .gitkeep         # Keeps the folder tracked by Git (outputs are ignored)
└── README.md
```

---

## 🌍 Changing the Location

The coordinates are set near the top of `weather_tracker.py`:

```python
latitude = 34.8503
longitude = 5.7281
```

Replace them with any coordinates you like. You can find coordinates for any city on [latlong.net](https://www.latlong.net/). Remember to update the chart title on this line too:

```python
plt.title('Biskra Weather - Past Week')
```

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> Built with Python · Data from [Open-Meteo](https://open-meteo.com/) (free, no API key required)
