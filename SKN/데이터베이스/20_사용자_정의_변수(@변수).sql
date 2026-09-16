USE world;

SET @target_continent = 'Asia';

SELECT Name, Continent, Population
FROM country
WHERE Continent = @target_continent
ORDER BY Population DESC
LIMIT 3;