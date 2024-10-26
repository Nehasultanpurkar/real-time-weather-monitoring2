def check_thresholds(weather):
    if weather['temp'] > 35:  # Example threshold check
        send_alert(f"Temperature alert! Current temp: {weather['temp']}°C")

def send_alert(message):
    print(message)  # or send an email
