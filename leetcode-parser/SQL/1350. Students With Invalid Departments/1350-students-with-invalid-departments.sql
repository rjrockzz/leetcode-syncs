# Write your MySQL query statement below
/*
Departments
* id
* name

Students
* id
* name
* department_id
*/

SELECT s.id, s.name
FROM Departments d
RIGHT JOIN Students s
ON d.id = s.department_id
WHERE d.id IS NULL