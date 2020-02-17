from __future__ import absolute_import, unicode_literals

import logging
import os

from django.conf import settings
from requests_toolbelt import MultipartEncoder

from starter_service.util.file_util import open_file
from starter_service.util.http_util import http_file, http_json
from starter_service.util.url_util import replace_base_url

log = logging.getLogger(__name__)


def upload(file_path, url='/file/upload', file_type=None):
    if file_path is None or not os.path.exists(file_path) or not os.path.isfile(file_path):
        return [False, None, 'un-existed file']

    if file_type is None:
        file_type = 0

    fields = {
        'file': (os.path.basename(file_path), open_file(None, file_path), 'binary'),
        'type': str(file_type),
    }
    multipart = MultipartEncoder(fields)

    ret_obj = http_json(r'%s%s' % (settings.API_URL, url), headers={
        'Content-Type': multipart.content_type
    }, data=multipart)

    if ret_obj is None:
        return [False, None, None]

    return [ret_obj.get('code') == 200, ret_obj.get('name'), ret_obj.get('url')]


def download(url, name=None, save_to_disc=False, save_as_temp=True):
    if url is None or len(url) <= 0:
        return [False, None, None]

    # map the url to internal
    url = replace_base_url(url, settings.API_URL)

    return http_file(url, save_to_disc=save_to_disc, save_as_temp=save_as_temp, name_prefix=name)


def download_by_name(name, save_to_disc=False, save_as_temp=True):
    if name is None or len(name) <= 0:
        return [False, None, None]

    return download(
        r'%s/file/%s' % (settings.API_URL, name), name=name,
        save_to_disc=save_to_disc, save_as_temp=save_as_temp
    )
