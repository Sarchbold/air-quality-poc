FROM ubuntu:latest
FROM python:3.9-slim-buster
WORKDIR /app
COPY /requirements.txt /app
COPY /src /app/src
WORKDIR /app/src/api
RUN apt-get update && \
    apt-get -y install gcc mono-mcs
RUN pip install -r /app/requirements.txt
CMD cd /app/src/api && \
    uvicorn responder:app --reload --host 0.0.0.0
