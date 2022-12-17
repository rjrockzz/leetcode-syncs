# Write your MySQL query statement below
/*
Activity
* player_id
* device_id
* event_date
* games_played
*/
select player_id, event_date, sum(games_played) over(partition by player_id order by event_date) as games_played_so_far from activity