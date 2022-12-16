# Write your MySQL query statement below
/*
Friendship
* user1_id
* user2_id
user1_id < user2_id
*/
with f as (
select user1_id, user2_id 
from Friendship
union 
select user2_id user1_id, user1_id user2_id
from Friendship
)

select a.user1_id, a.user2_id, count(c.user2_id) common_friend
from Friendship a 
join f b 
on a.user1_id = b.user1_id # u1 friends
join f c 
on a.user2_id = c.user1_id # u2 friends
and b.user2_id = c.user2_id # u1 u2 common friends
group by a.user1_id, a.user2_id
having count(c.user2_id) >= 3