FROM python:3.10.5-alpine3.16

WORKDIR /app

COPY /bot/requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./bot /app
