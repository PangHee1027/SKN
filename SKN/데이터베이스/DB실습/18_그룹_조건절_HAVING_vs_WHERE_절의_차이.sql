USE world;

SELECT
	Continent AS 대륙,
	SUM(Population) AS 총인구수
FROM country
GROUP BY Continent
HAVING 500000000 >= 총인구수 AND 총인구수 >= 400000000
ORDER BY 총인구수 DESC;