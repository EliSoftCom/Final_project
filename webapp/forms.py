from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, URLField, EmailField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, URL
import sqlalchemy as sa
from webapp import db
from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')


class AddParsingForm(FlaskForm):
    url_to_the_category = URLField('Cсылка на категорию',
                    validators=[DataRequired(message="Введите ссылку на категорию"),
                    URL(message="Введите валидную ссылку на категорию")], 
                    render_kw={"class":"form-control"})
    notification_email = EmailField('Почта для уведомлений', 
                    validators=[DataRequired(message="Введите Email"), 
                    Email(message="Введите валидный Email")], 
                    render_kw={"class":"form-control"})
    polling_interval = IntegerField('Интервал опроса (сек.)', validators=[DataRequired()], 
                    render_kw={"class":"form-control"})
    submit = SubmitField('Отправить!', render_kw={"class":"btn btn-primary"})
    