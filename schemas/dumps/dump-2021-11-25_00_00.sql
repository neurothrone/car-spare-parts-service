CREATE DATABASE  IF NOT EXISTS `car-spare-parts-db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `car-spare-parts-db`;
-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: car-spare-parts-db
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `car_details`
--

DROP TABLE IF EXISTS `car_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_details` (
  `car_detail_id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(45) NOT NULL,
  `model` varchar(45) NOT NULL,
  `year` int NOT NULL,
  PRIMARY KEY (`car_detail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_details`
--

LOCK TABLES `car_details` WRITE;
/*!40000 ALTER TABLE `car_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_details_has_products`
--

DROP TABLE IF EXISTS `car_details_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_details_has_products` (
  `car_detail_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`car_detail_id`,`product_id`),
  KEY `fk_car_details_has_products_products1_idx` (`product_id`),
  KEY `fk_car_details_has_products_car_details1_idx` (`car_detail_id`),
  CONSTRAINT `fk_car_details_has_products_car_details1` FOREIGN KEY (`car_detail_id`) REFERENCES `car_details` (`car_detail_id`),
  CONSTRAINT `fk_car_details_has_products_products1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_details_has_products`
--

LOCK TABLES `car_details_has_products` WRITE;
/*!40000 ALTER TABLE `car_details_has_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_details_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `reg_no` varchar(7) NOT NULL,
  `color` varchar(45) DEFAULT NULL,
  `car_detail_id` int NOT NULL,
  PRIMARY KEY (`reg_no`,`car_detail_id`),
  KEY `fk_cars_car_details_idx` (`car_detail_id`),
  CONSTRAINT `fk_cars_car_details` FOREIGN KEY (`car_detail_id`) REFERENCES `car_details` (`car_detail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_persons`
--

DROP TABLE IF EXISTS `contact_persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_persons` (
  `contact_person_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`contact_person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_persons`
--

LOCK TABLES `contact_persons` WRITE;
/*!40000 ALTER TABLE `contact_persons` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corporate_customers`
--

DROP TABLE IF EXISTS `corporate_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corporate_customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_type` char(1) NOT NULL,
  `organization_number` int NOT NULL,
  `organization_name` varchar(45) NOT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `organization_number_UNIQUE` (`organization_number`),
  KEY `fk_corporate_customers_customers1_idx` (`customer_id`,`customer_type`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_corporate_customers_customers1` FOREIGN KEY (`customer_id`, `customer_type`) REFERENCES `customers` (`customer_id`, `customer_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corporate_customers`
--

LOCK TABLES `corporate_customers` WRITE;
/*!40000 ALTER TABLE `corporate_customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `corporate_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_type` char(1) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(125) NOT NULL,
  `zip_code` varchar(7) NOT NULL,
  `city` varchar(50) NOT NULL,
  `reg_no` varchar(7) NOT NULL,
  `order_id` int NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`customer_id`,`customer_type`),
  KEY `fk_customers_cars1_idx` (`reg_no`),
  KEY `fk_customers_orders1_idx` (`order_id`),
  KEY `fk_customers_employees1_idx` (`employee_id`),
  CONSTRAINT `fk_customers_cars1` FOREIGN KEY (`reg_no`) REFERENCES `cars` (`reg_no`),
  CONSTRAINT `fk_customers_employees1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `fk_customers_orders1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `store_id` int NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `fk_employees_stores2_idx` (`store_id`),
  CONSTRAINT `fk_employees_stores2` FOREIGN KEY (`store_id`) REFERENCES `stores` (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `manufacturer_id` int NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `head_office_phone` varchar(25) NOT NULL,
  `head_office_address` varchar(100) NOT NULL,
  `contact_person_id` int NOT NULL,
  PRIMARY KEY (`manufacturer_id`),
  KEY `fk_manufacturers_contact_persons1_idx` (`contact_person_id`),
  CONSTRAINT `fk_manufacturers_contact_persons1` FOREIGN KEY (`contact_person_id`) REFERENCES `contact_persons` (`contact_person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `online_stores`
--

DROP TABLE IF EXISTS `online_stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `online_stores` (
  `store_id` int NOT NULL AUTO_INCREMENT,
  `store_type` char(1) NOT NULL DEFAULT 'o',
  PRIMARY KEY (`store_id`),
  KEY `fk_online_stores_stores1` (`store_id`,`store_type`),
  CONSTRAINT `fk_online_stores_stores1` FOREIGN KEY (`store_id`, `store_type`) REFERENCES `stores` (`store_id`, `store_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `online_stores`
--

LOCK TABLES `online_stores` WRITE;
/*!40000 ALTER TABLE `online_stores` DISABLE KEYS */;
/*!40000 ALTER TABLE `online_stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `ordered_date` timestamp NOT NULL,
  `shipped_date` timestamp NULL DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_has_products`
--

DROP TABLE IF EXISTS `orders_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_has_products` (
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity_ordered` int NOT NULL DEFAULT '1',
  `price_each` decimal(7,2) NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`),
  KEY `fk_orders_has_products_products1_idx` (`product_id`),
  KEY `fk_orders_has_products_orders1_idx` (`order_id`),
  CONSTRAINT `fk_orders_has_products_orders1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `fk_orders_has_products_products1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_has_products`
--

LOCK TABLES `orders_has_products` WRITE;
/*!40000 ALTER TABLE `orders_has_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `physical_stores`
--

DROP TABLE IF EXISTS `physical_stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `physical_stores` (
  `store_id` int NOT NULL AUTO_INCREMENT,
  `store_type` char(1) NOT NULL DEFAULT 'p',
  `address` varchar(125) NOT NULL,
  `zip_code` varchar(7) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`store_id`),
  KEY `fk_physical_stores_stores1` (`store_id`,`store_type`),
  CONSTRAINT `fk_physical_stores_stores1` FOREIGN KEY (`store_id`, `store_type`) REFERENCES `stores` (`store_id`, `store_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `physical_stores`
--

LOCK TABLES `physical_stores` WRITE;
/*!40000 ALTER TABLE `physical_stores` DISABLE KEYS */;
/*!40000 ALTER TABLE `physical_stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `private_customers`
--

DROP TABLE IF EXISTS `private_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_type` char(1) NOT NULL DEFAULT 'p',
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `fk_table1_customers1_idx` (`customer_id`,`customer_type`),
  CONSTRAINT `fk_table1_customers1` FOREIGN KEY (`customer_id`, `customer_type`) REFERENCES `customers` (`customer_id`, `customer_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `private_customers`
--

LOCK TABLES `private_customers` WRITE;
/*!40000 ALTER TABLE `private_customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `private_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `cost` decimal(7,2) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Part A','Description about product',25.50,40.90),(2,'Part A','Description about product',25.50,40.90);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_has_manufacturers`
--

DROP TABLE IF EXISTS `products_has_manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_has_manufacturers` (
  `product_id` int NOT NULL,
  `manufacturer_id` int NOT NULL,
  PRIMARY KEY (`product_id`,`manufacturer_id`),
  KEY `fk_products_has_manufacturers_manufacturers1_idx` (`manufacturer_id`),
  KEY `fk_products_has_manufacturers_products1_idx` (`product_id`),
  CONSTRAINT `fk_products_has_manufacturers_manufacturers1` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturers` (`manufacturer_id`),
  CONSTRAINT `fk_products_has_manufacturers_products1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_has_manufacturers`
--

LOCK TABLES `products_has_manufacturers` WRITE;
/*!40000 ALTER TABLE `products_has_manufacturers` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_has_manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_has_suppliers`
--

DROP TABLE IF EXISTS `products_has_suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_has_suppliers` (
  `product_id` int NOT NULL,
  `supplier_id` int NOT NULL,
  PRIMARY KEY (`product_id`,`supplier_id`),
  KEY `fk_products_has_suppliers_suppliers1_idx` (`supplier_id`),
  KEY `fk_products_has_suppliers_products1_idx` (`product_id`),
  CONSTRAINT `fk_products_has_suppliers_products1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `fk_products_has_suppliers_suppliers1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_has_suppliers`
--

LOCK TABLES `products_has_suppliers` WRITE;
/*!40000 ALTER TABLE `products_has_suppliers` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_has_suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores` (
  `store_id` int NOT NULL AUTO_INCREMENT,
  `store_type` char(1) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`store_id`),
  UNIQUE KEY `store_id` (`store_id`,`store_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;
/*!40000 ALTER TABLE `stores` DISABLE KEYS */;
/*!40000 ALTER TABLE `stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stores_has_products`
--

DROP TABLE IF EXISTS `stores_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores_has_products` (
  `store_id` int NOT NULL,
  `product_id` int NOT NULL,
  `stock_number` int NOT NULL DEFAULT '0',
  `critical_threshold` int NOT NULL DEFAULT '0',
  `amount_automatic_order` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`store_id`,`product_id`),
  KEY `fk_stores_has_products_products1_idx` (`product_id`),
  KEY `fk_stores_has_products_stores1_idx` (`store_id`),
  CONSTRAINT `fk_stores_has_products_products1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `fk_stores_has_products_stores1` FOREIGN KEY (`store_id`) REFERENCES `stores` (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores_has_products`
--

LOCK TABLES `stores_has_products` WRITE;
/*!40000 ALTER TABLE `stores_has_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `stores_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stores_has_suppliers`
--

DROP TABLE IF EXISTS `stores_has_suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores_has_suppliers` (
  `store_id` int NOT NULL,
  `supplier_id` int NOT NULL,
  PRIMARY KEY (`store_id`,`supplier_id`),
  KEY `fk_stores_has_suppliers_suppliers1_idx` (`supplier_id`),
  KEY `fk_stores_has_suppliers_stores1_idx` (`store_id`),
  CONSTRAINT `fk_stores_has_suppliers_stores1` FOREIGN KEY (`store_id`) REFERENCES `stores` (`store_id`),
  CONSTRAINT `fk_stores_has_suppliers_suppliers1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores_has_suppliers`
--

LOCK TABLES `stores_has_suppliers` WRITE;
/*!40000 ALTER TABLE `stores_has_suppliers` DISABLE KEYS */;
/*!40000 ALTER TABLE `stores_has_suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_id` int NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `head_office_phone` varchar(25) NOT NULL,
  `head_office_address` varchar(100) NOT NULL,
  `contact_person_id` int NOT NULL,
  PRIMARY KEY (`supplier_id`),
  KEY `fk_suppliers_contact_persons1_idx` (`contact_person_id`),
  CONSTRAINT `fk_suppliers_contact_persons1` FOREIGN KEY (`contact_person_id`) REFERENCES `contact_persons` (`contact_person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-25  0:02:04
