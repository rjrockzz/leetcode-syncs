# Write your MySQL query statement below
with c as (
    select l1.user_id as uid1, l2.user_id as uid2, count(distinct l1.song_id) as ct
    from listens l1
    join listens l2
    on l1.song_id=l2.song_id and l1.day=l2.day and l1.user_id<>l2.user_id  # make sure l1.user_id != l2.user_id, we don't wanna join on user_id itself
    group by l1.user_id, l2.user_id, l1.day
    having ct>=3  # make sure the number of different songs on each day >=3
), f (uid1, uid2) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select uid1 as user_id, uid2 as recommended_id
from c
where (uid1, uid2) not in (select uid1, uid2 from f)
group by uid1, uid2;