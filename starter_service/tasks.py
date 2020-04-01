from __future__ import absolute_import, unicode_literals

import json
import logging
import time

from celery import shared_task

from .mq.mq_service import send_msg_to_topic
from .util.task_util import dispatch_task

log = logging.getLogger(__name__)


def do_task(param_dict):
    log.info('do_task: %s, %s' % (type(param_dict), param_dict))
    job = dispatch_task(task, param_dict)

    param_dict['status'] = 'waiting'
    param_dict['task'] = job.id
    send_msg_to_topic({'status': 'waiting', 'id': param_dict['id']})
    return job


@shared_task
def task(param_str):
    log.info('task starts: %s, %s' % (type(param_str), param_str))

    param_dict = None
    try:
        param_dict = json.loads(param_str)
    except Exception as e:
        log.warning('Exception when parse param: %s' % str(e))

    log.info('parsed param: {}, {}'.format(type(param_dict), param_dict))

    param_dict['status'] = 'processing'
    send_msg_to_topic({'status': 'processing', 'id': param_dict['id']})

    # do something
    time.sleep(3)

    param_dict['status'] = 'finished'
    send_msg_to_topic({'status': 'finished', 'id': param_dict['id']})
    return 'finished'
