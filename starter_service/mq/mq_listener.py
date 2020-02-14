from __future__ import absolute_import, unicode_literals

import json
import logging

import stomp

log = logging.getLogger(__name__)


class MqListener(stomp.ConnectionListener):
    def on_message(self, headers, msg_str):
        log.info('Receive msg: %s, %s, %s' % (type(msg_str), msg_str, headers))

        msg_dict = None
        try:
            msg_dict = json.loads(msg_str)
        except Exception as e:
            log.warning('Exception when parse msg: %s' % str(e))

        log.info('Parsed msg: {}, {}'.format(type(msg_dict), msg_dict))

    def on_error(self, headers, msg_str):
        log.info('Error msg: %s, %s, %s' % (type(msg_str), msg_str, headers))
