# Write your MySQL query statement below
/*
Players
* player_id
* group_id

Matches
* match_id
* first_player
* second_player
* first_score
* second_score
*/
with cte as 
(
    select first_player as player_id, sum(first_score) sums from (
    select first_player, first_score from matches union all
    select second_player, second_score from matches
    ) e group by 1
), ranks as 
(
    select p.player_id, p.group_id, c.sums , rank() over (partition by group_id order by c.sums desc, p.player_id) `rank` from cte c join players p using(player_id)
)

select group_id, player_id from ranks where `rank` = 1