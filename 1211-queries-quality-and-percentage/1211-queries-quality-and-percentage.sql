# Write your MySQL query statement below
/*
Queries
* query_name
* result
* position
* rating
*/

SELECT 
	query_name,
	ROUND(AVG(rating / position), 2) AS quality,
	ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage 
FROM 
	Queries
GROUP BY 
	query_name