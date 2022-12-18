# Write your MySQL query statement below
/*
* order_id
* customer_id
* order_type
*/
SELECT * FROM Orders
WHERE (customer_id, order_type) 
IN (SELECT customer_id, MIN(order_type) 
    FROM Orders 
    GROUP BY customer_id)