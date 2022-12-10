# Write your MySQL query statement below
SELECT num
FROM mynumbers
GROUP BY num
HAVING count(*) = 1

UNION ALL
SELECT NULL

ORDER BY num DESC
LIMIT 1;