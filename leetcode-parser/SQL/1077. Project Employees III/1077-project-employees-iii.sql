# Write your MySQL query statement below
/*
Project
* project_id
* employee_id

Employee
* employee_id
* name
* experience_years
*/
select project_id, employee_id from (select p.project_id,p.employee_id, rank() over (partition by p.project_id order by e.experience_years desc) `ranks` from project p join employee e using(employee_id)) s where ranks = 1
