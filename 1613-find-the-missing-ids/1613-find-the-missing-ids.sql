# Write your MySQL query statement below
/*
Customer
* customer_id
* customer_name
*/


with recursive cte(num) as (
select 1 as num
    union all 
    select num+1 from cte where num+1<=(select max(customer_id) from customers)
)select num as ids from cte where num not in (select customer_id from customers)