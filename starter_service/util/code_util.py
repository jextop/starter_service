from __future__ import absolute_import, unicode_literals

import time
import random
import math

TIME_LEN = 18

def get_code():
    # generate 24-number code: yyMMdd + time(18)
    time_str = str(time.time()).replace(".", "")

    num_len = TIME_LEN - len(time_str)
    if num_len < 0:
        time_str = time_str[0:TIME_LEN]
    elif num_len > 0:
        num_str = str(random.randint(1, math.pow(10, num_len)) - 1)
        time_str = '%s%s' % (time_str, num_str.ljust(num_len, '0'))

    return '%s%s' % (time.strftime("%Y%m%d")[2:], time_str)
