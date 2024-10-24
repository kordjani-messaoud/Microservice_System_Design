CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth_password';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (   
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)

INSERT INTO user (name, email, password) VALUES ('messaoud', 'messaoud@email.com', 'messaoud')