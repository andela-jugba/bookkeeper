import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BLOG_ADMIN = os.environ.get('BOOKKEEPER_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
