from webapp import app
from webapp.data_parser_site import get_data_from_drom


with app.app_context():
    get_data_from_drom()