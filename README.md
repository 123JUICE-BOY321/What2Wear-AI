# 👕 What2Wear AI

**Your Mom Used to Tell You What to Wear. Now We Do.**

What2Wear AI is a personalized weather-based clothing recommendation app built using **Streamlit**, **OpenWeather API**, and **Google Gemini AI**. It detects your location, fetches real-time weather data, and uses generative AI to suggest what you should wear based on the weather and your current outfit choices.

---

## 🚀 Features

- 🌍 **Automatic or manual location detection**
- 🌦️ **Real-time weather fetching** via OpenWeather
- 🧥 **AI-powered outfit recommendations** using Google Gemini
- 🧠 Gemini responds like a professional stylist or personal butler
- 📍 **Dynamic weather map tile** based on coordinates
- 💡 Sleek and responsive UI with Streamlit

---

## 🛠️ Requirements

- Python 3.8+
- Streamlit
- `requests`
- `google-generativeai`

Install the dependencies:

```bash
pip install streamlit requests google-generativeai
```
---

## 🔐 API Keys Required

You'll need API keys from:

- [OpenWeather](https://openweathermap.org/api)
- [Google AI Studio (Gemini)](https://makersuite.google.com/app)

These are entered in the sidebar of the app when it runs.

---

## 🧪 How to Run

```bash
streamlit run app.py
```

Then open the app in your browser, follow the sidebar instructions to enter your location and API keys, and let What2Wear AI guide your fashion!

---

## 📸 Screenshot

_Add a screenshot here to show off your UI._

---

## 🤖 How It Works

1. Detects your city using IP or manual entry.
2. Fetches weather data from OpenWeather.
3. Displays weather metrics and a live map tile.
4. Accepts your clothing preferences.
5. Sends context and outfit choices to Gemini AI.
6. Returns a detailed, friendly fashion recommendation.

---

## ❤️ Built With

- [Streamlit](https://streamlit.io/)
- [OpenWeather](https://openweathermap.org/)
- [Google Gemini](https://ai.google.dev/)

---

## 📄 License

MIT License — feel free to use, modify, and share.

