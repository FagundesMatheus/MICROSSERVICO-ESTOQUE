#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  -- Cria usuário se não existir
  DO
  \$\$
  BEGIN
    IF NOT EXISTS (SELECT FROM pg_user WHERE usename = '$USER_ESTOQUE') THEN
      CREATE USER $USER_ESTOQUE WITH PASSWORD '$USER_PASS';
    END IF;
  END
  \$\$;

  -- Concede permissões
  GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $USER_ESTOQUE;
  GRANT USAGE ON SCHEMA public TO $USER_ESTOQUE;
  GRANT CREATE ON SCHEMA public TO $USER_ESTOQUE;
EOSQL
