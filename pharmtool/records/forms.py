from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired

class RecordForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    fbs = FloatField('Fasting Blood Sugar', validators=[DataRequired()])
    rbs = FloatField('Random Blood Sugar', validators=[DataRequired()])
    content = TextAreaField('Record', validators=[DataRequired()])
    submit = SubmitField('Create Record')

class UpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    fbs = FloatField('Fasting Blood Sugar', validators=[DataRequired()])
    rbs = FloatField('Random Blood Sugar', validators=[DataRequired()])
    content = TextAreaField('Record', validators=[DataRequired()])
    submit = SubmitField('Update Record')