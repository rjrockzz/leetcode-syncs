# Write your MySQL query statement below
select player_id, device_id from (select *, rank() over (partition by player_id order by event_date) `rank` from activity) s where s.rank = 1