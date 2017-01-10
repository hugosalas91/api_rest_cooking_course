#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Create makemigrations
echo "Create makemigrations"
python3 manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Start gunicorn
echo "Start gunicorn"
gunicorn cooking_course.wsgi:application -w 2 -b :8000