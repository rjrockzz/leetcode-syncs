# Write your MySQL query statement below
select t.month, 
count(distinct driver_id) active_drivers,
count(distinct rides.ride_id) accepted_rides 
from
(
    (select 1 as month)
    union (select 2 as month)
    union (select 3 as month)
    union (select 4 as month)
    union (select 5 as month)
    union (select 6 as month)
    union (select 7 as month)
    union (select 8 as month)
    union (select 9 as month)
    union (select 10 as month)
    union (select 11 as month)
    union (select 12 as month)
) t
# join driver table
left join
(
	select driver_id, 
	(case when year(join_date)=2019 then '1' else month(join_date) end) `month`
	from Drivers 
	where year(join_date)<=2020
) d
on d.month <= t.month
# join accepted ride table
left join
(
    select month(requested_at) as `month`, a.ride_id
    from AcceptedRides a 
    join Rides r
    on r.ride_id = a.ride_id
    where year(requested_at)=2020
) rides
on t.month = rides.month
group by t.month 
order by t.month 