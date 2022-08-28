# coding: utf-8
class DefaultConfig(object):
    DEBUG = True
    SECRET_KEY = 'dfghjklERTYUIO3456789456789#$%^&*FGHJKL:'
    # 数据库连接固定格式格式字符串
    # dialect+driver://username:password@host:port/database
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = "ysy131131"
    HOST = 'localhost'
    PORT = 3306
    DATABASE = 'nzoly'
    CHARSET= 'utf8'

    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset=utf8'.format(
        dialect=DIALECT, driver=DRIVER, username=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False