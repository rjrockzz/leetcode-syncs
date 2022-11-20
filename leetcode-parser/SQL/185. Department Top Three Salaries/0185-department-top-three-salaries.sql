WITH
  department_ranking AS (
  SELECT
    Name AS Employee,
    Salary,
    DepartmentId,
    DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS rnk
  FROM
    Employee )
SELECT
  Department.Name as Department,
  Employee,
  Salary
FROM
  department_ranking
JOIN
  Department
ON
  Department.id=department_ranking.DepartmentId
WHERE
  rnk<=3