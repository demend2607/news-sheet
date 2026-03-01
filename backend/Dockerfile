FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends cron tzdata \ 
    && rm -rf /var/lib/apt/lists/*

COPY app /app/app

WORKDIR /app/app

CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]