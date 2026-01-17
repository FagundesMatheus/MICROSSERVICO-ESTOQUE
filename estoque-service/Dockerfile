FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install -y build-essential curl \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install --no-cache-dir poetry

# Configura Poetry para instalar no sistema (sem venv)
RUN poetry config virtualenvs.create false

# Copia arquivos de dependências primeiro (cache)
COPY pyproject.toml poetry.lock* /app/

# Instala dependências
RUN poetry install --no-interaction --no-ansi --only main --no-root

# Copia o restante do código
COPY . /app

# Porta interna do container
EXPOSE 5000

# Comando de produção
ENV PYTHONPATH="/app"
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--chdir", "/app", "-b", "0.0.0.0:5000", "-w", "4", "--timeout", "60", "src.main:app"]

