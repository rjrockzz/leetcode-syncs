# Write your MySQL query statement below
/*
Customers
* customer_id
* name

Orders
* order_id
* order_date
* customer_id
* cost

Each customer has one order per day.
*/

with ranks as 
(select *, rank() over (partition by customer_id order by order_date desc) as `ranks` from orders)
select c.name as customer_name, r.customer_id, r.order_id, r.order_date from ranks r join customers c using(customer_id) where ranks <=3 order by 1, 2, 4 desc