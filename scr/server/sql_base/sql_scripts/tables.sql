CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    power_level INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY,
    stamp VARCHAR(100)  NOT NULL,
    year_of_release VARCHAR(100)  NOT NULL,
    volume_of_liters VARCHAR(100)  NOT NULL

);

CREATE TABLE IF NOT EXISTS auto_repair_shop(
    id INTEGER PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    number VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL

);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    patronymic VARCHAR(100) NOT NULL,
    date VARCHAR(100) NOT NULL,
    auto_repair_shop_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(id),
    FOREIGN KEY (auto_repair_shop_id) REFERENCES auto_repair_shop(id)
);

CREATE TABLE IF NOT EXISTS post(
    id INTEGER PRIMARY KEY,
    name_post VARCHAR(150),
    master_id INTEGER NOT NULL,
    FOREIGN KEY (master_id) REFERENCES master(id)
);

CREATE TABLE IF NOT EXISTS master(
    id INTEGER PRIMARY KEY,
    name_master VARCHAR(100) NOT NULL,
    type_of_service_id INTEGER NOT NULL,
    FOREIGN KEY(type_of_service_id) REFERENCES type_of_service(id)
);

CREATE TABLE IF NOT EXISTS type_of_service(
    id INTEGER PRIMARY KEY,
    name_service VARCHAR(100) NOT NULL,
    period_of_execution VARCHAR(100) NOT NULL,
    cost INTEGER NOT NULL
);
