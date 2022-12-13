# Write your MySQL query statement below
/*
OrderDetails
* order_id
* product_id
* quantity
(order_id, product_id) is the primary key for this table.
*/
with cte as (
    select order_id,
    avg(quantity) as avg_qty,
    max(quantity) as max_qty
    from ordersdetails
    group by order_id
)
select order_id from cte where max_qty>(select max(avg_qty) from cte);