FROM python:3.10

RUN mkdir code
WORKDIR code

ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME=musicbackend

RUN pip install -r requirements.txt

CMD gunicorn musicbackend.wsgi:application -b 0.0.0.0:8000
