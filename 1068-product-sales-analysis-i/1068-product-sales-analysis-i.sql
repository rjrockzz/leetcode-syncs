# Write your MySQL query statement below
/* 
Sales
* sale_id
* product_id
* year
* quantity
* price
(sale_id, year) is the primary key of this table.

Product
* product_id
* product_name
*/

select p.product_name, s.year, s.price from sales s join product p using(product_id)