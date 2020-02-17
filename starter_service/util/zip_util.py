from __future__ import absolute_import, unicode_literals

import zipfile

from .file_util import *

log = logging.getLogger(__name__)


def file_name_list(zip_file):
    if zip_file is None or not os.path.exists(zip_file):
        log.info('un existed zip file: %s' % zip_file)
        return None

    try:
        file = zipfile.ZipFile(zip_file)
        name_list = file.namelist()
        file.close()

        log.info('zipped file names: %s in %s' % (str(name_list), zip_file))
        return name_list
    except zipfile.BadZipFile as e:
        log.info('bad zip file: %s, %s' % (zip_file, str(e)))
        return None


def unzip_file(zip_file, dst_path):
    # check zip files
    name_list = file_name_list(zip_file)
    if name_list is None:
        return

    # dst path
    mk_dir(dst_path)

    # unzip
    file = zipfile.ZipFile(zip_file)
    for name in name_list:
        file_name = file_path(dst_path, name)
        mk_dir(os.path.dirname(file_name))
        save(None, file_name, file.read(name))

    file.close()
    return name_list


def zip_dir(src_path, zip_file):
    files = file_list(src_path)
    return zip_files(files, zip_file, src_path=src_path)


def zip_files(src_file_list, zip_file, src_path=''):
    if src_file_list is None or len(src_file_list) <= 0 or zip_file is None or len(zip_file) <= 0:
        return

    if not is_ext(zip_file, '.zip'):
        zip_file = '%s.zip' % zip_file

    file = zipfile.ZipFile(zip_file, "w", zipfile.zlib.DEFLATED)
    zip_file_name = file.filename

    for src_file in src_file_list:
        if not exists(src_file):
            continue

        arc_name = src_file[len(src_path):]
        log.info('Zip file: %s, to: %s' % (arc_name, zip_file_name))
        file.write(src_file, arc_name)

    file.close()
    return zip_file_name
