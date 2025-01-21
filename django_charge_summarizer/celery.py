import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_charge_summarizer.settings')

app = Celery('django_charge_summarizer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process-upload': {
        'task': 'django_crg_backend.tasks.check_upload_folder',
        'schedule': crontab(minute='*/1'),
    },
}