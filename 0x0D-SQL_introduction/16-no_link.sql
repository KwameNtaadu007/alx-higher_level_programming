-- Script which lists all records of second_table of the database hbtn_0c_0 in MySQL server.
-- Rows without a name value should not be listed
-- Results display the score and the name (in this order)
-- Records are listed by descending order of score
-- mysql is passed as database name as argument to mysql command

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
