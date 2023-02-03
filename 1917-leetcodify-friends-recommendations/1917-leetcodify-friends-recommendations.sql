# Write your MySQL query statement below
/* 
Almost the same requirements as the Leetcodify Friends Recommendations
We have to recommend some new friends, based on the firneships we establishes before in the frienship table, based on the previous conditions
*/
with BiDirectional as
(
    SELECT user1_id, user2_id from Friendship
    UNION
    SELECT user2_id, user1_id from Friendship
)
SELECT Distinct A.user_id as user_id,
                B.user_id as recommended_id
FROM
    LISTENS A
JOIN
    LISTENS B
ON
    A.user_id <> B.user_id AND
    A.song_id = B.song_id AND
    A.day = B.day
LEFT JOIN BiDirectional bi on
    bi.user1_id = A.user_id AND
    bi.user2_id = B.user_id
WHERE bi.user1_id is NULL
GROUP BY A.user_id, B.user_id, A.day
HAVING COUNT(DISTINCT A.song_id)>=3