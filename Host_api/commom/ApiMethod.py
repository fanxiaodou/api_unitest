import requests

from Host_api.commom.logger import Log

log = Log()


class Api:

    @staticmethod
    def request(data):
        if data.get('method') == 'post':
            if data.get('headers'):
                res = requests.request(**data)
                return res
            else:
                log.warning('缺少请求头，请核对数据')
        elif data.get('method') == 'get':
            if data.get('headers'):
                log.warning('get无需填写请求头，请核对数据')
            else:
                res = requests.request(**data)
                return res
        else:
            res = requests.request(**data)
            return res