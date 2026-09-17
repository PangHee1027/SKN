USE world;

# SELECT Name, Population
# FROM city
# WHERE CountryCode = "KOR" and Population >= 1000000
# ORDER BY Population DESC;

SELECT Name, Continent, LifeExpectancy
FROM country
WHERE LifeExpectancy >= 80