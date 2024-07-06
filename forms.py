from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import DataRequired, Email # type: ignore

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()