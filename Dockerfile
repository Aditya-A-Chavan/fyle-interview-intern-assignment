FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential libffi-dev
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 7755

CMD ["gunicorn", "-c", "gunicorn_config.py", "core.server:app"]
