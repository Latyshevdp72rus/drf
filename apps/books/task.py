from library.celery import app
import requests

# bind=True, name='update_noveltles_set'
@app.task()
def inform_new(x, y):
    print(x + y)
