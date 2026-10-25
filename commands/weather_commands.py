import requests
from config import WEATHER_API_KEY
from utils.logger import log_action
def get_weather():
    city = input("Enter city name: ")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
    )
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data["cod"] != 200:
            print("âŒ City not found. Please enter a valid city.")
            return
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print("\n" + "=" * 45)
        print("            ðŸŒ¦ WEATHER REPORT")
        print("=" * 45)
        print(f"ðŸ“ City        : {city_name}, {country}")
        print(f"ðŸŒ¡ Temperature : {temperature}Â°C")
        print(f"ðŸ¤— Feels Like  : {feels_like}Â°C")
        print(f"ðŸ’§ Humidity    : {humidity}%")
        print(f"ðŸŒ¥ Condition   : {description.title()}")
        print(f"ðŸ’¨ Wind Speed  : {wind_speed} m/s")
        print(f"ðŸ§­ Pressure    : {pressure} hPa")
        print("=" * 45)
        log_action(f"Checked weather for {city_name}")
    except requests.exceptions.RequestException:
        print("âŒ Unable to connect to the weather service.")
