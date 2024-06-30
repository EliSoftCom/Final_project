# Парсинг сайтов
Это WEB-приложение, которое по заданным фильтрам мониторит (парсит) сайты с объявлениями о продаже товаров и высылает пользователю уведомления в Telegram или другим доступным способом

## Установка

Скачайте проект с githab:
```
git clone https://github.com/EliSoftCom/Final_project.git
```

Создайте виртуальное окружение и установите зависимости:
```
pip install -r requirements.txt
```

Создайте файл config.py и задайте в нём базовые переменные:
```
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'data_parser.db')
SECRET_KEY = "Ваш секретный ключ"
```

## Запуск программы
Для запуска программы и вывода в браузер запустите файл:

Linux и Mac: 
```
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
```

Windows:
```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

Для создания таблицы базы данных запустите файл `create_db.py`:

Linux и Mac: 
```
python3 create_db.py
```

Windows:
```
python create_db.py
```
