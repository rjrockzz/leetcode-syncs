# Write your MySQL query statement below
/*
Buses
* bus_id
* arrival_time
* capacity
*/
WITH TEMP AS (
SELECT bus_id, b.arrival_time, capacity, count(passenger_id) AS num
FROM Buses b  LEFT JOIN Passengers p  ON p.arrival_time <= b.arrival_time
WHERE bus_id is not NULL
GROUP BY bus_id
ORDER BY arrival_time
)

SELECT bus_id, passengers_cnt from (
SELECT bus_id, capacity, num,
      @passengers_cnt:=LEAST(capacity,num-@accum) as passengers_cnt, 
      @accum:=@accum+@passengers_cnt
FROM TEMP, (SELECT @accum:= 0, @passengers_cnt:=0) INIT) temp
ORDER BY bus_id