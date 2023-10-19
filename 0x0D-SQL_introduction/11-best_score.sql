-- Script lists all records with a score >= 10 in second_table of the database hbtn_0c_0 in MySQL server
-- Result displays both score and name (in this order)
-- Records is ordered by score (top first)
-- mysql is passed as database name as argument of mysql command

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
