-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `emp_tree`
--

DROP TABLE IF EXISTS `emp_tree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_tree` (
  `emp_name` varchar(10) DEFAULT NULL,
  `mgr_name` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_tree`
--

LOCK TABLES `emp_tree` WRITE;
/*!40000 ALTER TABLE `emp_tree` DISABLE KEYS */;
INSERT INTO `emp_tree` VALUES ('김사원','박대리'),('박대리','최부장');
/*!40000 ALTER TABLE `emp_tree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `j_buy`
--

DROP TABLE IF EXISTS `j_buy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `j_buy` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(10) DEFAULT NULL,
  `prod_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `j_buy`
--

LOCK TABLES `j_buy` WRITE;
/*!40000 ALTER TABLE `j_buy` DISABLE KEYS */;
INSERT INTO `j_buy` VALUES (1,'KIM','노트북'),(2,'KIM','노트북');
/*!40000 ALTER TABLE `j_buy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `j_member`
--

DROP TABLE IF EXISTS `j_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `j_member` (
  `user_id` varchar(10) NOT NULL,
  `user_name` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `j_member`
--

LOCK TABLES `j_member` WRITE;
/*!40000 ALTER TABLE `j_member` DISABLE KEYS */;
INSERT INTO `j_member` VALUES ('KIM','김철수'),('LEE','이영희');
/*!40000 ALTER TABLE `j_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_point`
--

DROP TABLE IF EXISTS `member_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_point` (
  `user_id` varchar(10) NOT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `point` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_point`
--

LOCK TABLES `member_point` WRITE;
/*!40000 ALTER TABLE `member_point` DISABLE KEYS */;
INSERT INTO `member_point` VALUES ('KIM','김철수',200);
/*!40000 ALTER TABLE `member_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_tbl`
--

DROP TABLE IF EXISTS `member_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_tbl` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `member_name` varchar(20) NOT NULL,
  `member_age` int DEFAULT NULL,
  `reg_date` datetime DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_tbl`
--

LOCK TABLES `member_tbl` WRITE;
/*!40000 ALTER TABLE `member_tbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_tbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `real_user`
--

DROP TABLE IF EXISTS `real_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `real_user` (
  `user_id` varchar(10) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_ssn` varchar(14) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `real_user`
--

LOCK TABLES `real_user` WRITE;
/*!40000 ALTER TABLE `real_user` DISABLE KEYS */;
INSERT INTO `real_user` VALUES ('KIM','김철수','950101-1234567',4000000),('LEE','이영희','980202-2345678',3500000);
/*!40000 ALTER TABLE `real_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_table` (
  `col1` int NOT NULL AUTO_INCREMENT,
  `col2` varchar(50) NOT NULL,
  `col3` datetime DEFAULT NULL,
  PRIMARY KEY (`col1`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-17 14:29:35
