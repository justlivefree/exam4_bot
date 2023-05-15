FROM python:3.11-alpine

WORKDIR /apps

COPY . /apps

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirement.txt