# Write your MySQL query statement below
SELECT MIN(A.Id) AS Id, A.Company, A.Salary
FROM Employee A, Employee B
WHERE A.Company = B.Company
GROUP BY A.Company, A.Salary
HAVING SUM(CASE WHEN B.Salary >= A.Salary then 1 ELSE 0 END) >= COUNT(*)/2
AND SUM(CASE WHEN B.Salary <= A.Salary then 1 ELSE 0 END) >= COUNT(*)/2