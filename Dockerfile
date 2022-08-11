FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/flask
WORKDIR /var/www/flask

ENV PORT 5555

COPY ./requirements/*.pip requirements/

RUN pip install --no-cache-dir -r requirements/dev.pip

COPY . /var/www/flask/


