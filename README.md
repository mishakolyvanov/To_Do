# To_Do
Веб-приложение для создания своих To Do, и возможностью смотреть чужие To Do.

## Development workflow
Создать новое окружение `python -m venv venv`

Активировать созданное окружение `source venv/bin/activate`, деактивировать - выполнить `deactivate`

Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Для запуска выполнить `python manage.py runserver`

Приложение работает на порту 8000

Для перехода на сайт перейти по ссылке http://127.0.0.1:8000/ToDoApp/ToDo/authors

Для запуска тестов выполнить `python manage.py test`

Для создания 5ти рандомных пользователей с 3мя рандомными записями выполнить `python manage.py FillBase 5 3`
