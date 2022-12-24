# Write your MySQL query statement below
select b.item_category as 'CATEGORY', sum(case when weekday(a.order_date) = 0 then a.quantity else 0 end) as 'MONDAY',
sum(case when weekday(a.order_date) = 1 then a.quantity else 0 end) as 'TUESDAY',
sum(case when weekday(a.order_date) = 2 then a.quantity else 0 end) as 'WEDNESDAY',
sum(case when weekday(a.order_date) = 3 then a.quantity else 0 end) as 'THURSDAY',
sum(case when weekday(a.order_date) = 4 then a.quantity else 0 end) as 'FRIDAY',
sum(case when weekday(a.order_date) = 5 then a.quantity else 0 end) as 'SATURDAY',
sum(case when weekday(a.order_date) = 6 then a.quantity else 0 end) as 'SUNDAY'
from orders a right join items b on a.item_id = b.item_id
group by b.item_category
order by b.item_category