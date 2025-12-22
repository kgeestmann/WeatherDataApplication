import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(BASE_DIR, 'weather.db')

def create_db():
    """
    Erstellt die weather.db und die weather-Tabelle, falls noch nicht vorhanden
    """
    try:
        # Verbindung zur DB
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Tabelle erstellen, falls nicht vorhanden
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                description TEXT,
                temperature REAL,
                humidity INTEGER,
                rain_1h REAL,
                snow_1h REAL,
                timestamp TEXT
            )
        ''')

        conn.commit()

    except sqlite3.Error as e:
        print(f"DB Error: {e}")

    # Verbindung schließen, auch bei Exception
    finally:
        conn.close()

def insert_weather_data(weather_data: dict):
    """
    Fügt einen Wetter-Datensatz in die weather-Tabelle ein

    :param weather_data: Dictionary mit den Keys city, description, temperature, humidity, rain_1h, snow_1h, timestamp
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather (city, description, temperature, humidity, rain_1h, snow_1h, timestamp) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                weather_data['city'],
                weather_data['description'],
                weather_data['temperature'],
                weather_data['humidity'],
                weather_data.get('rain_1h', 0.0),
                weather_data.get('snow_1h', 0.0),
                weather_data['timestamp']
            )
        )
        conn.commit()

    except sqlite3.Error as e:
        print(f"DB Insert Error: {e}")

    finally:
        conn.close()