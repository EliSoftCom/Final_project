from flask import Flask, flash, redirect, url_for
from flask import render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from webapp.decorators import user_required
from webapp.forms import AddParsingForm
from webapp.models import db, Parser, User, ResultParser
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/')
    def index():
        return render_template('index.html')


    # добавляет в БД критерии поиска, введенные пользователем
    @app.route('/add_parsing', methods = ['GET', 'POST'])
    @user_required
    def add_parsing():  
        title = 'Парсинг'
        parsing = AddParsingForm()
        if parsing.validate_on_submit():
            url_to_the_category, notification_email, polling_interval = parsing.url_to_the_category.data, parsing.notification_email.data, parsing.polling_interval.data
            request_parser = Parser(url_to_the_category, notification_email, polling_interval)
            db.session.add(request_parser)
            db.session.commit()
            flash('Вы успешно добавили категорию поиска')
            return redirect(url_for('index'))
        return render_template('add_parsing.html', page_title=title, form=parsing)
    

    @app.route('/get_data_site')
    def get_data_site():
        title = 'Результат парсинга'
        result_parsing = ResultParser.query.all()
        return render_template('get_data_site.html', page_title = title, result_parsing = result_parsing)
    

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
    

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))
    

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))
    

    @app.route("/administrator")
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ!'
        else:
            return 'Ты не админ!'


    return app
