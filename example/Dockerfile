FROM ubuntu:20.04

ARG http_proxy
ARG https_proxy

RUN apt-get update && apt-get install -y locales
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y python3 python3-pip xvfb nano

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src src
RUN apt-get update -y && apt-get install ./src/google-chrome-stable_current_amd64.deb -y

COPY *.py config.json ./
COPY pages/*.py pages/

RUN mkdir log

CMD pytest -sv --headless=true --no-header --capture=tee-sys --alluredir=/var/opt/allure-results