FROM python:3.10

WORKDIR /src/

##ENV TELEGRAM_API_TOKEN = "1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU"
##ENV PYTHONDONTWRITEBYTECODE 1
##ENV PYTHONUNBUFFERED 1
RUN python -m venv /src/venvap

ENV PATH="/src/venvap/bin:$PATH"

COPY requirements.txt /src/

#RUN bash venvap/bin/activate 
RUN pip install --no-cache-dir -r /src/requirements.txt

COPY .env ./
COPY *.py ./
COPY app ./app
COPY public ./public


#COPY createdb.sql ./ / /

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
