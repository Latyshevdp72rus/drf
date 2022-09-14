from __future__ import absolute_import, unicode_literals
from library.celery import app as celery_app

__all__ = ('celery_app',)


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')