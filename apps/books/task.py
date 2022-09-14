from library.celery import app
import requests


@app.task(bind=True, name='update_noveltles_set')
def inform_new(*args, **kwargs):
    print('in magaze')
