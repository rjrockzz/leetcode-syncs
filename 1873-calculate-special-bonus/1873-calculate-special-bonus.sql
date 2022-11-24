# Write your MySQL query statement below
SELECT
  employee_id,
  CASE
    WHEN MOD(employee_id,2) <> 0 AND SUBSTRING(UPPER(name),1,1) <> "M" THEN salary
  ELSE
  0
END
  AS bonus
FROM
  employees ORDER BY 1