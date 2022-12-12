# Write your MySQL query statement below
/*
Employees
* employee_id
* name
* reports_to
* age

A classic self-join:)
*/
select e.reports_to as employee_id, n.name as name, count(*) as reports_count, round(avg(e.age)) as average_age from employees e join employees n on n.employee_id = e.reports_to group by 1,2 order by employee_id