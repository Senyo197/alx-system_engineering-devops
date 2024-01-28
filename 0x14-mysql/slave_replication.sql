GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

--use "'show master status' to get the master_log_pos and the master_log_file"
STOP SLAVE;

CHANGE MASTER TO
  MASTER_HOST = 'master_hostname or ip',
  MASTER_USER = 'replica_user',
  MASTER_PASSWORD = 'your_password',
  MASTER_PORT = 3306,
  MASTER_LOG_FILE = 'mysql-bin.000003',
  MASTER_LOG_POS = 157;

START SLAVE;
