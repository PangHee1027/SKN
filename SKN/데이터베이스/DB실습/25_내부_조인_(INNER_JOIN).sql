USE world;

SELECT
	C.Name AS 도시명,
	CO.Name AS 국가명,
	CO.Continent AS 대륙,
	C.Population AS 도시인구
FROM city AS C
INNER JOIN country AS CO ON C.CountryCode = CO.Code
WHERE CO.Continent = 'Asia'
ORDER BY C.Population DESC
LIMIT 5;