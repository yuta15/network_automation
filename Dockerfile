FROM python:3.11

RUN apt update && \
apt upgrade -y

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV TZ JST-9
ENV PYTHONUNBUFFERED=1
ENV NETWORK_TEST_HOST="172.18.1.2"
ENV NETWORK_TEST_USERNAME="Cisco"
ENV NETWORK_TEST_PASSWORD="Cisco"

WORKDIR /src

RUN pip install poetry && \
poetry config virtualenvs.create false

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi