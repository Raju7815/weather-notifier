import requests
from plyer import notification

API_KEY = '098d4423b2f1a7fc1f20b20148f392fe'
LAT = 17.3850  # Latitude for Hyderabad
LON = 78.4867  # Longitude for Hyderabad
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'

def get_weather_data(url):
    response = requests.get(url)
    return response.json()

def notify_weather(weather_data):
    title = f"Weather in {weather_data['name']}"
    description = f"Temperature: {weather_data['main']['temp']}°C\n" \
                  f"Weather: {weather_data['weather'][0]['description']}\n" \
                  f"Humidity: {weather_data['main']['humidity']}%\n" \
                  f"Wind Speed: {weather_data['wind']['speed']} m/s"
    notification.notify(
        title=title,
        message=description,
        timeout=10
    )

if _name_ == "_main_":
    weather_data = get_weather_data(URL)
    if weather_data['cod'] == 200:
        notify_weather(weather_data)
    else:
        print("Error fetching weather data")