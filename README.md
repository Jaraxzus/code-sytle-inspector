# Code style inspetor

Сервис для проверки вашего кода на соответсвие стандартам написания кода на
языке Python. Проверка выполняется с помощью 2х инструментов Pylint и Flake8

## Установка и запуск

Склонируйте репозиторий проекта:

```
git clone https://github.com/Jaraxzus/code-sytle-inspector.git; cd django-blog
```

Перед запуском создайте файл .env в папке с проектом и заполните следующие поля

```
POSTGRES_HOST=
POSTGRES_PASSWORD=
REDIS_HOST= SECRET_KEY=
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_USE_SSL=
CELERY_BEAT_DELAY_SEC=30.0
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=
```

Выполните команду для поднятия сервера:

```
docker-compose up -d
```

## Регистрация и аутентификация

Для регистарции и входа испльзуется email. С всеми сопутсвующими в виде
верефикации почты.
