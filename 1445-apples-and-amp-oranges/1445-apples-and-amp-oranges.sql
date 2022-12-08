# Write your MySQL query statement below
/*
Sales table
* sale_date
* fruit \U0001f34e \U0001f34f \U0001f349 
* sold_num
(sale_date, fruit) is the Primary Key for this table
*/
select sale_date, sum(case when fruit = "apples" then sold_num else -sold_num end) as diff from sales group by 1