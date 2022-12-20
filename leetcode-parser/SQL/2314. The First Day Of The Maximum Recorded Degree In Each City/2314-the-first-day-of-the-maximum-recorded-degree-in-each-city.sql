# Write your MySQL query statement below
/*
Weather
* city_id
* day
* degree

All the degrees are recorded in the year 2022.
*/
with cte as (select city_id, day, degree, rank() over(partition by city_id order by degree desc, day) `rank` from weather) 
select city_id, day,degree from cte where `rank` = 1