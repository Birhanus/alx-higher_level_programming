-- sql script that creates the table force_name on MYSQL server
-- the database name will be passed as an argument of the mysql command
-- it the table force_name arlrady ecists, your script should not fail

CREATE TABLE IF NOT EXISTS `force_name`(`id` INT, `name` VARCHAR(256));
