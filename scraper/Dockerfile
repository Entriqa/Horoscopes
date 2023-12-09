FROM python:3.11
LABEL authors="entriqua"

WORKDIR /app

COPY . .
COPY ../web/models /app/models
COPY ../web/db /app/db

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "scrapy.py"]