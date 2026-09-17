USE world;

SELECT
	Continent AS 대륙,
	COUNT(*) AS 국가수,
	SUM(Population) AS 총인구수,
	AVG(LifeExpectancy) AS 평균기대수명
FROM country
GROUP BY Continent
ORDER BY 총인구수 DESC;