USE testdb;

CREATE TABLE IF NOT EXISTS real_user (
 user_id VARCHAR(10) PRIMARY KEY,
 user_name VARCHAR(20) NOT NULL,
 user_ssn VARCHAR(14), # 주민번호 (민감정보)
 salary INT # 급여 (민감정보)
);
INSERT IGNORE INTO real_user VALUES
('KIM', '김철수', '950101-1234567', 4000000),
('LEE', '이영희', '980202-2345678', 3500000);

CREATE VIEW v_user_security AS
SELECT user_id, user_name
FROM real_user;

# SELECT * FROM v_user_security;

DROP VIEW v_user_security;
SELECT * FROM real_user;