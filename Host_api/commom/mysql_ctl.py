import pymysql
from pymysql import OperationalError, connect
from Host_api.commom.logger import Log
from Host_api.config.config import ReadIni
import time

# ======================读取db.ini的配置文件===============
data = ReadIni('db.ini').read_data('database', 'mysql_db_config')
log = Log()


class mysql:

    def __init__(self):
        # 连接数据库
        try:
            self.conn = connect(**data)
        except OperationalError as err:
            log.error('数据库连接异常：%s' % err)

    def clear(self, table_name):
        '''
        清空表数据
        :param table_name:  需要清空表的名字
        :return:
        '''
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()
        log.info('%s表数据已删除，删除时间%c'%(table_name,time.ctime()))

    def insert(self,sql):
        '''
        :param sql: insert 语句
        :return:
        '''
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()
        log.info('数据写入成功,写入时间%s'%time.ctime())

    def update(self, sql):
        '''
        :param sql: update 语句
        :return:
        '''
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()
        log.info('数据更新成功,更新时间%s'%time.ctime())

    def select(self,sql):
        '''
        :param sql: 查询语句
        :return:
        '''
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            data=cursor.fetchall()
        self.conn.commit()
        log.info('数据查询成功，时间为%s'%time.ctime())
        return list(data)


if __name__ == '__main__':
    my = mysql()
    print(my.select("select * from sys_user limit 1;"))