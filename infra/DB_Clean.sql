-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: MiteHunter
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Agricultor`
--

DROP TABLE IF EXISTS `Agricultor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Agricultor` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cpf` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `telefone` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `cpf_2` (`cpf`),
  UNIQUE KEY `cpf_3` (`cpf`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telefone` (`telefone`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Agricultor`
--

LOCK TABLES `Agricultor` WRITE;
/*!40000 ALTER TABLE `Agricultor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Agricultor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Amostragem`
--

DROP TABLE IF EXISTS `Amostragem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Amostragem` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `data_Amos` date NOT NULL,
  `cultivo_id` bigint unsigned NOT NULL,
  `classificacao_final` text,-- Host: localhost    Database: MiteHunter

  UNIQUE KEY `id` (`id`),
  KEY `cultivo_id` (`cultivo_id`),
  CONSTRAINT `Amostragem_ibfk_1` FOREIGN KEY (`cultivo_id`) REFERENCES `Cultivo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Amostragem`
--

LOCK TABLES `Amostragem` WRITE;
/*!40000 ALTER TABLE `Amostragem` DISABLE KEYS */;
/*!40000 ALTER TABLE `Amostragem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BudibaseIpCatch`
--

DROP TABLE IF EXISTS `BudibaseIpCatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BudibaseIpCatch` (
  `ip` varchar(15) NOT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BudibaseIpCatch`
--

LOCK TABLES `BudibaseIpCatch` WRITE;
/*!40000 ALTER TABLE `BudibaseIpCatch` DISABLE KEYS */;
INSERT INTO `BudibaseIpCatch` VALUES ('172.19.105.29');
/*!40000 ALTER TABLE `BudibaseIpCatch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cultivo`
--

DROP TABLE IF EXISTS `Cultivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cultivo` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `dataIni` date NOT NULL,
  `dataFim` date DEFAULT NULL,
  `numPlantas` int NOT NULL,
  `area` int unsigned NOT NULL,
  `talhao_id` bigint unsigned NOT NULL,
  `tipoCultivar_id` bigint unsigned NOT NULL,
  `nome` varchar(200) DEFAULT NULL,
  `forma` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `talhao_id` (`talhao_id`),
  KEY `tipoCultivar_id` (`tipoCultivar_id`),
  CONSTRAINT `Cultivo_ibfk_1` FOREIGN KEY (`talhao_id`) REFERENCES `Talhao` (`id`),
  CONSTRAINT `Cultivo_ibfk_2` FOREIGN KEY (`tipoCultivar_id`) REFERENCES `TipoCultivar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cultivo`
--

LOCK TABLES `Cultivo` WRITE;
/*!40000 ALTER TABLE `Cultivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cultivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Decisao`
--

DROP TABLE IF EXISTS `Decisao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Decisao` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `data_Deci` date NOT NULL,
  `produto_id` bigint unsigned DEFAULT NULL,
  `dosagem` varchar(50) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `volume` int DEFAULT NULL,
  `amostragem_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `produto_id` (`produto_id`),
  KEY `amostragem_id` (`amostragem_id`),
  CONSTRAINT `Decisao_ibfk_1` FOREIGN KEY (`produto_id`) REFERENCES `Produto` (`id`),
  CONSTRAINT `Decisao_ibfk_2` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Decisao`
--

LOCK TABLES `Decisao` WRITE;
/*!40000 ALTER TABLE `Decisao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Decisao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Foliolo`
--

DROP TABLE IF EXISTS `Foliolo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Foliolo` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `imgOrig` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `imgProc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `qntRajado` int DEFAULT NULL,
  `qntMacropilis` int DEFAULT NULL,
  `qntCalifornicus` int DEFAULT NULL,
  `amostragem_id` bigint unsigned DEFAULT NULL,
  `imgOigin` blob,
  `imgProces` blob,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `amostragem_id` (`amostragem_id`),
  CONSTRAINT `Foliolo_ibfk_1` FOREIGN KEY (`amostragem_id`) REFERENCES `Amostragem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=875 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Foliolo`
--

LOCK TABLES `Foliolo` WRITE;
/*!40000 ALTER TABLE `Foliolo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Foliolo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `PROPRIEDADE_VIEW`
--

DROP TABLE IF EXISTS `PROPRIEDADE_VIEW`;
/*!50001 DROP VIEW IF EXISTS `PROPRIEDADE_VIEW`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `PROPRIEDADE_VIEW` AS SELECT 
 1 AS `id`,
 1 AS `nome`,
 1 AS `latitude`,
 1 AS `longitude`,
 1 AS `distrito`,
 1 AS `municipio`,
 1 AS `nomeagri`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Produto`
--

DROP TABLE IF EXISTS `Produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Produto` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compat_macropilis` int DEFAULT NULL,
  `compat_californicus` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Produto`
--

LOCK TABLES `Produto` WRITE;
/*!40000 ALTER TABLE `Produto` DISABLE KEYS */;
INSERT INTO `Produto` VALUES (1,' Abadin 72 EC ',NULL,NULL),(2,'Abamectin Nortox',NULL,NULL),(3,'  Abamectin Prentis',2,1),(4,' Abamectin 72 EC Norto',NULL,NULL),(5,' Abamex     ',NULL,NULL),(6,' Abamex Max',NULL,NULL),(7,' Acarige',NULL,NULL),(8,' Acarit EC',NULL,NULL),(9,' Adver 240 S',NULL,NULL),(10,' Azamax',NULL,NULL),(11,' Borea',NULL,NULL),(12,' Clorfenapir Nortox',NULL,NULL),(13,' DalNeem E',NULL,NULL),(14,' Danimen 300 E',NULL,NULL),(15,' Devamectin 18 E',NULL,NULL),(16,' Epime',NULL,NULL),(17,' Fujimite 50 S',NULL,NULL),(18,' Kumulus DF',NULL,NULL),(19,' Matrine; Biophora; Oxymatrine; ',NULL,NULL),(20,' Meothrin 30',NULL,NULL),(21,' MilbekNoc',NULL,NULL),(22,' Omite 720 E',NULL,NULL),(23,' Ortus 50 S',NULL,NULL),(24,' Pausat',NULL,NULL),(25,' Pirat',NULL,NULL),(26,' Potenza Sino',NULL,NULL),(27,' Potenza Sinon Plus 36 E',NULL,NULL),(28,' Propargite Fersol 720 E',NULL,NULL),(29,' Sanmite E',NULL,NULL),(30,' Sumirody 30',NULL,NULL),(31,' Trigger 240 S',NULL,NULL),(32,' Veromit',NULL,NULL),(33,'Vertimec 18 EC   Abamectin Prentis',NULL,NULL);
/*!40000 ALTER TABLE `Produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Propriedade`
--

DROP TABLE IF EXISTS `Propriedade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Propriedade` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ponto` point DEFAULT NULL,
  `distrito` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `agricultor_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `agricultor_id` (`agricultor_id`),
  CONSTRAINT `Propriedade_ibfk_1` FOREIGN KEY (`agricultor_id`) REFERENCES `Agricultor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Propriedade`
--

LOCK TABLES `Propriedade` WRITE;
/*!40000 ALTER TABLE `Propriedade` DISABLE KEYS */;
/*!40000 ALTER TABLE `Propriedade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Talhao`
--

DROP TABLE IF EXISTS `Talhao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Talhao` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `area` int unsigned DEFAULT NULL,
  `propriedade_id` bigint unsigned NOT NULL,
  `area_livre` float(8,2) DEFAULT NULL,
  `area_usada` float(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `propriedade_id` (`propriedade_id`),
  CONSTRAINT `Talhao_ibfk_1` FOREIGN KEY (`propriedade_id`) REFERENCES `Propriedade` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Talhao`
--

LOCK TABLES `Talhao` WRITE;
/*!40000 ALTER TABLE `Talhao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Talhao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoCultivar`
--

DROP TABLE IF EXISTS `TipoCultivar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TipoCultivar` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoCultivar`
--

LOCK TABLES `TipoCultivar` WRITE;
/*!40000 ALTER TABLE `TipoCultivar` DISABLE KEYS */;
INSERT INTO `TipoCultivar` VALUES (11,'Cabrillo'),(12,'San Andreas'),(13,'Albion'),(14,'Monterey'),(15,'Portola'),(16,'Aromas');
/*!40000 ALTER TABLE `TipoCultivar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `PROPRIEDADE_VIEW`
--

/*!50001 DROP VIEW IF EXISTS `PROPRIEDADE_VIEW`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `PROPRIEDADE_VIEW` AS select `Propriedade`.`id` AS `id`,`Propriedade`.`nome` AS `nome`,st_x(`Propriedade`.`ponto`) AS `latitude`,st_y(`Propriedade`.`ponto`) AS `longitude`,`Propriedade`.`distrito` AS `distrito`,`Propriedade`.`municipio` AS `municipio`,`Agricultor`.`nome` AS `nomeagri` from (`Propriedade` join `Agricultor` on((`Propriedade`.`agricultor_id` = `Agricultor`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-29 18:48:17
