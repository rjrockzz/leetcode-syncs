# Write your MySQL query statement below
/* 
Warehouse table
* name
* product_id
* units
(name, product_id) is the PK for the table

Products table
* product_id
* product_name
* width
* length
* height
*/
with cte as(
select w.name, w.product_id, w.units as units, (p.width*p.length*p.height) as raw_volume from warehouse w left join products p on w.product_id=p.product_id)
select name as warehouse_name, sum(units*raw_volume) as volume from cte group by 1