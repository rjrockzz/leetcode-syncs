# Write your MySQL query statement below
/*
Candidates
* employee_id
* experience
* salary
total budget : $70000

1. Largest Number of Seniors
2. After hiring maximum number of seniors, use the remaining budget to hire the largest number of juniors.
*/

WITH CTE AS (SELECT employee_id, experience, SUM(salary) OVER(PARTITION BY experience ORDER BY salary,employee_id ASC) AS RN FROM Candidates)
      
SELECT 'Senior' AS experience, COUNT(employee_id) AS accepted_candidates FROM CTE WHERE experience = 'Senior' AND RN < 70000
UNION
SELECT 'Junior' AS experience, COUNT(employee_id) AS accepted_candidates FROM CTE WHERE experience = 'Junior' AND RN < (SELECT 70000 - IFNULL(MAX(RN),0) FROM CTE WHERE experience = 'Senior' AND RN < 70000)