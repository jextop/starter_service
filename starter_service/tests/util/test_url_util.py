import logging

from django.conf import settings
from django.test import TestCase

from starter_service.util.url_util import replace_base_url, quote

log = logging.getLogger(__name__)


class HttpUtilTest(TestCase):
    def test_quote(self):
        ret = quote('http://localhost:800/file/dl?name=文件')
        log.info(ret)
        self.assertIsNotNone(ret)

    def test_replace_base_url(self):
        io_tuple = (
            (None, None), ('', ''), ('http://a', 'http://a'),
            ('http://a/b.jpg', '{}/b.jpg'.format(settings.API_URL)),
        )

        for (i, o) in io_tuple:
            ret = replace_base_url(i, settings.API_URL)
            b_ret = o == ret

            if not b_ret:
                log.info('{}, {}'.format(o, ret))
            self.assertTrue(b_ret)
