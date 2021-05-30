from pharmtool import create_app, db
from pharmtool.models import User, Record

with app.app_context():
    db.create_all()
