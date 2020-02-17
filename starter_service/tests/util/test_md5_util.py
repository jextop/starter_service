import logging

from django.test import TestCase

from starter_service.util.b64_util import b64enc
from starter_service.util.md5_util import md5

log = logging.getLogger(__name__)


class Md5UtilTest(TestCase):
    def test_md5(self):
        ret = md5('hello md5')
        log.info('md5 returns: %s' % ret)
        self.assertTrue(len(ret) == 32)

        key = 'TEST22383178435468066920'
        secret = 'a2ec6728-9a05-11e8-8af7-e0d55e8d80e2'
        expected = 'YWI4Y2I5MzhmZmZkMTQyZGJiMGJlM2QzMzYxOWQyOWQ='

        ret = md5(key + secret)
        self.assertEqual(expected, b64enc(ret))
