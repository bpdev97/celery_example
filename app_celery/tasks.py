from celery import Celery
from time import sleep


app = Celery('tasks', broker='pyamqp://guest@localhost')


@app.task
def add(x, y):
    return x + y

@app.task
def count(range):
    for i in range(range):
        print(i)
        sleep(1)
