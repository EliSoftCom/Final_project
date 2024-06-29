from flask import Flask
from flask import render_template

from webapp.forms import AddParsingForm
from webapp.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add_parsing')
    def add_parsing():
        title = 'Парсинг'
        parsing = AddParsingForm()
        return render_template('add_parsing.html', page_title=title, form=parsing)
        
    return app
