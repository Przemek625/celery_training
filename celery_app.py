from celery import Celery
from time import sleep
app = Celery(
    'main',
    broker='amqp://myuser:mypassword@localhost:5672/myvhost',
    backend='rpc://',
    include=['tasks'],
)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'