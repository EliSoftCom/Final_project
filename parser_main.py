import sqlalchemy as sa
import sqlalchemy.orm as so
from webapp import create_app
from webapp.db import db
from webapp.models import User, Parser, ResultParser


@create_app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Parser': Parser, 'ResultParser': ResultParser}
