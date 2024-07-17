from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user

def user_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            flash('Эта страница доступна только авторизованным пользователям')
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view
