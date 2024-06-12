class WeatherImageMixin:
    weather_icons = {
        0: {"day": "wi-day-sunny", "night": "wi-night-clear"},  # Clear sky
        1: {"day": "wi-day-cloudy", "night": "wi-night-alt-cloudy"},  # Mainly clear
        2: {"day": "wi-day-cloudy", "night": "wi-night-alt-cloudy"},  # Partly cloudy
        3: {"day": "wi-cloudy", "night": "wi-night-cloudy"},  # Overcast
        45: {"day": "wi-fog", "night": "wi-night-fog"},  # Fog
        48: {"day": "wi-fog", "night": "wi-night-fog"},  # Depositing rime fog
        51: {"day": "wi-day-sprinkle", "night": "wi-night-alt-sprinkle"},  # Drizzle: Light intensity
        53: {"day": "wi-day-sprinkle", "night": "wi-night-alt-sprinkle"},  # Drizzle: Moderate intensity
        55: {"day": "wi-day-sprinkle", "night": "wi-night-alt-sprinkle"},  # Drizzle: Dense intensity
        56: {"day": "wi-day-rain-mix", "night": "wi-night-alt-rain-mix"},  # Freezing Drizzle: Light intensity
        57: {"day": "wi-day-rain-mix", "night": "wi-night-alt-rain-mix"},  # Freezing Drizzle: Dense intensity
        61: {"day": "wi-day-rain", "night": "wi-night-alt-rain"},  # Rain: Slight intensity
        63: {"day": "wi-day-rain", "night": "wi-night-alt-rain"},  # Rain: Moderate intensity
        65: {"day": "wi-day-rain", "night": "wi-night-alt-rain"},  # Rain: Heavy intensity
        66: {"day": "wi-day-rain-mix", "night": "wi-night-alt-rain-mix"},  # Freezing Rain: Light intensity
        67: {"day": "wi-day-rain-mix", "night": "wi-night-alt-rain-mix"},  # Freezing Rain: Heavy intensity
        71: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow fall: Slight intensity
        73: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow fall: Moderate intensity
        75: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow fall: Heavy intensity
        77: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow grains
        80: {"day": "wi-day-showers", "night": "wi-night-alt-showers"},  # Rain showers: Slight intensity
        81: {"day": "wi-day-showers", "night": "wi-night-alt-showers"},  # Rain showers: Moderate intensity
        82: {"day": "wi-day-showers", "night": "wi-night-alt-showers"},  # Rain showers: Violent intensity
        85: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow showers: Slight intensity
        86: {"day": "wi-day-snow", "night": "wi-night-alt-snow"},  # Snow showers: Heavy intensity
        95: {"day": "wi-day-thunderstorm", "night": "wi-night-alt-thunderstorm"},  # Thunderstorm: Slight or moderate
        96: {"day": "wi-day-thunderstorm", "night": "wi-night-alt-thunderstorm"},  # Thunderstorm with slight hail
        99: {"day": "wi-day-thunderstorm", "night": "wi-night-alt-thunderstorm"}  # Thunderstorm with heavy hail
    }
