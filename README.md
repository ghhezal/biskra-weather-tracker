# Biskra Weather Tracker

I built this to get comfortable with APIs, pandas, and matplotlib all in one small project. It pulls the last 7 days of real temperature data for Biskra from Open-Meteo (free, no API key), crunches the numbers, and spits out a chart and a CSV. Nothing fancy — just a clean script that does one thing well.

---

## What it does

- Hits the Open-Meteo API for daily max/min temps over the past week
- Calculates the daily average (midpoint between high and low)
- Plots all three as a line chart and saves it as a PNG
- Also saves the raw numbers to a CSV
- Creates the `data/` output folder automatically if it's not there

---

## Output

After running, you'll find two files in `data/`:

| File | What's in it |
|---|---|
| `weather_chart.png` | 7-day temperature trend (max, min, average) |
| `biskra_weather.csv` | The raw daily data behind the chart |

---

## Setup

Clone the repo and step into it:

```bash
git clone https://github.com/your-username/biskra-weather-tracker.git
cd biskra-weather-tracker
```

Create a virtual environment and activate it:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Run it

```bash
python weather_tracker.py
```

You should see something like:

```
Average temperature: 28.4°C
Files saved in 'data' folder
```

---

## Want to track a different city?

Two lines to change at the top of `weather_tracker.py`:

```python
latitude = 34.8503
longitude = 5.7281
```

Swap in any coordinates you want — [latlong.net](https://www.latlong.net/) is handy for that. Then update the chart title a bit further down so it matches:

```python
plt.title('Biskra Weather - Past Week')
```

---

## Project layout

```
biskra-weather-tracker/
├── weather_tracker.py   # the whole script
├── requirements.txt
├── .gitignore
├── data/
│   └── .gitkeep         # keeps the folder in git; actual output files are ignored
└── README.md
```

---

## Stack

`requests` · `pandas` · `matplotlib` · `datetime`

Weather data from [Open-Meteo](https://open-meteo.com/) — free and open, no account needed.
