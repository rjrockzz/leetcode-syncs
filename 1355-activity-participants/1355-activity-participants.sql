# Write your MySQL query statement below
/* 
Friends
* id
* name
* activity

Activites
* id 
* name
*/
SELECT activity
FROM Friends 
GROUP BY activity
HAVING 
    COUNT(*) <> (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 LIMIT 1)
    AND
    COUNT(*) <> (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 DESC LIMIT 1);