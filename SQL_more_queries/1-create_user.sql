-- Creates user_0d_1 with all privileges if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants every privilege on the server to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
