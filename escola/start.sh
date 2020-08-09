#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username $DJANGO_SUPERUSER_USER --email $DJANGO_SUPERUSER_EMAIL --no-input
python manage.py test
python manage.py runserver 0.0.0.0:8000
