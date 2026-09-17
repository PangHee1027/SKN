USE world;

SELECT
	CONCAT(Name, ' (', Continent, ')') AS 국가정보,
	UPPER(Name) AS 대문자국가명,
	SUBSTRING(Name, 1, 3) AS 약어
FROM country
LIMIT 5;