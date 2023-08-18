#!/bin/bash
source .env

echo "DJANGO_SUPERUSER_PASSWORD: $DJANGO_SUPERUSER_PASSWORD"
echo "DJANGO_SUPERUSER_USERNAME: $DJANGO_SUPERUSER_USERNAME"
echo "DJANGO_SUPERUSER_EMAIL : $DJANGO_SUPERUSER_EMAIL"
# python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput &
celery -A csi.celery beat -l info &
python manage.py runserver 0.0.0.0:8000
