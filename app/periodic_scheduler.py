import threading
import time
from app import weather_api,database

def weather_task(city: str):
    """
    Gibt eine Funktion zurück, die Wetterdaten für `city` abruft und speichert
    """
    def task():
        data = weather_api.get_weather_data(city)
        if 'error' not in data:
            database.insert_weather_data(data)
            print(f"Wetterdaten für {city} erfolgreich gespeichert.")
        else:
            print(f"API Fehler: {data['error']}")
    return task

def start_scheduler(task, interval: int):
    """
    Startet einen Thread, der `task` alle `interval` Sekunden ausführt

    :param task: Funktion, die ausgeführt werden soll
    :param interval: Intervall in Sekunden
    """
    def loop():
        while True:
            task()
            time.sleep(interval)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()