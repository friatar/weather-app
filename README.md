# 🌤️ Hourly Weather & Air Alert App

An automated Python script that monitors the weather forecast for Guwahati, Assam, and sends live alerts to a Telegram channel via a GitHub Actions CI/CD pipeline. 

Instead of manually checking the weather, this application runs entirely in the cloud, looking 12 hours into the future for heavy rain or thunderstorms and notifying you instantly if bad weather is detected.

## 🚀 Features
* **Predictive Radar:** Uses the Open-Meteo API to fetch the 12-hour hourly forecast.
* **Smart Alerting:** Triggers alerts specifically for heavy precipitation (> 5.0 mm) or severe WMO weather codes (Thunderstorms & Heavy Rain).
* **Automated CI/CD:** Runs continuously on a scheduled cron job (`0 * * * *`) using GitHub Actions.
* **Rich Notifications:** Dispatches formatted Markdown alerts directly to a personal Chat ID using the official Telegram Bot API.
* **Secure Credentials:** Keeps API tokens and Chat IDs completely hidden using GitHub Secrets.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Libraries:** `requests`
* **Automation:** GitHub Actions (Ubuntu Latest)
* **Data Provider:** [Open-Meteo API](https://open-meteo.com/) (Free, no-auth weather data)
* **Integration:** Telegram Bot API

## 📂 Project Structure
```text
├── .github/
│   └── workflows/
│       └── weather-alert.yml   # The CI/CD pipeline configuration
├── app.py                      # The main Python script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
