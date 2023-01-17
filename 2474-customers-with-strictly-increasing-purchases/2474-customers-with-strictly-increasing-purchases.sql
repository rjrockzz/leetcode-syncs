# Write your MySQL query statement below
/* Orders
* order_id
* customer_id
* order_date
* price

Catch -> We need to add / consider the years in between, if we have an year coming out to be 2015 and the next year is 2017 , we should consider the value for 2016 as 0
*/
with yearly_prices as (SELECT customer_id,  DATE_FORMAT(order_date, "%Y") year, sum(price) as total_price FROM Orders group by 1,2),
inc_dec as (
select * , 
 case when total_price > LAG(total_price) over (partition by customer_id order by year) and lag(year) over (partition by customer_id order by year)  = year - 1
    then 0 ELSE 1 END as increasing_decreasing
from yearly_prices)
select customer_id from inc_dec group by customer_id having sum(increasing_decreasing)=1 
