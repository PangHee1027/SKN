USE world;

# SELECT Name, Population FROM country
# WHERE Population BETWEEN 10000000 AND 20000000;

# SELECT Name, Continent FROM country
# WHERE Continent IN ('Asia', 'Europe', 'North America');

SELECT Name, Continent, Population, GovernmentForm FROM country WHERE Name LIKE 'South%';