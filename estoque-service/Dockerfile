FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-interaction --no-ansi --only main --no-root

COPY . /app

EXPOSE 5000

ENV PYTHONPATH="/app"
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--chdir", "/app", "-b", "0.0.0.0:5000", "-w", "4", "--timeout", "60", "src.main:app"]

