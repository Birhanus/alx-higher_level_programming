-- sql script that create database hbtn_0d_usa and table states.
-- in the database hbtn_0d_usa on your MYSQL server.
-- Table attribute id unique, auto generated, can't be null and primary ky.
-- If the database hbtn_0d_use already exists, your script should not fail.
-- If the table states already exists, your script should not fail.

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);