-- SQL Script: Create table unique_id in the hbtn_0d_2 database if not exists
-- Attempt to create the table unique_id in the hbtn_0d_2 database if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_2.unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Attempt to insert data into the unique_id table
INSERT INTO hbtn_0d_2.unique_id (name) VALUES ('Example_Name');

-- Attempt to insert data with an already existing id
INSERT INTO hbtn_0d_2.unique_id (id, name) VALUES (1, 'Another_Name');
