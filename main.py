from app import weather_api, database

def main():

    database.create_db()

    # Fest definierter Ort
    city_name = 'Bremen'

    weather_data = weather_api.get_weather_data(city_name)

    if 'error' not in weather_data:
        database.insert_weather_data(weather_data)
        print(f"Wetterdaten für {city_name} erfolgreich gespeichert.")
    else:
        print("API Fehler:", weather_data['error'])

    # Test-Print, ob alles gespeichert wurde
    print("Aktuell in DB gespeicherte Wetterdaten:")
    import sqlite3
    from app.database import DB_PATH

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weather")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    finally:
        conn.close()

if __name__ == "__main__":
        main()