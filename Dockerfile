FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input \
    && python manage.py migrate

EXPOSE 8000

CMD gunicorn app.wsgi:application --bind 0.0.0.0:8000
