FROM python:3.11-alpine3.19

WORKDIR /app

COPY poetry.lock /app
COPY pyproject.toml /app

RUN apk update && apk add poetry
RUN poetry install

ENTRYPOINT ["sh"]