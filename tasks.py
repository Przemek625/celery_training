from celery.app.task import Task

from celery_app import app
from time import sleep

@app.task
def hello():
    sleep(5)
    return 'hello world'


@app.task
def add(x, y):
    sleep(5)
    return x + y


@app.task
def mul(x, y):
    sleep(5)
    return x * y


@app.task
def xsum(numbers):
    sleep(5)
    return sum(numbers)


class MyFirstTask(Task):

    name = "MyFirstTask"

    def on_success(self, retval, task_id, args, kwargs):
        return "Task has succedded"

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        return "Task has failed"

    def run(self, *args, **kwargs):
        return 'Hellow from MyfirstTask class'


app.tasks.register(MyFirstTask)