import logging

from django.core.management.base import BaseCommand

from starter_service.mq import mq_service as mq
from starter_service.mq.mq_listener import MqListener

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'mq starts listener'

    def handle(self, *args, **options):
        log.info("mq starts")
        return mq.consume_msg(MqListener())
