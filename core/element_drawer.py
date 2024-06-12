import sys
from pathlib import Path

import cairosvg
from PIL import Image, ImageFilter, ImageDraw, ImageOps, ImageFont

from core.canvas_base import CanvasBase
from core.weather_getter import WeatherDataClass

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config


class ElementDrawer(CanvasBase):
    def __init__(self, canvas: Image, file_name: str):
        super().__init__()
        self.canvas: Image = canvas
        self.file_name = file_name

    def draw_time(self) -> None:
        self.draw_time_on_canvas()
        self.draw_utc_zone()
        self.canvas.save(self.file_name)

    def draw_time_on_canvas(self):
        draw = ImageDraw.Draw(self.canvas)
        font = ImageFont.truetype(str(config.FONT_FILE_PATH), 240)

        bbox = draw.textbbox((0, 0), self.formatted_current_time, font=font)
        width_font, height_font = bbox[2] - bbox[0], bbox[3] - bbox[1]
        coordinate = ((self.canvas.width - width_font) / 2, (self.canvas.height - height_font) / 2)
        draw.text(coordinate, self.formatted_current_time, fill=(255, 255, 255), font=font)

    def draw_utc_zone(self):
        current_zone = 'UTC +01:00'

        draw = ImageDraw.Draw(self.canvas)
        font = ImageFont.truetype(str(config.FONT_FILE_PATH), 60)

        bbox = draw.textbbox((0, 0), current_zone, font=font)
        width_font, height_font = bbox[2] - bbox[0], bbox[3] - bbox[1]
        coordinate = ((self.canvas.width - width_font) / 2, 380)
        draw.text(coordinate, current_zone, fill=(255, 255, 255), font=font)

    def draw_weather(self, weather_data: WeatherDataClass):
        icon_name: str = weather_data.weather_icon_name
        icon: Image = self._get_icon(icon_name)
        self.canvas.paste(icon, (130, 50), icon)
        self.canvas.save(self.file_name)

    @staticmethod
    def _get_icon(icon_name: str) -> Image:
        icon_svg_path = f"{str(config.ICONS_DIR)}/{icon_name}.svg"
        icon_png_path = f"{str(config.ICONS_DIR)}/{icon_name}.png"
        cairosvg.svg2png(url=icon_svg_path, write_to=icon_png_path, output_width=1000, output_height=1000)
        icon = Image.open(icon_png_path).resize((75, 75), Image.LANCZOS)
        icon = icon.convert("RGBA")
        data = icon.getdata()

        new_data = []
        for item in data:
            if item[3] != 0:
                new_data.append((255, 255, 255, item[3]))
            else:
                new_data.append(item)
        icon = icon.filter(ImageFilter.FIND_EDGES)
        icon.putdata(new_data)
        return icon
