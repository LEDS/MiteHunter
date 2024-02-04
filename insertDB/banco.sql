CREATE TABLE `Agricultor` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cpf` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `telefone` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Amostragem` (
  `id` bigint UNSIGNED NOT NULL,
  `data_Amos` date NOT NULL,
  `cultivo_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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


CREATE TABLE `Produto` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Propriedade` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ponto` point DEFAULT NULL,
  `distrito` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `agricultor_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Talhao` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `area` int UNSIGNED DEFAULT NULL,
  `tipo` int DEFAULT NULL,
  `propriedade_id` bigint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `TipoCultivar` (
  `id` bigint UNSIGNED NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `Agricultor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD UNIQUE KEY `cpf_2` (`cpf`),
  ADD UNIQUE KEY `cpf_3` (`cpf`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `telefone` (`telefone`);

ALTER TABLE `Amostragem`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `cultivo_id` (`cultivo_id`);

ALTER TABLE `Cultivo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `talhao_id` (`talhao_id`),
  ADD KEY `tipoCultivar_id` (`tipoCultivar_id`);

ALTER TABLE `Decisao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `produto_id` (`produto_id`),
  ADD KEY `amostragem_id` (`amostragem_id`);

ALTER TABLE `Foliolo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `amostragem_id` (`amostragem_id`);

ALTER TABLE `Produto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

ALTER TABLE `Propriedade`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `agricultor_id` (`agricultor_id`);

ALTER TABLE `Talhao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `propriedade_id` (`propriedade_id`);

ALTER TABLE `TipoCultivar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

ALTER TABLE `Agricultor`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

ALTER TABLE `Amostragem`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

ALTER TABLE `Cultivo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

ALTER TABLE `Decisao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `Foliolo`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

ALTER TABLE `Produto`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

ALTER TABLE `Propriedade`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

ALTER TABLE `Talhao`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

ALTER TABLE `TipoCultivar`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `Amostragem`
  ADD CONSTRAINT `Amostragem_ibfk_1` FOREIGN KEY (`cultivo_id`) REFERENCES `Cultivo` (`id`);

ALTER TABLE `Cultivo`
  ADD CONSTRAINT `Cultivo_ibfk_1` FOREIGN KEY (`talhao_id`) REFERENCES `Talhao` (`id`),
  ADD CONSTRAINT `Cultivo_ibfk_2` FOREIGN KEY (`tipoCultivar_id`) REFERENCES `TipoCultivar` (`id`);

ALTER TABLE `Decisao`
  ADD CONSTRAINT `Decisao_ibfk_1` FOREIGN KEY (`produto_id`) REFERENCES `Produto` (`id`),
  ADD CONSTRAINT `Decisao_ibfk_2` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`);

ALTER TABLE `Foliolo`
  ADD CONSTRAINT `Foliolo_ibfk_1` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`);

ALTER TABLE `Propriedade`
  ADD CONSTRAINT `Propriedade_ibfk_1` FOREIGN KEY (`agricultor_id`) REFERENCES `Agricultor` (`id`);

ALTER TABLE `Talhao`
  ADD CONSTRAINT `Talhao_ibfk_1` FOREIGN KEY (`propriedade_id`) REFERENCES `Propriedade` (`id`);
---------------
INSERT INTO `Agricultor` (`id`, `nome`, `cpf`, `email`, `telefone`) VALUES
(1, 'Bruno da Fonseca Chevitarese', '1889145091', 'bruno.chevitarese@estudante.ifes.edu.b', '27992795093'),
(2, 'Bruno', '18891480755', 'chevitarese.bruno@gmail.com', '27992795092'),
(8, 'Wilsiman', '5002055', 'will.evangelista@gmail.com', '2799279');

INSERT INTO `TipoCultivar` (`id`, `nome`) VALUES
(1, 'Moranguinho do Nordeste');

INSERT INTO `Propriedade` (`id`, `nome`, `ponto`, `distrito`, `municipio`, `agricultor_id`) VALUES
(42, 'Propriedade 2', 0x00000000010100000000000000000000000000000000000000, 'Distrito 01', 'Domingos Martins', 1),
(43, 'Propriedade 1', 0x00000000010100000000000000000000000000000000000000, 'Distrito 1', 'Santa Maria de Jetibá', 2),
(46, 'a', NULL, 'a', 'Domingos Martins', 8);

INSERT INTO `Talhao` (`id`, `nome`, `area`, `tipo`, `propriedade_id`) VALUES
(15, 'Estufa 1', 100, 1, 46),
(17, 'Estufa 0', 1000, 1, 46),
(22, 'Estufa Sul 1', 150, 1, 43),
(23, 'Campo Aberto 2', 300, 2, 42),
(24, 'Estufa Sul 1', 150, 1, 43),
(25, 'Campo Aberto 2', 300, 2, 43),
(26, 'Estufa Sul 1', 150, 1, 43),
(27, 'Campo Aberto 2', 300, 2, 43),
(28, 'Estufa Sul 1', 150, 1, 43),
(29, 'Campo Aberto 2', 300, 2, 43),
(30, 'Estufa Sul 1', 150, 1, 43),
(31, 'Campo Aberto 2', 300, 2, 43),
(32, 'Estufa Sul 1', 150, 1, 43),
(33, 'Campo Aberto 2', 300, 2, 43),
(34, 'a', 10, 1, 46);

INSERT INTO `Cultivo` (`id`, `dataIni`, `dataFim`, `numPlantas`, `area`, `talhao_id`, `tipoCultivar_id`, `nome`) VALUES
(9, '2024-01-16', NULL, 10, 10, 15, 1, NULL),
(10, '2024-01-10', NULL, 1000, 10, 15, 1, NULL),
(11, '2024-01-14', NULL, 10, 10, 15, 1, NULL),
(12, '2024-01-18', NULL, 1000, 10, 15, 1, NULL),
(13, '2024-01-03', NULL, 10, 10, 17, 1, NULL);

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
(12, '2024-01-11', 9);

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

INSERT INTO `Decisao` (`id`, `tipo`, `data_Deci`, `produto_id`, `dosagem`, `especie`, `quantidade`, `volume`, `amostragem_id`) VALUES
(1, '1', '2024-01-22', NULL, NULL, NULL, NULL, NULL, 2);

INSERT INTO `Foliolo` (`id`, `imgOrig`, `imgProc`, `qntRajado`, `qntMacropilis`, `qntCalifornicus`, `amostragem_id`, `imgOigin`, `imgProces`) VALUES
(1, NULL, NULL, 10, 10, 10, 2, 0x7b2273697a65223a3137313936332c226e616d65223a22436170747572612064652054656c61202831292e706e67222c2275726c223a222f66696c65732f7369676e65642f70726f642d627564692d6170702d6173736574732f6170705f61396464623165653333383434346636626131313763666231336533333138652f6174746163686d656e74732f63306431623463382d393937642d343838392d616430632d3830306233613535343764632e706e673f582d416d7a2d416c676f726974686d3d415753342d484d41432d53484132353626582d416d7a2d43726564656e7469616c3d6533343132356238373563323432663961363233323463343935386331343835253246323032343031313825324675732d656173742d312532467333253246617773345f7265717565737426582d416d7a2d446174653d3230323430313138543232343335335a26582d416d7a2d457870697265733d3336303026582d416d7a2d5369676e61747572653d3439653336663437336266643634343735326633316261306439396661326231393631336139633331666663373363383438646134336634396333646237656626582d416d7a2d5369676e6564486561646572733d686f7374222c22657874656e73696f6e223a22706e67222c226b6579223a226170705f61396464623165653333383434346636626131313763666231336533333138652f6174746163686d656e74732f63306431623463382d393937642d343838392d616430632d3830306233613535343764632e706e67227d, NULL),
(2, NULL, NULL, 20, 30, 10, 2, 0x73, NULL),
(4, NULL, NULL, 30, 10, 20, 4, 0x61, NULL);