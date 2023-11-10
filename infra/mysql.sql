-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Tempo de geração: 08/11/2023 às 20:17
-- Versão do servidor: 8.1.0
-- Versão do PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `Inventario`
--
CREATE DATABASE IF NOT EXISTS `Inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `Inventario`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Acaro`
--

CREATE TABLE `Acaro` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Acaro`
--

INSERT INTO `Acaro` (`id`, `nome`) VALUES
(1, 'Acaro1'),
(2, 'Acaro2'),
(3, 'Acaro3');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Agricultor`
--

CREATE TABLE `Agricultor` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `id_endereco` bigint UNSIGNED NOT NULL,
  `cpf` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Agricultor`
--

INSERT INTO `Agricultor` (`id`, `nome`, `email`, `telefone`, `id_endereco`, `cpf`) VALUES
(1, 'Agricultor1', 'agricultor1@email.com', '111-222-3333', 1, '111-222-333-44'),
(2, 'Agricultor2', 'agricultor2@email.com', '222-333-4444', 2, '222-333-444-55'),
(3, 'Agricultor3', 'agricultor3@email.com', '333-444-5555', 3, '333-444-555-66'),
(4, 'Agricultor4', 'agricultor4@email.com', '444-555-6666', 4, '444-555-666-77'),
(5, 'Agricultor5', 'agricultor5@email.com', '555-666-7777', 5, '555-666-777-88'),
(6, 'Agricultor6', 'agricultor6@email.com', '666-777-8888', 6, '666-777-888-99'),
(7, 'Agricultor7', 'agricultor7@email.com', '777-888-9999', 7, '777-888-999-00'),
(8, 'Agricultor8', 'agricultor8@email.com', '888-999-0000', 8, '888-999-000-11'),
(9, 'Agricultor9', 'agricultor9@email.com', '999-000-1111', 9, '999-000-111-22'),
(10, 'Agricultor10', 'agricultor10@email.com', '000-111-2222', 10, '000-111-222-33'),
(11, 'Agricultor11', 'agricultor11@email.com', '111-222-3333', 11, '111-222-333-44'),
(12, 'Agricultor12', 'agricultor12@email.com', '222-333-4444', 12, '222-333-444-55'),
(13, 'Agricultor13', 'agricultor13@email.com', '333-444-5555', 13, '333-444-555-66'),
(14, 'Agricultor14', 'agricultor14@email.com', '444-555-6666', 14, '444-555-666-77'),
(15, 'Agricultor15', 'agricultor15@email.com', '555-666-7777', 15, '555-666-777-88');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Amostra`
--

CREATE TABLE `Amostra` (
  `id` bigint UNSIGNED NOT NULL,
  `experimento_id` bigint UNSIGNED NOT NULL,
  `data_amostra` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Amostra`
--

INSERT INTO `Amostra` (`id`, `experimento_id`, `data_amostra`) VALUES
(1, 1, '2023-01-01'),
(2, 2, '2023-02-01'),
(3, 3, '2023-03-01'),
(4, 4, '2023-04-01'),
(5, 5, '2023-05-01'),
(6, 6, '2023-06-01'),
(7, 7, '2023-07-01'),
(8, 8, '2023-08-01'),
(9, 9, '2023-09-01'),
(10, 10, '2023-10-01'),
(11, 11, '2023-11-01'),
(12, 12, '2023-12-01'),
(13, 13, '2024-01-01'),
(14, 14, '2024-02-01'),
(15, 15, '2024-03-01'),
(16, 1, '2021-01-01');

-- --------------------------------------------------------

--
-- Estrutura para tabela `AmostraAcaro`
--

CREATE TABLE `AmostraAcaro` (
  `id` bigint UNSIGNED NOT NULL,
  `acaro_id` bigint UNSIGNED NOT NULL,
  `amostra_id` bigint UNSIGNED NOT NULL,
  `qtd` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `AmostraAcaro`
--

INSERT INTO `AmostraAcaro` (`id`, `acaro_id`, `amostra_id`, `qtd`) VALUES
(1, 1, 1, 10),
(2, 2, 1, 15),
(3, 3, 1, 20),
(4, 1, 2, 12),
(5, 2, 2, 18),
(6, 3, 2, 22),
(7, 1, 3, 14),
(8, 2, 3, 17),
(9, 3, 3, 25),
(10, 1, 4, 16),
(11, 2, 4, 20),
(12, 3, 4, 28),
(13, 1, 5, 18),
(14, 2, 5, 21),
(15, 3, 5, 30),
(16, 1, 6, 20),
(17, 2, 6, 25),
(18, 3, 6, 35),
(19, 1, 7, 22),
(20, 2, 7, 28),
(21, 3, 7, 40),
(22, 1, 8, 24),
(23, 2, 8, 30),
(24, 3, 8, 45),
(25, 1, 9, 26),
(26, 2, 9, 35),
(27, 3, 9, 50),
(28, 1, 16, 10);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Bairro`
--

CREATE TABLE `Bairro` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `cidade_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Bairro`
--

INSERT INTO `Bairro` (`id`, `nome`, `cidade_id`) VALUES
(1, 'Bairro1', 1),
(2, 'Bairro2', 2),
(3, 'Bairro3', 3),
(4, 'Bairro4', 4),
(5, 'Bairro5', 5),
(6, 'Bairro6', 6),
(7, 'Bairro7', 7),
(8, 'Bairro8', 8),
(9, 'Bairro9', 9),
(10, 'Bairro10', 10),
(11, 'Bairro11', 11),
(12, 'Bairro12', 12),
(13, 'Bairro13', 13),
(14, 'Bairro14', 14),
(15, 'Bairro15', 15);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Cidade`
--

CREATE TABLE `Cidade` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `estado_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Cidade`
--

INSERT INTO `Cidade` (`id`, `nome`, `estado_id`) VALUES
(1, 'Cidade1', 1),
(2, 'Cidade2', 2),
(3, 'Cidade3', 3),
(4, 'Cidade4', 4),
(5, 'Cidade5', 5),
(6, 'Cidade6', 6),
(7, 'Cidade7', 7),
(8, 'Cidade8', 8),
(9, 'Cidade9', 9),
(10, 'Cidade10', 10),
(11, 'Cidade11', 11),
(12, 'Cidade12', 12),
(13, 'Cidade13', 13),
(14, 'Cidade14', 14),
(15, 'Cidade15', 15);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Endereco`
--

CREATE TABLE `Endereco` (
  `id` bigint UNSIGNED NOT NULL,
  `numero` int DEFAULT NULL,
  `logradouro` varchar(255) DEFAULT NULL,
  `rua` varchar(255) DEFAULT NULL,
  `bairro_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Endereco`
--

INSERT INTO `Endereco` (`id`, `numero`, `logradouro`, `rua`, `bairro_id`) VALUES
(1, 1, 'Logradouro1', 'Rua1', 1),
(2, 2, 'Logradouro2', 'Rua2', 2),
(3, 3, 'Logradouro3', 'Rua3', 3),
(4, 4, 'Logradouro4', 'Rua4', 4),
(5, 5, 'Logradouro5', 'Rua5', 5),
(6, 6, 'Logradouro6', 'Rua6', 6),
(7, 7, 'Logradouro7', 'Rua7', 7),
(8, 8, 'Logradouro8', 'Rua8', 8),
(9, 9, 'Logradouro9', 'Rua9', 9),
(10, 10, 'Logradouro10', 'Rua10', 10),
(11, 11, 'Logradouro11', 'Rua11', 11),
(12, 12, 'Logradouro12', 'Rua12', 12),
(13, 13, 'Logradouro13', 'Rua13', 13),
(14, 14, 'Logradouro14', 'Rua14', 14),
(15, 15, 'Logradouro15', 'Rua15', 15);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Estado`
--

CREATE TABLE `Estado` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Estado`
--

INSERT INTO `Estado` (`id`, `nome`) VALUES
(1, 'Estado1'),
(2, 'Estado2'),
(3, 'Estado3'),
(4, 'Estado4'),
(5, 'Estado5'),
(6, 'Estado6'),
(7, 'Estado7'),
(8, 'Estado8'),
(9, 'Estado9'),
(10, 'Estado10'),
(11, 'Estado11'),
(12, 'Estado12'),
(13, 'Estado13'),
(14, 'Estado14'),
(15, 'Estado15');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Experimento`
--

CREATE TABLE `Experimento` (
  `id` bigint UNSIGNED NOT NULL,
  `plantacao_id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `tecnica_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Experimento`
--

INSERT INTO `Experimento` (`id`, `plantacao_id`, `nome`, `tecnica_id`) VALUES
(1, 1, 'Experimento1', 1),
(2, 2, 'Experimento2', 2),
(3, 3, 'Experimento3', 3),
(4, 4, 'Experimento4', 2),
(5, 5, 'Experimento5', 2),
(6, 6, 'Experimento6', 1),
(7, 7, 'Experimento7', 3),
(8, 8, 'Experimento8', 3),
(9, 9, 'Experimento9', 1),
(10, 10, 'Experimento10', 1),
(11, 11, 'Experimento11', 2),
(12, 12, 'Experimento12', 3),
(13, 13, 'Experimento13', 1),
(14, 14, 'Experimento14', 1),
(15, 15, 'Experimento15', 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Plantacao`
--

CREATE TABLE `Plantacao` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `numero_plantas` int DEFAULT NULL,
  `agricultor_id` bigint UNSIGNED NOT NULL,
  `area` int DEFAULT NULL,
  `cultivar` varchar(255) DEFAULT NULL,
  `localizacao` varchar(255) DEFAULT NULL,
  `TipoPlantacao_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Plantacao`
--

INSERT INTO `Plantacao` (`id`, `nome`, `numero_plantas`, `agricultor_id`, `area`, `cultivar`, `localizacao`, `TipoPlantacao_id`) VALUES
(1, 'Plantacao1', 100, 1, 500, 'Cultivar1', 'Local1', 1),
(2, 'Plantacao2', 200, 2, 600, 'Cultivar2', 'Local2', 2),
(3, 'Plantacao3', 300, 3, 700, 'Cultivar3', 'Local3', 3),
(4, 'Plantacao4', 400, 4, 800, 'Cultivar4', 'Local4', 4),
(5, 'Plantacao5', 500, 5, 900, 'Cultivar5', 'Local5', 5),
(6, 'Plantacao6', 600, 6, 1000, 'Cultivar6', 'Local6', 6),
(7, 'Plantacao7', 700, 7, 1100, 'Cultivar7', 'Local7', 7),
(8, 'Plantacao8', 800, 8, 1200, 'Cultivar8', 'Local8', 8),
(9, 'Plantacao9', 900, 9, 1300, 'Cultivar9', 'Local9', 9),
(10, 'Plantacao10', 1000, 10, 1400, 'Cultivar10', 'Local10', 10),
(11, 'Plantacao11', 1100, 11, 1500, 'Cultivar11', 'Local11', 11),
(12, 'Plantacao12', 1200, 12, 1600, 'Cultivar12', 'Local12', 12),
(13, 'Plantacao13', 1300, 13, 1700, 'Cultivar13', 'Local13', 13),
(14, 'Plantacao14', 1400, 14, 1800, 'Cultivar14', 'Local14', 14),
(15, 'Plantacao15', 1500, 15, 1900, 'Cultivar15', 'Local15', 15);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Tecnica`
--

CREATE TABLE `Tecnica` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Tecnica`
--

INSERT INTO `Tecnica` (`id`, `nome`) VALUES
(1, 'Químico 1'),
(2, 'Químico 2'),
(3, 'Controle Biológico');

-- --------------------------------------------------------

--
-- Estrutura para tabela `TipoPlantacao`
--

CREATE TABLE `TipoPlantacao` (
  `id` bigint NOT NULL,
  `nome` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TipoPlantacao`
--

INSERT INTO `TipoPlantacao` (`id`, `nome`) VALUES
(1, 'Tipo1'),
(2, 'Tipo2'),
(3, 'Tipo3'),
(4, 'Tipo4'),
(5, 'Tipo5'),
(6, 'Tipo6'),
(7, 'Tipo7'),
(8, 'Tipo8'),
(9, 'Tipo9'),
(10, 'Tipo10'),
(11, 'Tipo11'),
(12, 'Tipo12'),
(13, 'Tipo13'),
(14, 'Tipo14'),
(15, 'Tipo15');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `Acaro`
--
ALTER TABLE `Acaro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_endereco` (`id_endereco`);

--
-- Índices de tabela `Amostra`
--
ALTER TABLE `Amostra`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `experimento_id` (`experimento_id`);

--
-- Índices de tabela `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `acaro_id` (`acaro_id`),
  ADD KEY `amostra_id` (`amostra_id`);

--
-- Índices de tabela `Bairro`
--
ALTER TABLE `Bairro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `cidade_id` (`cidade_id`);

--
-- Índices de tabela `Cidade`
--
ALTER TABLE `Cidade`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `estado_id` (`estado_id`);

--
-- Índices de tabela `Endereco`
--
ALTER TABLE `Endereco`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `bairro_id` (`bairro_id`);

--
-- Índices de tabela `Estado`
--
ALTER TABLE `Estado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `Experimento`
--
ALTER TABLE `Experimento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `plantacao_id` (`plantacao_id`),
  ADD KEY `tecnica_id` (`tecnica_id`);

--
-- Índices de tabela `Plantacao`
--
ALTER TABLE `Plantacao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `agricultor_id` (`agricultor_id`),
  ADD KEY `fk_Plantacao_TipoPlantacao1_idx` (`TipoPlantacao_id`);

--
-- Índices de tabela `Tecnica`
--
ALTER TABLE `Tecnica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `TipoPlantacao`
--
ALTER TABLE `TipoPlantacao`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Acaro`
--
ALTER TABLE `Acaro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Amostra`
--
ALTER TABLE `Amostra`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de tabela `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de tabela `Bairro`
--
ALTER TABLE `Bairro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Cidade`
--
ALTER TABLE `Cidade`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Endereco`
--
ALTER TABLE `Endereco`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Estado`
--
ALTER TABLE `Estado`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Experimento`
--
ALTER TABLE `Experimento`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Plantacao`
--
ALTER TABLE `Plantacao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `Tecnica`
--
ALTER TABLE `Tecnica`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Agricultor`
--
ALTER TABLE `Agricultor`
  ADD CONSTRAINT `Agricultor_ibfk_1` FOREIGN KEY (`id_endereco`) REFERENCES `Endereco` (`id`);

--
-- Restrições para tabelas `Amostra`
--
ALTER TABLE `Amostra`
  ADD CONSTRAINT `Amostra_ibfk_1` FOREIGN KEY (`experimento_id`) REFERENCES `Experimento` (`id`);

--
-- Restrições para tabelas `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  ADD CONSTRAINT `AmostraAcaro_ibfk_1` FOREIGN KEY (`acaro_id`) REFERENCES `Acaro` (`id`),
  ADD CONSTRAINT `AmostraAcaro_ibfk_2` FOREIGN KEY (`amostra_id`) REFERENCES `Amostra` (`id`);

--
-- Restrições para tabelas `Bairro`
--
ALTER TABLE `Bairro`
  ADD CONSTRAINT `Bairro_ibfk_1` FOREIGN KEY (`cidade_id`) REFERENCES `Cidade` (`id`);

--
-- Restrições para tabelas `Cidade`
--
ALTER TABLE `Cidade`
  ADD CONSTRAINT `Cidade_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `Estado` (`id`);

--
-- Restrições para tabelas `Endereco`
--
ALTER TABLE `Endereco`
  ADD CONSTRAINT `Endereco_ibfk_1` FOREIGN KEY (`bairro_id`) REFERENCES `Bairro` (`id`);

--
-- Restrições para tabelas `Experimento`
--
ALTER TABLE `Experimento`
  ADD CONSTRAINT `Experimento_ibfk_1` FOREIGN KEY (`plantacao_id`) REFERENCES `Plantacao` (`id`),
  ADD CONSTRAINT `Experimento_ibfk_2` FOREIGN KEY (`tecnica_id`) REFERENCES `Tecnica` (`id`);

--
-- Restrições para tabelas `Plantacao`
--
ALTER TABLE `Plantacao`
  ADD CONSTRAINT `fk_Plantacao_TipoPlantacao1` FOREIGN KEY (`TipoPlantacao_id`) REFERENCES `TipoPlantacao` (`id`),
  ADD CONSTRAINT `Plantacao_ibfk_1` FOREIGN KEY (`agricultor_id`) REFERENCES `Agricultor` (`id`);
--
-- Banco de dados: `Sistema`
--
CREATE DATABASE IF NOT EXISTS `Sistema` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `Sistema`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Acaro`
--

CREATE TABLE `Acaro` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Acaro`
--

INSERT INTO `Acaro` (`id`, `nome`) VALUES
(1, 'Tetranychus urticae'),
(2, 'Amblyseius andersoni'),
(3, 'Phytoseiulus Californicus');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Agricultor`
--

CREATE TABLE `Agricultor` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Agricultor`
--

INSERT INTO `Agricultor` (`id`, `nome`, `email`, `senha`) VALUES
(1, 'Thiago Augusto', 'thiago.au@email.com', 'senha1'),
(2, 'Marcos Sousa', 'marcos.so@email.com', 'senha2'),
(3, 'Douglas Alkimim', 'douglas.al@email.com', 'senha3'),
(4, 'Bruno Chevitarese', 'bruno.ch@email.com', 'senha4'),
(5, 'Maria Castiglioni', 'maria.ca@email.com', 'senha5'),
(6, 'Willsiman Evangelista', 'willsiman.ev@email.com', 'senha6'),
(7, 'Wal Almeida', 'wal.al@email.com', 'senha7'),
(8, 'Harian Couto', 'harian.co@email.com', 'senha8'),
(9, 'Fidelis Batista', 'fidelis.ba@email.com', 'senha9'),
(10, 'Mateus Silva', 'mateus.si@email.com', 'senha10');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Amostra`
--

CREATE TABLE `Amostra` (
  `id` bigint UNSIGNED NOT NULL,
  `data` varchar(30) DEFAULT NULL,
  `experimento_id` bigint UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Amostra`
--

INSERT INTO `Amostra` (`id`, `data`, `experimento_id`) VALUES
(1, '2023-01-01', 1),
(2, '2023-02-28', 2),
(3, '2023-03-31', 3),
(4, '2023-04-30', 4),
(5, '2023-05-31', 5),
(6, '2023-06-30', 6),
(7, '2023-07-31', 7),
(8, '2023-08-31', 8),
(9, '2023-09-30', 9),
(10, '2023-10-31', 10),
(11, '2023-10-24', 1),
(12, '2023-10-25', 2),
(13, '2023-10-26', 3),
(14, '2023-10-27', 4),
(15, '2023-10-28', 5),
(16, '2023-10-29', 1),
(17, '2023-10-30', 2),
(18, '2023-10-31', 3),
(19, '2023-11-01', 4),
(20, '2024-03-02', 5),
(21, '2024-11-12', 1),
(22, '2024-10-29', 2),
(23, '2024-07-17', 3),
(24, '2024-03-29', 4),
(25, '2024-08-01', 5),
(26, '2024-03-12', 1),
(27, '2024-03-22', 2),
(28, '2024-07-13', 3),
(29, '2024-01-01', 4),
(30, '2024-05-30', 5),
(31, '2024-01-22', 1),
(32, '2024-01-20', 2),
(33, '2024-02-06', 3),
(34, '2024-05-03', 4),
(35, '2024-05-24', 5),
(36, '2024-12-19', 1),
(37, '2024-08-25', 2),
(38, '2024-05-09', 3),
(39, '2024-10-29', 4),
(40, '2024-01-31', 5),
(41, '2024-12-05', 1),
(42, '2024-05-29', 2),
(43, '2024-04-02', 3),
(44, '2024-01-17', 4),
(45, '2024-06-18', 5),
(46, '2024-03-09', 1),
(47, '2024-07-21', 2),
(48, '2024-03-17', 3),
(49, '2024-05-22', 4),
(50, '2024-04-28', 5),
(51, '2024-06-13', 1),
(52, '2024-04-14', 2),
(53, '2024-01-29', 3),
(54, '2024-07-16', 4),
(55, '2024-06-20', 5),
(56, '2024-09-24', 1),
(57, '2024-04-04', 2),
(58, '2024-02-06', 3),
(59, '2024-09-20', 4),
(60, '2024-04-23', 5),
(61, '2024-05-25', 1),
(62, '2024-01-22', 2),
(63, '2024-02-05', 3),
(64, '2024-04-25', 4),
(65, '2024-04-14', 5),
(66, '2024-06-29', 1),
(67, '2024-08-11', 2),
(68, '2024-07-30', 3),
(69, '2024-01-24', 4),
(70, '2024-08-03', 5),
(71, '2024-10-04', 1),
(72, '2024-01-11', 2),
(73, '2024-11-14', 3),
(74, '2024-04-09', 4),
(75, '2024-09-29', 5),
(76, '2024-12-01', 1),
(77, '2024-05-09', 2),
(78, '2024-01-08', 3),
(79, '2024-01-15', 4),
(80, '2024-02-23', 5),
(81, '2024-08-12', 6),
(82, '2024-08-18', 7),
(83, '2024-04-27', 8),
(84, '2024-09-17', 9),
(85, '2024-08-10', 10),
(86, '2024-11-29', 6),
(87, '2024-09-26', 7),
(88, '2024-12-12', 8),
(89, '2024-07-15', 9),
(90, '2024-11-04', 10),
(91, '2024-08-13', 6),
(92, '2024-07-22', 7),
(93, '2024-12-05', 8),
(94, '2024-12-23', 9),
(95, '2024-02-10', 10),
(96, '2024-08-15', 6),
(97, '2024-10-14', 7),
(98, '2024-01-26', 8),
(99, '2024-12-27', 9),
(100, '2024-09-28', 10),
(101, '2024-10-02', 6),
(102, '2024-07-16', 7),
(103, '2024-06-13', 8),
(104, '2024-08-16', 9),
(105, '2024-10-13', 10),
(106, '2024-01-20', 6),
(107, '2024-11-27', 7),
(108, '2024-05-22', 8),
(109, '2024-03-23', 9),
(110, '2024-12-18', 10),
(111, '2023-11-23', 6),
(112, '2023-11-24', 7),
(113, '2023-11-25', 8),
(114, '2023-11-26', 9),
(115, '2023-11-27', 10),
(116, '2023-11-28', 6),
(117, '2023-11-29', 7),
(118, '2023-11-30', 8),
(119, '2023-12-01', 9),
(120, '2023-12-02', 10),
(121, '2023-12-03', 6),
(122, '2023-12-04', 7),
(123, '2023-12-05', 8),
(124, '2023-12-06', 9),
(125, '2023-12-07', 10),
(126, '2023-12-08', 6),
(127, '2023-12-09', 7),
(128, '2023-12-10', 8),
(129, '2023-12-11', 9),
(130, '2023-12-12', 10),
(131, '2023-12-13', 6),
(132, '2023-12-14', 7),
(133, '2023-12-15', 8),
(134, '2023-12-16', 9),
(135, '2023-12-17', 10),
(136, '2023-12-18', 6),
(137, '2023-12-19', 7),
(138, '2023-12-20', 8),
(139, '2023-12-21', 9),
(140, '2023-12-22', 10);

-- --------------------------------------------------------

--
-- Estrutura para tabela `AmostraAcaro`
--

CREATE TABLE `AmostraAcaro` (
  `id` bigint UNSIGNED NOT NULL,
  `acaro_id` bigint UNSIGNED DEFAULT NULL,
  `amostra_id` bigint UNSIGNED DEFAULT NULL,
  `qtd` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `AmostraAcaro`
--

INSERT INTO `AmostraAcaro` (`id`, `acaro_id`, `amostra_id`, `qtd`) VALUES
(1, 1, 1, 5),
(2, 3, 2, 8),
(3, 3, 3, 4),
(4, 1, 4, 6),
(5, 1, 5, 7),
(6, 3, 6, 9),
(7, 1, 7, 3),
(8, 2, 8, 2),
(9, 1, 9, 10),
(10, 2, 10, 5),
(11, 1, 1, 10),
(12, 3, 2, 20),
(13, 1, 3, 30),
(14, 1, 4, 40),
(15, 3, 5, 50),
(16, 2, 6, 60),
(17, 1, 7, 70),
(18, 3, 8, 80),
(19, 3, 9, 90),
(20, 3, 10, 100),
(21, 1, 1, 10),
(22, 3, 2, 20),
(23, 2, 3, 30),
(24, 3, 4, 40),
(25, 3, 5, 50),
(26, 2, 6, 60),
(27, 3, 7, 70),
(28, 3, 8, 80),
(29, 1, 9, 90),
(30, 1, 10, 100),
(31, 3, 11, 110),
(32, 3, 12, 120),
(33, 3, 13, 130),
(34, 2, 14, 140),
(35, 3, 15, 150),
(36, 3, 16, 160),
(37, 1, 17, 170),
(38, 1, 18, 180),
(39, 3, 19, 190),
(40, 3, 20, 200),
(41, 2, 1, 10),
(42, 1, 2, 20),
(43, 2, 3, 30),
(44, 1, 4, 40),
(45, 1, 5, 50),
(46, 2, 6, 60),
(47, 3, 7, 70),
(48, 3, 8, 80),
(49, 2, 9, 90),
(50, 3, 10, 100),
(51, 1, 11, 110),
(52, 3, 12, 120),
(53, 2, 13, 130),
(54, 3, 14, 140),
(55, 2, 15, 150),
(56, 3, 16, 160),
(57, 3, 17, 170),
(58, 1, 18, 180),
(59, 2, 19, 190),
(60, 3, 20, 200),
(61, 1, 21, 210),
(62, 3, 22, 220),
(63, 1, 23, 230),
(64, 1, 24, 240),
(65, 1, 25, 250),
(66, 1, 26, 260),
(67, 2, 27, 270),
(68, 2, 28, 280),
(69, 1, 29, 290),
(70, 2, 30, 300),
(71, 1, 31, 310),
(72, 3, 32, 320),
(73, 1, 33, 330),
(134, 2, 1, 10),
(135, 3, 1, 15),
(136, 1, 2, 8),
(137, 3, 2, 12),
(138, 2, 3, 7),
(139, 3, 3, 11),
(140, 3, 4, 9),
(141, 3, 4, 14),
(142, 1, 5, 6),
(143, 3, 5, 10),
(144, 3, 6, 12),
(145, 1, 6, 8),
(146, 3, 7, 16),
(147, 2, 7, 18),
(148, 2, 8, 14),
(149, 3, 8, 9),
(150, 3, 9, 11),
(151, 2, 9, 7),
(152, 3, 10, 13),
(153, 2, 10, 6),
(154, 3, 11, 8),
(155, 2, 11, 12),
(156, 3, 12, 10),
(157, 3, 12, 15),
(158, 1, 13, 9),
(159, 3, 13, 16),
(160, 1, 14, 14),
(161, 2, 14, 10),
(162, 1, 15, 12),
(163, 1, 15, 8),
(164, 1, 16, 18),
(165, 3, 16, 15),
(166, 3, 17, 7),
(167, 3, 17, 11),
(168, 2, 18, 6),
(169, 1, 18, 13),
(170, 1, 19, 9),
(171, 1, 19, 14),
(172, 3, 20, 10),
(173, 2, 20, 15),
(174, 3, 21, 13),
(175, 1, 21, 8),
(176, 1, 22, 16),
(177, 1, 22, 12),
(178, 1, 23, 15),
(179, 3, 23, 9),
(180, 2, 24, 11),
(181, 1, 24, 7),
(182, 1, 25, 18),
(183, 2, 25, 16),
(184, 1, 26, 12),
(185, 3, 26, 8),
(186, 2, 27, 14),
(187, 3, 27, 10),
(188, 3, 28, 16),
(189, 2, 28, 12),
(190, 2, 29, 8),
(191, 3, 29, 14),
(192, 2, 30, 10),
(193, 2, 30, 13),
(194, 1, 31, 16),
(195, 1, 31, 18),
(196, 3, 32, 14),
(197, 1, 32, 9),
(198, 2, 33, 11),
(199, 2, 33, 7),
(200, 1, 34, 13),
(201, 2, 34, 6),
(202, 3, 35, 8),
(203, 2, 35, 12),
(204, 1, 36, 10),
(205, 3, 36, 15),
(206, 3, 37, 9),
(207, 2, 37, 16),
(208, 2, 38, 14),
(209, 1, 38, 10),
(210, 2, 39, 12),
(211, 1, 39, 8),
(212, 1, 40, 18),
(213, 2, 40, 15),
(214, 1, 41, 7),
(215, 3, 41, 11),
(216, 3, 42, 6),
(217, 2, 42, 13),
(218, 3, 43, 9),
(219, 3, 43, 14),
(220, 2, 44, 10),
(221, 1, 44, 15),
(222, 1, 45, 16),
(223, 2, 45, 9),
(224, 1, 46, 11),
(225, 1, 46, 7),
(226, 1, 47, 18),
(227, 2, 47, 16),
(228, 3, 48, 12),
(229, 2, 48, 8),
(230, 3, 49, 14),
(231, 1, 49, 10),
(232, 3, 50, 16),
(233, 1, 50, 12),
(234, 1, 51, 8),
(235, 1, 51, 14),
(236, 1, 52, 10),
(237, 2, 52, 13),
(238, 2, 53, 16),
(239, 1, 53, 18),
(240, 1, 54, 14),
(241, 2, 54, 9),
(242, 1, 55, 11),
(243, 2, 55, 7),
(244, 2, 56, 18),
(245, 2, 56, 15),
(246, 3, 57, 13),
(247, 3, 57, 8),
(248, 1, 58, 16),
(249, 2, 58, 12),
(250, 3, 59, 15),
(251, 1, 59, 9),
(252, 2, 60, 11),
(253, 3, 60, 7);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Experimento`
--

CREATE TABLE `Experimento` (
  `id` bigint UNSIGNED NOT NULL,
  `plantacao_id` bigint UNSIGNED DEFAULT NULL,
  `tecnica_id` bigint UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Experimento`
--

INSERT INTO `Experimento` (`id`, `plantacao_id`, `tecnica_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Plantacao`
--

CREATE TABLE `Plantacao` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `numero_plantas` int DEFAULT NULL,
  `agricultor_id` bigint UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Plantacao`
--

INSERT INTO `Plantacao` (`id`, `nome`, `numero_plantas`, `agricultor_id`) VALUES
(1, 'Morangal Leds', 1000, 1),
(2, 'Morangal SmartIdea', 800, 2),
(3, 'Morangal Bac', 1200, 3),
(4, 'Morangal CB', 950, 4),
(5, 'Morangal More', 1100, 5),
(6, 'Morangal Moje', 750, 6),
(7, 'Morangal IDFC', 900, 7),
(8, 'Morangal Blank', 1050, 8),
(9, 'Morangal Space', 1300, 9),
(10, 'Morangal Dark', 950, 10),
(11, 'Morangal Horse', 1908, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Tecnica`
--

CREATE TABLE `Tecnica` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Tecnica`
--

INSERT INTO `Tecnica` (`id`, `nome`) VALUES
(1, 'Acaricida Quimico 1'),
(2, 'Acaricida Quimico 2'),
(3, 'Acaricida Quimico 3'),
(4, 'Acaricida Quimico 4'),
(5, 'Acaricida Quimico 5'),
(6, 'Acaricida Quimico 6'),
(7, 'Acaricida Quimico 7'),
(8, 'Acaricida Quimico 8'),
(9, 'Controle Biologico 2'),
(10, 'Controle Biologico 2'),
(11, 'Óleo Essencial 1'),
(12, 'Óleo Essencial 2');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `Acaro`
--
ALTER TABLE `Acaro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `Amostra`
--
ALTER TABLE `Amostra`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `experimento_id` (`experimento_id`);

--
-- Índices de tabela `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `acaro_id` (`acaro_id`),
  ADD KEY `amostra_id` (`amostra_id`);

--
-- Índices de tabela `Experimento`
--
ALTER TABLE `Experimento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `plantacao_id` (`plantacao_id`),
  ADD KEY `tecnica_id` (`tecnica_id`);

--
-- Índices de tabela `Plantacao`
--
ALTER TABLE `Plantacao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `agricultor_id` (`agricultor_id`);

--
-- Índices de tabela `Tecnica`
--
ALTER TABLE `Tecnica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Acaro`
--
ALTER TABLE `Acaro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `Amostra`
--
ALTER TABLE `Amostra`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;

--
-- AUTO_INCREMENT de tabela `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=254;

--
-- AUTO_INCREMENT de tabela `Experimento`
--
ALTER TABLE `Experimento`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `Plantacao`
--
ALTER TABLE `Plantacao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `Tecnica`
--
ALTER TABLE `Tecnica`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Amostra`
--
ALTER TABLE `Amostra`
  ADD CONSTRAINT `Amostra_ibfk_1` FOREIGN KEY (`experimento_id`) REFERENCES `Experimento` (`id`);

--
-- Restrições para tabelas `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  ADD CONSTRAINT `AmostraAcaro_ibfk_1` FOREIGN KEY (`acaro_id`) REFERENCES `Acaro` (`id`),
  ADD CONSTRAINT `AmostraAcaro_ibfk_2` FOREIGN KEY (`amostra_id`) REFERENCES `Amostra` (`id`);

--
-- Restrições para tabelas `Experimento`
--
ALTER TABLE `Experimento`
  ADD CONSTRAINT `Experimento_ibfk_1` FOREIGN KEY (`plantacao_id`) REFERENCES `Plantacao` (`id`),
  ADD CONSTRAINT `Experimento_ibfk_2` FOREIGN KEY (`tecnica_id`) REFERENCES `Tecnica` (`id`);

--
-- Restrições para tabelas `Plantacao`
--
ALTER TABLE `Plantacao`
  ADD CONSTRAINT `Plantacao_ibfk_1` FOREIGN KEY (`agricultor_id`) REFERENCES `Agricultor` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
