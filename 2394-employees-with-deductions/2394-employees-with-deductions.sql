# Write your MySQL query statement below
/*
Employees
* employee_id
* needed_hours
Each row contains the id of an employee and the minimum number of hours needed for them to work to get their salary.

Logs 
* employee_id
* in_time
* out_time
*/
with cte as
(
    select employee_id, CEILING((sum(timestampdiff(SECOND, in_time, out_time)))/60) as total_time from logs group by 1
)
select e.employee_id from employees e left join cte c using(employee_id) where needed_hours*60>ifnull(total_time,0)