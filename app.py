import requests
import sys

# Rajarhat coordinates
LAT = 22.6148
LON = 88.4326

print("Fetching weather and air quality data...")

# 1. Get Weather Data
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}¤t=temperature_2m,precipitation"
w_data = requests.get(weather_url).json()
temp = w_data['current']['temperature_2m']
precip = w_data['current']['precipitation']

# 2. Get Air Quality (AQI) Data
aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={LAT}&longitude={LON}¤t=us_aqi"
aq_data = requests.get(aq_url).json()
aqi = aq_data['current']['us_aqi']

print(f"🌡️ Current Temperature: {temp}°C")
print(f"🌧️ Precipitation: {precip} mm")
print(f"🌫️ Air Quality Index (AQI): {aqi}")

# 3. Evaluate and Alert
if precip > 0 or aqi > 100:
    print("⚠️ ALERT CONDITION MET: Bad weather or smog detected!")
    # This exit code tells the CI/CD pipeline that the job "failed", triggering an email!
    sys.exit(1)
else:
    print("✅ Weather is clear and air is good. Have a great day!")