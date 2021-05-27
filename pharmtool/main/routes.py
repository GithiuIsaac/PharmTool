from flask import render_template, request, Blueprint
from flask_login import current_user
from flask_login.utils import login_required
from pharmtool.models import Record

main = Blueprint('main', __name__)

# Create routes using decorators - urls for different pages
# Decorators add additional functionalities to existing functions
# app.route decorator will handle the backend
# The function will return the information to be shown for a sepcific route

@main.route('/')
@main.route('/home')
@login_required
def home():
    # if current_user:
    page = request.args.get('page', 1, type=int)
    records = Record.query.order_by(Record.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', records=records)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
