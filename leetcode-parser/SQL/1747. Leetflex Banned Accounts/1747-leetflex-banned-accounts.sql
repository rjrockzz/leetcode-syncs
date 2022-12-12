# Write your MySQL query statement below
/*
LogInfo
* account_id
* ip_address
* login
* logout

Write an SQL query to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.
*/
select
distinct a.account_id
from LogInfo a, LogInfo b
where a.login between (b.login) and (b.logout)
and a.account_id = b.account_id
and a.ip_address !=b.ip_address