USE sakila;

SELECT
	UPPER(title) AS 영화제목,
	rental_duration,
	rental_rate,
    IF(rental_rate >= 3.0, '프리미엄', '일반') AS 분류
FROM film
LIMIT 10;