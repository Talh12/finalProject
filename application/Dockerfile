FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py .
COPY app/index.html .

EXPOSE 8081

ENV MONGO_HOST=host.docker.internal \
    MONGO_PORT=27017 \
    MONGO_DB=weather_db \
    MONGO_USER=weather_user \
    MONGO_PASSWORD=talpass

CMD ["python", "main.py"]
