-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema car-spare-parts-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema car-spare-parts-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `car-spare-parts-db` DEFAULT CHARACTER SET utf8 ;
USE `car-spare-parts-db` ;

-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`contact_persons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`contact_persons` (
  `contact_person_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`contact_person_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`manufacturers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`manufacturers` (
  `manufacturer_id` INT NOT NULL,
  `company_name` VARCHAR(45) NOT NULL,
  `head_office_phone` VARCHAR(25) NOT NULL,
  `head_office_address` VARCHAR(100) NOT NULL,
  `contact_person_id` INT NOT NULL,
  PRIMARY KEY (`manufacturer_id`),
  INDEX `fk_manufacturers_contact_persons1_idx` (`contact_person_id` ASC) VISIBLE,
  CONSTRAINT `fk_manufacturers_contact_persons1`
    FOREIGN KEY (`contact_person_id`)
    REFERENCES `car-spare-parts-db`.`contact_persons` (`contact_person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`suppliers` (
  `supplier_id` INT NOT NULL,
  `company_name` VARCHAR(45) NOT NULL,
  `head_office_phone` VARCHAR(25) NOT NULL,
  `head_office_address` VARCHAR(100) NOT NULL,
  `contact_person_id` INT NOT NULL,
  PRIMARY KEY (`supplier_id`),
  INDEX `fk_suppliers_contact_persons1_idx` (`contact_person_id` ASC) VISIBLE,
  CONSTRAINT `fk_suppliers_contact_persons1`
    FOREIGN KEY (`contact_person_id`)
    REFERENCES `car-spare-parts-db`.`contact_persons` (`contact_person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`car_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`car_details` (
  `car_detail_id` INT NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  PRIMARY KEY (`car_detail_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`cars` (
  `reg_no` VARCHAR(7) NOT NULL,
  `color` VARCHAR(45) NULL,
  `car_detail_id` INT NOT NULL,
  PRIMARY KEY (`reg_no`, `car_detail_id`),
  INDEX `fk_cars_car_details_idx` (`car_detail_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_car_details`
    FOREIGN KEY (`car_detail_id`)
    REFERENCES `car-spare-parts-db`.`car_details` (`car_detail_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(255) NULL,
  `cost` DECIMAL(7,2) NOT NULL,
  `price` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`stores` (
  `store_id` INT NOT NULL AUTO_INCREMENT,
  `store_type` CHAR(1) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`store_id`),
  UNIQUE INDEX `store_id` (`store_id` ASC, `store_type` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`employees` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `store_id` INT NOT NULL,
  PRIMARY KEY (`employee_id`),
  INDEX `fk_employees_stores2_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_employees_stores2`
    FOREIGN KEY (`store_id`)
    REFERENCES `car-spare-parts-db`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `ordered_date` TIMESTAMP NOT NULL,
  `shipped_date` TIMESTAMP NULL,
  `delivery_date` DATE NULL,
  `status` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`order_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`orders_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`orders_has_products` (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity_ordered` INT NOT NULL DEFAULT 1,
  `price_each` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`order_id`, `product_id`),
  INDEX `fk_orders_has_products_products1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_orders_has_products_orders1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_has_products_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `car-spare-parts-db`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_has_products_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-db`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`car_details_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`car_details_has_products` (
  `car_detail_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`car_detail_id`, `product_id`),
  INDEX `fk_car_details_has_products_products1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_car_details_has_products_car_details1_idx` (`car_detail_id` ASC) VISIBLE,
  CONSTRAINT `fk_car_details_has_products_car_details1`
    FOREIGN KEY (`car_detail_id`)
    REFERENCES `car-spare-parts-db`.`car_details` (`car_detail_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_details_has_products_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-db`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`products_has_manufacturers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`products_has_manufacturers` (
  `product_id` INT NOT NULL,
  `manufacturer_id` INT NOT NULL,
  PRIMARY KEY (`product_id`, `manufacturer_id`),
  INDEX `fk_products_has_manufacturers_manufacturers1_idx` (`manufacturer_id` ASC) VISIBLE,
  INDEX `fk_products_has_manufacturers_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_manufacturers_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-db`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_manufacturers_manufacturers1`
    FOREIGN KEY (`manufacturer_id`)
    REFERENCES `car-spare-parts-db`.`manufacturers` (`manufacturer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`products_has_suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`products_has_suppliers` (
  `product_id` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  PRIMARY KEY (`product_id`, `supplier_id`),
  INDEX `fk_products_has_suppliers_suppliers1_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `fk_products_has_suppliers_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_suppliers_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-db`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_suppliers_suppliers1`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `car-spare-parts-db`.`suppliers` (`supplier_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`online_stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`online_stores` (
  `store_id` INT NOT NULL AUTO_INCREMENT,
  `store_type` CHAR(1) NOT NULL DEFAULT 'o',
  PRIMARY KEY (`store_id`),
  CONSTRAINT `fk_online_stores_stores1`
    FOREIGN KEY (`store_id` , `store_type`)
    REFERENCES `car-spare-parts-db`.`stores` (`store_id` , `store_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
INSERT_METHOD = LAST;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`physical_stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`physical_stores` (
  `store_id` INT NOT NULL AUTO_INCREMENT,
  `store_type` CHAR(1) NOT NULL DEFAULT 'p',
  `address` VARCHAR(125) NOT NULL,
  `zip_code` VARCHAR(7) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`store_id`),
  CONSTRAINT `fk_physical_stores_stores1`
    FOREIGN KEY (`store_id` , `store_type`)
    REFERENCES `car-spare-parts-db`.`stores` (`store_id` , `store_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`stores_has_suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`stores_has_suppliers` (
  `store_id` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  PRIMARY KEY (`store_id`, `supplier_id`),
  INDEX `fk_stores_has_suppliers_suppliers1_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `fk_stores_has_suppliers_stores1_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_stores_has_suppliers_stores1`
    FOREIGN KEY (`store_id`)
    REFERENCES `car-spare-parts-db`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stores_has_suppliers_suppliers1`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `car-spare-parts-db`.`suppliers` (`supplier_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_type` CHAR(1) NOT NULL,
  `customer_name` VARCHAR(100) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `address` VARCHAR(125) NOT NULL,
  `zip_code` VARCHAR(7) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `reg_no` VARCHAR(7) NOT NULL,
  `order_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`customer_id`, `customer_type`),
  INDEX `fk_customers_cars1_idx` (`reg_no` ASC) VISIBLE,
  INDEX `fk_customers_orders1_idx` (`order_id` ASC) VISIBLE,
  INDEX `fk_customers_employees1_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_customers_cars1`
    FOREIGN KEY (`reg_no`)
    REFERENCES `car-spare-parts-db`.`cars` (`reg_no`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customers_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `car-spare-parts-db`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customers_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `car-spare-parts-db`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`corporate_customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`corporate_customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_type` CHAR(1) NOT NULL,
  `organization_number` INT NOT NULL,
  `organization_name` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `organization_number_UNIQUE` (`organization_number` ASC) VISIBLE,
  INDEX `fk_corporate_customers_customers1_idx` (`customer_id` ASC, `customer_type` ASC) INVISIBLE,
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `fk_corporate_customers_customers1`
    FOREIGN KEY (`customer_id` , `customer_type`)
    REFERENCES `car-spare-parts-db`.`customers` (`customer_id` , `customer_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`private_customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`private_customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_type` CHAR(1) NOT NULL DEFAULT 'p',
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  INDEX `fk_table1_customers1_idx` (`customer_id` ASC, `customer_type` ASC) VISIBLE,
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `fk_table1_customers1`
    FOREIGN KEY (`customer_id` , `customer_type`)
    REFERENCES `car-spare-parts-db`.`customers` (`customer_id` , `customer_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-db`.`stores_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-db`.`stores_has_products` (
  `store_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `stock_number` INT NOT NULL DEFAULT 0,
  `critical_threshold` INT NOT NULL DEFAULT 0,
  `amount_automatic_order` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`store_id`, `product_id`),
  INDEX `fk_stores_has_products_products1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_stores_has_products_stores1_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_stores_has_products_stores1`
    FOREIGN KEY (`store_id`)
    REFERENCES `car-spare-parts-db`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stores_has_products_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-db`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
