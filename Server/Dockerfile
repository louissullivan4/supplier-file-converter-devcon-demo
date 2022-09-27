# syntax=docker/dockerfile:1

## Build
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirments.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir -p static/uploads static/output

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]