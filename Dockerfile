FROM ubuntu:latest
FROM python:3.9-slim-buster
WORKDIR /app
COPY /requirements.txt /app
COPY /src /app/src
RUN apt-get update && \
    apt-get -y install gcc mono-mcs
RUN pip install -r /app/requirements.txt
CMD cd /app/src/requester_api && \
    uvicorn main:app --reload --host 0.0.0.0
