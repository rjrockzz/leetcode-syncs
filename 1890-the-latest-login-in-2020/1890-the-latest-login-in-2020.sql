# Write your MySQL query statement below
/*
i am wondering why
WHERE time_stamp BETWEEN '2020-01-01' AND '2020-12-31'
not working
* you need to specify completely
between '2020-01-01 00:00:00' and '2020-12-31 23:59:59'
* It's because of the hour. If you get a date of 2020-12-31 with a time other than 00:00:00, then it doesn't consider it as being inside the range, so you need to specify it as '2020-12-31 23:59:59'
*/
select user_id, max(time_stamp) last_stamp from logins where YEAR(time_stamp) = 2020  group by 1 