from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 69)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 69), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 69)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Register')

class BlogUpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    update = SubmitField('Update')