# Write your MySQL query statement below
/*
Flights
* departure_airport
* arrival_airport
* flights_count
(departure_airport, arrival_airport) is the primary key column for this table.
*/
WITH arpt
as
    (SELECT ar.airport_id, sum(ar.flights_count) as flights_count from 
     (SELECT departure_airport as airport_id, flights_count as flights_count from Flights
    UNION ALL
    SELECT arrival_airport as airport_id, flights_count as flights_count from Flights
    ) ar
    group by ar.airport_id)

SELECT a. airport_id from arpt a where a.flights_count = (select max(p.flights_count) from arpt p)
