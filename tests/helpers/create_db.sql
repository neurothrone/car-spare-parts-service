CREATE SCHEMA IF NOT EXISTS `mysqltest` DEFAULT CHARACTER SET utf8 ;
USE `mysqltest`;

create table car_details
(
    car_detail_id int auto_increment
        primary key,
    brand         varchar(45) not null,
    model         varchar(45) not null,
    year          int         not null
);

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

create table contact_persons
(
    contact_person_id int auto_increment
        primary key,
    first_name        varchar(45)  not null,
    last_name         varchar(45)  not null,
    phone             varchar(25)  not null,
    email             varchar(100) not null
);

create table manufacturers
(
    manufacturer_id     int auto_increment
        primary key,
    company_name        varchar(45)  not null,
    head_office_phone   varchar(25)  not null,
    head_office_address varchar(100) not null,
    contact_person_id   int          null,
    constraint manufacturers_contact_persons_contact_person_id_fk
        foreign key (contact_person_id) references contact_persons (contact_person_id)
);

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

create table products
(
    product_id  int auto_increment
        primary key,
    name        varchar(50)   not null,
    description varchar(255)  null,
    cost        decimal(7, 2) not null,
    price       decimal(7, 2) not null
);

create table car_details_has_products
(
    car_detail_id int not null,
    product_id    int not null,
    primary key (car_detail_id, product_id),
    constraint fk_car_details_has_products_car_details1
        foreign key (car_detail_id) references car_details (car_detail_id),
    constraint fk_car_details_has_products_products1
        foreign key (product_id) references products (product_id)
);

create index fk_car_details_has_products_car_details1_idx
    on car_details_has_products (car_detail_id);

create index fk_car_details_has_products_products1_idx
    on car_details_has_products (product_id);

create table products_has_manufacturers
(
    product_id      int not null,
    manufacturer_id int not null,
    primary key (product_id, manufacturer_id),
    constraint fk_products_has_manufacturers_manufacturers1
        foreign key (manufacturer_id) references manufacturers (manufacturer_id),
    constraint fk_products_has_manufacturers_products1
        foreign key (product_id) references products (product_id)
);

create index fk_products_has_manufacturers_manufacturers1_idx
    on products_has_manufacturers (manufacturer_id);

create index fk_products_has_manufacturers_products1_idx
    on products_has_manufacturers (product_id);

create table stores
(
    store_id   int auto_increment
        primary key,
    store_type char         not null,
    phone      varchar(25)  not null,
    email      varchar(100) not null,
    address    varchar(100) null,
    zip_code   varchar(7)   null,
    city       varchar(45)  null,
    constraint store_id
        unique (store_id, store_type)
)
    charset = utf8mb4;

create table employees
(
    employee_id int auto_increment
        primary key,
    first_name  varchar(45)  not null,
    last_name   varchar(45)  not null,
    phone       varchar(25)  not null,
    email       varchar(100) not null,
    store_id    int          null,
    constraint fk_employees_stores2
        foreign key (store_id) references stores (store_id)
);

create table customers
(
    customer_id        int auto_increment
        primary key,
    customer_type      char         not null,
    customer_name      varchar(100) null,
    contact_first_name varchar(45)  null,
    contact_last_name  varchar(45)  null,
    phone              varchar(25)  not null,
    email              varchar(100) not null,
    address            varchar(100) not null,
    zip_code           varchar(7)   not null,
    city               varchar(50)  not null,
    employee_id        int          null,
    constraint fk_customers_employees1
        foreign key (employee_id) references employees (employee_id)
);

create table cars
(
    reg_no        varchar(7)  not null,
    color         varchar(45) null,
    car_detail_id int         not null,
    customer_id   int         null,
    primary key (reg_no, car_detail_id),
    constraint fk_cars_car_details
        foreign key (car_detail_id) references car_details (car_detail_id),
    constraint fk_cars_customers1
        foreign key (customer_id) references customers (customer_id)
);

create index fk_cars_car_details_idx
    on cars (car_detail_id);

create index fk_cars_customers1_idx
    on cars (customer_id);

create index fk_customers_employees1_idx
    on customers (employee_id);

create index fk_employees_stores2_idx
    on employees (store_id);

create table orders
(
    order_id      int auto_increment
        primary key,
    ordered_date  timestamp   not null,
    shipped_date  timestamp   null,
    delivery_date date        null,
    status        varchar(15) not null,
    customer_id   int         not null,
    constraint fk_orders_customers1
        foreign key (customer_id) references customers (customer_id)
);

create table order_details
(
    order_id         int           not null,
    product_id       int           not null,
    quantity_ordered int           not null,
    price_each       decimal(7, 2) not null,
    primary key (order_id, product_id),
    constraint fk_order_details_orders1
        foreign key (order_id) references orders (order_id),
    constraint fk_order_details_products1
        foreign key (product_id) references products (product_id)
);

create index fk_order_details_products1_idx
    on order_details (product_id);

create index fk_orders_customers1_idx
    on orders (customer_id);

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

create table stores_has_products
(
    store_id               int           not null,
    product_id             int           not null,
    stock_number           int default 0 not null,
    critical_threshold     int default 0 not null,
    amount_automatic_order int default 0 not null,
    primary key (store_id, product_id),
    constraint fk_stores_has_products_products1
        foreign key (product_id) references products (product_id),
    constraint fk_stores_has_products_stores1
        foreign key (store_id) references stores (store_id)
)
    charset = utf8mb4;

create index fk_stores_has_products_products1_idx
    on stores_has_products (product_id);

create index fk_stores_has_products_stores1_idx
    on stores_has_products (store_id);

create table suppliers
(
    supplier_id         int auto_increment
        primary key,
    company_name        varchar(45)  not null,
    head_office_phone   varchar(25)  not null,
    head_office_address varchar(100) not null,
    contact_person_id   int          null,
    constraint suppliers_contact_persons_contact_person_id_fk
        foreign key (contact_person_id) references contact_persons (contact_person_id)
);

create table products_has_suppliers
(
    product_id  int not null,
    supplier_id int not null,
    primary key (product_id, supplier_id),
    constraint fk_products_has_suppliers_products1
        foreign key (product_id) references products (product_id),
    constraint fk_products_has_suppliers_suppliers1
        foreign key (supplier_id) references suppliers (supplier_id)
);

create index fk_products_has_suppliers_products1_idx
    on products_has_suppliers (product_id);

create index fk_products_has_suppliers_suppliers1_idx
    on products_has_suppliers (supplier_id);

create table stores_has_suppliers
(
    store_id    int not null,
    supplier_id int not null,
    primary key (store_id, supplier_id),
    constraint fk_stores_has_suppliers_stores1
        foreign key (store_id) references stores (store_id),
    constraint fk_stores_has_suppliers_suppliers1
        foreign key (supplier_id) references suppliers (supplier_id)
)
    charset = utf8mb4;

create index fk_stores_has_suppliers_stores1_idx
    on stores_has_suppliers (store_id);

create index fk_stores_has_suppliers_suppliers1_idx
    on stores_has_suppliers (supplier_id);

create index fk_suppliers_contact_persons1_idx
    on suppliers (contact_person_id);

create index fk_suppliers_contact_persons1_idxmanufacturers
    on suppliers (contact_person_id);

####### INSERT DATA   ######
insert into contact_persons(first_name, last_name, phone, email)
values ('Anders', 'Bob', '070 00 93 71 35', 'andersbob@email.com');

insert into manufacturers (company_name, head_office_phone, head_office_address, contact_person_id)
values ('Anderson AB', '070 00 93 71 35', 'ALEBACKEN 7, 76856 Göteborg', '1');