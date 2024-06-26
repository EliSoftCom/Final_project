from flask import Flask
from flask import render_template
from data_parser_site import get_data_in_dict_from_drom

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data_site')
def get_data_site():
    data_parser = get_data_in_dict_from_drom()
    return render_template('get_data_site.html', data_parser=data_parser)

if __name__ == '__main__':
    app.run(debug=True)
    