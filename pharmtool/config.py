import os
import re

class Config():
    # Secret key (token) to prevent cookie modification & X-site request forgery attacks
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Pass these as environment variables to prevent unauthroized access
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri

    # SQLite - sqlite:///db.db - relative path, DB is located in the project dir
    
    # Mail server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DEBUG = False
    FLASK_ENV = 'production'
