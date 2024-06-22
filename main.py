from flask import Flask
from flask import render_template
from get_data import get_data


app = Flask(__name__)

@app.route('/')
def index():
    data_parser = get_data()
    return render_template('index.html', data_parser=data_parser)

if __name__ == '__main__':
    app.run(debug=True)
    

