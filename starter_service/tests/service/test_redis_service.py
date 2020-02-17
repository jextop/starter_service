import logging

from django.test import TestCase

from starter_service.service import redis_service as cache

log = logging.getLogger(__name__)


class RedisServiceTest(TestCase):
    def test_str(self):
        # cache string
        key = 'test_redis_service_str'
        self.assertIsNone(cache.get(key))

        val = key
        cache.set(key, val)

        ret = cache.get(key)
        log.info('get from redis: %s, %s' % (type(ret), ret))
        self.assertEqual(val, ret)

        cache.delete(key)
        self.assertIsNone(cache.get(key))

    def test_dict(self):
        # cache dict
        key = 'test_redis_service_dict'
        self.assertIsNone(cache.get_dict(key))

        val = {key: key, 'val': 'val'}
        cache.set_dict(key, val)

        ret = cache.get_dict(key)
        log.info('get_dict from redis: %s, %s' % (type(ret), str(ret)))
        self.assertDictEqual(val, ret)

        cache.delete(key)
        self.assertIsNone(cache.get_dict(key))
