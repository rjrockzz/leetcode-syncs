# Write your MySQL query statement below
/*
Delivery
* delivery_id
* customer_id
* order_id
* customer_pref_delivery_date

If customer's preferred delivery date is the same as the order date, then the order is called *immediate*; otherwise, it is called *scheduled*.
*/
select round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)*100/count(*), 2) as immediate_percentage from delivery
