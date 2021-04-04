FROM python:3.8.7-slim-buster as builder

LABEL maintainer="Wojtek Warych woj.warych@gmail.com" \
      version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR ./src

COPY ./src .
