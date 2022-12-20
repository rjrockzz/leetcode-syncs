# Write your MySQL query statement below
/*
Subscriptions
* account_id
* start_date
* end_date

Streams
* session_id
* account_id
* stream_date
*/

SELECT
COUNT(Sub.account_id) AS accounts_count
FROM Subscriptions Sub
JOIN Streams Str
ON Sub.account_id = Str.account_id
WHERE (YEAR(start_date) = 2021 OR YEAR(end_date) = 2021) 
        AND YEAR(stream_date) <> 2021