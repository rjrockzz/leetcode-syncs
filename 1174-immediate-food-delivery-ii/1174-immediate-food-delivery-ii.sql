# Write your MySQL query statement below
/* 
Delivery
* delivery_id
* customer_id
* order_date
* customer_pref_delivery_date
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
*/
with cte as
(
    select customer_id, order_date, customer_pref_delivery_date, rank() over (partition by customer_id order by order_date) as ranks from delivery
)
select round(100*sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(*),2) immediate_percentage from cte where ranks = 1