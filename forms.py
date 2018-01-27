from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField


class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')


class SignupForm(FlaskForm):
    # email = Email('email')
    username = TextField('username')
    password = PasswordField('password')
