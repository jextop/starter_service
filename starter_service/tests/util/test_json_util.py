import logging

from django.test import TestCase

from starter_service.util.json_util import to_json, parse_json

log = logging.getLogger(__name__)


class JsonUtilTest(TestCase):
    def test_json(self):
        obj_dict = {
            "code": 200,
            "msg": "msg"
        }

        str_json = to_json(obj_dict)
        obj_json = parse_json(str_json)

        log.info('dict: %s, str: %s, dict: %s' % (obj_dict, str_json, obj_json))
        self.assertDictEqual(obj_dict, obj_json)
