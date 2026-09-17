# CREATE DATABASE shopdb;

USE shopdb;

# CREATE TABLE member_tbl (
	# member_id INT PRIMARY KEY AUTO_INCREMENT,
    # member_name VARCHAR(20) NOT NULL,
    # member_age INT,
    # reg_date DATETIME
# );

# ALTER TABLE member_tbl ADD LV INT;

# INSERT INTO member_tbl (member_name, member_age, reg_date) VALUES ('홍길동', 20, '2026-01-01'), ('이순신', 45, '2026-01-02'), ('강감찬', 50, '2026-01-03');

# UPDATE member_tbl SET  member_age = 21 WHERE member_name = '홍길동';
# DELETE FROM member_tbl WHERE member_name = '강감찬';
# INSERT INTO member_tbl (member_name, member_age, reg_date) VALUES ("이재현", 26, CURRENT_TIMESTAMP);

SELECT * FROM member_tbl;


