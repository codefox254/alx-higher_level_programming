-- SQL Script: Create database hbtn_0d_usa and table states if not exists
-- Check if the database hbtn_0d_usa already exists
SELECT COUNT(*) INTO @db_exists FROM information_schema.schemata WHERE schema_name = 'hbtn_0d_usa';

-- If hbtn_0d_usa does not exist, create the database
IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_usa;
    SELECT 'Database hbtn_0d_usa created.';
ELSE
    SELECT 'Database hbtn_0d_usa already exists.';
END IF;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Check if the table states already exists
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = 'hbtn_0d_usa' AND table_name = 'states';

-- If the table states does not exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL
    );
    SELECT 'Table states created.';
ELSE
    SELECT 'Table states already exists.';
END IF;
