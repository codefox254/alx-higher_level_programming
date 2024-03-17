-- SQL Script: Create MySQL database hbtn_0d_2 and user user_0d_2

-- Check if database hbtn_0d_2 already exists
SELECT COUNT(*) INTO @db_exists FROM information_schema.schemata WHERE schema_name = 'hbtn_0d_2';

-- If hbtn_0d_2 does not exist, create the database
IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_2;
    SELECT 'Database hbtn_0d_2 created.';
ELSE
    SELECT 'Database hbtn_0d_2 already exists.';
END IF;

-- Check if user_0d_2 already exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_2';

-- If user_0d_2 does not exist, create the user and grant privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
    GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_2 created and granted SELECT privilege on database hbtn_0d_2.';
ELSE
    SELECT 'User user_0d_2 already exists.';
END IF;
