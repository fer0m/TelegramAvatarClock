import os
import sys
from pathlib import Path

import cairosvg
from PIL import Image, ImageFilter, ImageDraw, ImageFont

from core.canvas_base import CanvasBase
from core.weather_getter import WeatherDataClass
import main_config
from core.wrap_tools import set_font_size

sys.path.append(str(Path(__file__).resolve().parent.parent))


class ElementDrawer(CanvasBase):
    current_zone = 'UTC +01:00'

    def __init__(self, canvas: Image, file_name: str):
        super().__init__()
        self.canvas: Image = canvas
        self.draw: ImageDraw = ImageDraw.Draw(self.canvas)
        self.file_name = file_name
        self.font = ImageFont.truetype(str(main_config.FONT_FILE_PATH))

    def draw_time(self) -> None:
        self.draw_time_on_canvas()
        self.draw_utc_zone()
        self.canvas.save(self.file_name)

    @set_font_size(240)
    def draw_time_on_canvas(self):
        bbox = self.draw.textbbox((0, 0), self.formatted_current_time, font=self.font)
        width_font, height_font = bbox[2] - bbox[0], bbox[3] - bbox[1]
        coordinate = ((self.canvas.width - width_font) / 2, (self.canvas.height - height_font) / 2)
        self.draw.text(coordinate, self.formatted_current_time, fill=(255, 255, 255), font=self.font)

    @set_font_size(60)
    def draw_utc_zone(self):
        bbox = self.draw.textbbox((0, 0), self.current_zone, font=self.font)
        width_font, height_font = bbox[2] - bbox[0], bbox[3] - bbox[1]
        coordinate = ((self.canvas.width - width_font) / 2, 380)
        self.draw.text(coordinate, self.current_zone, fill=(255, 255, 255), font=self.font)

    @set_font_size(60)
    def draw_weather_temperature(self):
        bbox = self.draw.textbbox((0, 0), self.current_zone, font=self.font)
        width_font, height_font = bbox[2] - bbox[0], bbox[3] - bbox[1]
        coordinate = ((self.canvas.width - width_font) / 2, 380)
        self.draw.text(coordinate, self.current_zone, fill=(255, 255, 255), font=self.font)

    def draw_weather(self, weather_data: WeatherDataClass):
        icon_name: str = weather_data.weather_icon_name
        icon: Image = self._get_icon(icon_name)
        self.canvas.paste(icon, (130, 50), icon)
        self.canvas.save(self.file_name)

    @staticmethod
    def _get_icon(icon_name: str) -> Image:
        icon_svg_path = f"{str(main_config.ICONS_DIR)}/{icon_name}.svg"
        icon_png_path = f"{str(main_config.ICONS_DIR)}/{icon_name}.png"
        if not os.path.exists(icon_svg_path):
            raise FileNotFoundError(f"SVG file not found: {icon_svg_path}")
        if not os.path.exists(icon_svg_path):
            raise FileNotFoundError(f"SVG file not found: {icon_png_path}")

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

    def draw_temperature(self, weather_data: WeatherDataClass):
        icon_name: str = str(weather_data.temperature)
        icon: Image = self._get_icon(icon_name)
        self.canvas.paste(icon, (130, 50), icon)
        self.canvas.save(self.file_name)
