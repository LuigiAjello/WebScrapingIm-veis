-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS dfimoveis_db;
USE dfimoveis_db;

-- Criação da tabela de imóveis
CREATE TABLE IF NOT EXISTS imoveis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    metragem INT,
    quartos INT,
    suites INT,
    vagas INT,
    PequenaDescricao TEXT,
    preco FLOAT,
    ValorMetroQuadrado FLOAT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
