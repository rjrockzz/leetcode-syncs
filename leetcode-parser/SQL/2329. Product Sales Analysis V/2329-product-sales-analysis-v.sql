# Write your MySQL query statement below
/*
Sales
* sale_id
* product_id
* user_id
* quantity

Product
* product_id
* price
*/
select s.user_id, sum(s.quantity * p.price) spending from sales s join product p using(product_id) group by 1 order by 2 desc ,1 