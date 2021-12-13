# Car Spare Parts Service

## About

## Setup

In the `docker` directory run the `docker-compose.yml` located inside the
`car-spare-parts-main` sub-directory to create a docker container for Mongo and MySQL databases.

## Project Structure

- app
    - controllers
    - converters
    - data
    - views
- docker
- generators
- schemas
    - dumps
    - models
- shared
    - models
    - tests
    - validators
- tests
    - controllers
    - mongo
    - mysql

## MySQL Database structure

![Entity-relationship model of MySQL database structure](schemas/mysql-database-structure.png?raw=true "ER-diagram of MySQL Database")

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