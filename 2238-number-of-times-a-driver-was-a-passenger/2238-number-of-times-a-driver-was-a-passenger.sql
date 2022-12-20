# Write your MySQL query statement below
/*
Rides
* ride_id
* driver_id
* passenger_id
Note that driver_id != passenger_id.
*/

SELECT
  D.driver_id,
  COUNT(R2.passenger_id) AS cnt
FROM
  (SELECT DISTINCT R1.driver_id FROM Rides R1) D
  LEFT JOIN Rides R2 ON D.driver_id = R2.passenger_id
GROUP BY
  D.driver_id;