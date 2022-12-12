# Write your MySQL query statement below
/*
Customer
* customer_id
* name
* visited_on
* amount

there will be atleast one customer every day,
we will be needing to calculate the running average of the amount paid by the customers
*/
SELECT   visited_on, 
         SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)   AS'amount',
         ROUND(CAST(SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS FLOAT)/7.0 ,2) AS'average_amount' 
FROM     Customer 
GROUP BY visited_on
ORDER BY visited_on limit 6,1000
