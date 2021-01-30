FROM python:3.8.7-slim-buster as builder

LABEL maintainer="Wojtek Warych woj.warych@gmail.com" \
      version="0.0.1"

ENV APP_USER=dev
ENV APP_HOME="/home/${APP_USER}"

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash $APP_USER
USER $APP_USER
WORKDIR "${APP_HOME}/src"

COPY requirements.txt /tmp/
RUN pip install --user -r /tmp/requirements.txt
ENV PATH="${APP_HOME}/.local/bin:${PATH}"
COPY ./src .
