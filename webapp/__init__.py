from flask import Flask
from flask import render_template

from data_parser_site import get_data_in_dict_from_drom
from webapp.forms import AddParsingForm
from webapp.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/get_data_site')
    def get_data_site():
        data_parser = get_data_in_dict_from_drom()
        return render_template('get_data_site.html', data_parser=data_parser)

    @app.route('/add_parsing')
    def add_parsing():
        title = 'Парсинг'
        parsing = AddParsingForm()
        return render_template('add_parsing.html', page_title=title, form=parsing)
        
    return app
