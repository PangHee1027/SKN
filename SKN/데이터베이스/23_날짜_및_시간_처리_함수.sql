SELECT
	NOW() AS 현재시간,
	DATE_ADD(NOW(), INTERVAL 7 DAY) AS 일주일후,
	DATEDIFF('2026-12-31', CURDATE()) AS 남은일수,
	DATE_FORMAT(NOW(), '%Y년 %m월 %d일 %H시') AS 포맷변환;