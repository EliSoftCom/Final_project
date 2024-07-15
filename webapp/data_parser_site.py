from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def all_data_parser_from_drom(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_data = soup.find('div', class_='css-1nvf6xk eojktn00').find('div').findAll('a')
        return all_data
    return False

def get_data_in_dict_from_drom(dataset_url):
    html = get_html(dataset_url)
    result_data = []
    for data in all_data_parser_from_drom(html):
        if data.find('div', class_='css-16kqa8y e3f4v4l2'):
            name = data.find('div', class_='css-16kqa8y e3f4v4l2').contents[0]
            url = data.get('href')
            price = data.find('span', class_='css-46itwz').find('span').text
            description = data.find('div', class_='css-1fe6w6s').get_text()
            date_of_announcement = data.find('div', class_='css-1x4jcds').get_text(', ')
            result_data.append({
                'name': name,
                'url': url,
                'price': price,
                'description': description,
                'date_of_announcement': date_of_announcement
            })
    return result_data            
   