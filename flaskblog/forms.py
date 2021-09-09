from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    colors = SelectField(u'Choose Colour: ', choices=[('yellow'), ('purple'), ('pink'), ('gray'), ('red'), ('green'), ('blue'), ('orange')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exists')


    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email has been taken, choose another.')


class EmailForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     submit = SubmitField('Confirm')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateAccountInfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already taken!')