import sqlite3

def save_weather_data(city, weather):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather_data (city, temp, feels_like, main, dt)
                      VALUES (?, ?, ?, ?, ?)''', (city, weather['temp'], weather['feels_like'], weather['main'], weather['dt']))
    conn.commit()
    conn.close()

def get_daily_summary():
    # Calculate daily rollups like average, max, min temp, and dominant weather
    pass
