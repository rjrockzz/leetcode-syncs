# Write your MySQL query statement below
/*
Customer
* customer_id
* customer_name
customer_id is the PK for the table

Orders
* order_id
* sale_date
* order_cost
* customer_id
* seller_id
order_id is the PK for the table

Sellers
* seller_id
* seller_name
seller_id is the PK for the table
*/
select s.seller_name from seller s left join orders o on s.seller_id=o.seller_id and year(o.sale_date) = 2020 where o.seller_id is NULL order by s.seller_name 