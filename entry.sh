#!/usr/bin/env sh
python manage.py collectstatic --no-input
python manage.py migrate
/opt/django_charge_summarizer/venv/bin/uwsgi --ini /opt/django_charge_summarizer/uwsgi.ini