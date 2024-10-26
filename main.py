import requests
from database import save_weather_data, get_daily_summary
from alerts import check_thresholds, send_alert

API_KEY = 'your_openweather_api_key'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'main': data['weather'][0]['main'],
        'dt': data['dt']
    }

def process_weather_data():
    for city in CITIES:
        weather = fetch_weather_data(city)
        weather['temp'] = convert_to_celsius(weather['temp'])  # Convert Kelvin to Celsius
        save_weather_data(city, weather)  # Save to DB
        check_thresholds(weather)  # Check for alerts

if __name__ == "__main__":
    process_weather_data()
