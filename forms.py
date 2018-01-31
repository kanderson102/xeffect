from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])


class SignupForm(FlaskForm):
    email = Email('email')
    username = StringField('username')
    password = PasswordField('password')
