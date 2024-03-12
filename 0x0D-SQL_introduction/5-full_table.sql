/*
Task:
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
The database name will be passed as an argument of the mysql command.
You are not allowed to use the DESCRIBE or EXPLAIN statements.
*/

-- Retrieve table structure without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' -- Change 'hbtn_0c_0' to the desired database name
    AND TABLE_NAME = 'first_table'; -- Change 'first_table' to the desired table name

