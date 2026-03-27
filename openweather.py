import requests
import os

def get_weather_data(city_name):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if not api_key:
        print("Warning: OPENWEATHER_API_KEY not set. Returning N/A for weather.")
        return "N/A"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        temp = data.get('main', {}).get('temp')
        if temp is not None:
            return temp
        return "N/A"
    except Exception as e:
        print(f"Error fetching weather data for {city_name}: {e}")
        return "N/A"
