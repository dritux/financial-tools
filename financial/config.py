# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = True if os.environ.get("DEBUG", None) else False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY", None)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql://dumny:dumny@db/financial"


class ProductionConfig(Config):

    USER = ''
    PASSWORD = ''
    DATABASE = ''
    CONNECTION_NAME = ''

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@localhost/{database}'
        '?unix_socket=/cloudsql/{connection_name}').format(
            user=USER, password=PASSWORD,
            database=DATABASE, connection_name=CONNECTION_NAME)
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql://dumny:dumny@0.0.0.0/financial"


config = {
    "default": "financial.config.Config",
    "development": "financial.config.DevelopmentConfig",
    "production": "financial.config.ProductionConfig",
    "testing": "financial.config.TestingConfig",
}
