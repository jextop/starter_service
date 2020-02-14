from __future__ import absolute_import, unicode_literals

import json
import logging

log = logging.getLogger(__name__)


def dispatch_task(task_func, param_dict):
    param_json = json.dumps(param_dict)

    try:
        return task_func.apply_async(
            [param_json],
            retry=True,
            retry_policy={
                'max_retries': 1,
                'interval_start': 0,
                'interval_step': 0.2,
                'interval_max': 0.2,
            },
        )
    except Exception as ex:
        log.info(ex)
        raise


def get_task_status(task_func, task_id):
    t = task_func.AsyncResult(task_id)
    status = t.state
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = t.info['progress']

    return {'status': status, 'progress': progress}
