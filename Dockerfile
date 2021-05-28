FROM python:3.9.2-slim-buster

COPY ./app /app
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"
WORKDIR /app
RUN poetry install
CMD poetry run uvicorn api.api:app --host 0.0.0.0 --reload
