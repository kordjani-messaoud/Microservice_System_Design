-- minikube-node.com is domain name for the minikube node whether a container of a VM
CREATE USER 'auth_user'@'minikube-node.com' IDENTIFIED BY 'auth_password';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'minikube-node.com';

USE auth;

CREATE TABLE user (   
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('messaoud', 'messaoud');