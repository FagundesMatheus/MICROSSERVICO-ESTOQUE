#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

    CREATE USER $USER_ESTOQUE WITH PASSWORD '$USER_PASS';

    -- Dá permissões ao usuário no banco criado
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $USER_ESTOQUE;

EOSQL