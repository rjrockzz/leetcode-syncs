# Write your MySQL query statement below
/*
Relations
* user_id
* follower_id
(user_id, follower_id) is the primary key for this table.
*/
with new as (select r1.user_id user1_id, r2.user_id user2_id, count(distinct r1.follower_id) as common
from relations r1
join relations r2
on r1.user_id <r2.user_id  and r1.follower_id = r2.follower_id
group by r1.user_id, r2.user_id)

select user1_id, user2_id
from new
where common in (select max(common) from new)