# CTEs
WITH RECURSIVE words_count_in_content AS (
    # 1. Update `Posts` table with column `num_of_words` showing count of words in `content`
    SELECT
        post_id
        , content
        , CHAR_LENGTH(content)
        - CHAR_LENGTH(
            REPLACE(content, ' ', '')
        )
        + 1 AS num_of_words
    FROM
        Posts
)
, max_words_count_in_content AS (
    # 2. Calculate max words number among all comments from `Posts` table
    SELECT
        MAX(num_of_words) AS max_num_of_words
    FROM
        words_count_in_content
)
, numbers AS (
    # 3. Recursion: create a series of integers from 1 to `max_num_of_words` with increment = 1
    SELECT
        1 AS num
    UNION ALL
    SELECT
        num + 1
    FROM
        numbers
    WHERE
        num < (
            # condition to stop recursion
            SELECT
                max_num_of_words
            FROM
                max_words_count_in_content
        )
)
, posts_and_separate_words AS (
    # 4. Create long table with primary key of (`post_id`, `word`)
    SELECT
        w.post_id
        , SUBSTRING_INDEX(
            SUBSTRING_INDEX(w.content, ' ', n.num),
            ' ',
            -1
         ) AS word
    FROM
        words_count_in_content AS w
            INNER JOIN numbers AS n
                ON w.num_of_words >= n.num
)
# Query's body
# 5. Calculate target result: convert `topic_id` to string, keep unique values only, use string aggregation for each post_id, if no corresponding topics impute NULL with string 'Ambiguous!'
SELECT
    p.post_id
    , COALESCE(
        GROUP_CONCAT(
            DISTINCT CONVERT(k.topic_id, char)
            ORDER BY k.topic_id ASC
            SEPARATOR ','
        ),
        'Ambiguous!'
    ) AS topic
FROM
    posts_and_separate_words AS p
        LEFT JOIN Keywords AS k # we use LEFT JOIN here to handle cases where there is no match in words for particular `topic_id`
            ON p.word = k.word
GROUP BY
    p.post_id
ORDER BY
    p.post_id ASC;
