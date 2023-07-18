-- Script which lists number of records with the same score in second_table of the database hbtn_0c_0 in MySQL server.
-- List is sorted by the number of records in (descending order)
-- mysql is passed as database name as argument to mysql command

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
