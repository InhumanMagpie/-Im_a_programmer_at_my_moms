# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add gcc musl-dev
RUN pip install --upgrade pip pipenv
COPY ./Pipfile* .
RUN pipenv install --deploy --system --clear

# copy project
COPY backend/drfblog .

# Collect static files
RUN python -m manage collectstatic -v 3 --no-input