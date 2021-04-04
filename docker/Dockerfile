FROM python:3.8.7-slim-buster as builder

LABEL maintainer="Wojtek Warych woj.warych@gmail.com" \
      version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1

ENV APP_USER=dev

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash $APP_USER
USER $APP_USER
ENV HOME /home/${APP_USER}
RUN mkdir "${HOME}/src"
WORKDIR "${HOME}/src"

COPY requirements.txt /tmp/
RUN pip install --user -r /tmp/requirements.txt
ENV PATH="${HOME}/.local/bin:${PATH}"

COPY --chown=$APP_USER ./src .
RUN cp reformat.sh ${HOME}/.local/bin/
