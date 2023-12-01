FROM python:3.11
LABEL authors="entriqua"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3030
COPY .. .
CMD ["python", "main.py"]