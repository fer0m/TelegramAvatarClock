from functools import wraps
from PIL import ImageFont

import main_config


def set_font_size(size):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.font = ImageFont.truetype(str(main_config.FONT_FILE_PATH), size)
            func(self, *args, **kwargs)
        return wrapper
    return decorator
