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
