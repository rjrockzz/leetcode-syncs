# Write your MySQL query statement below
select eu.unique_id, e.name from employees e left join employeeUNI eu using(id)