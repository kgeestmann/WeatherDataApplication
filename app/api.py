from fastapi import FastAPI, Query
from app import database
import sqlite3

app = FastAPI()

DB_PATH = database.DB_PATH

@app.get("/weather")
def get_weather(city: str | None = None):
    """
    Gibt die gespeicherten Wetterdaten zurück
    Optional kann nach 'city' gefiltert werden
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if city:
        cursor.execute(f'SELECT * FROM weather WHERE city = ?', (city,))
    else:
        cursor.execute('SELECT * FROM weather')

    rows = cursor.fetchall()
    conn.close()

    # result wird als Liste von Dictionaries aufgebaut
    result = []
    for row in rows:
        result.append({
            'id': row[0],
            'city': row[1],
            'description': row[2],
            'temperature': row[3],
            'humidity': row[4],
            'rain_1h': row[5],
            'snow_1h': row[6],
            'timestamp': row[7]
        })

    return result