USE world;

CREATE VIEW v_asia_city_info AS
SELECT
 C.Name AS city_name,
 CO.Name AS country_name,
 C.Population AS city_population
FROM city AS C
INNER JOIN country AS CO ON C.CountryCode = CO.Code
WHERE CO.Continent = 'Asia';

SELECT * FROM v_asia_city_info
WHERE city_population >= 5000000
ORDER BY city_population DESC;