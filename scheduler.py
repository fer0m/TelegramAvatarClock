from celery_app import app
from core.colored_canvas_creator import ColoredCanvasCreator
from core.element_drawer import ElementDrawer
from core.weather_getter import WeatherGetter, WeatherDataClass
from utils import console_logs, LogType

global_weather_data = None


@app.task
def do_hourly_weather_check():
    try:
        console_logs("Starting hourly weather check task.", LogType.INFO)
        global global_weather_data
        weather_data = WeatherGetter().get_weather_data()
        if weather_data:
            global_weather_data = weather_data
            console_logs("Weather data updated successfully.", LogType.INFO)
        else:
            console_logs("No weather data received.", LogType.INFO)
    except Exception as e:
        console_logs(f"Error in weather check task: {e}", LogType.ERROR)
        raise


@app.task
def do_minutely_create_canvas():
    try:
        console_logs("Starting canvas creation task.", LogType.INFO)
        canvas_creator = ColoredCanvasCreator()
        colored_canvas = canvas_creator.canvas_create()
        elem_drawer = ElementDrawer(colored_canvas, file_name=canvas_creator.filename)
        elem_drawer.draw_time()

        if global_weather_data is None:
            console_logs("Global weather data is null. Make first call to get weather data.", LogType.INFO)
            do_hourly_weather_check()

        if isinstance(global_weather_data, WeatherDataClass):
            elem_drawer.draw_weather(global_weather_data)
            elem_drawer.draw_temperature(global_weather_data)

        console_logs("Canvas creation task completed successfully.", LogType.INFO)
    except Exception as e:
        console_logs(f"Error in canvas creation task: {e}", LogType.ERROR)
        raise
