import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'weather.db')

def create_db():
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