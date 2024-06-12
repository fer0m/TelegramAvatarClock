import typing

from PIL import Image
from fastapi import FastAPI

from core.colored_canvas_creator import ColoredCanvasCreator
from core.element_drawer import ElementDrawer
from core.weather_getter import WeatherGetter, WeatherDataClass

app = FastAPI()


@app.get("/")
async def root():
    canvas_creator: ColoredCanvasCreator = ColoredCanvasCreator()
    colored_canvas: Image = canvas_creator.canvas_create()

    elem_drawer: ElementDrawer = ElementDrawer(colored_canvas, file_name=canvas_creator.filename)
    elem_drawer.draw_time()

    weather_data: typing.Union[WeatherDataClass | None] = WeatherGetter().get_weather_data()
    if weather_data:
        elem_drawer.draw_weather(weather_data)
    return {"message": "Create"}