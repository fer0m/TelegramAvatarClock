from dataclasses import dataclass

import requests

from core.weather_mixin import WeatherImageMixin


@dataclass
class WeatherDataClass:
    temperature: int
    weather_icon_name: str


class WeatherGetter(WeatherImageMixin):
    API_URL = "https://api.open-meteo.com/v1/forecast"
    PARAMS = {
        "latitude": 49.4521,  # Широта Нюрнберга
        "longitude": 11.0767,  # Долгота Нюрнберга
        "current_weather": True
    }

    def get_weather_from_api(self):
        response = requests.get(self.API_URL, params=self.PARAMS)
        data = response.json()

        if response.status_code == 200:
            weather = data['current_weather']
            return {
                "temperature": weather['temperature'],
                "windspeed": weather['windspeed'],
                "weathercode": weather['weathercode'],
                "is_day": weather['is_day']
            }
        else:
            return {"error": data}

    def get_weather_data(self) -> WeatherDataClass or None:
        try:
            weather = self.get_weather_from_api()
            icon_set = self.weather_icons.get(weather['weathercode'], {"day": "wi-na", "night": "wi-na"})
            icon_name = icon_set["day"] if weather["is_day"] else icon_set["night"]
            return WeatherDataClass(
                temperature=weather.get("temperature"),
                weather_icon_name=icon_name
            )
        except Exception as e:
            print(f"[ERROR] 'get_weather_data' finished with error: {e}")
            return None

