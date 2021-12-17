# Car Spare Parts Service

## Setup

In the `docker` directory run the `docker-compose.yml` located inside the
`car-spare-parts-main` sub-directory to create a docker container for Mongo and MySQL databases.

## Project Structure
- app
    - controllers
    - converters
      - data module converters from mysql to mongo
    - data
      - mongo specific db setup, repositories and models
      - mysql specific db setup, repositories and models
      - database interface with differentiation
    - views
      - web interface
    - config and settings
- docker
  - main docker file (mongo and mysql db)
  - mongo docker file
  - mysql docker file
- dumps
  - mongo dump
  - mysql dump
- generators
    - fake data and mysql model generators
- schemas
    - mysql workbench model
    - image of mysql database structure
    - mysql db sql creation scripts
- shared (reusable components)
    - exc
    - models
    - tests
    - validators
- tests
    - controllers
    - converters
    - mongo (mongo specific)

## MySQL Database structure

![Entity-relationship model of MySQL database structure](schemas/mysql-database-structure.png?raw=true "ER-diagram of MySQL Database")

## Mongo Database structure
- cars
  - car specific data and reference to owner (customer_id)
- contact persons
  - person data specifics
- customers
  - person or company client data specifics
- employees
  - employee specific data and reference to workplace (store_id)
- manufacturers
  - manufacturer specific data and reference to contact person if one exists
- products
  - product specific data
- stores
  - store specific data with lists of:
    - storage: for reference to products and storage specific data for those products
    - employees: for reference to employees and employee specific data for those employees
- suppliers
  - supplier specific data and reference to contact person if one exists


## Configuration

A text file named `.env` should be created in the root project directory with these variables set to appropriate values
such as shown below by the example:

```bash
MONGO_DB_NAME=car-spare-parts-mongo-db
MONGO_DB_PROTOCOL=mongodb
MONGO_DB_USER=root
MONGO_DB_PASS=super-secret-password
MONGO_DB_HOST=localhost
MONGO_DB_PORT=27017

MYSQL_DB_NAME=car-spare-parts-mysql-db
MYSQL_DB_PROTOCOL=mysql+mysqlconnector
MYSQL_DB_USER=root
MYSQL_DB_PASS=super-secret-password
MYSQL_DB_HOST=localhost
MYSQL_DB_PORT=3306
```