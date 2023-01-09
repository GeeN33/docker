FROM python:alpine

WORKDIR /app

RUN pip install redis

COPY . .

CMD ["python", "client.py"]
