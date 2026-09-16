USE testdb;

CREATE TABLE IF NOT EXISTS member_point (
	user_id VARCHAR(10) PRIMARY KEY,
	user_name VARCHAR(20),
	point INT
);

# INSERT INTO member_point VALUES ('KIM', '김철수', 100) ON DUPLICATE KEY UPDATE point = point + 100;

# INSERT INTO member_point VALUES ('KIM', '김철수', 100) ON DUPLICATE KEY UPDATE point = point + 100;

SELECT * FROM member_point;