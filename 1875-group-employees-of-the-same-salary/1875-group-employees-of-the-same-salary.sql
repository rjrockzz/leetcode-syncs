# Write your MySQL query statement below
SELECT employee_id, name, salary, DENSE_RANK() OVER (ORDER BY salary) team_id
FROM (
SELECT *, COUNT(employee_id) OVER (PARTITION BY salary) as ct
FROM Employees) temp
WHERE ct>1
ORDER BY 4, 1