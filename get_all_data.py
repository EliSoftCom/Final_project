from webapp import create_app
from webapp.data_parser_site import get_data_from_drom

app = create_app()
with app.app_context():
    get_data_from_drom()