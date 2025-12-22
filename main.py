from pydantic_core.core_schema import date_schema

from app import database
from app.periodic_scheduler import start_scheduler, weather_task
import time

def main():
    database.create_weather_db()
    database.create_config_db()

    print("Willkommen! Bitte wähle:")
    print("1. Vorhandene Konfiguration auswählen")
    print("2. Neue Konfiguration erstellen")
    print("3. Default (Bremen, 30min)\n")

    choice = input("Deine Wahl: ")

    try:
        if choice not in {"1", "2", "3"}:
            raise ValueError("Bitte 1, 2 oder 3 eingeben\n")

        if choice == "1":
            configs = database.get_all_configs()
            if not configs:
                print("Keine Konfigurationen vorhanden.\n")
                return main()

            print("Verfügbare Konfigurationen:")
            for cfg_id, city_name, interval in configs:
                print(f"{cfg_id}. {city_name} ({interval}s)")

            selected_id = int(input("Wähle eine Konfiguration (ID): "))

            selected_config = next(
                (cfg for cfg in configs if cfg[0] == selected_id),
                None
            )

            if not selected_config:
                raise ValueError("Ungültige Konfigurations-ID")

            city_name, interval = selected_config[1], selected_config[2]

        elif choice == "2":
            city_name = input("Stadtname: ").strip()
            if not city_name:
                raise ValueError("Stadtname darf nicht leer sein\n")

            interval = int(input("Intervall in Sekunden: "))
            if interval <= 0:
                raise ValueError("Intervall muss größer als 0 sein\n")

            database.add_city_config(city_name, interval)

        elif choice == "3":
            city_name = "Bremen"
            interval = 1800

    except ValueError as e:
        print(f"Fehler: {e}\n")
        return main()

    # Scheduler starten
    task = weather_task(city_name)
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