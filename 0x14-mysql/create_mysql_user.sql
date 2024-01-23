-- Create a MySQL user named 'holberton_user' with the host 'localhost' and set the password to 'projectcorrection280hbtn'
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant the REPLICATION CLIENT privilege to the 'holberton_user' on all databases and tables
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes immediately
FLUSH PRIVILEGES;
