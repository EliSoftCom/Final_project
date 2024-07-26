from flask import Flask
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_migrate import Migrate
from flask import render_template, flash, redirect, url_for, request

from urllib.parse import urlsplit

from webapp.db import db
from webapp.config import Config
from webapp.models import User, Parser, ResultParser
from webapp.forms import AddParsingForm
from webapp.forms import LoginForm
from webapp.forms import RegistrationForm

import sqlalchemy as sa


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
  
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/')
    def index():
        return render_template('index.html', the_title='Парсим легко!')


    @app.route('/login', methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно вошли на сайт')
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        return render_template('login.html', the_title='Sign In', form=form)


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)


    # добавляет в БД критерии поиска, введенные пользователем
    @app.route('/add_parsing', methods = ['GET', 'POST'])
    @login_required
    def add_parsing():  
        title = 'Парсинг'
        parsing = AddParsingForm()
        if parsing.validate_on_submit():
            url_to_the_category, notification_email, polling_interval = parsing.url_to_the_category.data, parsing.notification_email.data, parsing.polling_interval.data
            request_parser = Parser(url_to_the_category, notification_email, polling_interval)
            db.session.add(request_parser)
            db.session.commit()
            flash('Вы успешно добавили категорию поиска')
            return redirect(url_for('get_data_site'))
        return render_template('add_parsing.html', page_title=title, form=parsing)


    @app.route('/get_data_site')
    @login_required
    def get_data_site():
        title = 'Результат парсинга'
        result_parsing = ResultParser.query.all()
        return render_template('get_data_site.html', page_title = title, result_parsing = result_parsing)


    @app.route("/administrator")
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ!'
        else:
            return 'Ты не админ!'


    return app


