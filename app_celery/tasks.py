from celery import Celery
from time import sleep


app = Celery('tasks', broker='pyamqp://guest@localhost')


@app.task
def add(x, y):
    return x + y

@app.task
def count(rng):
    for i in range(rng):
        print(i)
        sleep(1)
