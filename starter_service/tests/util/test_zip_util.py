import logging

from django.test import TestCase

from starter_service.util.file_util import exists, temp_path, file_path
from starter_service.util.zip_util import file_name_list, unzip_file, zip_dir, zip_files

log = logging.getLogger(__name__)


class ZipUtilTest(TestCase):
    help = 'test zip'
    zip_file = file_path(temp_path(), 'zip.zip')
    dst_path = temp_path('zip_test')

    def test_file_names(self):
        name_list = file_name_list(self.zip_file)
        log.info('name list: %s, from: %s' % (name_list, self.zip_file))
        self.assertTrue(name_list is None or len(name_list) > 0)

    def test_unzip(self):
        name_list = unzip_file(self.zip_file, self.dst_path)
        log.info('unzipped name list: %s, to: %s, from: %s' % (name_list, self.dst_path, self.zip_file))
        self.assertTrue(name_list is None or len(name_list) > 0)

    def test_zip_dir(self):
        src_path = 'conf'
        zip_file = zip_dir(src_path, file_path(temp_path(), 'test_zip_dir.zip'))
        log.info('zip dir: %s, path: %s' % (zip_file, src_path))

    def test_zip_files(self):
        file_list = [file_path(temp_path(), 'zip.zip'), 'service/urls.py', 'un existed file.txt']
        zip_file = zip_files(file_list, file_path(temp_path(), 'test_zip_files.zip'))
        log.info('zip files: %s, files: %s' % (zip_file, file_list))
        self.assertTrue(exists(zip_file))
