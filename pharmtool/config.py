import os

class Config:
    # Secret key (token) to prevent cookie modification & X-site request forgery attacks
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Pass these as environment variables to prevent unauthroized access

    # SQLite - sqlite:///db.db - relative path, DB is located in the project dir
    
    # Mail server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')