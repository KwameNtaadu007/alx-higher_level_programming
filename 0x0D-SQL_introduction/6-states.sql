-- Script creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server.
-- states description:
-- 	  id INT unique, auto generated, primary key and cannot be null
--	  name VARCHAR(256) cannot be null
-- If the database hbtn_0d_usa already exists, script should not fail
-- If the table states already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);
