/*
Task:
Write a script that lists all the tables of a database in your MySQL server.
The database name will be passed as an argument of the mysql command (in the following example: mysql is the name of the database).
*/

USE `mysql`; -- Change 'mysql' to the desired database name

-- List all tables in the specified database
SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = DATABASE();

