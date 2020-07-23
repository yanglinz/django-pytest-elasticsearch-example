FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app && mkdir /home/app
WORKDIR /app
ENV HOME /home/app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${HOME}/.poetry/bin:${PATH}"
COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN poetry install

COPY . /app
