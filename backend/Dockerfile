FROM python:3.7.1-alpine3.8

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir --proxy $http_proxy -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY src /app/src
WORKDIR /app

ENTRYPOINT python3 /app/src/server.py
