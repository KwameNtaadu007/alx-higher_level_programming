# This script creates the table hbtn_0d_usa with table states.
# The table has the following fields:
#   id: INT NOT NULL AUTO_INCREMENT, the primary key
#   name: VARCHAR(256) NOT NULL

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);

