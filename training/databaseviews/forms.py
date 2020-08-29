from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('ID Number of puppy to Remove: ')
    submit = SubmitField('Remove Puppy')
