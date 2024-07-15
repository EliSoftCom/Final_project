from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from webapp import app
from webapp.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from webapp import db
from webapp.models import User
from webapp.forms import RegistrationForm
from webapp.forms import AddParsingForm
from webapp.data_parser_site import get_data_in_dict_from_drom


@app.route('/')
@app.route('/index')
@login_required
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


@app.route('/add_parsing', methods = ['GET', 'POST'])
@login_required
def add_parsing():
    form = AddParsingForm()
    if form.validate_on_submit():
        url_to_the_category, notification_email, polling_interval = form.url_to_the_category.data, form.notification_email.data, form.polling_interval.data
        data_parser = { 'name': "ihujgui",
                'url': "fuygjhug",
                'price': 654564654,
                'description': "ohuyg7g6rguihu",
                'date_of_announcement': "jhguyfytygftt"}
        #data_parser = get_data_in_dict_from_drom(url_to_the_category)
        #return render_template('get_data_site.html', data_parser=data_parser)
        #request_parser = Parser(url_to_the_category, notification_email, polling_interval)
        #db.session.add(request_parser)
        #db.session.commit()
        return render_template('get_data_site.html', data_parser=data_parser)
    return render_template('add_parsing.html', form=form)

