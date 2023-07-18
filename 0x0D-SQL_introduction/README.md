# Concepts

* Databases
* Relational databases
* SQL
* MySQL
* DDL and DML
* CREATE or ALTER a table
* SELECT data from a table
* INSERT, UPDATE or DELETE data
* Subqueries
* MySQL functions

# Resources

* [What is Database & SQL?](https://www.w3schools.com/sql/sql_intro.asp)
* [A Basic MySQL Tutorial](https://www.w3schools.com/sql/sql_mysql.asp)
* [Basic SQL statements: DDL and DML](https://www.w3schools.com/sql/sql_ddl_dml.asp)
* [Basic queries: SQL and RA](https://www.w3schools.com/sql/sql_query.asp)
* [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
* [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
* [What makes the big difference between a backtick and an apostrophe?](https://dev.mysql.com/doc/refman/8.0/en/back-quotes.html)
* [MySQL Cheat Sheet](https://dev.mysql.com/doc/refman/8.0/en/cheatsheet.html)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [installing MySQL in Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

# Learning Objectives

* Understand what a database is.
* Understand what a relational database is.
* Understand what SQL stands for.
* Understand what MySQL is.
* Create a database in MySQL.
* Understand what DDL and DML stand for.
* Create or ALTER a table.
* SELECT data from a table.
* INSERT, UPDATE or DELETE data.
* Understand what subqueries are.
* Use MySQL functions.

# Requirements

* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

# More Info

Comments for your SQL file:

```python
# 3 first students in the Batch ID=3
# because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$


$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

