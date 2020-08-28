from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DefForm(FlaskForm):
    id = IntegerField('ID Number of puppy to Remove: ')
    submit = SubmitField('Remove Puppy')
