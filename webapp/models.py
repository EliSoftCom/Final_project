from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from webapp.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)
    

class Parser(db.Model):
    __tablename__='parsing'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    url_to_the_category: so.Mapped[str] = so.mapped_column(index=True, unique=True)
    notification_email: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    polling_interval: so.Mapped[int] = so.mapped_column()

    def __init__(self, url_to_the_category, notification_email, polling_interval):
        self.url_to_the_category =  url_to_the_category
        self.notification_email = notification_email
        self.polling_interval = polling_interval

    def __repr__(self):
        return '<URL {}, Email {}, Интервал опроса {}, id {}>'.format(self.url_to_the_category, self.notification_email, 
                                                                    self.polling_interval, self.id)
    

class ResultParser(db.Model):
    __tablename__='Result_parser'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    url: so.Mapped[str] = so.mapped_column(index=True, unique=True)
    price: so.Mapped[int] = so.mapped_column(index=True)
    description: so.Mapped[str] = so.mapped_column(sa.String)

    def __repr__(self):
        return '<Name {}, price {}, id {}>'.format(self.name, self.price, self.id)
