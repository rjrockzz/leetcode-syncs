# Write your MySQL query statement below
/*
Activity
* player_id
* device_id
* event_date
* games_played
(player_id, event_date) is the primary key of this table.
*/
SELECT ROUND(COUNT(t2.player_id)/COUNT(t1.player_id),2) AS fraction
FROM
(SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) t1 LEFT JOIN Activity t2
ON t1.player_id = t2.player_id AND t1.first_login = t2.event_date - 1