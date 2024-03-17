-- SQL Script: Create database hbtn_0d_usa and table states if not exists
-- Check if the database hbtn_0d_usa already exists by attempting to create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Check if the table states already exists by attempting to create it
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Attempt to insert data into the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
