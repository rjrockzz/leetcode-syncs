# Write your MySQL query statement below
select left(order_date, 7) month, count(distinct order_id) order_count, 
count(distinct customer_id) customer_count
from orders
where invoice > 20
group by 1;