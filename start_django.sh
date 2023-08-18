#!/bin/bash

python manage.py makemigrations
python manage.py migrate
celery -A csi.celery beat -l info &
python manage.py runserver 0.0.0.0:8000
