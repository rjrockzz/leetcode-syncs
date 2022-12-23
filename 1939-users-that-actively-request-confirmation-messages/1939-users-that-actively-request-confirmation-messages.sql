# Write your MySQL query statement below
/*
Signups
* user_id
* time_stamp

Confirmations
* user_id
* time_stamp
* action
*/
select
distinct c.user_id
from confirmations c
join confirmations d
on c.user_id=d.user_id and c.time_stamp>d.time_stamp and 
timestampdiff(second, d.time_stamp,c.time_stamp)<=86400