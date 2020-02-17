from __future__ import absolute_import, unicode_literals

import time


def get_code():
    # generate 24-number code: yyyyMMdd + time
    time_str = str(int(time.time() * 1000 * 1000 * 10))
    if len(time_str) > 16:
        time_str = time_str[-16:]
    else:
        time_str = time_str.ljust(16, '0')

    return '%s%s' % (time.strftime("%Y%m%d"), time_str)
