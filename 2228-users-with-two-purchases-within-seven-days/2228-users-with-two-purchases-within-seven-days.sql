# Write your MySQL query statement below
/*
Purchases
* purchase_id
* user_id
* purchase_date
*/
select distinct p_left.user_id from purchases p_left join purchases p_right on ABS(datediff(p_left.purchase_date, p_right.purchase_date))<=7 and p_left.user_id = p_right.user_id and p_left.purchase_id!= p_right.purchase_id order by p_left.user_id