# Write your MySQL query statement below
/*
Keywords
* topic_id
* word
Each row of this table contains the id of a topic and a word that is used to express this topic.
There may be more than one word to express the same topic and one word may be used to express multiple topics.

Posts
* post_id
* content
*/
SELECT 
    P.post_id, 
    IFNULL(GROUP_CONCAT(DISTINCT K.topic_id ORDER BY K.topic_id), 'Ambiguous!') AS topic
FROM Posts AS P
LEFT JOIN Keywords AS K
ON CONCAT(' ', LOWER(P.content), ' ') LIKE CONCAT('% ', LOWER(K.word), ' %')
GROUP BY P.post_id