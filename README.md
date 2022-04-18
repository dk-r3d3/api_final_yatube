# api_final
api final

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

'''git clone https://github.com/dk-r3d3/api_final_yatube.git'''

'''cd yuatube_api_final'''

Cоздать и активировать виртуальное окружение:

'''python3 -m venv env'''

'''source env/bin/activate'''

Установить зависимости из файла requirements.txt:

'''python3 -m pip install --upgrade pip'''

'''pip install -r requirements.txt'''

Установите с помощью pip:

'''pip install djoser'''

Выполнить миграции:

'''cd yatube_api''' - директория с manage.py

'''python3 manage.py migrate'''

Запустить проект:

'''python3 manage.py runserver'''

Примеры:

Создать публикацию:
POST "http://127.0.0.1:8000/api/v1/posts/"

Получить публикацию:
GET "http://127.0.0.1:8000/api/v1/posts/{id}/"

Получить список всех публикаций:
GET "http://127.0.0.1:8000/api/v1/posts/"

Изменить публикацию:
PUT "http://127.0.0.1:8000/api/v1/posts/{id}/"

Удалить публикацию:
DELETE "http://127.0.0.1:8000/api/v1/posts/{id}/"

Создать группу:
POST "http://127.0.0.1:8000/api/v1/groups/"

Получить список групп:
GET "http://127.0.0.1:8000/api/v1/groups/"

Получить группу:
GET "http://127.0.0.1:8000/api/v1/groups/{id}/"

Создать комментарий:
POST "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/"

Получить комментарий:
GET "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/"

Оформить подписку на автора:
POST "http://127.0.0.1:8000/api/v1/follow/"

Создать нового пользователя:
POST "http://127.0.0.1:8000/api/v1/auth/users/"

Получить список аутентифицированных пользователей:
GET "http://127.0.0.1:8000/api/v1/auth/users/"

Получить JWT токен:
POST "http://127.0.0.1:8000/api/v1/jwt/create/"

Обновить JWT токен:
POST "http://127.0.0.1:8000/api/v1/jwt/refresh/"

Проверить JWT токен:
POST "http://127.0.0.1:8000/api/v1/jwt/verify/"
