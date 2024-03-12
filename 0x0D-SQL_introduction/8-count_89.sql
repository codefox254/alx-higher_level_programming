/*
Task:
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
The database name will be passed as an argument of the mysql command.
*/

-- Count the number of records with id = 89 in first_table
SELECT COUNT(*)
FROM hbtn_0c_0.first_table
WHERE id = 89;

