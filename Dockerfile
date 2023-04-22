FROM python:3.10

WORKDIR /usr/src/

##ENV TELEGRAM_API_TOKEN = "1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU"
##ENV PYTHONDONTWRITEBYTECODE 1
##ENV PYTHONUNBUFFERED 1
RUN python -m venv /usr/src/venvap

ENV PATH="/usr/src/venvap/bin:$PATH"

COPY requirements.txt /usr/src/

#RUN bash venvap/bin/activate 
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

COPY .env ./
COPY *.py ./
COPY app ./app
COPY public ./public


#COPY createdb.sql ./ / /

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
