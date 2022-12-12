# Write your MySQL query statement below
/*
Cinema
* seat_id 
* free

consecutive means leads and lags:)
*/
SELECT seat_id
FROM cinema
WHERE free = 1 AND (
    seat_id - 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
    OR
    seat_id + 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
);