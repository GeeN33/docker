FROM python:alpine

WORKDIR /app2

RUN pip install redis

COPY . .

CMD ["python", "worker.py"]
