import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class Development(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    SQLALCHEMY_DATABASE_URI = 'postgres://cuxwxedgorsvlz:JOUSDhsl0fNgMfwyiLu0HQEwMe@ec2-107-21-101-67.compute-1.amazonaws.com:5432/d1mrcoa2cq7kcv'
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class Production(Config):
    DEBUG = False
    TESTING = False
