import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WEATHER_DB_PATH = os.path.join(BASE_DIR, 'weather.db')
CONFIG_DB_PATH = os.path.join(BASE_DIR, 'config.db')

def create_config_db():
    """
    Erstellt die config.db und die config-Tabelle, falls noch nicht vorhanden
    """
    try:
        conn = sqlite3.connect(CONFIG_DB_PATH)  # <-- hier Config-DB
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS config (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT UNIQUE,
                interval INTEGER
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Config DB Error: {e}")
    finally:
        conn.close()

def add_city_config(city: str, interval: int):
    """
    Fügt eine neue Konfiguration hinzu

    :param city: Name der Stadt
    :param interval: Intervall in Sekunden
    """
    try:
        conn = sqlite3.connect(CONFIG_DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO config (city, interval) VALUES (?, ?)",
            (city, interval)
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Config DB Insert Error: {e}")
    finally:
        conn.close()

def get_all_configs():
    """
    Gibt alle gespeicherten Konfigurationen zurück
    :return: Liste von Tuples (city, interval)
    """
    try:
        conn = sqlite3.connect(CONFIG_DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT city, interval FROM config")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Config DB Select Error: {e}")
        return []
    finally:
        conn.close()

def create_weather_db():
    """
    Erstellt die weather.db und die weather-Tabelle, falls noch nicht vorhanden
    """
    try:
        # Verbindung zur DB
        conn = sqlite3.connect(WEATHER_DB_PATH)
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
        conn = sqlite3.connect(WEATHER_DB_PATH)
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