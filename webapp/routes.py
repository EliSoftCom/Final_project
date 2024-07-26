from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from webapp import app
from webapp.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from webapp import db
from webapp.models import User, Parser, ResultParser
from webapp.forms import RegistrationForm
from webapp.forms import AddParsingForm
from webapp.data_parser_site import get_data_from_drom


@app.route('/')
@app.route('/index')
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
        query = sa.select(Parser)
        parsers = db.session.scalars(query)
        for p in parsers:
            if parsing.url_to_the_category.data == p.url_to_the_category:
                 flash('Url c таким адресом уже были')
                 return redirect(url_for('add_parsing'))
        request_parser = Parser(url_to_the_category = parsing.url_to_the_category.data, notification_email = parsing.notification_email.data, polling_interval = parsing.polling_interval.data, author = current_user)
        db.session.add(request_parser)
        db.session.commit()
        user_now =User.query.get(current_user.id)
        querys = user_now.parser.select()
        parser_user = db.session.scalars(querys).all()
        parser_id = parser_user[-1].id
        get_data_from_drom(parsing.url_to_the_category.data, current_user.id, parser_id)
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
