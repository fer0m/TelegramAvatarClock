from celery.schedules import crontab
from celery import Celery

app = Celery('task', broker='pyamqp://guest@localhost//')
app.conf.update(
    worker_hijack_root_logger=False,
    worker_log_color=False,
    worker_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    worker_task_log_format="[%(asctime)s: %(levelname)s/%(processName)s] [%(task_name)s(%(task_id)s)] %(message)s",
    log_level='INFO'
)

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
