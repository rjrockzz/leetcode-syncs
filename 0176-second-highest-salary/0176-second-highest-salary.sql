WITH CTE AS
(SELECT Salary, DENSE_RANK () OVER (ORDER BY Salary desc) AS RANK_desc
FROM Employee)
SELECT MAX(Salary) as SecondHighestSalary
FROM CTE
where RANK_DESC = 2