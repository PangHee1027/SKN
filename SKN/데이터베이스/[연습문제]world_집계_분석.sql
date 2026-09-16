USE world;

SELECT CountryCode, COUNT(Name) FROM city
GROUP BY CountryCode
HAVING COUNT(Name) >= 10
ORDER BY COUNT(*) DESC;
