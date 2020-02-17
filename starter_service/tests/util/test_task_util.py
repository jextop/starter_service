import logging

from django.test import TestCase

from starter_service.tasks import task
from starter_service.util.task_util import dispatch_task, get_task_status

log = logging.getLogger(__name__)


class TasksTest(TestCase):
    def test_get_task_status(self):
        job = dispatch_task(task, {'msg': 'test_task'})
        self.assertIsNotNone(job)

        ret = get_task_status(task, job.id)
        log.info('task status: %s,%s, %s' % (ret, job.id, str(task)))
        self.assertIsNotNone(ret.get('status'))
