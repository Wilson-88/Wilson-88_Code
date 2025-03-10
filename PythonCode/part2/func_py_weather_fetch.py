# func_py_weather_fetch.py
import requests

def func_py_weather_fetch(city):
    api_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(api_url)
    return response.text if response.status_code == 200 else "Failed to fetch weather"

print(func_py_weather_fetch("London"))
