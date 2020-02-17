import logging

from django.test import TestCase

from starter_service.util.file_util import save_temp, exists, save, temp_path

log = logging.getLogger(__name__)


class FileUtilTest(TestCase):
    def test_save(self):
        name = save(temp_path(), 'test_save_file.txt', 'test file'.encode('utf-8'))
        log.info('save file: %s' % name)
        self.assertTrue(exists(name))

    def test_save_temp(self):
        name = save_temp('test save temp file'.encode('utf-8'), '.txt')
        log.info('save temp file: %s' % name)
        self.assertTrue(exists(name))
