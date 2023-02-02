# Write your MySQL query statement below
/*
Orders
* order_id
* product_id
* quantity
* purchase_date

Products that were ordered three or more times in two consecutive years.
*/
with cte as
(
    select product_id, left(purchase_date, 4) as years from orders group by 1,2 having count(order_id)>=3
)select distinct c1.product_id from cte c1 join cte c2 on c1.years+1=c2.years and c1.product_id = c2.product_id