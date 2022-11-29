# Write your MySQL query statement below
/*
Activity Table
* user_id 
* session_id
* activity_date
* activity_type
It may have duplicate rows. 
*/
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE (activity_date > "2019-06-27" AND activity_date <= "2019-07-27")
GROUP BY activity_date;