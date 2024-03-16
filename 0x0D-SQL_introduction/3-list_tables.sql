USE `mysql`; -- Change 'mysql' to the desired database name

-- List all tables in the specified database
SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = DATABASE();
