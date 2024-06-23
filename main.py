from flask import Flask
from flask import render_template
from data_parser_site import data_parser_from_drom, get_html
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data_site')
def get_data_site():
    html = get_html(config.DATASET_URL)
    data_parser = data_parser_from_drom(html)
    return render_template('get_data_site.html', data_parser=data_parser)

if __name__ == '__main__':
    app.run(debug=True)
    

