# Write your MySQL query statement below
/*
Employee
* employee_id
* team_id
*/
select e.employee_id, t.team_size from employee e 
join (select team_id, count(*) as team_size from employee group by 1) t 
using(team_id)