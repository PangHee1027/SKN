USE world;

SELECT
	COUNT(*) AS 전체국가수,
	SUM(Population) AS 전세계총인구,
	AVG(Population) AS 국가별평균인구,
	MAX(Population) AS 최고인구수,
	MIN(Population) AS 최저인구수
FROM country;