-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Tempo de geração: 28/03/2024 às 11:20
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

-- --------------------------------------------------------

--
-- Estrutura para tabela `Amostragem`
--

CREATE TABLE `Amostragem` (
  `id` bigint UNSIGNED NOT NULL,
  `data_Amos` date NOT NULL,
  `cultivo_id` bigint UNSIGNED NOT NULL,
  `classificacao_final` text,
  `media_rajado_foliolo` float(8,2) DEFAULT NULL,
  `acao_sugerida` text,
  `qtd_total` smallint DEFAULT NULL,
  `seis_a_nove` float(8,2) DEFAULT NULL,
  `mais_dez` float(8,2) DEFAULT NULL,
  `um_a_cinco` float(8,2) DEFAULT NULL,
  `sem_predador_rajado` float(8,2) DEFAULT NULL,
  `predador_sem_rajado` float(8,2) DEFAULT NULL,
  `com_predador_rajado` float(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `nome` varchar(200) DEFAULT NULL,
  `forma` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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

-- --------------------------------------------------------

--
-- Estrutura para tabela `Produto`
--

CREATE TABLE `Produto` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compat_macropilis` int DEFAULT NULL,
  `compat_californicus` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Produto`
--

INSERT INTO `Produto` (`id`, `nome`, `compat_macropilis`, `compat_californicus`) VALUES
(1, ' Abadin 72 EC ', NULL, NULL),
(2, 'Abamectin Nortox', NULL, NULL),
(3, '  Abamectin Prentis', 2, 1),
(4, ' Abamectin 72 EC Norto', NULL, NULL),
(5, ' Abamex     ', NULL, NULL),
(6, ' Abamex Max', NULL, NULL),
(7, ' Acarige', NULL, NULL),
(8, ' Acarit EC', NULL, NULL),
(9, ' Adver 240 S', NULL, NULL),
(10, ' Azamax', NULL, NULL),
(11, ' Borea', NULL, NULL),
(12, ' Clorfenapir Nortox', NULL, NULL),
(13, ' DalNeem E', NULL, NULL),
(14, ' Danimen 300 E', NULL, NULL),
(15, ' Devamectin 18 E', NULL, NULL),
(16, ' Epime', NULL, NULL),
(17, ' Fujimite 50 S', NULL, NULL),
(18, ' Kumulus DF', NULL, NULL),
(19, ' Matrine; Biophora; Oxymatrine; ', NULL, NULL),
(20, ' Meothrin 30', NULL, NULL),
(21, ' MilbekNoc', NULL, NULL),
(22, ' Omite 720 E', NULL, NULL),
(23, ' Ortus 50 S', NULL, NULL),
(24, ' Pausat', NULL, NULL),
(25, ' Pirat', NULL, NULL),
(26, ' Potenza Sino', NULL, NULL),
(27, ' Potenza Sinon Plus 36 E', NULL, NULL),
(28, ' Propargite Fersol 720 E', NULL, NULL),
(29, ' Sanmite E', NULL, NULL),
(30, ' Sumirody 30', NULL, NULL),
(31, ' Trigger 240 S', NULL, NULL),
(32, ' Veromit', NULL, NULL),
(33, 'Vertimec 18 EC   Abamectin Prentis', NULL, NULL);

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

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `PROPRIEDADE_VIEW`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `PROPRIEDADE_VIEW` (
`distrito` varchar(100)
,`id` bigint unsigned
,`latitude` double
,`longitude` double
,`municipio` varchar(100)
,`nome` varchar(255)
,`nomeagri` varchar(255)
);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Talhao`
--

CREATE TABLE `Talhao` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `area` int UNSIGNED DEFAULT NULL,
  `propriedade_id` bigint UNSIGNED NOT NULL,
  `area_livre` float(8,2) DEFAULT NULL,
  `area_usada` float(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `TipoCultivar`
--

CREATE TABLE `TipoCultivar` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para view `PROPRIEDADE_VIEW`
--
DROP TABLE IF EXISTS `PROPRIEDADE_VIEW`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `PROPRIEDADE_VIEW`  AS SELECT `Propriedade`.`id` AS `id`, `Propriedade`.`nome` AS `nome`, st_x(`Propriedade`.`ponto`) AS `latitude`, st_y(`Propriedade`.`ponto`) AS `longitude`, `Propriedade`.`distrito` AS `distrito`, `Propriedade`.`municipio` AS `municipio`, `Agricultor`.`nome` AS `nomeagri` FROM (`Propriedade` join `Agricultor` on((`Propriedade`.`agricultor_id` = `Agricultor`.`id`))) ;

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
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de tabela `Amostragem`
--
ALTER TABLE `Amostragem`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=147;

--
-- AUTO_INCREMENT de tabela `Cultivo`
--
ALTER TABLE `Cultivo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de tabela `Decisao`
--
ALTER TABLE `Decisao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de tabela `Foliolo`
--
ALTER TABLE `Foliolo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=875;

--
-- AUTO_INCREMENT de tabela `Produto`
--
ALTER TABLE `Produto`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de tabela `Propriedade`
--
ALTER TABLE `Propriedade`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de tabela `Talhao`
--
ALTER TABLE `Talhao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de tabela `TipoCultivar`
--
ALTER TABLE `TipoCultivar`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
