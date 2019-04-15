-- Arquivo de banco de dados
-- POSTGRESQL

-- excluir uma base de dados
DROP DATABASE aular;

-- Criar uma base de dados
CREATE DATABASE aular;

-- Conectar a uma base de dados
\c aular

-- criar uma tabela

CREATE TABLE produto(
codigo		serial		primary key,
nome		varchar(50)	not null,
preco		float		not null,
quantidade	int			not null
);

\d produto;

\d

-- Inserir dados

INSERT INTO produto(nome, preco, quantidade) VALUES('PS4', 1200.0, 10);
INSERT INTO produto(nome, preco, quantidade) VALUES('Xbosta one', 400.0, 3);
INSERT INTO produto(nome, preco, quantidade) VALUES('Super Nitendo', 254.0, 8);
INSERT INTO produto(nome, preco, quantidade) VALUES('Mega Driver', 1800.0, 4);
INSERT INTO produto(nome, preco, quantidade) VALUES('Geladeira', 1200.0, 10);
INSERT INTO produto(nome, preco, quantidade) VALUES('TV LCD', 1350.0, 5);
INSERT INTO produto(nome, preco, quantidade) VALUES('Monitor', 450.0, 5);
INSERT INTO produto(nome, preco, quantidade) VALUES('TV LCD 42', 800.0, 6);
INSERT INTO produto(nome, preco, quantidade) VALUES('Lava Roupas Brastemp', 1500.0, 7);
