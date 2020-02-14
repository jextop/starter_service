from __future__ import absolute_import, unicode_literals

import json
import logging
import time

from django.http import JsonResponse

from starter_service.mq import mq_service as mq
from starter_service.service import redis_service as cache
from starter_service.tasks import do_task

log = logging.getLogger(__name__)


def index(req):
    return JsonResponse({
        'ip': req.get_host(),
        'msg': 'Hello, starter, 你好',
        'date': time.strftime("%Y-%m-%d %H:%M:%S"),
    })


def chk(req):
    return JsonResponse({
        'chk': 'ok',
        'msg': '消息',
        'date': time.strftime("%Y-%m-%d %H:%M:%S"),
        'services': [
            json.loads(chk_cache(req).content),
            json.loads(chk_mq(req).content),
            json.loads(chk_job(req).content),
        ],
    }, safe=False)


def chk_cache(req):
    key = 'chk_cache: %s, %s, %s' % (req.get_raw_uri(), req.get_full_path(), req.get_host())
    value = cache.incr(key)
    cache.set(key, value * 2)

    return JsonResponse({
        'chk': 'cache',
        'msg': value,
        'status': value * 2 == cache.get(key),
    })


def chk_mq(req):
    msg_dict = {
        'chk': 'mq',
        'msg': {
            'src': 'from python',
            'url': req.get_raw_uri(),
            'path': req.get_full_path(),
            'host': req.get_host(),
        },
    }

    mq.send_msg_to_queue(msg_dict)
    return JsonResponse(msg_dict)


def chk_job(req):
    param_dict = {
        'url': req.get_raw_uri(),
        'path': req.get_full_path(),
        'host': req.get_host(),
    }
    job = do_task(param_dict)

    return JsonResponse({
        'chk': 'job',
        'msg': job.task_id
    })
