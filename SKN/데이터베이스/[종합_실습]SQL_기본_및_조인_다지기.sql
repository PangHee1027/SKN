USE world;

SELECT co.Continent AS 대륙, SUM(c.Population) AS 총도시인구합계
FROM city AS c
INNER JOIN country AS co on c.CountryCode = co.Code
GROUP BY co.Continent
HAVING SUM(c.Population) > 100000000
ORDER BY SUM(c.Population) DESC;