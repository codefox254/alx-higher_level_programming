-- SQL Script: Create table unique_id in the hbtn_0d_2 database if not exists
-- Attempt to create the table unique_id in the hbtn_0d_2 database if it doesn't exist
REATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
