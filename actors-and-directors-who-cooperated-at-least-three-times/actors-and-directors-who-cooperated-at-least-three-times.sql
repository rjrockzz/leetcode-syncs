# Write your MySQL query statement below
select actor_id, director_id from (select actor_id, director_id, count(*) colabs from actordirector group by 1, 2) a where colabs>=3