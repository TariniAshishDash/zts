import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}