import logging

from django.test.runner import DiscoverRunner

log = logging.getLogger(__name__)


class TestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        log.info('TestRunner.setup_databases passes\n')
        pass

    def teardown_databases(self, old_config, **kwargs):
        log.info('TestRunner.teardown_databases passes\n')
        pass
