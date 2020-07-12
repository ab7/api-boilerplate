FROM python:3.8-slim-buster

RUN pip install fastapi uvicorn

COPY . .

CMD uvicorn api:app --host 0.0.0.0 --reload