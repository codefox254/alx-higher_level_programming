-- SQL Script: Create database hbtn_0d_usa and table states if not exists
-- Check if the database hbtn_0d_usa already exists by attempting to create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- uses a database
USE hbtn_0d_usa;
-- Will create a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
