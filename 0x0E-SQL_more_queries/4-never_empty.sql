-- SQL Script: Create table id_not_null in the hbtn_0d_2 database if not exists
-- Attempt to create the table id_not_null in the hbtn_0d_2 database if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_2.id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Check if the table was created or already exists
IF ROW_COUNT() > 0 THEN
    SELECT 'Table id_not_null created in hbtn_0d_2 database.';
ELSE
    SELECT 'Table id_not_null already exists in hbtn_0d_2 database.';
END IF;
