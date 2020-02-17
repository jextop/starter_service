from __future__ import absolute_import, unicode_literals

import base64
import logging

log = logging.getLogger(__name__)


def b64enc(s):
    ret = base64.b64encode(s.encode('utf-8'))
    return str(ret, 'utf-8')


def b64dec(s):
    ret = base64.b64decode(s)
    return str(ret, 'utf-8')
