class BaseConfig:
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECURITY_PASSWORD_HASH = 'bcrypt'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    APP_NAME = 'App name'
    # SECURITY_REGISTERABLE = True
    # SECURITY_RECOVERABLE = True
    # SECURITY_TRACKABLE = True
    # SECURITY_PASSWORD_HASH = 'sha512_crypt'
    # SECURITY_PASSWORD_SALT = 'add_salt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<...>'
    HASH_SALT = '<...>'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:pass@localhost/db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///foo.db'
    SECURITY_PASSWORD_SALT = '<...>'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '<...>'
    HASH_SALT = '<...>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///foo.db'
    SECURITY_PASSWORD_SALT = '<...>'
    DOMAIN = 'http://127.0.0.1:5000/'
