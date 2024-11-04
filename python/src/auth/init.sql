-- CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth_password';
CREATE USER 'auth_user'@'192.168.59.100' IDENTIFIED BY 'auth_password';

CREATE DATABASE auth;

-- GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';
GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'192.168.50.100';

USE auth;

CREATE TABLE user (   
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('messaoud', 'messaoud');