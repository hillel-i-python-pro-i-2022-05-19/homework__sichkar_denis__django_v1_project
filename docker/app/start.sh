#!/usr/bin/env sh


make migrate
make create-data
python manage.py runserver 0.0.0.0:8000