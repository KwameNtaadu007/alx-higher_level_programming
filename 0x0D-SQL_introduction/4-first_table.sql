-- Script creates table called first_table in the current database in MySQL server.
-- first_table description:
--             id INT
--             name VARCHAR(256)
-- The database name is passed as an argument of mysql command
-- If the first_table already exists, script should not fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
