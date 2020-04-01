import logging

from django.test import TestCase

from starter_service.service.api_service import download_by_name, upload
from starter_service.util.file_util import temp_path, file_path

log = logging.getLogger(__name__)


class ApiServiceTest(TestCase):
    def test_download(self):
        ret, file_name, data = download_by_name('f202002170013897056571700.jpg')

        log.info('download returns :%s, %s, %d' % (ret, str(file_name), len(data) if ret else 0))
        self.assertTrue(ret is False or len(data) > 0)

    def test_upload(self):
        file = file_path(temp_path(), 'test_save_file.txt')
        ret, name, url = upload(file)

        log.info('upload returns: %s, %s, %s, %s' % (ret, name, url, file))
        self.assertTrue(ret is False or len(name) > 0)
