FROM python:3.10

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR ${APP_HOME}
COPY ./requirements/ ${APP_HOME}/requirements/
RUN pip install -r requirements/local.txt

COPY ./docker/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/start /start
RUN chmod +x /start

COPY ./src ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
