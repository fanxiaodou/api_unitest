import inspect
import json
import os
import yaml

from Host_api.commom.logger import Log

log = Log()


class Yaml:

    @staticmethod
    def load_yaml(filename, *kwargs):
        '''
        读取存放接口信息的yaml文件
        :param filename:  传入文件名
        :param kwargs:  传入ddt解包数据
        :return:   返回读取的yaml数据 ，便于
        '''
        path = os.path.abspath(filename).split('\\')
        path[-2] = 'data'
        file_path = '\\'.join(path)
        _data = kwargs
        if len(_data)>0:
            try:
                with open(file_path, encoding='utf-8') as f:
                    name = inspect.stack()[1].function
                    data = yaml.safe_load(f)[name]
                    raw = json.dumps(data)
                # 以下步骤是实现DDT驱动的核心，用于替换%{变量}的数据，实现数据驱动

                for i in _data:
                    for key, value in i.items():
                        result = raw.replace(f'${{{key}}}', value)
                        result_data = json.loads(result)
                        return result_data
            except Exception as err:
                log.warning('读取yaml文件出错:%s' % err)
        else:
            with open(file_path, encoding='utf-8') as f:
                name = inspect.stack()[1].function
                data = yaml.safe_load(f)[name]
            return data

    @staticmethod
    def load_data(filename):
        path = os.path.abspath(filename).split('\\')
        path[-2] = 'data'
        file_path = '\\'.join(path)
        with open(file_path, encoding='utf-8') as f:
            # name = inspect.stack()[1].function
            data = yaml.safe_load(f)
        return data

# def test_login_pwd_empty():
#     data = Yaml.load_yaml('login.yaml')
#     print(data)
#
# if __name__ == '__main__':
#
#
#
#     test_login_pwd_empty()
if __name__ == '__main__':

    print(Yaml.load_data('login_data.yaml').get('test_login_user_err'))
