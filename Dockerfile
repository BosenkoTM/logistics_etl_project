FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# По умолчанию запускаем тесты при старте контейнера
CMD ["pytest", "test_etl.py", "-v"]