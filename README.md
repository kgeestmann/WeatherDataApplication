# Weather Data Application

## Ziel der Anwendung
Die Anwendung dient dazu, Wetterdaten für bestimmte Orte automatisch abzurufen,
zu speichern und für spätere Analysen bereitzustellen.  
NutzerInnen sollen historische Wetterdaten einsehen können, ohne diese
manuell erfassen zu müssen.

---

## Funktionale Anforderungen

### Basis-Funktionen (Level 1 - Pflicht)

- Anbindung einer Wetter-API (z.B. OpenWeatherMap)
(Temperatur, Niederschlag, Luftfeuchtigkeit)
- Periodisches Abrufen von Wetterdaten
(z.B. alle 30 Minuten)
- Die Wetterdaten müssen für einen fest definierten Ort abgefragt werden
- Persistierung der Daten in einer Datenbank
- Einfacher API-Endpoint zum Abfragen der gespeicherten Daten

---

## Erweiterbare Anforderungen (optional)

### Level 2
- Ort (z.B. Koordinaten) und Abfrage-Intervall sollen konfigurierbar sein
- Persistierung der Konfiguration
- Einfache grafische Oberfläche zur Darstellung der historischen Wetterdaten

### Level 3
- Suchfunktion nach Ort und Zeitraum in der grafischen Oberfläche
- Speicherung des Suchverlaufs

---

## Abhängigkeiten installieren

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

---

## Lokale API Keys einrichten

Damit die Anwendung auf die Wetter-API zugreifen kann, muss ein API-Key hinterlegt werden:

1. Die Datei `.env_example` kopieren und umbenennen in `.env`
2. In `.env` den Platzhalter `dein_api_key_hier` mit deinem echten API-Key von **OpenWeatherMap** ersetzen

Die Anwendung liest den Key automatisch aus `.env`, sodass er nicht im Code oder im GitHub-Repository sichtbar ist.

---

## Lokalen FastAPI-Server starten

Um den API-Server zu starten, verwende:

```bash
uvicorn app.api:app --reload
```
---

# Quellen
- OpenWeatherMap API Tutorial (https://youtu.be/aQZzMJgPMqQ?si=50JCfIDU3Oh1jdju)
- OpenWeatherMap API Dokumentation (https://openweathermap.org/current)
- SQLite Tutorial (https://youtube.com/playlist?list=PLJJcOjd3n1ZfwZKYMu_JSs0xSejPsQlav&si=8Og2eIMdopEc4nVv)