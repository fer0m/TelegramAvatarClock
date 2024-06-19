from celery_app import app
from core.colored_canvas_creator import ColoredCanvasCreator
from core.element_drawer import ElementDrawer
from core.weather_getter import WeatherGetter

global_weather_data = None


@app.task
def do_hourly_weather_check():
    global global_weather_data
    weather_data = WeatherGetter().get_weather_data()
    if weather_data:
        global_weather_data = weather_data


@app.task
def do_minutely_create_canvas():
    canvas_creator = ColoredCanvasCreator()
    colored_canvas = canvas_creator.canvas_create()
    elem_drawer = ElementDrawer(colored_canvas, file_name=canvas_creator.filename)
    elem_drawer.draw_time()
    if global_weather_data:
        elem_drawer.draw_weather(global_weather_data)
        elem_drawer.draw_temperature(global_weather_data)
