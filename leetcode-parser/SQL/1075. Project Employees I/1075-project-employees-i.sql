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

select p.project_id, round(avg(e.experience_years),2) as average_years from project p join employee e using(employee_id) group by 1