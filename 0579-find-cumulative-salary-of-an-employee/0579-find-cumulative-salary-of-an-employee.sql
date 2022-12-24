# Write your MySQL query statement below
select e1.id,e1.month month,sum(e2.salary) salary
from
employee e1 inner join employee e2 on e1.id=e2.id and (e1.Month - e2.Month) between 0 and 2
where (e1.id,e1.month) not in (select id,max(month) from employee group by id)
group by e1.id,e1.month
order by e1.id,e1.month desc
