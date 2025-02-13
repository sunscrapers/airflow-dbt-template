FROM python:3.11-slim

USER root
RUN apt-get update -y \
    && apt-get install -y build-essential \
    && apt-get install gcc -y \
    && apt-get install git -y \
    && apt-get install sudo -y\
    && apt-get install -y python3-dev \
    && apt-get install -y libpq-dev \
    && apt-get clean \
    && pip install psycopg2-binary

RUN adduser --disabled-password --gecos '' airflow

WORKDIR /opt/python_scripts
COPY . .

USER airflow

COPY ./requirements.txt /opt/python_scripts/requirements.txt
COPY ./postgres_utils.py /opt/python_scripts/postgres_utils.py

RUN cd /opt/python_scripts && pip install -r requirements.txt

USER root
RUN chgrp airflow -R /opt/python_scripts && chmod g+rwx -R /opt/python_scripts
USER airflow
