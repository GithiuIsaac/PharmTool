import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
# Create DB instance
bcrypt = Bcrypt()
login_manager = LoginManager()
# Initialize LoginManager - Add functionalities to DB models that handles all
# sessions in the background
login_manager.login_view = 'users.login'
# Set login route
login_manager.login_message_category = 'info'
# Display the customized flash message

mail = Mail()

import pharmtool
from pharmtool.config import Config, ProdConfig, DevConfig

def create_app(config_class=os.environ.get('APP_SETTINGS')):
    app = Flask(__name__)
    # app variable is set to an instance of the Flask class
    # __name__ lets flask know where to look for the templates & static files
    app.config.from_object(config_class)
    db.init_app(app)
    with app.app_context():
        from pharmtool.models import User, Record
        db.create_all()
        
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from pharmtool.users.routes import users
    from pharmtool.records.routes import records
    from pharmtool.main.routes import main
    from pharmtool.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(records)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

