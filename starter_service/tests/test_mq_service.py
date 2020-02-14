import logging

from django.test import TestCase

from ..mq import mq_service as mq

log = logging.getLogger(__name__)


class MQServiceTest(TestCase):
    def test_send_msg(self):
        msg_dict = {'content': 'test msg dict', 'msg': 'queue from python'}
        mq.send_msg_to_queue(msg_dict)
        mq.send_msg_to_topic({'msg': "test topic from python"})
