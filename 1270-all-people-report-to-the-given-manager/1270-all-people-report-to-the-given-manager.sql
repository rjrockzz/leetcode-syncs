# Write your MySQL query statement below
/*
Employees
* employee_id
* employee_name
* manager_id
The head of the company is the employee with employee_id = 1.
*/
select e_eid as employee_id from (select e.employee_id e_eid, e.manager_id e_mid, j1.manager_id j1_mid, j2.manager_id j2_mid from employees e join employees j1 on e.manager_id = j1.employee_id join employees j2 on j1.manager_id = j2.employee_id) e where e_eid <> 1 and (e_mid = 1 or j1_mid = 1 or j2_mid = 1)