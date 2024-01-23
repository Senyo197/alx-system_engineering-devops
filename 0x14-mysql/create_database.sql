-- Create the tyrell_corp database
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create the nexus6 table
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

-- Insert at least one entry into the nexus6 table
INSERT INTO nexus6 (Sanjay) VALUES ('Replicant-1');

-- Grant SELECT permissions to holberton_user on the nexus6 table
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
