from celery import Celery
from celery.schedules import crontab

app = Celery('your_project')

app.conf.beat_schedule = {
    'send_event_reminders': {
        'task': 'yourapp.management.commands.send_event_reminder',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
}