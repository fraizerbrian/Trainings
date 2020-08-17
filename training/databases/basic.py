import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#  __file__ --> basic.py and grabs directoryname and pathname ieC://Users/Fraize/Desktop/training/databases/basic.py
basedir =  os.path.abspath(os.path.dirname(__file__))
# print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

##################################################
class Puppy(db.Model):
    # manual tablename choice
    __tablename__ = 'puppies'

    # columns for the table
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"
