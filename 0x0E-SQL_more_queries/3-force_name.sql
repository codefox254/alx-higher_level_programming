-- SQL Script: Create MySQL database hbtn_0d_2 and user user_0d_2
-- Attempt to create the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Attempt to create the user user_0d_2 and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Check if the user user_0d_2 was created or already exists
IF ROW_COUNT() > 0 THEN
    GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_2 created and granted SELECT privilege on database hbtn_0d_2.';
ELSE
    SELECT 'User user_0d_2 already exists.';
END IF;
