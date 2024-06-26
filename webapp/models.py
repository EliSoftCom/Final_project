from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Parser(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url_to_the_category: Mapped[str] = mapped_column(index=True, unique=True)
    notification_email: Mapped[str] = mapped_column(String(30), index=True)
    polling_interval: Mapped[int] = mapped_column()

    def __repr__(self):
        return 'URL {}, Email {}, Интервал опроса {}, id {}'.format(self.url_to_the_category, 
                                                                    self.notification_email, 
                                                                    self.polling_interval,
                                                                    self.id)