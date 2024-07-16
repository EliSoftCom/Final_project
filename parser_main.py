import sqlalchemy as sa
import sqlalchemy.orm as so
from webapp import app, db
from webapp.models import User, Query


@app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Query': Query}
