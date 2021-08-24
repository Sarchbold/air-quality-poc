FROM ubuntu:latest
FROM python:3.9-slim-buster
WORKDIR /app
COPY /requirements.txt /app
COPY /src /app/src
WORKDIR /app/src
RUN pip3 install -r /app/requirements.txt
RUN uvicorn responder:app --reload --host 0.0.0.0
