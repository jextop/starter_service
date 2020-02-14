from __future__ import absolute_import, unicode_literals

import logging
import json

from celery import shared_task
from .util.task_util import dispatch_task

log = logging.getLogger(__name__)


@shared_task
def task(param_str):
    log.info('task starts: %s, %s' % (type(param_str), param_str))

    param_dict = None
    try:
        param_dict = json.loads(param_str)
    except Exception as e:
        log.warning('Exception when parse param: %s' % str(e))

    log.info('parsed param: {}, {}'.format(type(param_dict), param_dict))
    return 'finished'


def do_task(param_dict):
    log.info('do_task: %s, %s' % (type(param_dict), param_dict))
    return dispatch_task(task, param_dict)
