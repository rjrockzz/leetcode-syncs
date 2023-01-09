/* 
Accounts
* account_id
* max_income

Transactions
* transaction_id
* account_id
* type
* amount
* day

creditor > max_income, for 2 or more consecutive months
The catch here is to actually find out the consecutiveness right.
*/
with total_transactions as
(
    select t.account_id, sum(amount) as total_amount, DATE_FORMAT(day, "%Y%m") as month, a.max_income as max_income from transactions t left join accounts a using (account_id) where t.type = "Creditor" group by t.account_id, left(day,7) having total_amount>max_income 
)
select t1.account_id from total_transactions t1, total_transactions t2 where t1.account_id = t2.account_id and PERIOD_DIFF(t1.month, t2.month)=1
group by 1 order by 1