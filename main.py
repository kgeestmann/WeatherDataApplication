from app import weather_api, database

database.create_db()
print(weather_api.get_weather_data('Bremen'))