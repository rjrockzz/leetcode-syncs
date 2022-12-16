# Write your MySQL query statement below
/*
Cinema
* id
* movie
* description
* rating
rating is a 2 decimal places float in the range [0, 10]
*/
select id, movie, description, rating from cinema where id%2<>0 and description<>"boring" order by 4 desc