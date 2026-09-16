USE world;

# SELECT
	# Name,
	# LifeExpectancy,
	# IF(LifeExpectancy >= 75, '장수국가', '일반국가') AS 국가분류,
	# IFNULL(GNPOld, 0) AS 이전GNP
# FROM country LIMIT 5;

SELECT Name, Population,
CASE
	WHEN Population >= 100000000 THEN '초대형 국가'
	WHEN Population >= 30000000 THEN '중대형 국가'
	ELSE '소형 국가'
	END AS 인구규모분류
FROM country LIMIT 5;