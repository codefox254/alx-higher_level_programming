-- SQL Script: Create table id_not_null in the hbtn_0d_2 database if not exists

-- Check if the table already exists
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = 'hbtn_0d_2' AND table_name = 'id_not_null';

-- If the table does not exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE hbtn_0d_2.id_not_null (
        id INT DEFAULT 1,
        name VARCHAR(256)
    );
    SELECT 'Table id_not_null created in hbtn_0d_2 database.';
ELSE
    SELECT 'Table id_not_null already exists in hbtn_0d_2 database.';
END IF;
