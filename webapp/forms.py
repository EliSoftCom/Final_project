from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, URLField, EmailField
from wtforms.validators import DataRequired, URL, Email


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

    
