-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Tempo de geração: 05/02/2024 às 10:59
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
-- Estrutura para tabela `Agricultor`
--

CREATE TABLE `Agricultor` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cpf` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `telefone` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Agricultor`
--

INSERT INTO `Agricultor` (`id`, `nome`, `cpf`, `email`, `telefone`) VALUES
(1, 'Bruno da Fonseca Chevitarese', '1889145091', 'bruno.chevitarese@estudante.ifes.edu.b', '27992795093'),
(2, 'Bruno', '18891480755', 'chevitarese.bruno@gmail.com', '27992795092'),
(8, 'Wilsiman', '5002055', 'will.evangelista@gmail.com', '2799279');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Amostragem`
--

CREATE TABLE `Amostragem` (
  `id` bigint UNSIGNED NOT NULL,
  `data_Amos` date NOT NULL,
  `cultivo_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Amostragem`
--

INSERT INTO `Amostragem` (`id`, `data_Amos`, `cultivo_id`) VALUES
(2, '2024-01-01', 9),
(3, '2024-01-02', 10),
(4, '2024-01-03', 9),
(5, '2024-01-04', 10),
(6, '2024-01-05', 9),
(7, '2024-01-06', 10),
(8, '2024-01-07', 9),
(9, '2024-01-08', 10),
(10, '2024-01-09', 9),
(11, '2024-01-10', 10),
(12, '2024-01-11', 9),
(13, '2023-10-25', 13),
(14, '2023-10-25', 13),
(15, '2023-10-25', 13),
(16, '2023-10-25', 13),
(17, '2023-10-25', 13),
(18, '2023-10-25', 13),
(19, '2023-10-25', 13),
(20, '2023-10-25', 13),
(21, '2023-10-25', 13),
(22, '2023-10-25', 13),
(23, '2023-10-25', 13),
(24, '2023-10-25', 13),
(25, '2023-10-25', 13),
(26, '2023-10-25', 13),
(27, '2023-10-25', 13),
(28, '2023-10-25', 13),
(29, '2023-10-25', 13),
(30, '2023-10-25', 13),
(31, '2023-10-25', 13),
(32, '2023-10-25', 13),
(33, '2023-10-25', 13),
(34, '2023-10-25', 13),
(35, '2023-10-25', 13),
(36, '2023-10-25', 13),
(37, '2023-10-25', 13),
(38, '2023-10-25', 13),
(39, '2023-10-25', 13),
(40, '2023-10-25', 13),
(41, '2023-10-25', 13),
(42, '2023-10-25', 13);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Cultivo`
--

CREATE TABLE `Cultivo` (
  `id` bigint UNSIGNED NOT NULL,
  `dataIni` date NOT NULL,
  `dataFim` date DEFAULT NULL,
  `numPlantas` int NOT NULL,
  `area` int UNSIGNED NOT NULL,
  `talhao_id` bigint UNSIGNED NOT NULL,
  `tipoCultivar_id` bigint UNSIGNED NOT NULL,
  `nome` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Cultivo`
--

INSERT INTO `Cultivo` (`id`, `dataIni`, `dataFim`, `numPlantas`, `area`, `talhao_id`, `tipoCultivar_id`, `nome`) VALUES
(9, '2024-01-16', NULL, 10, 10, 15, 1, NULL),
(10, '2024-01-10', NULL, 1000, 10, 15, 1, NULL),
(11, '2024-01-14', NULL, 10, 10, 15, 1, NULL),
(12, '2024-01-18', NULL, 1000, 10, 15, 1, NULL),
(13, '2024-01-03', NULL, 10, 10, 17, 1, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Decisao`
--

CREATE TABLE `Decisao` (
  `id` bigint UNSIGNED NOT NULL,
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `data_Deci` date NOT NULL,
  `produto_id` bigint UNSIGNED DEFAULT NULL,
  `dosagem` varchar(50) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `volume` int DEFAULT NULL,
  `amostragem_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Decisao`
--

INSERT INTO `Decisao` (`id`, `tipo`, `data_Deci`, `produto_id`, `dosagem`, `especie`, `quantidade`, `volume`, `amostragem_id`) VALUES
(1, '1', '2024-01-22', NULL, NULL, NULL, NULL, NULL, 2),
(2, 'Nada a Fazer', '2024-01-23', NULL, '', '', 0, 0, 4);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Foliolo`
--

CREATE TABLE `Foliolo` (
  `id` bigint UNSIGNED NOT NULL,
  `imgOrig` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `imgProc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `qntRajado` int DEFAULT NULL,
  `qntMacropilis` int DEFAULT NULL,
  `qntCalifornicus` int DEFAULT NULL,
  `amostragem_id` bigint UNSIGNED DEFAULT NULL,
  `imgOigin` blob,
  `imgProces` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Foliolo`
--

INSERT INTO `Foliolo` (`id`, `imgOrig`, `imgProc`, `qntRajado`, `qntMacropilis`, `qntCalifornicus`, `amostragem_id`, `imgOigin`, `imgProces`) VALUES
(1, NULL, NULL, 10, 10, 10, 2, 0x7b2273697a65223a3137313936332c226e616d65223a22436170747572612064652054656c61202831292e706e67222c2275726c223a222f66696c65732f7369676e65642f70726f642d627564692d6170702d6173736574732f6170705f61396464623165653333383434346636626131313763666231336533333138652f6174746163686d656e74732f63306431623463382d393937642d343838392d616430632d3830306233613535343764632e706e673f582d416d7a2d416c676f726974686d3d415753342d484d41432d53484132353626582d416d7a2d43726564656e7469616c3d6533343132356238373563323432663961363233323463343935386331343835253246323032343031313825324675732d656173742d312532467333253246617773345f7265717565737426582d416d7a2d446174653d3230323430313138543232343335335a26582d416d7a2d457870697265733d3336303026582d416d7a2d5369676e61747572653d3439653336663437336266643634343735326633316261306439396661326231393631336139633331666663373363383438646134336634396333646237656626582d416d7a2d5369676e6564486561646572733d686f7374222c22657874656e73696f6e223a22706e67222c226b6579223a226170705f61396464623165653333383434346636626131313763666231336533333138652f6174746163686d656e74732f63306431623463382d393937642d343838392d616430632d3830306233613535343764632e706e67227d, NULL),
(2, NULL, NULL, 20, 30, 10, 2, 0x73, NULL),
(4, NULL, NULL, 30, 10, 20, 4, 0x61, NULL),
(5, 'img', 'imgP', 10, 5, 2, 13, NULL, NULL),
(6, 'img', 'imgP', 10, 5, 2, 13, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Produto`
--

CREATE TABLE `Produto` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Produto`
--

INSERT INTO `Produto` (`id`, `nome`) VALUES
(3, '  Abamectin Prentis'),
(1, ' Abadin 72 EC '),
(4, ' Abamectin 72 EC Norto'),
(5, ' Abamex     '),
(6, ' Abamex Max'),
(7, ' Acarige'),
(8, ' Acarit EC'),
(9, ' Adver 240 S'),
(10, ' Azama'),
(11, ' Borea'),
(12, ' Clorfenapir Nortox'),
(13, ' DalNeem E'),
(14, ' Danimen 300 E'),
(15, ' Devamectin 18 E'),
(16, ' Epime'),
(17, ' Fujimite 50 S'),
(18, ' Kumulus DF'),
(19, ' Matrine; Biophora; Oxymatrine; '),
(20, ' Meothrin 30'),
(21, ' MilbekNoc'),
(22, ' Omite 720 E'),
(23, ' Ortus 50 S'),
(24, ' Pausat'),
(25, ' Pirat'),
(26, ' Potenza Sino'),
(27, ' Potenza Sinon Plus 36 E'),
(28, ' Propargite Fersol 720 E'),
(29, ' Sanmite E'),
(30, ' Sumirody 30'),
(31, ' Trigger 240 S'),
(32, ' Veromit'),
(2, 'Abamectin Nortox'),
(33, 'Vertimec 18 EC   Abamectin Prentis');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Propriedade`
--

CREATE TABLE `Propriedade` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ponto` point DEFAULT NULL,
  `distrito` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `agricultor_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Propriedade`
--

INSERT INTO `Propriedade` (`id`, `nome`, `ponto`, `distrito`, `municipio`, `agricultor_id`) VALUES
(42, 'Propriedade 2', 0x000000000101000000b9c667b27f0634c028f38fbe495f44c0, 'Distrito 01', 'Domingos Martins', 1),
(43, 'Propriedade 1', 0x000000000101000000b9c667b27f0634c028f38fbe495f44c0, 'Distrito 1', 'Santa Maria de Jetibá', 2),
(46, 'a', 0x000000000101000000b9c667b27f0634c028f38fbe495f44c0, 'a', 'Domingos Martins', 8);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Talhao`
--

CREATE TABLE `Talhao` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `area` int UNSIGNED DEFAULT NULL,
  `tipo` int DEFAULT NULL,
  `propriedade_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Talhao`
--

INSERT INTO `Talhao` (`id`, `nome`, `area`, `tipo`, `propriedade_id`) VALUES
(15, 'Estufa 1', 100, 1, 46),
(17, 'Estufa 2', 1000, 1, 46),
(23, 'Campo Aberto 2', 300, 2, 42),
(24, 'Estufa Sul 1', 150, 1, 43),
(26, 'Estufa Sul 1', 150, 1, 43),
(28, 'Estufa Sul 1', 150, 1, 43),
(30, 'Estufa Sul 1', 150, 1, 43),
(32, 'Estufa Sul 1', 150, 1, 43),
(33, 'Campo Aberto 2', 300, 2, 43),
(34, 'a', 10, 1, 46),
(35, 'asadsa', 2525, 1, 43);

-- --------------------------------------------------------

--
-- Estrutura para tabela `TipoCultivar`
--

CREATE TABLE `TipoCultivar` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TipoCultivar`
--

INSERT INTO `TipoCultivar` (`id`, `nome`) VALUES
(1, 'Moranguinho do Nordeste');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD UNIQUE KEY `cpf_2` (`cpf`),
  ADD UNIQUE KEY `cpf_3` (`cpf`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `telefone` (`telefone`);

--
-- Índices de tabela `Amostragem`
--
ALTER TABLE `Amostragem`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `cultivo_id` (`cultivo_id`);

--
-- Índices de tabela `Cultivo`
--
ALTER TABLE `Cultivo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `talhao_id` (`talhao_id`),
  ADD KEY `tipoCultivar_id` (`tipoCultivar_id`);

--
-- Índices de tabela `Decisao`
--
ALTER TABLE `Decisao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `produto_id` (`produto_id`),
  ADD KEY `amostragem_id` (`amostragem_id`);

--
-- Índices de tabela `Foliolo`
--
ALTER TABLE `Foliolo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `amostragem_id` (`amostragem_id`);

--
-- Índices de tabela `Produto`
--
ALTER TABLE `Produto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- Índices de tabela `Propriedade`
--
ALTER TABLE `Propriedade`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `agricultor_id` (`agricultor_id`);

--
-- Índices de tabela `Talhao`
--
ALTER TABLE `Talhao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `propriedade_id` (`propriedade_id`);

--
-- Índices de tabela `TipoCultivar`
--
ALTER TABLE `TipoCultivar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `Amostragem`
--
ALTER TABLE `Amostragem`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de tabela `Cultivo`
--
ALTER TABLE `Cultivo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `Decisao`
--
ALTER TABLE `Decisao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `Foliolo`
--
ALTER TABLE `Foliolo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `Produto`
--
ALTER TABLE `Produto`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de tabela `Propriedade`
--
ALTER TABLE `Propriedade`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de tabela `Talhao`
--
ALTER TABLE `Talhao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de tabela `TipoCultivar`
--
ALTER TABLE `TipoCultivar`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Amostragem`
--
ALTER TABLE `Amostragem`
  ADD CONSTRAINT `Amostragem_ibfk_1` FOREIGN KEY (`cultivo_id`) REFERENCES `Cultivo` (`id`);

--
-- Restrições para tabelas `Cultivo`
--
ALTER TABLE `Cultivo`
  ADD CONSTRAINT `Cultivo_ibfk_1` FOREIGN KEY (`talhao_id`) REFERENCES `Talhao` (`id`),
  ADD CONSTRAINT `Cultivo_ibfk_2` FOREIGN KEY (`tipoCultivar_id`) REFERENCES `TipoCultivar` (`id`);

--
-- Restrições para tabelas `Decisao`
--
ALTER TABLE `Decisao`
  ADD CONSTRAINT `Decisao_ibfk_1` FOREIGN KEY (`produto_id`) REFERENCES `Produto` (`id`),
  ADD CONSTRAINT `Decisao_ibfk_2` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`);

--
-- Restrições para tabelas `Foliolo`
--
ALTER TABLE `Foliolo`
  ADD CONSTRAINT `Foliolo_ibfk_1` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`);

--
-- Restrições para tabelas `Propriedade`
--
ALTER TABLE `Propriedade`
  ADD CONSTRAINT `Propriedade_ibfk_1` FOREIGN KEY (`agricultor_id`) REFERENCES `Agricultor` (`id`);

--
-- Restrições para tabelas `Talhao`
--
ALTER TABLE `Talhao`
  ADD CONSTRAINT `Talhao_ibfk_1` FOREIGN KEY (`propriedade_id`) REFERENCES `Propriedade` (`id`);
--
-- Banco de dados: `Teste`
--
CREATE DATABASE IF NOT EXISTS `Teste` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `Teste`;

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
(3, 'Acaro3'),
(4, 'Acaro1'),
(5, 'Acaro2'),
(6, 'Acaro3'),
(7, 'Acaro1'),
(8, 'Acaro2'),
(9, 'Acaro3');

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
(15, 'Agricultor15', 'agricultor15@email.com', '555-666-7777', 15, '555-666-777-88'),
(16, 'Agricultor1', 'agricultor1@email.com', '111-222-3333', 1, '111-222-333-44'),
(17, 'Agricultor2', 'agricultor2@email.com', '222-333-4444', 2, '222-333-444-55'),
(18, 'Agricultor3', 'agricultor3@email.com', '333-444-5555', 3, '333-444-555-66'),
(19, 'Agricultor4', 'agricultor4@email.com', '444-555-6666', 4, '444-555-666-77'),
(20, 'Agricultor5', 'agricultor5@email.com', '555-666-7777', 5, '555-666-777-88'),
(21, 'Agricultor6', 'agricultor6@email.com', '666-777-8888', 6, '666-777-888-99'),
(22, 'Agricultor7', 'agricultor7@email.com', '777-888-9999', 7, '777-888-999-00'),
(23, 'Agricultor8', 'agricultor8@email.com', '888-999-0000', 8, '888-999-000-11'),
(24, 'Agricultor9', 'agricultor9@email.com', '999-000-1111', 9, '999-000-111-22'),
(25, 'Agricultor10', 'agricultor10@email.com', '000-111-2222', 10, '000-111-222-33'),
(26, 'Agricultor11', 'agricultor11@email.com', '111-222-3333', 11, '111-222-333-44'),
(27, 'Agricultor12', 'agricultor12@email.com', '222-333-4444', 12, '222-333-444-55'),
(28, 'Agricultor13', 'agricultor13@email.com', '333-444-5555', 13, '333-444-555-66'),
(29, 'Agricultor14', 'agricultor14@email.com', '444-555-6666', 14, '444-555-666-77'),
(30, 'Agricultor15', 'agricultor15@email.com', '555-666-7777', 15, '555-666-777-88'),
(31, 'Agricultor1', 'agricultor1@email.com', '111-222-3333', 1, '111-222-333-44'),
(32, 'Agricultor2', 'agricultor2@email.com', '222-333-4444', 2, '222-333-444-55'),
(33, 'Agricultor3', 'agricultor3@email.com', '333-444-5555', 3, '333-444-555-66'),
(34, 'Agricultor4', 'agricultor4@email.com', '444-555-6666', 4, '444-555-666-77'),
(35, 'Agricultor5', 'agricultor5@email.com', '555-666-7777', 5, '555-666-777-88'),
(36, 'Agricultor6', 'agricultor6@email.com', '666-777-8888', 6, '666-777-888-99'),
(37, 'Agricultor7', 'agricultor7@email.com', '777-888-9999', 7, '777-888-999-00'),
(38, 'Agricultor8', 'agricultor8@email.com', '888-999-0000', 8, '888-999-000-11'),
(39, 'Agricultor9', 'agricultor9@email.com', '999-000-1111', 9, '999-000-111-22'),
(40, 'Agricultor10', 'agricultor10@email.com', '000-111-2222', 10, '000-111-222-33'),
(41, 'Agricultor11', 'agricultor11@email.com', '111-222-3333', 11, '111-222-333-44'),
(42, 'Agricultor12', 'agricultor12@email.com', '222-333-4444', 12, '222-333-444-55'),
(43, 'Agricultor13', 'agricultor13@email.com', '333-444-5555', 13, '333-444-555-66'),
(44, 'Agricultor14', 'agricultor14@email.com', '444-555-6666', 14, '444-555-666-77'),
(45, 'Agricultor15', 'agricultor15@email.com', '555-666-7777', 15, '555-666-777-88');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Amostra`
--

CREATE TABLE `Amostra` (
  `id` bigint UNSIGNED NOT NULL,
  `experimento_id` bigint UNSIGNED NOT NULL,
  `data_amostra` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(15, 'Bairro15', 15),
(16, 'Bairro1', 1),
(17, 'Bairro2', 2),
(18, 'Bairro3', 3),
(19, 'Bairro4', 4),
(20, 'Bairro5', 5),
(21, 'Bairro6', 6),
(22, 'Bairro7', 7),
(23, 'Bairro8', 8),
(24, 'Bairro9', 9),
(25, 'Bairro10', 10),
(26, 'Bairro11', 11),
(27, 'Bairro12', 12),
(28, 'Bairro13', 13),
(29, 'Bairro14', 14),
(30, 'Bairro15', 15),
(31, 'Bairro1', 1),
(32, 'Bairro2', 2),
(33, 'Bairro3', 3),
(34, 'Bairro4', 4),
(35, 'Bairro5', 5),
(36, 'Bairro6', 6),
(37, 'Bairro7', 7),
(38, 'Bairro8', 8),
(39, 'Bairro9', 9),
(40, 'Bairro10', 10),
(41, 'Bairro11', 11),
(42, 'Bairro12', 12),
(43, 'Bairro13', 13),
(44, 'Bairro14', 14),
(45, 'Bairro15', 15);

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
(15, 'Cidade15', 15),
(16, 'Cidade1', 1),
(17, 'Cidade2', 2),
(18, 'Cidade3', 3),
(19, 'Cidade4', 4),
(20, 'Cidade5', 5),
(21, 'Cidade6', 6),
(22, 'Cidade7', 7),
(23, 'Cidade8', 8),
(24, 'Cidade9', 9),
(25, 'Cidade10', 10),
(26, 'Cidade11', 11),
(27, 'Cidade12', 12),
(28, 'Cidade13', 13),
(29, 'Cidade14', 14),
(30, 'Cidade15', 15),
(31, 'Cidade1', 1),
(32, 'Cidade2', 2),
(33, 'Cidade3', 3),
(34, 'Cidade4', 4),
(35, 'Cidade5', 5),
(36, 'Cidade6', 6),
(37, 'Cidade7', 7),
(38, 'Cidade8', 8),
(39, 'Cidade9', 9),
(40, 'Cidade10', 10),
(41, 'Cidade11', 11),
(42, 'Cidade12', 12),
(43, 'Cidade13', 13),
(44, 'Cidade14', 14),
(45, 'Cidade15', 15);

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
(15, 15, 'Logradouro15', 'Rua15', 15),
(16, 1, 'Logradouro1', 'Rua1', 1),
(17, 2, 'Logradouro2', 'Rua2', 2),
(18, 3, 'Logradouro3', 'Rua3', 3),
(19, 4, 'Logradouro4', 'Rua4', 4),
(20, 5, 'Logradouro5', 'Rua5', 5),
(21, 6, 'Logradouro6', 'Rua6', 6),
(22, 7, 'Logradouro7', 'Rua7', 7),
(23, 8, 'Logradouro8', 'Rua8', 8),
(24, 9, 'Logradouro9', 'Rua9', 9),
(25, 10, 'Logradouro10', 'Rua10', 10),
(26, 11, 'Logradouro11', 'Rua11', 11),
(27, 12, 'Logradouro12', 'Rua12', 12),
(28, 13, 'Logradouro13', 'Rua13', 13),
(29, 14, 'Logradouro14', 'Rua14', 14),
(30, 15, 'Logradouro15', 'Rua15', 15),
(31, 1, 'Logradouro1', 'Rua1', 1),
(32, 2, 'Logradouro2', 'Rua2', 2),
(33, 3, 'Logradouro3', 'Rua3', 3),
(34, 4, 'Logradouro4', 'Rua4', 4),
(35, 5, 'Logradouro5', 'Rua5', 5),
(36, 6, 'Logradouro6', 'Rua6', 6),
(37, 7, 'Logradouro7', 'Rua7', 7),
(38, 8, 'Logradouro8', 'Rua8', 8),
(39, 9, 'Logradouro9', 'Rua9', 9),
(40, 10, 'Logradouro10', 'Rua10', 10),
(41, 11, 'Logradouro11', 'Rua11', 11),
(42, 12, 'Logradouro12', 'Rua12', 12),
(43, 13, 'Logradouro13', 'Rua13', 13),
(44, 14, 'Logradouro14', 'Rua14', 14),
(45, 15, 'Logradouro15', 'Rua15', 15);

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
(15, 'Estado15'),
(16, 'Estado1'),
(17, 'Estado2'),
(18, 'Estado3'),
(19, 'Estado4'),
(20, 'Estado5'),
(21, 'Estado6'),
(22, 'Estado7'),
(23, 'Estado8'),
(24, 'Estado9'),
(25, 'Estado10'),
(26, 'Estado11'),
(27, 'Estado12'),
(28, 'Estado13'),
(29, 'Estado14'),
(30, 'Estado15'),
(31, 'Estado1'),
(32, 'Estado2'),
(33, 'Estado3'),
(34, 'Estado4'),
(35, 'Estado5'),
(36, 'Estado6'),
(37, 'Estado7'),
(38, 'Estado8'),
(39, 'Estado9'),
(40, 'Estado10'),
(41, 'Estado11'),
(42, 'Estado12'),
(43, 'Estado13'),
(44, 'Estado14'),
(45, 'Estado15');

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
(15, 'Plantacao15', 1500, 15, 1900, 'Cultivar15', 'Local15', 15),
(16, 'Plantacao1', 100, 1, 500, 'Cultivar1', 'Local1', 1),
(17, 'Plantacao2', 200, 2, 600, 'Cultivar2', 'Local2', 2),
(18, 'Plantacao3', 300, 3, 700, 'Cultivar3', 'Local3', 3),
(19, 'Plantacao4', 400, 4, 800, 'Cultivar4', 'Local4', 4),
(20, 'Plantacao5', 500, 5, 900, 'Cultivar5', 'Local5', 5),
(21, 'Plantacao6', 600, 6, 1000, 'Cultivar6', 'Local6', 6),
(22, 'Plantacao7', 700, 7, 1100, 'Cultivar7', 'Local7', 7),
(23, 'Plantacao8', 800, 8, 1200, 'Cultivar8', 'Local8', 8),
(24, 'Plantacao9', 900, 9, 1300, 'Cultivar9', 'Local9', 9),
(25, 'Plantacao10', 1000, 10, 1400, 'Cultivar10', 'Local10', 10),
(26, 'Plantacao11', 1100, 11, 1500, 'Cultivar11', 'Local11', 11),
(27, 'Plantacao12', 1200, 12, 1600, 'Cultivar12', 'Local12', 12),
(28, 'Plantacao13', 1300, 13, 1700, 'Cultivar13', 'Local13', 13),
(29, 'Plantacao14', 1400, 14, 1800, 'Cultivar14', 'Local14', 14),
(30, 'Plantacao15', 1500, 15, 1900, 'Cultivar15', 'Local15', 15);

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
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `Agricultor`
--
ALTER TABLE `Agricultor`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `Amostra`
--
ALTER TABLE `Amostra`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `AmostraAcaro`
--
ALTER TABLE `AmostraAcaro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `Bairro`
--
ALTER TABLE `Bairro`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `Cidade`
--
ALTER TABLE `Cidade`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `Endereco`
--
ALTER TABLE `Endereco`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `Estado`
--
ALTER TABLE `Estado`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `Experimento`
--
ALTER TABLE `Experimento`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `Plantacao`
--
ALTER TABLE `Plantacao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
