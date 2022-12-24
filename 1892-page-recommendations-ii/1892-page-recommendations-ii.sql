# Write your MySQL query statement below
-- first, prep a table that contains all users and their friends
with t1 as (
    select user1_id as user_id, user2_id as friend_id from friendship
    union
    select user2_id as user_id, user1_id as friend_id from friendship)
    
-- then, join table
select t1.user_id, l.page_id, count(distinct t1.friend_id) as friends_likes
from t1
left join likes as l
on t1.friend_id=l.user_id

-- filter out pages that are already liked by the user
left join likes as l2
on t1.user_id=l2.user_id and l.page_id=l2.page_id
where l2.page_id is null

-- get the final output
group by t1.user_id, l.page_id