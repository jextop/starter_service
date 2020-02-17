import logging

from django.test import TestCase

from starter_service.util.b64_util import b64enc, b64dec

log = logging.getLogger(__name__)


class EncUtilTest(TestCase):
    def test_base64(self):
        s = '81e3bc884e452f32ed8ebccc8860702d'
        ret = b64enc(s)

        log.info('base64enc returns: %s' % ret)
        self.assertEqual(s, b64dec(ret))
