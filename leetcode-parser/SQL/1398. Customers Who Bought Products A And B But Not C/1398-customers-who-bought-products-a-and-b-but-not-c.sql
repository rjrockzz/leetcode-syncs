# Write your MySQL query statement below
/* 
Customers 
* customer_id
* customer_name
customer_id is the PK for the table.

Orders
* order_id
* customer_id
* product_name
*/
select customer_id, customer_name from customers where customer_id not in (select distinct customer_id from orders where product_name = "C") and customer_id in (select distinct customer_id from orders where product_name = "A") and customer_id in (select distinct customer_id from orders where product_name = "B")