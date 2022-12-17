# Write your MySQL query statement below
/*
Teams 
* team_id
* team_name

Matches
* home_team_id
* away_team_id
* home_team_goals
* away_team_goals
(home_team_id, away_team_id) is the primary key for this table.
The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points. If a match ends with a draw, both teams get one point.

EPL question:)
*/
with matches_union as 
( 
    select * from matches union all
    select away_team_id, home_team_id, away_team_goals, home_team_goals from matches
)
select t.team_name, count(*) as matches_played, sum(case when home_team_goals>away_team_goals then 3 when home_team_goals<away_team_goals then 0 else 1 end) points, sum(home_team_goals) as goal_for, sum(away_team_goals) as goal_against, sum(home_team_goals) - sum(away_team_goals) as goal_diff from matches_union m join teams t on m.home_team_id = t.team_id group by 1 order by 3 desc, goal_diff desc, 1