# Write your MySQL query statement below
/*
Scores
* player_name
* gender
* day
* score_points
(gender, day) is the PK table
we have to tk
*/
SELECT gender, day, 
       SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores