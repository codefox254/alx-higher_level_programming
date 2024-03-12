/*
Task:
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
The result column name should be average.
The database name will be passed as an argument of the mysql command.
*/

-- Compute average score of all records in second_table
SELECT AVG(score) AS average
FROM hbtn_0c_0.second_table;

