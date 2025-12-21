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




