FROM python:3.11-slim

USER root
RUN apt-get update && apt-get install -y git

# Create necessary directories
RUN mkdir -p /opt/dbt /opt/dbt/logs /opt/dbt/target

# Copy files
COPY . /opt/dbt/

# Install requirements
RUN pip install -r /opt/dbt/requirements.txt 

# Create dbt user and set permissions
RUN if ! id -u dbt >/dev/null 2>&1; then useradd -m dbt; fi
RUN chown -R dbt:dbt /opt/dbt && \
    chmod -R 775 /opt/dbt/logs && \
    chmod -R 775 /opt/dbt/target

# Install dbt dependencies
USER dbt
WORKDIR /opt/dbt
RUN dbt deps
