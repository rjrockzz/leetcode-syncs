# Write your MySQL query statement below
/* 
Customers
* customer_id
* name

Orders
* order_id
* order_date
* customer_id
* product_id
No customer will order the same product more than once in a single day.

Products
* product_id
* product_name
* price
*/
with counts_cte as (select customer_id, product_id, count(*) as counts from orders group by 1,2) select o.customer_id, o.product_id, p.product_name from counts_cte o left join (select customer_id, max(counts) counts from counts_cte group by 1) c on o.customer_id=c.customer_id and o.counts = c.counts left join products p using(product_id) where c.counts is not null