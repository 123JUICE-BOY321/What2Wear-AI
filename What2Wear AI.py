import streamlit as st
import requests
import math
import google.generativeai as genai

st.set_page_config("What2Wear AI", page_icon="👕", layout="wide", initial_sidebar_state="expanded")

# HEADER
st.title("👕 What2Wear AI")
st.caption("Your Mom Used to Tell You What to Wear. Now We Do.")

# SIDEBAR
st.sidebar.title("⚙️ Configuration")
st.sidebar.subheader("🌍 Location")
if "city" not in st.session_state:
    st.session_state["city"] = ""
if st.sidebar.button("📍 Detect My Location"):
    try:
        location_data = requests.get("https://ipinfo.io/json").json()
        st.session_state["city"] = location_data.get("city", "")
    except Exception as e:
        st.error("Failed to fetch location. Check your internet connection.")
        print(e)
st.session_state["city"] = st.sidebar.text_input("Or enter your city manually", value=st.session_state["city"])
st.sidebar.subheader("🔐 API Keys")
weather_api_key = st.sidebar.text_input("🌦️ OpenWeather API Key", type="password")
gemini_api_key = st.sidebar.text_input("🧠 Google Gemini API Key", type="password")
with st.sidebar.expander("🔑 Grab API keys below:"):
    st.markdown("- [🌦️ OpenWeather API](https://openweathermap.org/api)")
    st.markdown("- [🧠 Google Gemini API](https://ai.google.dev/gemini-api/docs)")

# LOCATION
city = st.session_state.get("city")
if city:
    st.success(f"Location detected: {city}")
else:
    st.info("Please detect or enter your city to continue.")

# WEATHER
def get_weather(city, api_key):
    if not api_key:
        return None
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        st.error("Failed to fetch weather. Check your internet connection.")
        print(e)
    return None

weather = ""
if city and weather_api_key:
    if not weather:
        weather = get_weather(city, weather_api_key)
    if weather:
        st.header(f"🏙️ Weather in {city}")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.metric("🌡️ Temperature", f"{weather['main']['temp']}°C", border=True)
            col3, col4 = st.columns([1, 1])
            with col3:
                weather_icon={"Thunderstorm":"⛈️", "Drizzle":"🌦️", "Rain":"🌧️", "Snow":"🌨️", "Clear":"☀️", "Clouds":"🌥️"}
                st.metric(f"{weather['weather'][0]['description'].title()}", f"{weather_icon.get(weather['weather'][0]['main'], "🌫️")}", border=True)
            with col4:
                st.metric("☁️ Cloud Cover", f"{weather['clouds']['all']}%", border=True)
            col5, col6= st.columns([1, 1])
            with col5:
                st.metric("💧 Humidity", f"{weather['main']['humidity']}%", border=True)
            with col6:
                st.metric("🍃 Wind Speed", f"{weather['wind']['speed']}m/s", border=True)
        with col2:
            lon = weather['coord']['lon']
            lat = math.radians(weather['coord']['lat'])
            z = 4
            x = int((lon + 180.0) / 360.0 * (2 ** z))
            y = int((1.0 - math.log(math.tan(lat) + 1 / math.cos(lat)) / math.pi) / 2.0 * (2 ** z))
            map_url = f"https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid={weather_api_key}"
            st.image(map_url, use_container_width=True)
elif city:
    st.info("Please enter your OpenWeather API Key to continue.")

# GOOGLE GEMINI
if weather and gemini_api_key:
    genai.configure(api_key=gemini_api_key)
    st.divider()
    st.header("🧥 Clothing Recommendation")
    clothing_options = ["T-shirt", "Sweater", "Jacket", "Coat", "Shorts", "Jeans", "Raincoat", "Hat", "Scarf", "Gloves", "Sunglasses", "Sandals", "Sneakers", "Boots"]
    selected_clothing = st.multiselect("🧍 What are YOU thinking of wearing?", clothing_options)
    if st.button("🤖 Ask Google Gemini"):
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-lite")
            prompt = f"""
You are a weather-aware fashion assistant. Given the current weather and the user's selected clothing items, respond in the following format:

1. 🌡️ Weather Summary
2. 🧍 User's Selected Outfit
3. 🧠 Gemini's Verdict
4. 👕 Gemini's Suggested Outfit
5. ☂️ Umbrella Check

Weather:
- City: {city}
- Temperature: {weather['main']['temp']}°C
- Condition: {weather['weather'][0]['description']}
- Cloud Cover: {weather['clouds']['all']}
- Humidity: {weather['main']['humidity']}%
- Wind Speed: {weather['wind']['speed']} m/s

User's Outfit: {', '.join(selected_clothing) if selected_clothing else 'No outfit selected'}

☂️ Umbrella Check: Suggest carrying an umbrella if weather conditions include rain, drizzle, or thunderstorms.

Answer like a personal professional butler.
            """
            with st.spinner("🧠 Gemini is evaluating your outfit..."):
                response = model.generate_content(prompt)
                st.info(response.text.strip())
        except Exception as e:
            st.error(f"Failed to fetch Gemini Result. Check your internet connection.")
            print(e)
elif weather:
    st.info("Please enter your Google Gemini API Key to continue.")

st.divider()
st.caption("Built with ❤️ using Streamlit, OpenWeather and Google Gemini.")