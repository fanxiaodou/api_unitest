import unittest
import ddt
from Host_api.commom.ApiMethod import Api
from Host_api.commom.logger import Log
from Host_api.commom.yaml_ctl import Yaml

log = Log()


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        log.info('登录接口用例开始执行')

    def tearDown(self) -> None:
        log.info('登录接口用例执行结束')
        log.info('-------------------------------------------')

    def test_login_suesscs(self):
        try:
            log.info('用例标题：验证登录接口请求成功')
            res = Api.request(Yaml.load_yaml('login.yaml'))
            log.info('接口请求成功')
            self.assertEqual(200, res.status_code, msg='断言失败状态码不正确，状态码为%s' % res.status_code)
            log.info('接口返回状态断言成功，状态码为%s' % res.status_code)
            self.assertIn('登录成功', res.json()['msg'], msg='断言失败，msg信息不正确！')
            log.info('响应体msg信息断言成功')
            self.assertEqual('200', res.json()['code'], msg='断言失败，状态码不正确!状态码为%s' % res.json()['code'])
            log.info('响应体状态码断言成功，状态码为%s' % res.json()['code'])
            log.info('验证接口登录成功')
        except Exception as err:
            log.warning('【erro】：%s' % err)

    @ddt.data(*Yaml.load_data('login_data.yaml').get('test_login_user_err'))
    def test_login_user_err(self, data):
        try:
            log.info('用例标题：验证用户名错误请求失败')
            res = Api.request(Yaml.load_yaml('login.yaml', data))
            log.info('接口请求成功')
            self.assertEqual(200, res.status_code, msg='断言失败状态码不正确，状态码为%s' % res.status_code)
            log.info('接口返回状态断言成功，状态码为%s' % res.status_code)
            self.assertIn('登录帐号不存在', res.json()['msg'], msg='断言失败，msg信息不正确！返回信息为%s' % res.json()['msg'])
            log.info('响应体msg信息断言成功')
            self.assertEqual('400', res.json()['code'], msg='断言失败，状态码不正确!状态码为%s' % res.json()['code'])
            log.info('响应体状态码断言成功，状态码为%s' % res.json()['code'])
            log.info('验证用户名错误请求失败成功')
        except Exception as err:
            log.warning('【erro】：%s' % err)

    def test_login_user_empty(self):
        try:
            log.info('用例标题：验证用户名为空请求失败')
            res = Api.request(Yaml.load_yaml('login.yaml'))
            log.info('接口请求成功')
            self.assertEqual(200, res.status_code, msg='断言失败状态码不正确，状态码为%s' % res.status_code)
            log.info('接口返回状态断言成功，状态码为%s' % res.status_code)
            self.assertIn('登录帐号不能为空', res.json()['msg'], msg='断言失败，msg信息不正确！返回信息为%s' % res.json()['msg'])
            log.info('响应体msg信息断言成功')
            self.assertEqual('400', res.json()['code'], msg='断言失败，状态码不正确!状态码为%s' % res.json()['code'])
            log.info('响应体状态码断言成功，状态码为%s' % res.json()['code'])
            log.info('验证用户名为空请求失败成功')
        except Exception as err:
            log.warning('【erro】：%s' % err)

    @ddt.data(*Yaml.load_data('login_data.yaml').get('test_login_pwd_err'))
    def test_login_pwd_err(self, data):
        try:
            log.info('用例标题：验证密码错误请求失败')
            res = Api.request(Yaml.load_yaml('login.yaml', data))
            log.info('接口请求成功')
            self.assertEqual(200, res.status_code, msg='断言失败状态码不正确，状态码为%s' % res.status_code)
            log.info('接口返回状态断言成功，状态码为%s' % res.status_code)
            self.assertIn('登录密码不正确', res.json()['msg'], msg='断言失败，msg信息不正确！返回信息为%s' % res.json()['msg'])
            log.info('响应体msg信息断言成功')
            self.assertEqual('400', res.json()['code'], msg='断言失败，状态码不正确!状态码为%s' % res.json()['code'])
            log.info('响应体状态码断言成功，状态码为%s' % res.json()['code'])
            log.info('验证密码错误请求失败成功')
        except Exception as err:
            log.warning('【erro】：%s' % err)

    def test_login_pwd_empty(self):
        try:
            log.info('用例标题：验证密码为空请求失败')
            res = Api.request(Yaml.load_yaml('login.yaml'))
            log.info('接口请求成功')
            self.assertEqual(200, res.status_code, msg='断言失败状态码不正确，状态码为%s' % res.status_code)
            log.info('接口返回状态断言成功，状态码为%s' % res.status_code)
            self.assertIn('登录密码不能为空', res.json()['msg'], msg='断言失败，msg信息不正确！返回信息为%s' % res.json()['msg'])
            log.info('响应体msg信息断言成功')
            self.assertEqual('400', res.json()['code'], msg='断言失败，状态码不正确!状态码为%s' % res.json()['code'])
            log.info('响应体状态码断言成功，状态码为%s' % res.json()['code'])
            log.info('验证密码为空请求失败成功')
        except Exception as err:
            log.warning('【erro】：%s' % err)


if __name__ == '__main__':
    unittest.main()
