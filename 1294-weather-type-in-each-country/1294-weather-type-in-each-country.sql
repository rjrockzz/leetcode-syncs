# Write your MySQL query statement below
/*
Countries
* country_id
* country_name
country_id is the PK

Weather
* country_id
* weather_state
* day
(country_id, day) is the PK

"2019-11"
*/
select c.country_name, w.weather_type from (select country_id, case when avg(weather_state)<=15 then "Cold" when avg(weather_state)>=25 then "Hot" else "Warm" end as weather_type from weather where left(day, 7)="2019-11" group by 1) w join countries c using(country_id)
