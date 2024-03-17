-- SQL Script: Create MySQL user user_0d_1 with all privileges
-- Check if user_0d_1 already exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- If user_0d_1 does not exist, create the user and grant all privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created and granted all privileges.';
ELSE
    SELECT 'User user_0d_1 already exists.';
END IF;
