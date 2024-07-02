from flask import Flask
from flask import render_template

from webapp.data_parser_site import get_data_in_dict_from_drom
from webapp.forms import AddParsingForm
from webapp.models import db, Parser


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # парсит сайт Дрома
    @app.route('/get_data_site')
    def get_data_site():
        data_parser = get_data_in_dict_from_drom()
        return render_template('get_data_site.html', data_parser=data_parser)

    # добавляет в БД критерии поиска, введенные пользователем
    @app.route('/add_parsing', methods = ['GET', 'POST'])
    def add_parsing():
        title = 'Парсинг'
        parsing = AddParsingForm()
        if parsing.validate_on_submit():
            url_to_the_category, notification_email, polling_interval = parsing.url_to_the_category.data, parsing.notification_email.data, parsing.polling_interval.data
            request_parser = Parser(url_to_the_category, notification_email, polling_interval)
            db.session.add(request_parser)
            db.session.commit()
            return f'Вы успешно добавили категорию поиска: {url_to_the_category}'
        return render_template('add_parsing.html', page_title=title, form=parsing)
    

    return app
