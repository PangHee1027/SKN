USE testdb;

CREATE TABLE IF NOT EXISTS j_member (
	user_id VARCHAR(10) PRIMARY KEY,
    user_name VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS j_buy (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(10),
    prod_name
	VARCHAR(20)
);

INSERT IGNORE INTO j_member VALUES ('KIM', '김철수'), ('LEE', '이영희');
INSERT IGNORE INTO j_buy VALUES (NULL, 'KIM', '노트북'); 

SELECT M.user_id, M.user_name, B.prod_name
FROM j_member M
LEFT JOIN j_buy B ON M.user_id = B.user_id;