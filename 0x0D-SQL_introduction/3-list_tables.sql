-- List all tables in the current database
SELECT TABLE_NAME AS Tables_in_hbtn_test_db_0 -- Select the table names and alias the column
FROM information_schema.TABLES -- From the information schema's tables
WHERE TABLE_SCHEMA = DATABASE(); -- Where the table schema matches the current database
<<<<<<< HEAD

=======
>>>>>>> 88e20eb2e58d5a9b4221e1324c2d0a3f7c53d65e
