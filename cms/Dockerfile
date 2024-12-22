FROM python:3.11-slim-buster as cms_base

WORKDIR /app

COPY cms/requirements.txt /app/cms/requirements.txt
COPY shared/requirements /app/shared/requirements

RUN pip install -r /app/cms/requirements.txt

COPY ../cms /app/cms
COPY ../shared /app/shared

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app