# Write your MySQL query statement below
/*
Friendship
* user1_id
* user2_id
(user1_id, user2_id) are the PK for the table.

Likes
* user_id
* page_id
(user_id, page_id) are the PK for the table.
*/
# FIRST FIND ALL FRIENDS FOR user1_id = 1
WITH ALL_FRIENDS_TABLE AS(
                            SELECT user2_id 
                            FROM Friendship 
                            WHERE user1_id  = 1
                            UNION
                            SELECT user1_id 
                            FROM Friendship 
                            WHERE user2_id  = 1
                           )
## THEN FIND ALL DISTINCT PAGES THESE FRIEDS HAVE LIKED
SELECT DISTINCT(page_id) AS recommended_page 
FROM Likes
WHERE user_id IN (SELECT * FROM ALL_FRIENDS_TABLE)  
### AND FINALY EXCLUDE PAGES user1_id = 1 HAS LIKED
AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)