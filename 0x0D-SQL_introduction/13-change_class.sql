-- Script which removes all records with a score <= 5 in second_table of the database hbtn_0c_0 in MySQL server.
-- mysql is passed as database name as argument of mysql command

DELETE FROM second_table WHERE score <=5;
