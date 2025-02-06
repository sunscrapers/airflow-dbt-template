FROM python:3.11-slim

USER root
RUN apt-get update && apt-get install -y git

COPY . /opt/dbt

RUN pip install -r /opt/dbt/config/requirements.txt 
RUN if ! id -u dbt >/dev/null 2>&1; then useradd -m dbt; fi
RUN chown -R dbt:dbt /opt/dbt

WORKDIR /opt/dbt/config
RUN dbt deps

WORKDIR /opt/dbt
USER dbt
COPY config/profiles.yml /home/dbt/.dbt/profiles.yml
RUN rm config/profiles.yml
