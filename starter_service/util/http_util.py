from __future__ import absolute_import, unicode_literals

import json
import logging
from urllib import error
from urllib import parse
from urllib import request

from .code_util import get_code
from .file_util import save, save_temp, temp_path

log = logging.getLogger(__name__)


def http_str(url, headers={}, data=None, method=None):
    data = http_data(url, headers, data, method)
    return None if data is None else data.decode('utf-8')


def http_json(url, headers={}, data=None, method=None):
    data = http_data(url, headers, data, method)
    return None if data is None else json.loads(data)


def http_data(url, headers={}, data=None, method=None):
    try:
        req = request.Request(url, headers=headers, method=method, data=encode(data))
        resp = request.urlopen(req)
        data = resp.read()
        log.info('http_data returns: %d, %s, %s' % (len(data), type(data), url))
        return data
    except (ConnectionError, error.URLError) as e:
        log.error('ConnectionError in http_data: %s, %s' % (url, str(e)))
    except Exception as e:
        log.error('Exception in http_data: %s, %s' % (url, str(e)))

    return None


def http_file(url, headers={}, data=None, method=None, save_to_disc=False, save_as_temp=True, name_prefix=None):
    try:
        req = request.Request(url, headers=headers, method=method, data=encode(data))
        resp = request.urlopen(req)
        data = resp.read()
        log.info('download_file returns: %d, %s, %s' % (len(data), type(data), url))

        # parse file type, e.g. audio/wav
        file_type = None
        content_type = resp.getheader('Content-Type')
        if '/' in str(content_type):
            file_type = content_type.split('/')[1]

            # Error info when fail to download
            if file_type == 'json':
                ret = json.loads(data)
                return [False, ret.get('msg'), ret.get('code')]

        # parse file name, e.g. attachment;fileName=zip.zip
        file_name = None
        disposition = resp.getheader('Content-Disposition')
        if '=' in str(disposition):
            file_name = disposition.split('=')[1]

        # use a new file name
        if file_name is None:
            file_name = '%s.%s' % (get_code(), file_type or 'dat')

        # save to file
        if save_to_disc:
            name_prefix = '' if name_prefix is None else '%s_' % name_prefix

            if save_as_temp:
                file_name = save_temp(data, ext=file_name, prefix=name_prefix)
            else:
                file_name = save(temp_path('http_download'), '%s%s' % (name_prefix, file_name), data)

        return [True, file_name, data]
    except ConnectionRefusedError as e:
        log.error('ConnectionError in download_file: %s, %s' % (url, str(e)))
    except Exception as e:
        log.error('Exception in download_file: %s, %s' % (url, str(e)))

    return [False, None, None]


def encode(data):
    if isinstance(data, dict):
        data = parse.urlencode(data)

    if isinstance(data, str):
        data = data.encode('utf-8')

    return data
