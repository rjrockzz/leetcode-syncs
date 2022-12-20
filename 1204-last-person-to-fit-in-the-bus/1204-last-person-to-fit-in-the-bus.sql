# Write your MySQL query statement below
/*
Queue
* person_id
* person_name
* weight
* turn
*/
with cte as 
(
    select turn, person_name, sum(weight) over(order by turn) as running_weight from queue order by 1
)
select * from 
(select person_name from cte where turn =(select turn from cte where running_weight>1000 limit 1)-1
union all
select person_name from cte where turn = (select max(turn) from cte)) s limit 1