from __future__ import absolute_import, unicode_literals

import hashlib
import logging

log = logging.getLogger(__name__)


def md5(s):
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf=8'))
    return hl.hexdigest()
