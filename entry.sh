#!/usr/bin/env sh
python manage.py migrate
/opt/insumate/venv/bin/uwsgi --ini /opt/insumate/uwsgi.ini