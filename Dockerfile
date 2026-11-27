FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/ranking

COPY ranking /app/ranking

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
