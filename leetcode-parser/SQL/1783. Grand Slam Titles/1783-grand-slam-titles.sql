# Write your MySQL query statement below
/* 
Players
* player_id
* player_name
player_id is the PK

Championships
* year
* Wimbledon
* Fr_open
* US_open
* Au_open
*/
with champions as(
select year, wimbledon as grand_slams_count from championships union all
select year, Fr_open from championships union all
select year, US_open from championships union all
select year, Au_open from championships
) select p.player_id, p.player_name,count(*) as grand_slams_count from champions c join players p on c.grand_slams_count = p.player_id group by 1,2