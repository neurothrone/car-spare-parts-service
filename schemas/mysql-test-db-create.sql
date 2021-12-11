-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema car-spare-parts-mysql-db-test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema car-spare-parts-mysql-db-test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `car-spare-parts-mysql-db-test` DEFAULT CHARACTER SET utf8 ;
USE `car-spare-parts-mysql-db-test` ;

-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`contact_persons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`contact_persons` (
  `contact_person_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`contact_person_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`manufacturers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`manufacturers` (
  `manufacturer_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(45) NOT NULL,
  `head_office_phone` VARCHAR(25) NOT NULL,
  `head_office_address` VARCHAR(100) NOT NULL,
  `contact_person_id` INT NULL,
  PRIMARY KEY (`manufacturer_id`),
  INDEX `fk_manufacturers_contact_persons1_idx` (`contact_person_id` ASC) VISIBLE,
  CONSTRAINT `fk_manufacturers_contact_persons1`
    FOREIGN KEY (`contact_person_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`contact_persons` (`contact_person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`suppliers` (
  `supplier_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(45) NOT NULL,
  `head_office_phone` VARCHAR(25) NOT NULL,
  `head_office_address` VARCHAR(100) NOT NULL,
  `contact_person_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`supplier_id`),
  INDEX `fk_suppliers_contact_persons1_idx` (`contact_person_id` ASC) VISIBLE,
  CONSTRAINT `fk_suppliers_contact_persons1`
    FOREIGN KEY (`contact_person_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`contact_persons` (`contact_person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`car_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`car_details` (
  `car_detail_id` INT NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  PRIMARY KEY (`car_detail_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`stores` (
  `store_id` INT NOT NULL AUTO_INCREMENT,
  `store_type` CHAR(1) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `address` VARCHAR(100) NULL,
  `zip_code` VARCHAR(7) NULL,
  `city` VARCHAR(45) NULL,
  PRIMARY KEY (`store_id`),
  UNIQUE INDEX `store_id` (`store_id` ASC, `store_type` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`employees` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `store_id` INT NULL,
  PRIMARY KEY (`employee_id`),
  INDEX `fk_employees_stores2_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_employees_stores2`
    FOREIGN KEY (`store_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_type` CHAR(1) NOT NULL,
  `customer_name` VARCHAR(100) NULL,
  `contact_first_name` VARCHAR(45) NULL,
  `contact_last_name` VARCHAR(45) NULL,
  `phone` VARCHAR(25) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `address` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(7) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `employee_id` INT NULL,
  PRIMARY KEY (`customer_id`),
  INDEX `fk_customers_employees1_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_customers_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`cars` (
  `reg_no` VARCHAR(7) NOT NULL,
  `color` VARCHAR(45) NULL,
  `car_detail_id` INT NOT NULL,
  `customer_id` INT NULL,
  PRIMARY KEY (`reg_no`, `car_detail_id`),
  INDEX `fk_cars_car_details_idx` (`car_detail_id` ASC) VISIBLE,
  INDEX `fk_cars_customers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_car_details`
    FOREIGN KEY (`car_detail_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`car_details` (`car_detail_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cars_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`customers` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(255) NULL,
  `cost` DECIMAL(7,2) NOT NULL,
  `price` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `ordered_date` TIMESTAMP NOT NULL,
  `shipped_date` TIMESTAMP NULL,
  `delivery_date` DATE NULL,
  `status` VARCHAR(15) NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `fk_orders_customers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`customers` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`car_details_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`car_details_has_products` (
  `car_detail_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`car_detail_id`, `product_id`),
  INDEX `fk_car_details_has_products_products1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_car_details_has_products_car_details1_idx` (`car_detail_id` ASC) VISIBLE,
  CONSTRAINT `fk_car_details_has_products_car_details1`
    FOREIGN KEY (`car_detail_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`car_details` (`car_detail_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_details_has_products_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`products_has_manufacturers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`products_has_manufacturers` (
  `product_id` INT NOT NULL,
  `manufacturer_id` INT NOT NULL,
  PRIMARY KEY (`product_id`, `manufacturer_id`),
  INDEX `fk_products_has_manufacturers_manufacturers1_idx` (`manufacturer_id` ASC) VISIBLE,
  INDEX `fk_products_has_manufacturers_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_manufacturers_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_manufacturers_manufacturers1`
    FOREIGN KEY (`manufacturer_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`manufacturers` (`manufacturer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`products_has_suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`products_has_suppliers` (
  `product_id` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  PRIMARY KEY (`product_id`, `supplier_id`),
  INDEX `fk_products_has_suppliers_suppliers1_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `fk_products_has_suppliers_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_suppliers_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_suppliers_suppliers1`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`suppliers` (`supplier_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`stores_has_suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`stores_has_suppliers` (
  `store_id` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  PRIMARY KEY (`store_id`, `supplier_id`),
  INDEX `fk_stores_has_suppliers_suppliers1_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `fk_stores_has_suppliers_stores1_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_stores_has_suppliers_stores1`
    FOREIGN KEY (`store_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stores_has_suppliers_suppliers1`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`suppliers` (`supplier_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`stores_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`stores_has_products` (
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
    REFERENCES `car-spare-parts-mysql-db-test`.`stores` (`store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stores_has_products_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `car-spare-parts-mysql-db-test`.`order_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car-spare-parts-mysql-db-test`.`order_details` (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity_ordered` INT NOT NULL,
  `price_each` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`order_id`, `product_id`),
  INDEX `fk_order_details_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_details_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_details_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `car-spare-parts-mysql-db-test`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Triggers
-- -----------------------------------------------------

create table changed_address_manufacturer
(
    id                      int auto_increment
        primary key,
    company_name            varchar(45)  not null,
    head_office_phone       varchar(25)  not null,
    old_head_office_address varchar(100) null,
    new_head_office_address varchar(100) null,
    contact_person_id       int          null,
    change_date             datetime     not null,
    action                  varchar(100) not null
);

create table changed_address_store
(
    store_id    int auto_increment
        primary key,
    store_type  char         not null,
    phone       varchar(25)  not null,
    email       varchar(100) not null,
    old_address varchar(100) null,
    new_address varchar(100) null,
    zip_code    varchar(7)   null,
    city        varchar(45)  null,
    change_date datetime     not null,
    action      varchar(100) not null,
    constraint store_id
        unique (store_id, store_type)
);

#######'triggers_manufacturers'##########

create definer = root@`%` trigger before_changed_address
    before insert
    on manufacturers
    for each row
    INSERT INTO changed_address_manufacturer
    SET action                  = 'insert',
        company_name            = company_name,
        head_office_phone       = head_office_phone,
        new_head_office_address = NEW.head_office_address,
        change_date             = NOW();

create definer = root@`%` trigger before_delete_address
    before delete
    on manufacturers
    for each row
    INSERT INTO changed_address_manufacturer
    SET action                  = 'delete',
        company_name            = company_name,
        head_office_phone       = head_office_phone,
        old_head_office_address = OLD.head_office_address,
        change_date             = NOW();

create definer = root@`%` trigger before_update_address
    before update
    on manufacturers
    for each row
    INSERT INTO changed_address_manufacturer
    SET action                  = 'update',
        company_name            = company_name,
        head_office_phone       = head_office_phone,
        old_head_office_address = OLD.head_office_address,
        new_head_office_address = NEW.head_office_address,
        change_date             = NOW();

#######'triggers_stores'##########

create definer = root@`%` trigger before_changed_address_store
    before insert
    on stores
    for each row
    INSERT INTO changed_address_store
    SET action      = 'insert',
        store_type  = store_type,
        phone       = phone,
        email       = email,
        new_address = NEW.zip_code,
        city        = city,
        change_date = NOW();

create definer = root@`%` trigger before_delete_address_store
    before delete
    on stores
    for each row
    INSERT INTO changed_address_store
    SET action      = 'delete',
        store_type  = store_type,
        phone       = phone,
        email       = email,
        old_address = OLD.address,
        city        = city,
        change_date = NOW();

create definer = root@`%` trigger before_update_address_store
    before update
    on stores
    for each row
    INSERT INTO changed_address_store
    SET action      = 'update',
        store_type  = store_type,
        phone       = phone,
        email       = email,
        old_address = OLD.address,
        new_address = NEW.zip_code,
        city        = city,
        change_date = NOW();


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
