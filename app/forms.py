from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    """This class create a contact form for our app"""
    name = TextField('Name', [validators.Required('Please enter your name!\n')])
    email = TextField('Email', [validators.Required(), validators.Email('Please enter a valid mail address!\n')])
    subject = TextField('Subject', [validators.Required('Please complete with a subject!\n')])
    message = TextAreaField('Messaje', [validators.Required('Please write your message!')])
    submit = SubmitField('Send')
