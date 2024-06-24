from datetime import datetime
import main_config


class CanvasBase:
    TIME_COLORS_RATIO = {
        "6:00-9:00": ((255, 255, 204), (255, 229, 204)),
        "9:00-12:00": ((255, 229, 204), (204, 229, 255)),
        "12:00-15:00": ((204, 229, 255), (204, 255, 255)),
        "15:00-18:00": ((204, 255, 255), (204, 255, 204)),
        "18:00-19:30": ((255, 204, 204), (204, 204, 255)),
        "19:30-21:00": ((204, 204, 255), (153, 153, 255)),
        "21:00-24:00": ((153, 153, 255), (102, 102, 204)),
        "00:00-3:00": ((102, 102, 204), (51, 51, 153)),
        "03:00-6:00": ((51, 51, 153), (255, 255, 204)),
    }

    def __init__(self):
        self.width = 500
        self.height = 500

        self.formatted_current_time: str = datetime.now().strftime("%H:%M")
        self.datetime: datetime = datetime.strptime(self.formatted_current_time, '%H:%M')
        self.filename = self.create_filename()

    @staticmethod
    def create_filename():
        return main_config.GENERATED_AVATAR_PATH
