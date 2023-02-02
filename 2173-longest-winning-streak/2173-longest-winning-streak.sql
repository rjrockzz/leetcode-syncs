# Write your MySQL query statement below
/*
Matches 
* player_id
* match_id
* result

We have to find the longest Winning Streak for each of the players
*/
with cte as
(
  select
    player_id, match_day, result, 
    DENSE_RANK() over(partition by player_id order by match_day) - 
    DENSE_RANK() over(partition by player_id,result order by match_day) as sequence_groupings    
    from matches
) , final as (select player_id, count(*) as win_counts from cte where result = "Win" group by player_id, sequence_groupings)
select distinct m.player_id, ifnull(max(win_counts),0) as longest_streak from matches m left join final using (player_id) group by 1 

