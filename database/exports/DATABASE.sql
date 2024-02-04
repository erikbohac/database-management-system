-- Author: Erik Boháč
-- Project: Database Manager
-- Contacts: bohac2@spsejecna.cz

START TRANSACTION;
CREATE DATABASE  IF NOT EXISTS `auctions` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `auctions`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: auctions
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `auction`
--

DROP TABLE IF EXISTS `auction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auction` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `START_DATE` datetime NOT NULL,
  `END_DATE` datetime NOT NULL,
  `AUCTION_TYPE` enum('PUBLIC','ANONYMOUS') NOT NULL,
  `AUCTION_DESCRIPTION` varchar(255) NOT NULL,
  `ITEM_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `ITEM_ID` (`ITEM_ID`),
  CONSTRAINT `auction_ibfk_1` FOREIGN KEY (`ITEM_ID`) REFERENCES `item` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auction`
--

LOCK TABLES `auction` WRITE;
/*!40000 ALTER TABLE `auction` DISABLE KEYS */;
INSERT INTO `auction` VALUES (1,'2024-02-11 10:00:00','2024-02-12 18:00:00','PUBLIC','Antique Silverware Auction',1),(2,'2024-02-12 12:00:00','2024-02-15 20:00:00','ANONYMOUS','Asian Art Auction',2),(3,'2024-02-13 09:00:00','2024-02-17 17:00:00','PUBLIC','Fine China Auction',3),(4,'2024-02-14 11:00:00','2024-02-20 19:00:00','PUBLIC','Ancient Artifacts Auction',4),(5,'2024-02-15 10:00:00','2024-02-22 18:00:00','PUBLIC','Silver Teapot Auction',5),(6,'2024-02-16 12:00:00','2024-02-25 20:00:00','ANONYMOUS','Porcelain Vase Auction',6);
/*!40000 ALTER TABLE `auction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `auction_winners`
--

DROP TABLE IF EXISTS `auction_winners`;
/*!50001 DROP VIEW IF EXISTS `auction_winners`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `auction_winners` AS SELECT 
 1 AS `SURNAME`,
 1 AS `LAST_NAME`,
 1 AS `AMOUNT`,
 1 AS `AUCTION_DESCRIPTION`,
 1 AS `ITEM_NAME`,
 1 AS `ITEM_DESCRIPTION`,
 1 AS `OFFER_DATE`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `bidder`
--

DROP TABLE IF EXISTS `bidder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bidder` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SURNAME` varchar(255) NOT NULL,
  `LAST_NAME` varchar(255) NOT NULL,
  `ADDRESS` varchar(255) NOT NULL,
  `POST_CODE` int NOT NULL,
  `PHONE_NUMBER` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `PHONE_NUMBER` (`PHONE_NUMBER`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bidder`
--

LOCK TABLES `bidder` WRITE;
/*!40000 ALTER TABLE `bidder` DISABLE KEYS */;
INSERT INTO `bidder` VALUES (1,'Smith','John','123 Main St',12345,'555-1234'),(2,'Johnson','Emily','456 Elm St',54321,'555-5678'),(3,'Williams','Michael','789 Oak St',67890,'555-9012'),(4,'Brown','Jessica','321 Pine St',98765,'555-3456'),(5,'Taylor','Matthew','567 Cherry St',13579,'555-6789'),(6,'Anderson','Sophia','890 Walnut St',24680,'555-2345');
/*!40000 ALTER TABLE `bidder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ITEM_NAME` varchar(255) NOT NULL,
  `ITEM_DESCRIPTION` varchar(255) NOT NULL,
  `START_PRICE` float NOT NULL,
  `OWNER_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `OWNER_ID` (`OWNER_ID`),
  CONSTRAINT `item_ibfk_1` FOREIGN KEY (`OWNER_ID`) REFERENCES `owner` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Antique Chair','Beautiful antique chair made of oak.',500.5,1),(2,'Oil Painting','Original oil painting by a local artist.',750.9,2),(3,'Vintage Record Player','Fully functional vintage record player.',300.7,3),(4,'Rare Book Collection','Collection of rare and valuable books.',1000.9,4),(5,'Silver Teapot','Vintage silver teapot with intricate designs.',200.9,1),(6,'Porcelain Vase','Elegant porcelain vase from the Ming Dynasty.',1500.99,2);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer`
--

DROP TABLE IF EXISTS `offer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offer` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `AMOUNT` float NOT NULL,
  `OFFER_DATE` datetime NOT NULL,
  `AUCTION_ID` int NOT NULL,
  `BIDDER_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `AUCTION_ID` (`AUCTION_ID`),
  KEY `BIDDER_ID` (`BIDDER_ID`),
  CONSTRAINT `offer_ibfk_1` FOREIGN KEY (`AUCTION_ID`) REFERENCES `auction` (`ID`),
  CONSTRAINT `offer_ibfk_2` FOREIGN KEY (`BIDDER_ID`) REFERENCES `bidder` (`ID`),
  CONSTRAINT `offer_chk_1` CHECK ((`AMOUNT` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer`
--

LOCK TABLES `offer` WRITE;
/*!40000 ALTER TABLE `offer` DISABLE KEYS */;
INSERT INTO `offer` VALUES (1,1000,'2024-02-11 11:30:00',1,1),(2,1200,'2024-02-11 11:35:00',1,2),(3,1300,'2024-02-11 11:40:00',1,1),(4,1500,'2024-02-11 14:50:00',1,2),(5,1500,'2024-02-12 14:45:00',2,2),(6,1650,'2024-02-12 14:50:00',2,3),(7,800,'2024-02-13 10:20:00',3,3),(8,900,'2024-02-13 14:50:00',3,4),(9,2000,'2024-02-14 13:10:00',4,5),(10,2200,'2024-02-14 13:30:00',4,4),(11,1700,'2024-02-15 11:31:00',5,6),(12,1800,'2024-02-16 14:50:00',6,5);
/*!40000 ALTER TABLE `offer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `offer_counts_by_bidder`
--

DROP TABLE IF EXISTS `offer_counts_by_bidder`;
/*!50001 DROP VIEW IF EXISTS `offer_counts_by_bidder`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `offer_counts_by_bidder` AS SELECT 
 1 AS `AUCTION_DESCRIPTION`,
 1 AS `AUCTION_TYPE`,
 1 AS `SURNAME`,
 1 AS `LAST_NAME`,
 1 AS `OFFERS_COUNT`,
 1 AS `ITEM_NAME`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owner` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SURNAME` varchar(255) NOT NULL,
  `LAST_NAME` varchar(255) NOT NULL,
  `ADDRESS` varchar(255) NOT NULL,
  `POST_CODE` int NOT NULL,
  `PHONE_NUMBER` varchar(255) NOT NULL,
  `IS_VERIFIED` tinyint(1) NOT NULL DEFAULT '0',
  `EMAIL` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `PHONE_NUMBER` (`PHONE_NUMBER`),
  UNIQUE KEY `EMAIL` (`EMAIL`),
  CONSTRAINT `owner_chk_1` CHECK ((`EMAIL` like _utf8mb4'%@%.%'))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (1,'Anderson','David','111 Maple St',13579,'555-1111',1,'david@example.com'),(2,'Martinez','Maria','222 Birch St',24680,'555-2222',0,'maria@example.com'),(3,'Lee','Christopher','333 Cedar St',35791,'555-3333',1,'chris@example.com'),(4,'Garcia','Samantha','444 Walnut St',46802,'555-4444',1,'samantha@example.com');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `winning_offer`
--

DROP TABLE IF EXISTS `winning_offer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `winning_offer` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `OFFER_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `OFFER_ID` (`OFFER_ID`),
  CONSTRAINT `winning_offer_ibfk_1` FOREIGN KEY (`OFFER_ID`) REFERENCES `offer` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `winning_offer`
--

LOCK TABLES `winning_offer` WRITE;
/*!40000 ALTER TABLE `winning_offer` DISABLE KEYS */;
INSERT INTO `winning_offer` VALUES (1,4),(2,6),(3,8),(4,10),(5,11),(6,12);
/*!40000 ALTER TABLE `winning_offer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `auction_winners`
--

/*!50001 DROP VIEW IF EXISTS `auction_winners`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `auction_winners` AS select `bidder`.`SURNAME` AS `SURNAME`,`bidder`.`LAST_NAME` AS `LAST_NAME`,`offer`.`AMOUNT` AS `AMOUNT`,`auction`.`AUCTION_DESCRIPTION` AS `AUCTION_DESCRIPTION`,`item`.`ITEM_NAME` AS `ITEM_NAME`,`item`.`ITEM_DESCRIPTION` AS `ITEM_DESCRIPTION`,`offer`.`OFFER_DATE` AS `OFFER_DATE` from ((((`offer` join `winning_offer` on((`winning_offer`.`OFFER_ID` = `offer`.`ID`))) join `auction` on((`auction`.`ID` = `offer`.`AUCTION_ID`))) join `item` on((`item`.`ID` = `auction`.`ITEM_ID`))) join `bidder` on((`bidder`.`ID` = `offer`.`BIDDER_ID`))) where `offer`.`ID` in (select `winning_offer`.`OFFER_ID` from `winning_offer`) order by `bidder`.`SURNAME`,`bidder`.`LAST_NAME` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `offer_counts_by_bidder`
--

/*!50001 DROP VIEW IF EXISTS `offer_counts_by_bidder`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `offer_counts_by_bidder` AS select `auction`.`AUCTION_DESCRIPTION` AS `AUCTION_DESCRIPTION`,`auction`.`AUCTION_TYPE` AS `AUCTION_TYPE`,`bidder`.`SURNAME` AS `SURNAME`,`bidder`.`LAST_NAME` AS `LAST_NAME`,count(`offer`.`BIDDER_ID`) AS `OFFERS_COUNT`,`item`.`ITEM_NAME` AS `ITEM_NAME` from (((`offer` join `auction` on((`auction`.`ID` = `offer`.`AUCTION_ID`))) join `item` on((`item`.`ID` = `auction`.`ITEM_ID`))) join `bidder` on((`bidder`.`ID` = `offer`.`BIDDER_ID`))) group by `bidder`.`SURNAME`,`bidder`.`LAST_NAME`,`auction`.`AUCTION_DESCRIPTION`,`auction`.`AUCTION_TYPE`,`item`.`ITEM_NAME` */;
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
COMMIT;
-- Dump completed on 2024-02-04 19:57:26
