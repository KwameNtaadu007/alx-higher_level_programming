-- Script which lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains just 1 record of name = California
-- Results are sorted in ascending order using cities.id
-- The use of the JOIN keyword is prohibited
-- mysql is passed as database name as argument of mysql command

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
