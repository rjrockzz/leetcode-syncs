# Write your MySQL query statement below
/*
Per User we need to find the first login time
The challenge in this problem is to figure out how to access and report an extreme value (i.e., first login date) for each player. How could we group all rows by player and report the "smallest" date (i.e., the earliest occurring date) for each player?

Approach 1 below highlights what is probably the most natural solution, namely using GROUP BY in conjunction with MIN(). Approach 2 highlights more advanced alternative solutions that rely on using window functions.
*/
SELECT
  A.player_id,
  MIN(A.event_date) AS first_login
FROM
  Activity A
GROUP BY
  A.player_id;
