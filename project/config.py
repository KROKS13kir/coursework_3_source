import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    JSON_AS_ASCII = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEMS_PER_PAGE = 12



class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.dirname(BASEDIR), "project.db"
    )
