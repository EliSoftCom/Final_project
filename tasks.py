from celery import Celery
from celery.schedules import crontab

from webapp import app
from webapp.data_parser_site import get_data_from_drom

celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def get_data_drom():
    with app.app_context():
        get_data_from_drom()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), get_data_drom.s())
