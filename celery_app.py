from celery.schedules import crontab
from celery import Celery

app = Celery('task', broker='pyamqp://guest@localhost//')

import scheduler  # Need to import main 'scheduler' module for celery search.

app.conf.beat_schedule = {
    'do_hourly_weather_check': {
        'task': 'scheduler.do_hourly_weather_check',
        'schedule': crontab(minute=0),
    },
    'do_minutely_create_canvas': {
        'task': 'scheduler.do_minutely_create_canvas',
        'schedule': crontab(minute='*'),
    },
}
