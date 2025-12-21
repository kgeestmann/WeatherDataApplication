from dotenv import load_dotenv
import os
import requests

# Umgebungsvariablen aus .env laden
load_dotenv()

# API-Key auslesen
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# API-Key prüfen
if not API_KEY:
    raise ValueError(
        "API-Key nicht gefunden! "
        "Erstellen Sie eine Datei '.env' basierend auf '.env_example' "
        "und tragen dort deinen API-Key ein."
    )

city_name = "Bremen"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

print('success')