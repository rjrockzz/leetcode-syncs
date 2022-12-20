# Write your MySQL query statement below
/*
Signups
* user_id
* time_stamp

Confirmations
* user_id
* time_stamp
* action
*/
SELECT 
    user_id,
    ROUND(AVG(IF(action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups LEFT JOIN Confirmations USING (user_id)
GROUP BY 1
ORDER BY 1