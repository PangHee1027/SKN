USE sakila;

SELECT customer_id as 고객_ID, SUM(amount) as 총결재금액
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC;
