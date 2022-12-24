# Write your MySQL query statement below
with 
# inner join two tables for future use
cte0 as (select p1.*, p2.price, quantity * price as prices from Purchases p1 join Products p2 on p1.product_id = p2.product_id), 
# rank the invoices per their purchase amount from high to low
cte1 as (select invoice_id, rank() over (order by sum(prices) desc) as rnk from cte0 group by invoice_id), 
# select the invoice with the maximum purchase amount and the smallest invoice_id
cte2 as (select invoice_id from cte1 where rnk = 1 order by invoice_id limit 1)
# select its product_id, quantity, and total price for each product_id
select product_id, quantity, prices as price from cte0 where invoice_id in (select * from cte2);