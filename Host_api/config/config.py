import configparser
import json
import os


class ReadIni:

    def __init__(self,path):

        self.parser = configparser.ConfigParser()
        self.parser.read(os.path.abspath(os.path.dirname( os.path.abspath(__file__) ) + r'\\' + path))


    def read_data(self,sec,key):

         ini_data= self.parser.get(sec,key)
         return json.loads(ini_data)






if __name__ == '__main__':
    a=ReadIni('db.ini')
    print(a.read_data('database','mysql_db_config'))
    data=a.read_data('database','mysql_db_config')
    # print(type(data))
