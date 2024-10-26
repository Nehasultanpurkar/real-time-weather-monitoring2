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

