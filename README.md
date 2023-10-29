## Курсовая 6. Основы веб-разработки на Django

Для запуска проекта необходимо:
### 1. настроить виртуальное окружение и установить зависимости 
    Команда для Windows:
        1 - python -m venv venv
        2 - venv\Scripts\activate
        3 - pip install -r requirements.txt
        4 - psql -U postgres
            create database <название  БД>;

### 2. запустить celery:
        1- celery -A config worker -l info  

### 3. запустить redis:
    Redis официально не поддерживается в Windows: 
        1 - Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
        2 - sudo apt-get update
        3 - sudo service redis-server start
        4 - redis-cli
        5 - ping
        
        Ответом от сервиса должно быть PONG. Это означает что Redis подключен

### 4. заполнить моделb данными: 
    Команда для Windows:
        1- python manage.py add_blog
        2- python manage.py add_message

### 5. заполнить файл:
    - .env

### 6. создать администратора (createsuperuser)
    - заполните поля email, PASSWORD. users/management/commands/csu.py
    Команда для Windows
    1- python manage.py csu

### 7. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver


### 8. Для отправки рассылки из командной строки: 
    Команда для Windows:
    - python manage.py sendmessage N, где N - это PK рассылки (узнать PK рассылки можно в админке)
