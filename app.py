import requests
import sys
import os

# Grab the secrets securely passed by GitHub Actions
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

LAT = 26.1722
LON = 91.7458

print("Fetching forecast for the next 12 hours...")

url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=precipitation,weathercode&forecast_hours=12"
data = requests.get(url).json()

if 'hourly' not in data:
    print("❌ API Error!")
    sys.exit(1)

precip_list = data['hourly']['precipitation']
codes_list = data['hourly']['weathercode']

bad_weather_detected = False
alert_message = ""

for i in range(12):
    precip = precip_list[i]
    code = codes_list[i]
    
    if precip > 5.0 or code in [65, 95, 96, 99]:
        bad_weather_detected = True
        hour_word = "hours" if i != 1 else "hour"
        alert_message = f"🚨 *Weather Alert for Guwahati* 🚨\nHeavy Rain or Thunderstorm expected in about {i} {hour_word}!"
        break

if bad_weather_detected:
    print("⚠️ Bad weather detected! Sending Telegram alert...")
    
    # Send the message via Telegram API
    tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": alert_message,
        "parse_mode": "Markdown"
    }
    requests.post(tg_url, json=payload)
    
    # We exit cleanly now (exit code 0) so the pipeline stays green!
    sys.exit(0)
else:
    print("✅ Forecast clear. No alert sent.")