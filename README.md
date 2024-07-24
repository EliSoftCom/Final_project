# Парсинг сайтов
Это WEB-приложение, которое по заданным фильтрам мониторит (парсит) сайты с объявлениями о продаже товаров и высылает пользователю уведомления на электронную почту, Telegram или другим доступным способом, также можно посмотреть результат парсинга на сайте.

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
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'data_parser.db')
    SECRET_KEY = "Ваш секретный ключ"
    DATASET_URL = 'https://auto.drom.ru/mitsubishi/outlander/'
```

Для работы Flask-Migrate и создания таблиц базы данных нужно выполнить поочередно команды:

Linux и Mac: 
```
export FLASK_APP=webapp && flask db init
```
```
flask db migrate -m "Описание того, что создаётся"
```
```
flask db upgrade
```

Windows: 
```
set FLASK_APP=webapp && flask db init
```
```
flask db migrate -m "Описание того, что создаётся"
```
```
flask db upgrade
```

Для парсинга по расписанию:

Windows:

Установить Linux-подсистему (Ubuntu) для Windows.
В командной строке Windows вызвать Linux-подсистему (Ubuntu) - `wsl`. Далее здесь же:
```
sudo apt-get install redis-server
```
```
sudo systemctl enable redis-server.service
```
```
sudo service redis-server start
```
```
redis-cli
```
```
monitor
```
Запустить celery в отдельной командной строке Windows в папке приложения или окне терминала:
```
celery -A tasks worker -l info --pool=solo
```
Чтобы запуск задач по расписанию работал, мы должны запустить celery-beat также в отдельной командной строке Windows в папке приложения или окне терминала:
```
celery -A tasks beat
```


## Запуск программы

Для запуска программы и вывода в браузер запустите файл:

Скрипт для Linux и MacOs

Linux и Mac: 
В корне проекта создайте файл run.sh:
#!/bin/sh
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
Сохраните файл и в корне проекта выполните в консоли команду chmod +x run.sh - это сделает файл исполняемым. Теперь для запуска проекта нужно писать 
```
./run.sh. 
```

Windows:
```
run.bat
```
или 

```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```


Для добавления данных результата парсинга в БД запустите файл `get_all_data.py`.
