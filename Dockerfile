FROM python:3.8-slim-buster

COPY . /app
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"
WORKDIR /app
RUN poetry update && poetry install
CMD poetry run uvicorn api:app --host 0.0.0.0 --reload
