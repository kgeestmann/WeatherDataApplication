from dotenv import load_dotenv
import os
import requests

# Umgebungsvariablen aus .env laden
load_dotenv()

# API-Key auslesen
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather_data(city_name: str) -> dict:
    """
    Ruft aktuelle Wetterdaten für eine Stadt ab

    :param city_name: Name der Stadt
    :return: Dictionary mit Keys city, description, temperature, humidity, rain_1h, snow_1h, timestamp oder 'error'
    """
    # API-Key prüfen
    if not API_KEY:
            raise ValueError("API-Key nicht gefunden!")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # HTTP-Fehler abfangen
        data = response.json()

        return {
            "city": city_name,
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rain_1h": data.get("rain", {}).get("1h", 0.0),
            "snow_1h": data.get("snow", {}).get("1h", 0.0),
            "timestamp": data["dt"]
        }
    except requests.RequestException as e:
        return {"error": str(e)}