from __future__ import absolute_import, unicode_literals

import json

from django.core.cache import cache


def incr(key, amount=1):
    if cache.has_key(key):
        return cache.incr(key, amount)

    cache.set(key, amount)
    return amount


def get(key):
    return cache.get(key)


def set(key, value):
    return cache.set(key, value)


def delete(key):
    return cache.delete(key)


def ttl(key):
    return cache.ttl(key)


# cache dict: json.dumps and loads, not hash
def get_dict(key):
    value = cache.get(key)
    if value is None:
        return None

    return json.loads(value)


def set_dict(key, value_dict):
    return cache.set(key, json.dumps(value_dict))
