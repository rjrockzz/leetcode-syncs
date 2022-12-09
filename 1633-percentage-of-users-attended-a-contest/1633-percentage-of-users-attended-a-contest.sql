# Write your MySQL query statement below
/*
---- Users ----
* user_id
* user_name

---- Register ----
* contest_id
* user_id
*/
SELECT contest_id
    , ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register 
GROUP BY contest_id
    ORDER BY percentage DESC, contest_id