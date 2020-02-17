from django.test import TestCase

from starter_service.util.http_util import *

log = logging.getLogger(__name__)


class HttpUtilTest(TestCase):
    def test_http_str(self):
        ret_str = http_str('http://www.baidu.com')
        log.info('http_str returns: %s' % ret_str[0: 20])
        self.assertIsNotNone(ret_str)

    def test_http_json(self):
        ret_json = http_json('https://openapi.baidu.com/oauth/2.0/token', headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        }, data={
            'grant_type': 'client_credentials',
            'client_id': 'kVcnfD9iW2XVZSMaLMrtLYIz',
            'client_secret': 'O9o1O213UgG5LFn0bDGNtoRN3VWl2du6',
        }, method='POST')

        log.info('http_json returns: %s' % ret_json)
        self.assertIsNotNone(ret_json)

        token = ret_json.get('access_token')
        self.call_http_file(token)

    def call_http_file(self, token):
        [ret, file_name, data] = http_file('https://tsn.baidu.com/text2audio', headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        }, data={
            'tex': 'Python开发异步任务调度和业务处理',
            'tok': token,
            'cuid': 'starter_service_http_util',
            'ctp': '1',
            'lan': 'zh',
            'spd': '6',
            'per': '1',
        }, method='POST', save_to_disc=True, save_as_temp=False)

        log.info('http_file returns: %s, %s, %s' % (ret, str(file_name), type(data)))
        self.assertIsNotNone(ret is False or len(data) > 0)

    def test_encode(self):
        ret = encode({'name': '文件', 'type': '2'})
        log.info(ret)
        self.assertIsNotNone(ret)

    def test_urlopen(self):
        resp = request.urlopen(r'http://www.baidu.com')
        data = resp.read()
        data_str = data.decode('utf-8')

        log.info('urlopen returns: %d, %s, %s' % (len(data_str), type(data), type(resp)))
        log.info('content: %s' % data_str[0: 10])
        self.assertIsNotNone(data_str)

    def test_request(self):
        req = request.Request(r'http://www.baidu.com', headers={})
        resp = request.urlopen(req)
        data = resp.read()
        data_str = data.decode('utf-8')

        log.info('request returns: %d, %s, %s' % (len(data_str), type(data), type(resp)))
        log.info('content: %s' % data_str[0: 10])
        self.assertIsNotNone(data_str)
