# Write your MySQL query statement below
/*
Employees
* employee_id
* name
* manager_id
* salary
*/
SELECT DISTINCT emp.employee_id
FROM   employees emp
       LEFT JOIN employees mng
              ON( emp.manager_id = mng.employee_id )
WHERE  emp.manager_id IS NOT NULL
       AND emp.salary < 30000
       AND mng.employee_id IS NULL
ORDER  BY emp.employee_id 