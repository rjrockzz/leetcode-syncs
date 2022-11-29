# Write your MySQL query statement below
/* 
Followers Table
* user_id 
* follower_id
*/

select user_id, count(distinct follower_id) followers_count from followers group by 1 order by 1