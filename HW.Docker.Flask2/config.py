import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #инициируем переменные класса Config из окружения
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG=os.environ.get('DEBUG')
    # postgresql://user:pass@localhost:5432/my_db
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SALT = os.environ.get('SALT')
    JSON_AS_ASCII = os.environ.get('JSON_AS_ASCII')