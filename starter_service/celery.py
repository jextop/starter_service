from __future__ import absolute_import, unicode_literals

import os

from celery import Celery, platforms
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starter_service.settings')

app = Celery(
    'starter_service',
    include=['starter_service.tasks'],
    broker=settings.CELERY_BROKER,
    backend=settings.CELERY_BACKEND
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    CELERY_ACKS_LATE=True,
    CELERY_ACCEPT_CONTENT=['pickle', 'json'],
    CELERYD_FORCE_EXECV=True,
    CELERYD_MAX_TASKS_PER_CHILD=500,
    BROKER_HEARTBEAT=0,
)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,  # celery任务执行结果的超时时间，即结果在backend里的保存时间，单位s
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

platforms.C_FORCE_ROOT = True
