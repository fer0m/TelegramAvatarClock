from PIL import Image, ImageDraw

from core.canvas_base import CanvasBase


class ColoredCanvasCreator(CanvasBase):
    brightness_factor = 0.90

    @staticmethod
    def interpolate_color(color1, color2, factor):
        """Interpolate between two RGB colors by a given factor (0.0 - 1.0)"""
        return tuple(int(a + (b - a) * factor) for a, b in zip(color1, color2))

    @staticmethod
    def get_gradient_colors(time_str: str):
        current_hour, current_minute = map(int, time_str.split(':'))
        current_time_in_minutes = current_hour * 60 + current_minute
        for interval in CanvasBase.TIME_COLORS_RATIO:
            start_time, end_time = interval.split('-')
            start_hour, start_minute = map(int, start_time.split(':'))
            end_hour, end_minute = map(int, end_time.split(':'))

            start_time_in_minutes = start_hour * 60 + start_minute
            end_time_in_minutes = end_hour * 60 + end_minute

            if start_time_in_minutes <= current_time_in_minutes < end_time_in_minutes:
                return CanvasBase.TIME_COLORS_RATIO[interval], start_hour, end_hour

    def calculate_time_factor(self, start_hour, end_hour) -> float:
        start_seconds = start_hour * 3600
        end_seconds = end_hour * 3600
        current_seconds = self.datetime.hour * 3600 + self.datetime.minute * 60
        if start_seconds > end_seconds:
            end_seconds += 24 * 3600  # Handle midnight wrap-around
        factor = (current_seconds - start_seconds) / (end_seconds - start_seconds)
        return factor

    def create_gradient_image(self, start_end_color, time_factor):
        base = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(base)

        for x in range(self.width):
            factor = x / self.width * (1 - time_factor) + time_factor
            interpolated_color = self.interpolate_color(*start_end_color, factor)
            draw.line((x, 0, x, self.height), fill=interpolated_color)

        return base

    @staticmethod
    def adjust_brightness(img: Image, brightness_factor: float) -> Image:
        """ Adjust the image brightness."""

        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                new_r = max(0, min(255, int(r * brightness_factor)))
                new_g = max(0, min(255, int(g * brightness_factor)))
                new_b = max(0, min(255, int(b * brightness_factor)))
                pixels[x, y] = (new_r, new_g, new_b)

        return img

    def canvas_create(self):
        start_end_color, start_hour, end_hour = self.get_gradient_colors(self.formatted_current_time)
        time_factor: float = self.calculate_time_factor(start_hour, end_hour)
        img: Image = self.create_gradient_image(start_end_color, time_factor)
        img: Image = self.adjust_brightness(img, self.brightness_factor)
        img.save(self.filename)
        return img
