# Write your MySQL query statement below
/* 
Transactions table
* id \U0001f194 
* country
* state
* amount
* trans_date
id is the PK
)
*/
with cte as (select LEFT(trans_date,7) as month, country, state, amount, trans_date from transactions)
select month, country, count(*) as trans_count, sum(case when state = "approved" then 1 else 0 end) as approved_count, sum(amount) as trans_total_amount, sum(case when state="approved" then amount else 0 end) as approved_total_amount from cte group by 1,2