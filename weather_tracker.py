import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# --- Configuration ---
latitude = 34.8503
longitude = 5.7281

# --- Fetch Data ---
today = datetime.now()
week_ago = today - timedelta(days=7)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_max,temperature_2m_min"
)

response = requests.get(url)
data = response.json()

# --- Data Processing ---
# Load daily temperature records into a DataFrame
df = pd.DataFrame({
    'date': pd.to_datetime(data['daily']['time']),
    'max_temp': data['daily']['temperature_2m_max'],
    'min_temp': data['daily']['temperature_2m_min']
})

# Compute daily average as the midpoint between recorded high and low
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2