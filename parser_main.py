import sqlalchemy as sa
import sqlalchemy.orm as so
from webapp import app
from webapp.db import db
from webapp.models import User, Parser, ResultParser


@app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Parser': Parser, 'ResultParser': ResultParser}
