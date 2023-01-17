# Write your MySQL query statement below
/*
* experiment_id -> PK
* platform -> ("Android", "IOS", "Web")
* experiment_name -> ('Reading', 'Sports', 'Programming')

Catch ->
- You need to cosider that the enums are exisitng separately.

*/
with platform as(
    select "Android" as platform union all
    select "IOS" UNION ALL
    select "Web"
),
experiment_name as(
    select "Reading" as experiment_name union all
    select "Sports" union all
    select "Programming"
)
,overall_table as
(
    select distinct a.platform, b.experiment_name from platform a,experiment_name b 
),
counts as (
    select platform, experiment_name, count(*) as num_experiments from experiments group by 1,2
) select o.platform, o.experiment_name, ifnull(c.num_experiments,0) as num_experiments from overall_table o left join counts c on o.platform = c.platform and o.experiment_name=c.experiment_name