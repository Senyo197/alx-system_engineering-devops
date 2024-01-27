-- Create a new user 'replica_user' with a wildcard host (%), and set a password.
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'web-01';

-- Grant replication privileges to 'replica_user' on all databases and tables.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Connect to MySQL as a user with appropriate privileges, such as 'root'.
CREATE USER 'holberton_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT SELECT ON mysql.user TO 'holberton_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes.
FLUSH PRIVILEGES;
