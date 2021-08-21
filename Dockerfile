FROM ubuntu:latest
FROM python:3.9-slim-buster
WORKDIR /app
COPY /requirements.txt /app
RUN pip3 install -r /app/requirements.txt
