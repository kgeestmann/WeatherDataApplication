from app import database
from app.periodic_scheduler import start_scheduler, weather_task
import time

def main():
    city_name = "Bremen"
    interval = 5

    database.create_db()

    task = weather_task(city_name)

    # Scheduler starten
    start_scheduler(task, interval)
    print(f"Scheduler gestartet für {city_name}, alle {interval} Sekunden.")

    # Hauptthread aktiv halten
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programm beendet.")

if __name__ == "__main__":
    main()