from bs4 import BeautifulSoup
import requests
from webapp.config import Config
from webapp.models import db, ResultParser


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

# собирает все данные 1 страницы сайта с лимитом - первые 5
def all_data_parser_from_drom(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_data = soup.find('div', class_='css-1nvf6xk').findAll('div', class_='css-1f68fiz', limit=5)
        return all_data
    return False

def get_data_from_drom():
    html = get_html(Config.DATASET_URL)
    for data in all_data_parser_from_drom(html):
        if data.find('h3', class_='css-16kqa8y'):
            name = data.find('h3', class_='css-16kqa8y').contents[0]
            url = data.find('div', class_='css-jlnpz8').find('a').get('href')
            price = data.find('div', class_='css-1dkhqyq').get_text(' ')
            description = data.find('div', class_='css-jlnpz8')\
            .find('div', class_='css-1fe6w6s').get_text()
            save_data_parser(name, url, price, description)


def save_data_parser(name, url, price, description):
    data_exists = ResultParser.query.filter(ResultParser.url == url).count()
    if not data_exists:
        data_parser = ResultParser(name=name, url=url, price=price, description=description)
        db.session.add(data_parser)
        db.session.commit()
   