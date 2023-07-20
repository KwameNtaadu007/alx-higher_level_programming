-- Script creates the database hbtn_0d_usa and cities table on MySQL server.
-- Cities description:
-- 	  id INT unique, auto generated,  primary key and cannot be null
--	  state_id INT, cannot be null and is a FOREIGN KEY  referencing id of the states table
-- 	  name VARCHAR(256) cannot be null
-- If the database hbtn_0d_usa already exists, script should not fail
-- If the table cities already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
