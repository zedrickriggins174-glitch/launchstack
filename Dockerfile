FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot_v2.py .
RUN mkdir -p /app/memory
CMD ["python3", "bot_v2.py"]
