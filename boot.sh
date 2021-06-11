#!/bin/bash

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Register database tables/models"
python3 manage.py makemigrations

echo "Apply database migrations"
python3 manage.py migrate

echo "Run gourmet"
gunicorn gourmet.wsgi:application --bind 0.0.0.0:8000