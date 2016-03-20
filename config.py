import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres://cuxwxedgorsvlz:JOUSDhsl0fNgMfwyiLu0HQEwMe@ec2-107-21-101-67.compute-1.amazonaws.com:5432/d1mrcoa2cq7kcv'


class Development(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class Production(Config):
    DEBUG = False
    TESTING = False
