import os


class Config:
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = False
    TEMPLATES_AUTO_RELOAD = False
    SECRET_KEY = os.urandom(24) or "super-secret-key"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
