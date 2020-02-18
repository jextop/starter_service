import logging

from django.test import TestCase

log = logging.getLogger(__name__)


class LogTest(TestCase):
    def test_log(self):
        log.debug('log debug')
        log.info('log info')
        log.warning('log warning')
        log.error('log error')
