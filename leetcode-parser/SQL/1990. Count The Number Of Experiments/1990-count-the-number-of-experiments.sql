with cte as (select * from 
(select "Android" as platform 
union 
select "IOS" as platform 
union 
select "Web" as platform) as a 
join
(select "Reading" as experiment_name 
union 
select "Sports" as experiment_name 
union 
select "Programming" as experiment_name) as b
order by platform)

select cte.platform,
       cte.experiment_name,
	   coalesce(count(experiment_id),0) as num_experiments 
from cte 
left join 
Experiments as e 
on cte.platform=e.platform 
   and 
   cte.experiment_name=e.experiment_name
group by 1,2
order by 1