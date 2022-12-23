# Write your MySQL query statement below
/*
Activity
* player_id
* device_id
* event_date
* games_played

The install date of a player is the first login day of that player.
*/
/*
Approach: CTEs, indicator variable, and LEFT JOIN
Intuition
As noted in the preferred approach for part IV in this problem series, CTEs can be powerful agents of clarity when it comes to tackling difficult SQL problems. We will aim to reshape the sequence of CTEs used in part IV to craft a solution to this fifth and final problem in the Game Play Analysis series.

The "reshaping" referenced above is also a strong selling point for using CTEs -- they can be quite modular. If a complicated problem changes in a minor way, then a chain of CTEs can often be refactored to accommodate the new changes (such is the case in going from the preferred solution to part IV to this solution for part V).

Algorithm
Identify the first login date for each player.
Use an indicator variable (also referred to as a "dummy variable" in some statistical contexts), logged_in_consecutively, to identify which players from step 1 logged in consecutively starting from their first login date. All players who logged in consecutively will have a value of 1 recorded for logged_in_consecutively while all those who did not will have a 0 recorded (the LEFT JOIN makes it possible to identify those players who did not login consecutively from their first login date).
Group the information obtained in step 2 by first login date to calculate field values as appropriate.
Implementation
MySQL
*/
WITH first_logins AS (
  SELECT
    A.player_id,
    MIN(A.event_date) AS first_login
  FROM
    Activity A
  GROUP BY
    A.player_id
), consec_login_info AS (
  SELECT
    F.player_id,
    (CASE
      WHEN A.player_id IS NULL THEN 0
      ELSE 1
    END) AS logged_in_consecutively,
    F.first_login
  FROM
    first_logins F
    LEFT JOIN Activity A ON F.player_id = A.player_id
    AND F.first_login = DATE_SUB(A.event_date, INTERVAL 1 DAY)
)
SELECT
  C.first_login AS install_dt,
  COUNT(C.player_id) AS installs,
  ROUND(
    SUM(C.logged_in_consecutively)
    / COUNT(C.player_id)
  , 2) AS Day1_Retention
FROM
  consec_login_info C
GROUP BY
  C.first_login;