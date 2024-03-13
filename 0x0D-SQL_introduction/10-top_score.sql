/*
Task:
A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
*/
-- Select all records from second_table, displaying score and name, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
ORDER BY score DESC;
