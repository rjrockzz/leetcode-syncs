# Write your MySQL query statement below
with a as (select employee_id, experience,salary, sum(salary)over(partition by experience order by salary) as budget
from Candidates),

b as (select employee_id, budget from a where experience="senior"and budget<=70000),
c as (select employee_id from a where budget<= 70000-(select ifnull(max(budget),0) from b) )

(select employee_id from b)
union
(select employee_id from c)