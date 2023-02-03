# Write your MySQL query statement below
/*
Listens
* user_id
* song_id
* day

Friendship
* user1_id
* user2_id
user1_id < user2_id

Concept: Mapping Question, wish we could use a Hashmap haha.
*/
select distinct A.user_id as user1_id, B.user_id as user2_id from listens A, listens B
where A.day = B.day AND
A.song_id = B.song_id AND
A.user_id!= B.user_id AND
(A.user_id, B.user_id) IN (select * from friendship)
GROUP BY a.user_id, b.user_id, a.day
having COUNT(DISTINCT A.song_id)>=3