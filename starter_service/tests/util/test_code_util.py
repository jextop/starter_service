import logging

from django.test import TestCase

from starter_service.util.code_util import get_code
import time

log = logging.getLogger(__name__)


class TasksTest(TestCase):
    def test_get_code(self):
        code_set = set()
        count = 1000
        for i in range(count):
            time.sleep(0.000001)
            code = get_code()
            if code in code_set:
                log.error('duplicated code: %s' % code)
                continue

            code_set.add(code)
            if i == count - 1:
                log.info('the last code: %s' % code)

        log.info('code count: %d, duplicated ones: %d' % (count, count - len(code_set)))
        self.assertEqual(count, len(code_set))
