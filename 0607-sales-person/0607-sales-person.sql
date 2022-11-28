# Write your MySQL query statement below
/*
SalesPerson Table : 
    - sales_id *
    - name
    - salary
    - commission_rate 
    - hire
Company Table
    - com_id *
    - name 
    - city
Orders Table
    - order_id
    - order_date
    - com_id *
    - sales_id *
    - amount
Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
*/
SELECT name from salesperson
where sales_id not in 
(
    select sales_id from orders where com_id in 
	(select com_id from company where name='RED')
)
