from flask import  Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from pharmtool import db
from pharmtool.models import Record
from pharmtool.records.forms import RecordForm, UpdateForm


records = Blueprint('records', __name__)

@records.route('/record/new', methods=['GET', 'POST'])
@login_required
def new_record():
    form = RecordForm()
    
    if form.validate_on_submit():
        entry = Record(title=form.title.data, fbs=form.fbs.data, rbs=form.rbs.data, content=form.content.data, author=current_user)
        db.session.add(entry)
        db.session.commit()
        flash('Your record has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('new_record.html', title='New Patient Record', 
    form=form, legend='New Patient Record')


@records.route('/record/<int:record_id>')
@login_required
def record(record_id):
    record = Record.query.get_or_404(record_id)
    return render_template('record.html', title=record.title, record=record)


@records.route('/record/<int:record_id>/update', methods=['GET', 'POST'])
@login_required
def update_record(record_id):
    record = Record.query.get_or_404(record_id)
    if record.author != current_user:
        abort(403)
    form = UpdateForm()
    if form.validate_on_submit():
        record.title = form.title.data
        record.fbs = form.fbs.data
        record.rbs = form.rbs.data
        record.content = form.content.data
        db.session.commit()
        flash('Your record has been updated!', 'success')
        return redirect(url_for('records.record', record_id=record.id))
    elif request.method == 'GET':
        form.title.data = record.title
        form.fbs.data = record.fbs
        form.rbs.data = record.rbs
        form.content.data = record.content
    return render_template('new_record.html', title='Update Patient Record', 
    form=form, legend='Update Patient Record')


@records.route('/record/<int:record_id>/delete', methods=['POST'])
@login_required
def delete_record(record_id):
    record = Record.query.get_or_404(record_id)
    if record.author != current_user:
        abort(403)
    db.session.delete(record)
    db.session.commit()
    flash('Your record has been deleted!', 'success')
    return redirect(url_for('main.home'))

