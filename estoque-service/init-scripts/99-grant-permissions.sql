-- Concede permissões em todas as tabelas existentes ao usuário operador
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO operador;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO operador;

-- Configura permissões padrão para tabelas futuras
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO operador;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO operador;
