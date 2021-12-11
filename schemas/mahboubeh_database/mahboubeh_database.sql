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
