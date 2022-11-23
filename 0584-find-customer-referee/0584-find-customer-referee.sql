  # Write your MySQL query statement below
# MySQL uses three-valued logic -- TRUE, FALSE and UNKNOWN. Anything compared to NULL evaluates to the third value: UNKNOWN. That “anything” includes NULL itself! That’s why MySQL provides the IS NULL and IS NOT NULL operators to specifically check for NULL.
SELECT
  name
FROM
  customer
WHERE
  referee_id != 2
  OR referee_id IS null