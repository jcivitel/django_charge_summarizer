FROM python:3.13-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev \
    postgresql-dev linux-headers gcc gettext

WORKDIR /opt/django_charge_summarizer/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/django_charge_summarizer/

FROM builder AS install
WORKDIR /opt/django_charge_summarizer
ENV VIRTUAL_ENV=/opt/django_charge_summarizer/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/django_charge_summarizer/requirements.txt
RUN python manage.py collectstatic --no-input
RUN python manage.py compilemessages --ignore=venv

FROM install

EXPOSE 8000
CMD ["sh", "entry.sh"]
