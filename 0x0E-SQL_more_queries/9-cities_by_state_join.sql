-- Script lists all cities in the database hbtn_0d_usa.
-- Each record displays:
-- cities.id - cities.name - states.name
-- Results are sorted in ascending order using cities.id
-- Just 1  SELECT statement is allowed
-- mysql is passed as database name as argument of mysql command

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
