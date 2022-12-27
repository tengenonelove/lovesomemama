CREATE TABLE cars(
    id INTEGER NOT NULL PRIMARY KEY,
    stamp VARCHAR(100)  NOT NULL
    year_of_release VARCHAR(100)  NOT NULL
    volume_of_liters VARCHAR(100)  NOT NULL

);

CREATE TABLE auto_repair_shop(
    id INTEGER NOT NULL PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    number VARCHAR(50) NOT NULL,
    name INTEGER NOT NULL,
    cars_id INTEGER NOT NULL,
    FOREIGN KEY (cars_id) REFERENCES cars(id)
);

CREATE TABLE staff(
    id INTEGER NOT NULL PRIMARY KEY,
    name_type VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    patronymic VARCHAR(100) NOT NULL,
    date VARCHAR(100) NOT NULL,
    auto_repair_shop VARCHAR(100) NOT NULL,
    post_id INTEGER NOT NULL,
    auto_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(id)
    FOREIGN KEY (auto_repair_id) REFERENCES auto_repair(id)
);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name_post VARCHAR(150)
    master_id INTEGER NOT NULL,
    FOREIGN KEY (master_id) REFERENCES master(id)
);

CREATE TABLE master(
    id INTEGER NOT NULL PRIMARY KEY,
    name_master INTEGER NOT NULL,
    type_of_service_id INTEGER NOT NULL,
    FOREIGN KEY(type_of_service_id) REFERENCES type_of_service(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(type_of_service_id) REFERENCES type_of_service(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE type_of_service(
    id INTEGER NOT NULL PRIMARY KEY,
    name_service INTEGER NOT NULL,
    period_of_execution INTEGER NOT NULL,
    cost INTEGER NOT NULL,
);

NSERT INTO cars(stamp, year_of_release, volume_of_liters)
VALUES ('stamp', 'year_of_release', 'volume_of_liters'),('stamp1', 'year_of_release1', 'volume_of_liters1');

INSERT INTO auto_repair_shop(city, number, name)
VALUES ('city', 'number', 'name'),('city1','number1','name1',);

INSERT INTO staff(name_type, surname, patronomic, date, auto_repair_shop)
VALUES ('name_type', 'surname', 'patronomic', 'date', 'auto_repair_shop'), ('name_type1', 'surname1', 'patronomic1', 'date1', 'auto_repair_shop1');

INSERT INTO post(name_post)
VALUES ('name_post'), ('name_post1');

INSERT INTO master('name_master')
VALUES ('name_master'),('name_master1');

INSERT INTO type_of_services(name_service, period_of_execution, cost)
VALUES ('name_service', 'period_of_execution', 'cost'),('name_service1', 'period_of_execution1', 'cost1');