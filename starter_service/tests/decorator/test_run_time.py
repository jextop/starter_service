import logging
import time

from django.test import TestCase

from starter_service.decorator.run_time import run_time

log = logging.getLogger(__name__)


@run_time
def func_run_time(duration):
    time.sleep(duration)
    log.info('func_run_time: %s' % duration)
    pass


class RunTimeTest(TestCase):
    def test_run_time(self):
        func_run_time(0.01)
        func_run_time(0.2)
        func_run_time(0.5)
        func_run_time(1)
