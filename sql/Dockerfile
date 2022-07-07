FROM python:3.9-buster

ENV DOCKER 1
ENV ENV_FOR_DYNACONF production

WORKDIR /usr/src/app
RUN apt-get update -y && apt-get install -y nano && pip install pipenv

COPY ./Pipfile* ./
RUN pipenv install --deploy --system --clear

COPY . .

CMD gunicorn --bind 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker main:app
