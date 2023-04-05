FROM python:3.9

WORKDIR /app

ENV TELEGRAM_API_TOKEN= "1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80


COPY . ./
#COPY createdb.sql ./ / /

ENTRYPOINT ["python", "./main.py"]

