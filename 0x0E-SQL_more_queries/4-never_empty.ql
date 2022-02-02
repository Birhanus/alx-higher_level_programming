-- sql script that creats the table id_not_null on MYSQL server
-- table attribute id default value 1
-- the database name will be passed as an argument of the mysql command
-- if the table id_not_null already exists, your scripr should not fail

CREATE TABLE IF NOT EXISTS `id_not_null`(`id` INT DEFAULT 1, `name` VARCHAR(256))
