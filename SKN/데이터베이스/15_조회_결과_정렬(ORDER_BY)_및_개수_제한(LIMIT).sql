USE world;

SELECT Name, Continent, Population
FROM country
ORDER BY Population DESC
LIMIT 5;