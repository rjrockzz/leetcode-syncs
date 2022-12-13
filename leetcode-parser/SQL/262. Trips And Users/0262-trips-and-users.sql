# Write your MySQL query statement below
select Request_at as day ,  round(sum(if(status like 'cancelled%',1,0))/count(id),2) as 'Cancellation Rate' 
from trips
join users u1
on client_id = u1.users_id
join users u2 
on driver_id = u2.users_id
where
u1.banned ='No' and u2.banned='No'
and request_at between '2013-10-01' and '2013-10-03'
group by day
order by 1;