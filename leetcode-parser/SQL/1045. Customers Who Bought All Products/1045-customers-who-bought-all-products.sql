# Write your MySQL query statement below
/* 
Customer
* customer_id
* product_key

Product
* product_key
*/
select customer_id from customer group by 1 having count(distinct product_key) = (select count(product_key) from product)