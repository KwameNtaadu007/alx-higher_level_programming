# This script creates the database hbtn_0d_usa with the table cities.
# The table has the following fields:
#   id: INT NOT NULL AUTO_INCREMENT, the primary key
#   state_id: INT NOT NULL, the foreign key
#   name: VARCHAR(256) NOT NULL

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`),
    `id`       INT          NOT NULL AUTO_INCREMENT,
    `state_id` INT          NOT NULL,
    `name`     VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);

