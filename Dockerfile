FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY index.html .

EXPOSE 8081

ENV MONGO_DB_HOST=host.docker.internal \
    MONGO_DB_PORT=27017 \
    MONGO_DB_NAME=weather_db \
    MONGO_DB_USER=weather_user \
    MONGO_DB_PASS=talpass

CMD ["python", "main.py"]
