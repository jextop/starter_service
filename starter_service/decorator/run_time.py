from __future__ import absolute_import, unicode_literals

import logging
import time

log = logging.getLogger(__name__)


def run_time(func):
    def run(*argv):
        start_time = time.clock()
        if argv:
            ret = func(*argv)
        else:
            ret = func()

        seconds = time.clock() - start_time
        s = '%s used: %.1f seconds\n' % (func.__name__, seconds)

        if seconds > 1:
            log.error(s)
        elif seconds > 0.5:
            log.warning(s)
        elif seconds > 0.2:
            log.info(s)

        return ret

    return run
