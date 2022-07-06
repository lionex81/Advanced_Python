import os


class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    pass


class ProdConfig:
    DEBUG = False
    ENV = 'production'

