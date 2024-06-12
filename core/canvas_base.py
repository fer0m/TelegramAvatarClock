from datetime import datetime


class CanvasBase:
    def __init__(self):
        self.width = 500
        self.height = 500

        self.formatted_current_time: str = datetime.now().strftime("%H:%M")
        self.datetime: datetime = datetime.strptime(self.formatted_current_time, '%H:%M')
        self.filename = self.create_filename()

    def create_filename(self):
        return f'avatar_{self.formatted_current_time}.png'
