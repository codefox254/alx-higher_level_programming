-- Retrieve the structure of a table named 'first_table' in the 'hbtn_0c_0' database
-- by selecting column name, type, nullability, key, default value, and extra information
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' -- Specify the desired database name
    AND TABLE_NAME = 'first_table'; -- Specify the desired table name
