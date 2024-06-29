import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'data_parser.db')
SECRET_KEY = "asd5dfv12dfg5gf53&bnbnb^2vvbvgals"