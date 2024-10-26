# real-time-weather-monitoring2
Project Overview

This project is a real-time data processing system designed to monitor weather conditions from major metros in India using the OpenWeatherMap API. The system collects weather data at configurable intervals, processes it to provide daily summaries and triggers alerts based on predefined thresholds. Key features include data rollups and aggregates (average, max, and min temperatures), threshold-based alerting, and data visualization.
Features

    Real-Time Weather Data Collection:
        Continuously fetches weather data from OpenWeatherMap API.
        Retrieves data for Indian metros: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
        Converts temperatures from Kelvin to Celsius or Fahrenheit (based on user preference).

    Daily Weather Summary:
        Calculates daily aggregate metrics:
            Average temperature
            Maximum temperature
            Minimum temperature
            Dominant weather condition
        Stores daily summaries in a database for further analysis.

    Alert System:
        Configurable threshold alerts (e.g., if temperature exceeds 35°C).
        Alerts are triggered if thresholds are breached (e.g., via email or console output).

    Visualization:
        Generates graphs for daily weather summaries and historical trends using matplotlib or Plotly.
        Displays triggered alerts.

    Extensible:
        Support for additional weather parameters (e.g., humidity, wind speed).
        Ability to incorporate weather forecasts for future conditions.

Prerequisites

Before running the application, ensure you have the following installed:

    Python 3.x (Recommended: 3.8 or later)
    pip (Python package manager)
    SQLite/PostgreSQL (For persistent storage)
    Docker (For containerization, optional)
    OpenWeatherMap API Key

Setup Instructions
1. Clone the Repository

bash

git clone https://github.com/your_username/real-time-weather-monitoring.git
cd real-time-weather-monitoring

2. Install Dependencies

Create a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Then install the required Python libraries:

bash

pip install -r requirements.txt

3. Set Up OpenWeatherMap API Key

    Sign up at OpenWeatherMap and obtain a free API key.
    Create a .env file in the root of your project:

bash

touch .env

Add the following content to the .env file:

makefile

API_KEY=your_openweather_api_key

4. Set Up Database

By default, the application uses SQLite for local development. To set up the database:

bash

python setup_db.py

This script will create the necessary tables for storing weather data and daily summaries.
5. Run the Application

Start the weather monitoring system:

bash

python main.py

The system will start fetching weather data at a 5-minute interval and will display information on the console.
6. (Optional) Running with Docker

To run the application in a Docker container:

    Ensure Docker is installed on your machine.
    Build the Docker image:

bash

docker build -t weather-monitor .

    Run the container:

bash

docker run -d --env-file .env weather-monitor

Configuration
Interval Configuration

By default, the system fetches weather data every 5 minutes. You can change this interval in the config.py file:

python

FETCH_INTERVAL = 300  # 300 seconds (5 minutes)

User Preferences

You can set user preferences (like temperature unit, thresholds) in the config.py file.
Threshold Configuration

You can configure threshold values for alerts in the config.py file. For example:

python

TEMP_THRESHOLD = 35  # Celsius
ALERT_CONSECUTIVE_READINGS = 2  # Alert if exceeded for 2 consecutive updates

Application Structure

bash

.
├── main.py            # Entry point for the weather monitoring system
├── config.py          # Configurations for the system (intervals, thresholds)
├── database.py        # Database interaction logic
├── alerts.py          # Alert system for threshold-based notifications
├── visualizations.py  # Code for generating graphs and visualizations
├── setup_db.py        # Script for setting up the database
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

Key Files:

    main.py: Orchestrates the weather data retrieval, processing, and alert system.
    config.py: Contains configurable settings such as API keys, data fetch intervals, and alert thresholds.
    database.py: Handles storing and retrieving weather data from the SQLite/PostgreSQL database.
    alerts.py: Contains logic for threshold checking and alert triggering.
    visualizations.py: Responsible for generating visualizations (daily weather summaries and alerts).

Test Cases

You can run test cases to validate the functionality of the system:
1. System Setup:

    Test that the system starts correctly and connects to the OpenWeatherMap API with a valid API key.

2. Data Retrieval:

    Simulate weather data API calls and check if the data is retrieved and parsed correctly.

3. Temperature Conversion:

    Verify the correct conversion of temperatures from Kelvin to Celsius (or Fahrenheit).

4. Daily Weather Summary:

    Simulate multiple weather updates and verify the correctness of daily aggregate calculations (average, max, min temperatures, and dominant weather condition).

5. Alerting Thresholds:

    Configure a threshold for temperature and simulate data exceeding this threshold to ensure alerts are triggered appropriately.

To run tests (use a framework like unittest or pytest):

bash

pytest tests/

Visualizations

The application includes visualizations for:

    Daily Weather Summaries: Displayed as line charts for average, maximum, and minimum temperatures.
    Historical Trends: Graphs showing temperature trends over multiple days.
    Alerts: Visual markers indicating when thresholds were breached.

The visualizations are generated using matplotlib and can be accessed via a simple Flask-based web dashboard or directly in the console.
Additional Features

    Support for additional weather parameters: Humidity, wind speed, and pressure.
    Future Weather Forecasts: Fetch and analyze future weather predictions from the OpenWeatherMap API.

Known Issues and Future Enhancements

    Issue: In some cases, the OpenWeatherMap API might rate-limit requests if exceeded.
    Future Enhancements: Adding a Redis cache layer to store frequent data and reduce API request

To run test cases separately in your project, here’s a guide to organize and execute them individually. We'll use unittest or pytest as test frameworks, and you can organize tests in different files or directories to run them selectively.
1. Organize Test Cases

Create a dedicated folder named tests to store all test files:

bash

mkdir tests

Inside the tests directory, create separate test files for each module. For example:

plaintext

tests/
├── test_data_retrieval.py
├── test_temperature_conversion.py
├── test_daily_summary.py
├── test_alerting_thresholds.py
└── __init__.py

    Each file should contain test cases relevant to a specific functionality (e.g., test_data_retrieval.py for testing the data retrieval logic).
    Ensure each test file imports necessary modules and functions from your main application.

2. Write Separate Test Cases

Each test file will have specific test cases. Here’s an example structure for test_data_retrieval.py using unittest:

python

# tests/test_data_retrieval.py
import unittest
from your_main_module import fetch_weather_data  # Adjust import as per your structure

class TestDataRetrieval(unittest.TestCase):
    def test_fetch_weather_data(self):
        """Test data retrieval from OpenWeatherMap API"""
        city = "Delhi"
        result = fetch_weather_data(city)
        self.assertIn('temp', result)
        self.assertIn('main', result)
        # Add other assertions as needed

if __name__ == "__main__":
    unittest.main()

3. Run Test Cases Individually

To run test files separately, use the following commands:

    Using unittest (in terminal):

    bash

python -m unittest tests/test_data_retrieval.py

This runs only test_data_retrieval.py. You can replace this with other test file names to run different tests.

Using pytest:

Install pytest if you haven't:

bash

pip install pytest

Run a specific test file with:

bash

pytest tests/test_data_retrieval.py

Or, run all tests in the tests folder:

bash

    pytest tests/

4. Run Individual Test Functions

If you want to run a specific test function within a file:

    With unittest:

    bash

python -m unittest tests.test_data_retrieval.TestDataRetrieval.test_fetch_weather_data

With pytest:

bash

    pytest tests/test_data_retrieval.py::TestDataRetrieval::test_fetch_weather_data

5. Add a Test Runner Script (Optional)

For convenience, create a script (run_tests.sh for Linux/macOS or run_tests.bat for Windows) to run all tests or specific ones.

Example run_tests.sh:

bash

#!/bin/bash
pytest tests/  # Runs all tests

Make it executable:

bash

chmod +x run_tests.sh
./run_tests.sh

This setup lets you run tests in a modular way, helping you isolate and troubleshoot issues more efficiently.
You said:
explian briefly about bonus features iwith code
ChatGPT said:
ChatGPT

For the Real-Time Weather Monitoring System, let’s dive into two bonus features: adding support for additional weather parameters and incorporating weather forecast summaries. These can enrich the application and provide more insightful weather data.
Bonus Feature 1: Support for Additional Weather Parameters

Expanding to additional parameters (e.g., humidity, wind speed, and pressure) involves fetching these values from the OpenWeatherMap API and including them in the rollups and alerts.

    Fetch Additional Parameters:

    OpenWeatherMap’s response JSON includes humidity, wind.speed, and pressure. Update fetch_weather_data() to retrieve these fields.

    python

import requests

API_KEY = 'your_openweather_api_key'

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    return {
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'main': data['weather'][0]['main'],
        'dt': data['dt']
    }

Update Database and Rollup Calculations:

Extend your database schema to store these new parameters, and update the daily rollups to include averages for humidity, pressure, and wind speed.

python

# database.py
def save_weather_data(city, weather):
    # Example for SQLite
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather_data (city, temp, feels_like, humidity, pressure, wind_speed, main, dt)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                      (city, weather['temp'], weather['feels_like'], weather['humidity'], 
                       weather['pressure'], weather['wind_speed'], weather['main'], weather['dt']))
    conn.commit()
    conn.close()

Daily Rollup with New Parameters:

Modify the rollup function to calculate daily average humidity, pressure, and wind speed.

python

    def calculate_daily_rollups():
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT date, AVG(temp), AVG(humidity), AVG(pressure), AVG(wind_speed)
                          FROM weather_data GROUP BY date''')
        daily_summary = cursor.fetchall()
        conn.close()
        return daily_summary

Bonus Feature 2: Weather Forecast Summaries

OpenWeatherMap provides forecast data, which allows you to display predictions for temperature, humidity, and other conditions in upcoming days.

    Fetch Forecast Data:

    Use OpenWeatherMap's forecast endpoint to retrieve data for future weather conditions.

    python

def fetch_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    forecasts = []
    for forecast in data['list']:
        forecasts.append({
            'temp': forecast['main']['temp'],
            'humidity': forecast['main']['humidity'],
            'pressure': forecast['main']['pressure'],
            'wind_speed': forecast['wind']['speed'],
            'main': forecast['weather'][0]['main'],
            'dt': forecast['dt']
        })
    return forecasts

Process Forecast Data:

Calculate average daily forecast for each parameter to summarize upcoming weather.

python

from datetime import datetime

def calculate_forecast_summary(forecasts):
    daily_summary = {}
    for forecast in forecasts:
        date = datetime.fromtimestamp(forecast['dt']).date()
        if date not in daily_summary:
            daily_summary[date] = {
                'temp_sum': 0, 'humidity_sum': 0, 'pressure_sum': 0, 'wind_speed_sum': 0,
                'count': 0, 'dominant_conditions': {}
            }
        daily_summary[date]['temp_sum'] += forecast['temp']
        daily_summary[date]['humidity_sum'] += forecast['humidity']
        daily_summary[date]['pressure_sum'] += forecast['pressure']
        daily_summary[date]['wind_speed_sum'] += forecast['wind_speed']
        daily_summary[date]['count'] += 1
        condition = forecast['main']
        daily_summary[date]['dominant_conditions'][condition] = \
            daily_summary[date]['dominant_conditions'].get(condition, 0) + 1

    # Aggregate
    forecast_summary = []
    for date, values in daily_summary.items():
        avg_temp = values['temp_sum'] / values['count']
        avg_humidity = values['humidity_sum'] / values['count']
        avg_pressure = values['pressure_sum'] / values['count']
        avg_wind_speed = values['wind_speed_sum'] / values['count']
        dominant_weather = max(values['dominant_conditions'], key=values['dominant_conditions'].get)
        forecast_summary.append({
            'date': date,
            'avg_temp': avg_temp,
            'avg_humidity': avg_humidity,
            'avg_pressure': avg_pressure,
            'avg_wind_speed': avg_wind_speed,
            'dominant_weather': dominant_weather
        })
    return forecast_summary

Display Forecast Summaries:

This forecast summary can be visualized using a chart (e.g., line chart for daily temperatures, bar chart for humidity) on the dashboard.

Bonus: Set Forecast-Based Alerts

You can extend threshold alerts to future predictions. For instance, trigger an alert if the forecast predicts temperatures above a certain level.

python

    def check_forecast_alerts(forecast_summary, threshold_temp=35):
        for forecast in forecast_summary:
            if forecast['avg_temp'] > threshold_temp:
                print(f"Alert: Expected high temperature of {forecast['avg_temp']}°C on {forecast['date']}")
The Real-Time Weather Monitoring System effectively demonstrates how real-time data processing can deliver valuable insights and timely alerts using live weather data from OpenWeatherMap. By implementing continuous data retrieval, the system provides daily summaries and enables threshold-based alerts, empowering users to monitor weather conditions for major Indian metros efficiently.

The project highlights key capabilities such as:

    Data Aggregation and Summarization: The system calculates daily rollups (average, max, and min temperatures, and dominant weather conditions) to provide a comprehensive daily summary.
    Real-Time Alerting: Configurable alerts based on temperature or other conditions offer proactive notifications when specified thresholds are breached.
    Forecast-Based Predictions: By incorporating future weather data, the system enables users to anticipate conditions for better planning and awareness.

In addition to these core features, support for additional weather parameters and visualization tools enhances the user experience by providing insights into trends, historical data, and forecast summaries. Overall, this project serves as a robust foundation for real-time weather monitoring, with potential for further expansion to support a broader range of data sources, more granular analytics, and predictive modeling.

