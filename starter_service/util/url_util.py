from __future__ import absolute_import, unicode_literals

import logging
from urllib import parse

log = logging.getLogger(__name__)


def quote(url):
    return parse.quote(url)


def replace_base_url(url, base_url):
    if url is None or base_url is None or url.lower().startswith(base_url.lower()):
        return url

    http_flag = '//'
    path_flag = '/'

    # find http flag
    i = url.find(http_flag)
    if i > 0:
        new_url = url[i + len(http_flag):]

        # find path flag
        i = new_url.find(path_flag)
        if i > 0:
            if base_url.endswith(path_flag):
                i += 1

            # combine with base url
            url = '{}{}'.format(base_url, new_url[i:])

    return url
