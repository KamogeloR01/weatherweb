import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Get your free API key at https://openweathermap.org/api
# Then either set it as an environment variable named OPENWEATHER_API_KEY,
# or paste it directly below where it says "YOUR_API_KEY_HERE".
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city from the OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # gives temperature directly in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException:
        return None, "Could not connect to the weather service. Check your internet connection."

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data.get("name", city.title()),
            "country": data["sys"].get("country", ""),
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],
        }
        return weather, None
    elif response.status_code == 404:
        return None, f'City "{city}" not found. Check the spelling and try again.'
    elif response.status_code == 401:
        return None, "Invalid API key. Add a valid OpenWeatherMap API key in app.py."
    else:
        return None, "Something went wrong fetching the weather. Please try again."


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            weather, error = get_weather(city)
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
