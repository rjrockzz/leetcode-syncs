# Write your MySQL query statement below

# Write your MySQL query statement below
SELECT user_id,user_name,
IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)+a.credit as credit,
CASE WHEN IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)>=-a.credit THEN "No" ELSE "Yes" END as credit_limit_breached
FROM Users as a
LEFT JOIN Transactions as b
ON a.user_id=b.paid_by OR a.user_id=b.paid_to
GROUP BY a.user_id;