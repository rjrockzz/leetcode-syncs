/*
TeamPoints
* team_id
* name
* points

PointsChange
* team_id
* points_change

- 0: indicates no change in points.
- positive: indicates an increase in points.
- negative: indicates a decrease in points.
*/
# Write your MySQL query statement below
SELECT a.team_id,a.name,
CAST(ROW_NUMBER() OVER(ORDER BY points DESC,name ASC) AS SIGNED)-
CAST(ROW_NUMBER() OVER(ORDER BY points+points_change DESC,name ASC) as SIGNED) as rank_diff
FROM TeamPoints as a
JOIN PointsChange as b
ON a.team_id=b.team_id