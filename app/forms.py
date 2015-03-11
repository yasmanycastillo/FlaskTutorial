from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    """This class create a contact form for our app"""
    name = TextField('Name', [validators.Required('Please enter your name!')])
    email = TextField('Email', [validators.Required('Please enter a valid mail address!'), validators.Email('Please enter a valid mail address!')])
    subject = TextField('Subject', [validators.Required('Please complete with a subject!')])
    message = TextAreaField('Messaje', [validators.Required('Please write your message!')])
    submit = SubmitField('Send')
