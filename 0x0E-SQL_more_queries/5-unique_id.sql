-- sql script that creates the table unique_ID on your MYSQL server.
-- Table attribute id with default value 1 and must be unique.
-- The database name will be passed as an argument of the mysql command.
-- If the table unique_id already exists, your script should not fail.

CREATE TABLE IF NOT EXISTS `unique_id`(`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
