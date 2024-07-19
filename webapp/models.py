from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class Parser(db.Model):
    __tablename__='parsing'
    id: Mapped[int] = mapped_column(primary_key=True)
    url_to_the_category: Mapped[str] = mapped_column(index=True, unique=True)
    notification_email: Mapped[str] = mapped_column(String(30), index=True)
    polling_interval: Mapped[int] = mapped_column()

    def __init__(self, url_to_the_category, notification_email, polling_interval):
        self.url_to_the_category =  url_to_the_category
        self.notification_email = notification_email
        self.polling_interval = polling_interval

    def __repr__(self):
        return '<URL {}, Email {}, Интервал опроса {}, id {}>'.format(self.url_to_the_category, self.notification_email, 
                                                                    self.polling_interval, self.id)


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    password: Mapped[str] = mapped_column(db.String(128))
    role: Mapped[str] = mapped_column(String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)
    

class ResultParser(db.Model):
    __tablename__='Result_parser'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), index=True)
    url: Mapped[str] = mapped_column(index=True, unique=True)
    price: Mapped[int] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return '<Name {}, price {}, id {}>'.format(self.name, self.price, self.id) 
