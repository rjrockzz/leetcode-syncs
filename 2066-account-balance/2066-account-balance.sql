# Write your MySQL query statement below
/*
Transactions
* account_id
* day
* type
* amount


Solution -
1. Identify each types, and assign them a positive or negative
2. Take a running sum on that assignment
*/
select account_id, day, sum(case when type = "Deposit" then amount else -amount end) over (partition by account_id order by day) as balance from transactions