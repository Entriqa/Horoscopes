FROM python:3.11
LABEL authors="entriqua"

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3030
CMD ["python", "main.py"]